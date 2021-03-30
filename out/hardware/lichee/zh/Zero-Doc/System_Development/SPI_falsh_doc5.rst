uboot 对SPI flash 的识别
=====================================================

.. contents:: 本文目录

flash信息在

.. code-block:: c
   :caption: drivers/mtd/spi/spi_flash_ids.c

    const struct spi_flash_info spi_flash_ids[] = {
            {"w25p80",         INFO(0xef2014, 0x0,  64 * 1024,    16, 0) },
            {"w25p16",         INFO(0xef2015, 0x0,  64 * 1024,    32, 0) },
            {"w25p32",         INFO(0xef2016, 0x0,  64 * 1024,    64, 0) },
            {"w25x40",         INFO(0xef3013, 0x0,  64 * 1024,     8, SECT_4K) },
            {"w25x16",         INFO(0xef3015, 0x0,  64 * 1024,    32, SECT_4K) },
            {"w25x32",         INFO(0xef3016, 0x0,  64 * 1024,    64, SECT_4K) },
            {"w25x64",         INFO(0xef3017, 0x0,  64 * 1024,   128, SECT_4K) },
            {"w25q80bl",       INFO(0xef4014, 0x0,  64 * 1024,    16, RD_FULL | WR_QPP | SECT_4K) },
            {"w25q16cl",       INFO(0xef4015, 0x0,  64 * 1024,    32, RD_FULL | WR_QPP | SECT_4K) },
            {"w25q32bv",       INFO(0xef4016, 0x0,  64 * 1024,    64, RD_FULL | WR_QPP | SECT_4K) },
            {"w25q64cv",       INFO(0xef4017, 0x0,  64 * 1024,   128, RD_FULL | WR_QPP | SECT_4K) },
            {"w25q128bv",      INFO(0xef4018, 0x0,  64 * 1024,   256, RD_FULL | WR_QPP | SECT_4K) },
            {"w25q256",        INFO(0xef4019, 0x0,  64 * 1024,   512, RD_FULL | WR_QPP | SECT_4K) },
            {"w25q80bw",       INFO(0xef5014, 0x0,  64 * 1024,    16, RD_FULL | WR_QPP | SECT_4K) },
            {"w25q16dw",       INFO(0xef6015, 0x0,  64 * 1024,    32, RD_FULL | WR_QPP | SECT_4K) },
            {"w25q32dw",       INFO(0xef6016, 0x0,  64 * 1024,    64, RD_FULL | WR_QPP | SECT_4K) },
            {"w25q64dw",       INFO(0xef6017, 0x0,  64 * 1024,   128, RD_FULL | WR_QPP | SECT_4K) },
            {"w25q128fw",      INFO(0xef6018, 0x0,  64 * 1024,   256, RD_FULL | WR_QPP | SECT_4K) },


    #define INFO(_jedec_id, _ext_id, _sector_size, _n_sectors, _flags)      \
                    .id = {                                                 \
                            ((_jedec_id) >> 16) & 0xff,                     \
                            ((_jedec_id) >> 8) & 0xff,                      \
                            (_jedec_id) & 0xff,                             \
                            ((_ext_id) >> 8) & 0xff,                        \
                            (_ext_id) & 0xff,                               \
                            },                                              \
                    .id_len = (!(_jedec_id) ? 0 : (3 + ((_ext_id) ? 2 : 0))),       \
                    .sector_size = (_sector_size),                          \
                    .n_sectors = (_n_sectors),                              \
                    .page_size = 256,                                       \
                    .flags = (_flags),


    struct spi_flash_info {
            /* Device name ([MANUFLETTER][DEVTYPE][DENSITY][EXTRAINFO]) */
            const char      *name;

            /*
            * This array stores the ID bytes.
            * The first three bytes are the JEDIC ID.
            * JEDEC ID zero means "no ID" (mostly older chips).
            */
            u8              id[SPI_FLASH_MAX_ID_LEN];
            u8              id_len;

            /*
            * The size listed here is what works with SPINOR_OP_SE, which isn't
            * necessarily called a "sector" by the vendor.
            */
            u32             sector_size;
            u32             n_sectors;

            u16             page_size;

            u16             flags;

            
    #define SECT_4K                 BIT(0)  /* CMD_ERASE_4K works uniformly */
    #define E_FSR                   BIT(1)  /* use flag status register for */
    #define SST_WR                  BIT(2)  /* use SST byte/word programming */
    #define WR_QPP                  BIT(3)  /* use Quad Page Program */
    #define RD_QUAD                 BIT(4)  /* use Quad Read */
    #define RD_DUAL                 BIT(5)  /* use Dual Read */
    #define RD_QUADIO               BIT(6)  /* use Quad IO Read */
    #define RD_DUALIO               BIT(7)  /* use Dual IO Read */
    #define RD_FULL                 (RD_QUAD | RD_DUAL | RD_QUADIO | RD_DUALIO)
    };
