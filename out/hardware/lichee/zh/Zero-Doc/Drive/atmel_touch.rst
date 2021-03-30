atmel触摸屏驱动分析
=============================

.. contents:: 本文目录

最新代码在：https://github.com/atmel-maxtouch/linux  3847行

从下往上走读：

版权信息

.. code-block:: c

    /* Module information */
    MODULE_AUTHOR("Joonyoung Shim <jy0922.shim@samsung.com>");
    MODULE_DESCRIPTION("Atmel maXTouch Touchscreen driver");
    MODULE_LICENSE("GPL");

设备树匹配的名称：

.. code-block:: c

    static const struct i2c_device_id mxt_id[] = {
        { "qt602240_ts", 0 },
        { "atmel_mxt_ts", 0 },
        { "atmel_mxt_tp", 0 },
        { "maxtouch", 0 },
        { "mXT224", 0 },
        { }
    };

待机模式操作

.. code-block:: c

    static SIMPLE_DEV_PM_OPS(mxt_pm_ops, mxt_suspend, mxt_resume);

    #define SIMPLE_DEV_PM_OPS(name, suspend_fn, resume_fn) \  
    const struct dev_pm_ops name = { \  
        SET_SYSTEM_SLEEP_PM_OPS(suspend_fn, resume_fn) \  
    }  

移除操作

.. code-block:: c

    static int mxt_remove(struct i2c_client *client)
    {
        struct mxt_data *data = i2c_get_clientdata(client);

        sysfs_remove_group(&client->dev.kobj, &mxt_fw_attr_group);
        mxt_debug_msg_remove(data);
        mxt_sysfs_remove(data);

    #ifndef __POLL
        if (data->irq)
            free_irq(data->irq, data);
    #endif

        regulator_put(data->reg_avdd);
        regulator_put(data->reg_vdd);
        mxt_free_input_device(data);
        mxt_free_object_table(data);
        kfree(data);

        return 0;
    }

插入操作

.. code-block:: c

    static int mxt_probe(struct i2c_client *client, const struct i2c_device_id *id)
    {
        struct mxt_data *data;
        const struct mxt_platform_data *pdata;
        int error;

        pdata = mxt_get_platform_data(client);	//获取平台数据
        if (IS_ERR(pdata))
            return PTR_ERR(pdata);

        data = kzalloc(sizeof(struct mxt_data), GFP_KERNEL);
        if (!data)
            return -ENOMEM;

        snprintf(data->phys, sizeof(data->phys), "i2c-%u-%04x/input0",
            client->adapter->nr, client->addr);

        data->client = client;
        data->pdata = pdata;
        i2c_set_clientdata(client, data);	//保存数据

        if (data->pdata->cfg_name)	//配置文件名
            mxt_update_file_name(&data->client->dev,
                        &data->cfg_name,
                        data->pdata->cfg_name,
                        strlen(data->pdata->cfg_name));

        init_completion(&data->chg_completion);
        init_completion(&data->reset_completion);
        init_completion(&data->crc_completion);
        mutex_init(&data->debug_msg_lock);

        if (pdata->suspend_mode == MXT_SUSPEND_REGULATOR) {
            __D;
            error = mxt_acquire_irq(data);
            if (error)
                goto err_free_mem;

            error = mxt_probe_regulators(data);
            if (error)
                goto err_free_irq;

            disable_irq(data->irq);
        }

        error = sysfs_create_group(&client->dev.kobj, &mxt_fw_attr_group);
        if (error) {
            dev_err(&client->dev, "Failure %d creating fw sysfs group\n",
                error);
            return error;
        }

        error = mxt_initialize(data);
        if (error)
            goto err_free_irq;

        return 0;

    err_free_irq:
        if (data->irq)
            free_irq(data->irq, data);
    err_free_mem:
        kfree(data);
        return error;
    }

获取平台数据

.. code-block:: c

    static const struct mxt_platform_data *
    mxt_get_platform_data(struct i2c_client *client)
    {
        const struct mxt_platform_data *pdata;

        pdata = dev_get_platdata(&client->dev);  //已经获取过就直接返回
        if (pdata)
            return pdata;

        pdata = mxt_parse_dt(client);		//解析dts//初始化gpio_reset，cfg_name，input_name，gpio-keymap，suspend_mode
        if (!IS_ERR(pdata) || PTR_ERR(pdata) != -ENOENT)
            return pdata;

        pdata = mxt_parse_acpi(client);
        if (!IS_ERR(pdata) || PTR_ERR(pdata) != -ENOENT)
            return pdata;

        pdata = mxt_default_pdata(client);
        if (!IS_ERR(pdata))
            return pdata;

        dev_err(&client->dev, "No platform data specified\n");
        return ERR_PTR(-EINVAL);
    }

获取中断

.. code-block:: c

    static int mxt_acquire_irq(struct mxt_data *data)
    {
        int error;
    #ifndef __POLL
        if (!data->irq) {	//没有中断的话申请中断线程
            error = request_threaded_irq(data->client->irq, NULL,
                    mxt_interrupt,
                    data->pdata->irqflags | IRQF_ONESHOT,
                    data->client->name, data);
            if (error) {
                dev_err(&data->client->dev, "Error requesting irq\n");
                return error;
            }

            /* Presence of data->irq means IRQ initialised */
            data->irq = data->client->irq;
        } else {	//存在中断，则使能
            enable_irq(data->irq);
        }
    #endif
        if (data->object_table && data->use_retrigen_workaround) {
            error = mxt_process_messages_until_invalid(data);
            if (error)
                return error;
        }

        return 0;
    }

中断服务例程

.. code-block:: c

    static irqreturn_t mxt_interrupt(int irq, void *dev_id)
    {
        struct mxt_data *data = dev_id;

        complete(&data->chg_completion);

        if (data->in_bootloader) {
            if (data->flash && &data->flash->work)
                cancel_delayed_work_sync(&data->flash->work);

            return IRQ_RETVAL(mxt_check_bootloader(data));
        }

        if (!data->object_table)
            return IRQ_HANDLED;

        if (data->T44_address) {	//有T44地址
            return mxt_process_messages_t44(data);
        } else {
            return mxt_process_messages(data);
        }
    }

处理消息

.. code-block:: c

    static irqreturn_t mxt_process_messages(struct mxt_data *data)
    {
        int total_handled, num_handled;
        u8 count = data->last_message_count;

        if (count < 1 || count > data->max_reportid)
            count = 1;

        /* include final invalid message */
        total_handled = mxt_read_and_process_messages(data, count + 1);
        if (total_handled < 0)
            return IRQ_NONE;
        /* if there were invalid messages, then we are done */
        else if (total_handled <= count)
            goto update_count;

        /* keep reading two msgs until one is invalid or reportid limit */
        do {
            num_handled = mxt_read_and_process_messages(data, 2);
            if (num_handled < 0)
                return IRQ_NONE;

            total_handled += num_handled;

            if (num_handled < 2)
                break;
        } while (total_handled < data->num_touchids);

    update_count:
        data->last_message_count = total_handled;

        if (data->update_input) {
            mxt_input_sync(data);
            data->update_input = false;
        }

        return IRQ_HANDLED;
    }
