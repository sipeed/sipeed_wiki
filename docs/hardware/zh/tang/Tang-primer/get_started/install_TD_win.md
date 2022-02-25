# Windows的开发环境配置

## 安装TD

想要进行FPGA开发需要安装TD，可以通过[下载站](https://dl.sipeed.com/shareURL/TANG/Premier/IDE)，下载TD安装包和license，如果下载速度过慢的时候，建议使用[百度网盘](https://eyun.baidu.com/s/3i6FbQzr)进行下载

![TD_1](./../../assets/get_started/TD_1.png)
![TD_2](./../../assets/get_started/TD_2.png)

双击打开第一个文件进行安装，建议使用默认的安装路径，安装结束之后，将 Anlogic_20220130.lic 修改成Anlogic.lic放到C:\Anlogic\TD5.0.27252\license中

然后打开TD就可以了

## 安装usb串口

将 Tang Primer 插入您的计算机并打开设备管理器以查看信息。 根据 Windows 版本，它可能被命名为 WinUsb Device 或 USB-JTAG-Cable。 确保 USB VID:PID 为 0547:1002
win7系统没有安装驱动时
![no_driver](./../../assets/get_started/no_driver.png)

win10系统没有安装驱动时
![no_driver_win10](./../../assets/get_started/no_driver_win10.png)

### win7安装驱动

双击 WinUsb Device 选择更新驱动程序 
![update_drive1](./../../assets/get_started/update_driver1.png)
![update_drive2](./../../assets/get_started/update_driver2.png)

浏览文件夹，选择TD安装目录下的驱动目录。 单击确定开始安装
![choosefolder](./../../assets/get_started/choosefolder.png)

安装成功，在设备管理器中可以看到 
![installsuccess](./../../assets/get_started/installsuccess.png)

### win10安装驱动

> 在安装驱动程序本身之前，请确保首先禁用驱动程序签名强制，否则 Windows 10 将不允许您安装来自 Anlogic 的未签名驱动程序

双击 WinUsb Device 选择更新驱动程序 
![update_drive1](./../../assets/get_started/update_driver1_win10.png)
![update_drive2](./../../assets/get_started/update_driver2_win10.png)

浏览文件夹，选择TD安装目录下的driver\win8_10_64目录。 单击确定。 然后单击让我从计算机上的可用驱动程序列表中选择
![choosefolder](./../../assets/get_started/choosefolder_win10.png)

单击Have Disk...，然后选择您在上一步中选择的目录，然后单击OK  
![install_from_disk_win10](./../../assets/get_started/install_from_disk_win10.png)

安装成功，在设备管理器中可以看到
![installsuccess](./../../assets/get_started/installsuccess.png)

## 验证安装
打开TD，点击下载,如图所示
![](./../../assets/get_started/87078310026779781.jpg)

将 Tang Primer 插入您的计算机，然后点击下载对话框上的刷新按钮
![](./../../assets/get_started/1823555291194601.jpg)

出现上图的信息，则表示安装成功