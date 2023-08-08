# 移植FatFS，为RISCV添加FAT32文件系统

> 编辑于2022.05.26

- 原文链接:https://bbs.sipeed.com/thread/1482

搬运有改动。

首先新建一个项目工程，选型时不要选错型号。

## Gowin 相关设置

在 IP generator 生成中选择 Gowin_PicoRV32，软核最大可以跑到50MHz，这个频率做一些基本控制是绰绰有余的。

打开IP后，双击要修改的模块进行设置。

此处去掉了 RV32C 和 RV32M 指令集的扩展，关闭了Jtag debug功能。

然后是定制ITCM和DTCM，由于我选择将程序编译后直接放到ITCM中运行（MCU boot and run in ITCM），并且编译后的文件大约需要22KB，所以分给了ITCM 32KB的空间，DTCM保持默认16KB。

外设方面，启用UART来输出打印信息，SPI Master用于与SD卡通信，GPIO用来点灯。我还打开了AHB扩展，并在上面挂载了一片内存用于后续LCD的显存。

还需要调用PLL，为CPU提供50MHz的时钟，SD卡的读写速度也是50MHz，最后绑定好pin脚，生成FPGA的下载文件。

## GMD 相关的操作

接下去的工作就要转到[GMD](http://www.gowinsemi.com.cn/prodshow.aspx)中了。参考半导体官方文档[IPUG910](http://cdn.gowinsemi.com.cn/IPUG910-1.4_Gowin_PicoRV32_IDE%E8%BD%AF%E4%BB%B6%E5%8F%82%E8%80%83%E6%89%8B%E5%86%8C.pdf)进行开发环境搭建和程序编译，外设的驱动编写可以参考[IPUG911](http://cdn.gowinsemi.com.cn/IPUG911-1.3_Gowin_PicoRV32%E8%BD%AF%E4%BB%B6%E7%BC%96%E7%A8%8B%E5%8F%82%E8%80%83%E6%89%8B%E5%86%8C.pdf)，最后程序的下载可以参考[IPUG913](http://cdn.gowinsemi.com.cn/IPUG913-1.4_Gowin_PicoRV32%E8%BD%AF%E4%BB%B6%E4%B8%8B%E8%BD%BD%E5%8F%82%E8%80%83%E6%89%8B%E5%86%8C.pdf)。

C的开发环境搭建完成后，就开始进行SD卡驱动和fatfs的移植，这里我将SD卡作为只读设备，编写了相应的驱动。

### SD Command

SD卡的通信，主要是通过Matser发送CMD命令进行的，驱动见下面代码。

```c
#define SPI_ID 0

uint8_t sd_sendcmd(uint8_t cmd, uint32_t arg, uint8_t crc)
{
        uint8_t r1, cnt;

        cnt = 0;

        wbspi_master_select_slave(PICO_WBSPI_MASTER,SPI_ID);

        wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);

        wbspi_master_txdata(PICO_WBSPI_MASTER,(cmd | 0x40));
        wbspi_master_txdata(PICO_WBSPI_MASTER,arg>>24);
        wbspi_master_txdata(PICO_WBSPI_MASTER,arg>>16);
        wbspi_master_txdata(PICO_WBSPI_MASTER,arg>>8);
        wbspi_master_txdata(PICO_WBSPI_MASTER,arg);
        wbspi_master_txdata(PICO_WBSPI_MASTER,crc);

        do{
                r1 = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
                cnt++;
                if(cnt > 50) break;
        }while(r1 == 0xFF);

        return r1;
}
```

### SD Init

基于上面这个函数，就开始编写SD卡初始化函数，初始化的流程为：
1、发送大于74个周期的时钟信号，等待SD卡内部逻辑稳定；
2、发送CMD0，让SD卡进入IDLE状态；
3、发送CMD8，查询卡的型号是不是支持SD 2.0协议；
4、这里只处理支持SD 2.0协议的卡，发送CMD55+ACMD41进行初始化；
5、发送CMD58，查询卡支不支持SDHC；
6、发送CMD9，CMD10，获取SD卡的CID和OCR信息

```C
uint8_t sd_init(void)
{
        uint32_t i;
        uint8_t r1;
        uint8_t buff[16];
        uint8_t cnt = 0;

        wbspi_master_select_slave(PICO_WBSPI_MASTER,SPI_ID);
        for(i=0; i<1000; i++);

        for(i=0; i<10; i++)
                wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);

        r1 = sd_sendcmd(0,0,0x95);

        r1 = sd_sendcmd(8,0x1aa,0x87);
        if(r1 == 0x01)
        {
                buff[0] = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
                buff[1] = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
                buff[2] = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
                buff[3] = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);

                do{
                        r1 = sd_sendcmd(55,0,0);
                        if(r1 != 0x01)
                                return -1;

                        r1 = sd_sendcmd(41,0x40000000,1);
                        cnt++;
                        if(cnt>100) return -1;
                }while(r1!=0);
        }

        r1 = sd_sendcmd(58,0,0);
        if(r1 != 0x00) return -1;

        buff[0] = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
        buff[1] = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
        buff[2] = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
        buff[3] = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
        wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);

        if(buff[0]&0x40)
                printf("sdhc rdy\r\n");
        else
                printf("sd2.0 rdy\r\n");

        r1 = sd_sendcmd(9,0,0xFF);
        if(r1 != 0x00) return -1;
        do{
                r1 = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
        }while(r1 != 0xFE);

        for(i=0; i<16; i++)
        {
                r1 = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
        }

        r1 = sd_sendcmd(10,0,0xFF);
        if(r1 != 0x00) return -1;
        do{
                r1 = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
        }while(r1 != 0xFE);
        for(i=0; i<16; i++)
        {
                r1 = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
        }
        return 0;
}
```

### SD Read Block

下面是SD卡读单块和多块的驱动。

```C
BYTE SD_ReadSingleBlock(UINT sector, BYTE *buffer)
{
  BYTE r1;
  WORD i;
  i=512;

   r1 = sd_sendcmd(17, sector, 1);        //发送CMD17 读命令
   if(r1 != 0x00)        return r1;

   do{
                   r1 = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
   }while(r1 != 0xFE);

   while(i!=0)
   {
           *buffer = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
           buffer++;
           i--;
   }
   wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
   wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);


   return 0;                 //读取正确，返回0
}

BYTE SD_ReadMultiBlock(UINT sector, BYTE *buffer, BYTE count)
{
  BYTE r1;
  WORD i;

  r1 = sd_sendcmd(18, sector, 1);                //读多块命令
  if(r1 != 0x00)        return r1;

  while(count != 0){
          i = 512;
          do{
                        r1 = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
          }while(r1 != 0xFE);

          while(i!=0)
          {
                   *buffer = wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
                   buffer++;
                   i--;
          }
          buffer+=512;
          count--;
          wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
  }

  sd_sendcmd(12, 0, 1);        //全部传输完成，发送停止命令
  wbspi_master_txdata(PICO_WBSPI_MASTER,0xFF);
  if(count != 0)
    return count;   //如果没有传完，返回剩余个数
  else
    return 0;
}
```

### FatFs File system

SD卡驱动完成后，开始移植FatFs文件系统

源码下载：http://elm-chan.org/fsw/ff/archives.html 

选择最新的FatFs R0.14b ，并添加到工程。

FFConf.h用于FatFs的定制，这里需要将FF_FS_READONLY的宏改为1，将SD卡作为只读设备。

还需要改写diskio.c文件，适配SD卡。这里只做了最简单的适配，完成了初始化和读，查询状态和获取时间都是空函数。由于宏设置，这两个函数disk_ioctl和disk_write就不管了

```C
#define SD_CARD 0

DSTATUS disk_initialize (
        BYTE pdrv                   /* Physical drive nmuber (0..) */
)
{
        DRESULT status = STA_NOINIT;
        switch(pdrv)
        {
                case SD_CARD://SD卡
                        status = sd_init();
                          break;
                default:
                        status = STA_NOINIT;
        }   

        return status;
}  

//获得磁盘状态
DSTATUS disk_status (
        BYTE pdrv                   /* Physical drive nmuber (0..) */
)
{
        return 0;
}

//读扇区
//drv:磁盘编号0~9
//*buff:数据接收缓冲首地址
//sector:扇区地址
//count:需要读取的扇区数
DRESULT disk_read (
        BYTE pdrv,                  /* Physical drive nmuber (0..) */
        BYTE *buff,                 /* Data buffer to store read data */
        DWORD sector,               /* Sector address (LBA) */
        UINT count                  /* Number of sectors to read (1..128) */
)
{
        DRESULT status = RES_PARERR;
    if (!count)return RES_PARERR;   //count不能等于0，否则返回参数错误  
        switch(pdrv)
        {
                case SD_CARD://SD卡
                        if(count == 1)
                                status=SD_ReadSingleBlock(sector, buff);
                        else
                                status=SD_ReadMultiBlock(sector, buff, count);
                        break;
                default:
                        status=RES_PARERR;
        }

        return status;
}
DWORD get_fattime (void)
{         
        return 0;
}
```

最后进行测试，在SD卡的根目录放一个txt文件，然后RV32 CPU通过串口，将文件大小和内容打印出来。

```C
        res = f_mount(&fs, "", 1);
        res = f_open(&file, "top.txt", FA_READ);
        printf("\r\nfile size:%d\r\n", file.obj.objsize);
        f_read(&file, fbuff, file.obj.objsize, &br);
        printf("%s\r\n",fbuff);
        f_close(&file);
```

