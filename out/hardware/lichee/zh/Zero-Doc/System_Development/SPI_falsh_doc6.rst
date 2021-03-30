关于系统reboot
=================================

.. contents:: 本文目录

在使用spi flash时，执行reboot命令，有时会无法重启，这里追查下原因。

正常重启信息
---------------------------------

:: 

    # reboot 
    # Stopping network: OK
    Saving random seed... done.
    Stopping logging: OK
    umount: devtmpfs busy - remounted read-only
    [   16.812893] EXT4-fs (mmcblk0p2): re-mounted. Opts: (null)
    Sent SIGTERM to all processes
    Sent SIGKILL to all processes
    Requesting system reboot
    [   18.830716] reboot: Restarting system

.. code-block:: c
   :caption: kernel/reboot.c:

    void kernel_restart(char *cmd)
    {
            kernel_restart_prepare(cmd);
            migrate_to_reboot_cpu();
            syscore_shutdown();
            if (!cmd)
                    pr_emerg("Restarting system\n");
            else
                    pr_emerg("Restarting system with command '%s'\n", cmd);
            kmsg_dump(KMSG_DUMP_RESTART);
            machine_restart(cmd);
    }

arch/arm/kernel/setup.c:  ``arm_pm_restart = mdesc->restart;``

重启失败
-------------------------------------

.. code-block:: c
   :caption: arch/arm/kernel/reboot.c

    void machine_restart(char *cmd)
    {       
            local_irq_disable();
            smp_send_stop();
            
            if (arm_pm_restart)
                    arm_pm_restart(reboot_mode, cmd);
            else    
                    do_kernel_restart(cmd);
            //正常来说不会走到这里
            /* Give a grace period for failure to restart of 1s */
            mdelay(1000);
            
            /* Whoops - the platform was unable to reboot. Tell the user! */
            printk("Reboot failed -- System halted\n");
            while (1);
    }


.. code-block:: c
   :caption: kernel/reboot.c

    void do_kernel_restart(char *cmd)
    {
            atomic_notifier_call_chain(&restart_handler_list, reboot_mode, cmd);
    }
    register_restart_handler


.. code-block:: c
   :caption: kernel/notifier.c

    int atomic_notifier_call_chain(struct atomic_notifier_head *nh,
                    unsigned long val, void *v)
    {
        return __atomic_notifier_call_chain(nh, val, v, -1, NULL);
    }

spi flash问题

:: 

    [  312.719945] INFO: trying to register non-static key.
    [  312.724967] the code is fine but needs lockdep annotation.
    [  312.730448] turning off the locking correctness validator.
    [  312.735943] CPU: 0 PID: 162 Comm: sync Not tainted 4.13.0-licheepi-zero+ #55
    [  312.742981] Hardware name: Allwinner sun8i Family
    [  312.747734] [<c010e8a8>] (unwind_backtrace) from [<c010b594>] (show_stack+0x10/0x14)
    [  312.755483] [<c010b594>] (show_stack) from [<c048ec4c>] (dump_stack+0x84/0x98)
    [  312.762711] [<c048ec4c>] (dump_stack) from [<c015e698>] (register_lock_class+0x3f8/0x624)
    [  312.770886] [<c015e698>] (register_lock_class) from [<c015fb0c>] (__lock_acquire.constprop.7+0x60/0x954)
    [  312.780358] [<c015fb0c>] (__lock_acquire.constprop.7) from [<c0160468>] (lock_acquire+0x68/0x84)
    [  312.789143] [<c0160468>] (lock_acquire) from [<c0132498>] (flush_work+0x50/0x290)
    [  312.796624] [<c0132498>] (flush_work) from [<c0133f00>] (__cancel_work_timer+0xec/0x1c4)
    [  312.804722] [<c0133f00>] (__cancel_work_timer) from [<c028d1b4>] (jffs2_sync_fs+0x14/0x38)
    [  312.812995] [<c028d1b4>] (jffs2_sync_fs) from [<c0207e30>] (iterate_supers+0xc0/0x120)
    [  312.820912] [<c0207e30>] (iterate_supers) from [<c0233708>] (sys_sync+0x44/0xa4)
    [  312.828310] [<c0233708>] (sys_sync) from [<c0107620>] (ret_fast_syscall+0x0/0x3c)


.. code-block:: c
   :caption: fs/jffs2/super.c

    static int jffs2_sync_fs(struct super_block *sb, int wait)
    {
            struct jffs2_sb_info *c = JFFS2_SB_INFO(sb);

    #ifdef CONFIG_JFFS2_FS_WRITEBUFFER
            cancel_delayed_work_sync(&c->wbuf_dwork);
    #endif

            mutex_lock(&c->alloc_sem);
            jffs2_flush_wbuf_pad(c);
            mutex_unlock(&c->alloc_sem);
            return 0;
    }

    bool cancel_delayed_work_sync(struct delayed_work *dwork)
    {
        return __cancel_work_timer(&dwork->work, true);
    }
    EXPORT_SYMBOL(cancel_delayed_work_sync);

*CONFIG_JFFS2_FS_WRITEBUFFER* 去掉，可以不出现oops信息

原因
--------------------------------------------

是使用了32M flash，在重启的时候，没有退出4-byte地址模式导致。（因为板子上没有PMU，没有对flash进行复位）


.. code-block:: c

    static void spi_nor_set_4byte_opcodes(struct spi_nor *nor,
                                        const struct flash_info *info)
    {
            /* Do some manufacturer fixups first */
            switch (JEDEC_MFR(info)) {
            case SNOR_MFR_SPANSION:
                    /* No small sector erase for 4-byte command set */
                    nor->erase_opcode = SPINOR_OP_SE;
                    nor->mtd.erasesize = info->sector_size;
                    break;

            default:
                    break;
            }

            nor->read_opcode = spi_nor_convert_3to4_read(nor->read_opcode);
            nor->program_opcode = spi_nor_convert_3to4_program(nor->program_opcode);
            nor->erase_opcode = spi_nor_convert_3to4_erase(nor->erase_opcode);
    }

    /* Enable/disable 4-byte addressing mode. */
    static inline int set_4byte(struct spi_nor *nor, const struct flash_info *info,
                                int enable)
    {
            int status;
            bool need_wren = false;
            u8 cmd;

            switch (JEDEC_MFR(info)) {
            case SNOR_MFR_MICRON:
                    /* Some Micron need WREN command; all will accept it */
                    need_wren = true;
            case SNOR_MFR_MACRONIX:
            case SNOR_MFR_WINBOND:
                    if (need_wren)
                            write_enable(nor);   //nor->write_reg(nor, SPINOR_OP_WREN, NULL, 0);

                    cmd = enable ? SPINOR_OP_EN4B : SPINOR_OP_EX4B;
                    status = nor->write_reg(nor, cmd, NULL, 0);
                    if (need_wren)
                            write_disable(nor);

                    return status;
            default:
                    /* Spansion style */
                    nor->cmd_buf[0] = enable << 7;
                    return nor->write_reg(nor, SPINOR_OP_BRWR, nor->cmd_buf, 1);
            }
    }

.. code-block:: c

    struct m25p {
            struct spi_device       *spi;
            struct spi_nor          spi_nor;
            u8                      command[MAX_CMD_SIZE];
    };

.. code-block:: c

    static int m25p_remove(struct spi_device *spi)
    {
            struct m25p     *flash = spi_get_drvdata(spi);
    //add to exit 4-byte address mode

            /* Clean up MTD stuff. */
            return mtd_device_unregister(&flash->spi_nor.mtd);
    }

新增关机接口
--------------------------------------------

.. code-block:: c

    static void m25p_shutdown(struct spi_device *spi)
    {               
            struct m25p     *flash = spi_get_drvdata(spi);
            struct spi_nor nor = flash->spi_nor;
    int status;             
    //add to exit 4-byte address mode       
    nor.write_reg(&nor, SPINOR_OP_WREN, NULL, 0);
    status = nor.write_reg(&nor, SPINOR_OP_EX4B, NULL, 0);
    printk("remove spi flash!\n"); 
            /* Clean up MTD stuff. */
            mtd_device_unregister(&flash->spi_nor.mtd);
            return;         
    }   

.. code-block:: c

    static struct spi_driver m25p80_driver = {
            .driver = {
                    .name   = "m25p80",
                    .of_match_table = m25p_of_table,
            },
            .id_table       = m25p_ids,
            .probe  = m25p_probe,
            .remove = m25p_remove,
            .shutdown = m25p_shutdown,
            /* REVISIT: many of these chips have deep power-down modes, which
            * should clearly be entered on suspend() to minimize power use.
            * And also when they're otherwise idle...
            */
    };

**CONFIG_SPI_FLASH_BAR**

参考资料
-------------------------------

| http://www.wowotech.net/linux_kenrel/reboot.html

   http://blog.csdn.net/manfeel/article/details/43530817
