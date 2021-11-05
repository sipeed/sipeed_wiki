# FPGA码流烧录

----

<font size = 5>**Attention!! 下载码流需要先保证驱动安装成功**</font>

1. 打开TD软件，选择 download
![](https://fdvad021asfd8q.oss-cn-hangzhou.aliyuncs.com/migrate/E203_TD_download.png)

2. 添加 bitstream文件，选择 [LicheeTangNewIoMap_BitStream.bit](https://fdvad021asfd8q.oss-cn-hangzhou.aliyuncs.com/LicheeTang/LicheeTangNewIoMap_BitStream.bit) 或其他码流文件
![](https://fdvad021asfd8q.oss-cn-hangzhou.aliyuncs.com/migrate/E203_TD_add.png)

3. 如果 Mode 为 JTAG，断电后则恢复默认，所以为了上电自动启动，需要选择 PROGRAM FLASH 。（时间较长）

4. E203源码已开放，如果需要进行IO修改，或者功能修改，请使用源码自行进行修改。可以到 [Github](https://github.com/Lichee-Pi/Tang_E203_Mini.git) 下载。

5. FPGA例程已上传，请到 [Tang_FPGA_Examples](https://github.com/Lichee-Pi/Tang_FPGA_Examples.git) 下载。