atmel触摸屏中断改轮询
=============================

.. contents:: 本文目录

普通电容式触摸屏是中断方式的，由于v3s引脚较少，所以尝试改为轮询方式驱动，节省一个IO。

.. code-block:: c

    static int __devexit mxt_remove(struct i2c_client *client)
    #ifndef _TS_POLL
        free_irq(data->irq, data);
    #endif

.. code-block:: c

    static int __devinit mxt_probe(struct i2c_client *client,
            const struct i2c_device_id *id)
    err_free_irq:
    #ifndef _TS_POLL
        free_irq(client->irq, data);
    #endif

    #ifndef _TS_POLL
        error = request_threaded_irq(client->irq, NULL, mxt_interrupt,
                pdata->irqflags, client->dev.driver->name, data);
        if (error) {
            dev_err(&client->dev, "Failed to register interrupt\n");
            goto err_free_object;
        }
        error = input_register_device(input_dev);
        if (error)
            goto err_free_irq;
    #else
        {
            struct input_polled_dev *polled_dev;
            polled_dev = devm_input_allocate_polled_device(dev);
            if (!polled_dev) {
                dev_err(dev,
                    "Failed to allocate polled input device\n");
                return -ENOMEM;
            }
            polled_dev->private = data;
            polled_dev->poll = mxt_poll;
            polled_dev->poll_interval = POLL_INTERVAL;
            polled_dev->input = input_dev;

            error = input_register_polled_device(polled_dev);
        }
    #endif

    #ifdef _TS_POLL
    #define POLL_INTERVAL 5

    static void mxt_poll(struct input_polled_dev *dev)
    {
        struct mxt_data *data = dev->private;
        struct mxt_message message;
        struct mxt_object *object;
        struct device *dev = &data->client->dev;
        int id;
        u8 reportid;
        u8 max_reportid;
        u8 min_reportid;

        do {
            if (mxt_read_message(data, &message)) {
                dev_err(dev, "Failed to read message\n");
                goto end;
            }

            reportid = message.reportid;

            /* whether reportid is thing of MXT_TOUCH_MULTI_T9 */
            object = mxt_get_object(data, MXT_TOUCH_MULTI_T9);
            if (!object)
                goto end;

            max_reportid = object->max_reportid;
            min_reportid = max_reportid - object->num_report_ids + 1;
            id = reportid - min_reportid;

            if (reportid >= min_reportid && reportid <= max_reportid)
                mxt_input_touchevent(data, &message, id);
            else
                mxt_dump_message(dev, &message);
        } while (reportid != 0xff);

    end:
        return;
    }
    #endif

.. code-block:: c

    #ifndef _FLIP_X
	input_report_abs(input_dev, ABS_MT_POSITION_X, finger[id].x);
	#else
	input_report_abs(input_dev, ABS_MT_POSITION_X, 800-finger[id].x);
	#end
	#ifndef _FLIP_Y		
	input_report_abs(input_dev, ABS_MT_POSITION_Y, finger[id].y);
	#else
	input_report_abs(input_dev, ABS_MT_POSITION_Y, 480-finger[id].y);
	#endif
