sunxi-fel增加对16M以上Flash的支持
=====================================================

.. contents:: 本文目录

由于SPI flash 的地址是24bit，也就是最大16M 地址空间，所以对于32M flash，需要增加bank切换支持。

uboot中有 *CONFIG_SPI_FLASH_BAR* 选项可以使能bank切换。

但是sunxi-fel中尚未支持，所以下载的时候超出16M会循环覆盖掉。

这里介绍对sunxi-fel增加16M以上flash支持的方法。

u-boot的支持
-----------------------------------------------------

.. code-block:: c
   :caption: drivers/mtd/spi/spi_flash.c

    static int write_bar(struct spi_flash *flash, u32 offset)
    {
        u8 cmd, bank_sel;
        int ret;

        bank_sel = offset / (SPI_FLASH_16MB_BOUN << flash->shift);
        if (bank_sel == flash->bank_curr)
            goto bar_end;

        cmd = flash->bank_write_cmd;
        ret = spi_flash_write_common(flash, &cmd, 1, &bank_sel, 1);
        if (ret < 0) {
            debug("SF: fail to write bank register\n");
            return ret;
        }

    bar_end:
        flash->bank_curr = bank_sel;
        return flash->bank_curr;
    }

sunxi-fel的支持
-----------------------------------------------------

.. code-block:: c
   :caption: fel-spiflash.c

    #define CMD_WRITE_ENABLE 0x06
    #define SPI_FLASH_16MB_BOUN  0x1000000
    # define CMD_BANKADDR_BRWR              0x17	//only SPANSION flash use it
    # define CMD_BANKADDR_BRRD              0x16
    # define CMD_EXTNADDR_WREAR             0xC5
    # define CMD_EXTNADDR_RDEAR             0xC8
    size_t bank_curr = 0;

    void aw_fel_spiflash_write_helper(feldev_handle *dev,
                    uint32_t offset, void *buf, size_t len,
                    size_t erase_size, uint8_t erase_cmd,
                    size_t program_size, uint8_t program_cmd)
    {
        uint8_t *buf8 = (uint8_t *)buf;
        size_t max_chunk_size = dev->soc_info->scratch_addr - dev->soc_info->spl_addr;
        size_t cmd_idx, bank_sel;

        if (max_chunk_size > 0x1000)
            max_chunk_size = 0x1000;
        uint8_t *cmdbuf = malloc(max_chunk_size);
        cmd_idx = 0;

        prepare_spi_batch_data_transfer(dev, dev->soc_info->spl_addr);
        //add bank support
        {
        cmd_idx = 0;
        bank_sel = offset /SPI_FLASH_16MB_BOUN;
        if (bank_sel == bank_curr)
            goto bar_end;

        /* Emit write enable command */
        cmdbuf[cmd_idx++] = 0;
        cmdbuf[cmd_idx++] = 1;
        cmdbuf[cmd_idx++] = CMD_WRITE_ENABLE;
        /* Emit write bank */
        cmdbuf[cmd_idx++] = 0;
        cmdbuf[cmd_idx++] = 2;
        cmdbuf[cmd_idx++] = CMD_EXTNADDR_WREAR;
        cmdbuf[cmd_idx++] = offset >> 24;
        /* Emit wait for completion */
        cmdbuf[cmd_idx++] = 0xFF;
        cmdbuf[cmd_idx++] = 0xFF;
        /* Emit the end marker */
        cmdbuf[cmd_idx++] = 0;
        cmdbuf[cmd_idx++] = 0;
        aw_fel_write(dev, cmdbuf, dev->soc_info->spl_addr, cmd_idx);
        aw_fel_remotefunc_execute(dev, NULL);
        bar_end:
            bank_curr = bank_sel;
        }
        
        cmd_idx = 0;

重新编译sunxi-fel后就可以烧录32M flash了~
