Blink 闪灯程序
=====

## 创建 Blink 工程

* 打开 PIO 主页 选择 `Project Examples`

![](http://blog.sipeed.com/wp-content/uploads/2019/04/d977e844490e6ccc4625f701883a29f5.png)

* 选择 `arduino blink` 点击 `Import` 导入示例程序 （初次导入需要下载架构文件及工具，需要等待较长时间）
![](http://blog.sipeed.com/wp-content/uploads/2019/04/82943a6b74077e6210e2d9421cb5438f.png)

* 导入成功后即可见到示例工程
![](http://blog.sipeed.com/wp-content/uploads/2019/04/1262373ca7b0b483e30dac1124adaabf.png)

## 工程配置文件


* 我们首先需要编辑工程配置文件 `platformio.ini` 根据自己的开发板型号，删掉其他开发板环境。

![](./../../assets/pio_ini_cfg.png)

配置示例
```ini
[env:sipeed-longan-nano]
platform = gd32v          ;平台，选择gd32v
framework = arduino       ;可选 gd32vf103-sdk 或 arduino
board = sipeed-longan-nano ; 开发板
monitor_speed = 115200     ; 串口监视器波特率
upload_protocol = serial   ; 下载工具 默认串口， 可选 dfu、jlink、gd-link 等
debug_tool = jlink         ; 调试工具 默认jlink ，可选 sipeed-rv-debugger 等
```
PIO 可以在配置文件中实现设置宏定义， 控制编译流程等自定义功能，高级用法请参阅 [PIO 官方文档](https://docs.platformio.org/en/latest/projectconf.html).

## 一键编译

点击左下角的 `Build` 即可构建项目
![](../../assets/pio_complie.png)

## 连接开发板
### 串口 ISP 下载
* 准备 USB 转 串口下载器
* 连接开发板与下载器
* 修改 `platformio.ini` 文件， 添加下面一行内容：
```ini
upload_protocol = serial
```
* 开发板按住 `BOOT` 键，再按 `RESET` 键重启开发板后再松开 `BOOT` 键，进入下载模式。

### JTAG 下载
* 准备J-link 或 Sipeed RV 调试器
* 连接开发板
* 修改 `platformio.ini` 文件， 添加下面一行内容：
```ini
upload_protocol = jlink
```
或者
```ini
upload_protocol = sipeed-rv-debugger
```

### USB DFU 下载
* **首次** 使用需要安装 libusb 驱动程序， 请参考此步骤 [使用 Zaidig 安装驱动](#使用zadig安装驱动).
* 准备 USB Type-c 数据线
* 使用数据线连接电脑与开发板
* 修改 `platformio.ini` 文件， 添加下面一行内容：
```ini
upload_protocol = dfu
```
* 开发板按住 `BOOT` 键，再按 `RESET` 键重启开发板后再松开 `BOOT` 键，进入 DFU 模式。


## 一键下载

按照上面步骤选择好下载方式后，即可使用 PIO 内置工具一键下载。

点击左下角的 `Upload` 即可向开发板上传程序。

![](../../assets/pio_upload.png)

## 使用Zadig安装驱动
PIO 内置 dfu-util 下载工具，使用此工具需要为开发板安装 libusb 驱动。（注意： 与 GD 官方驱动不同）

建议通过 Zadig 安装 winusb 驱动。[下载地址](https://github.com/pbatard/libwdi/releases/download/b721/zadig-2.4.exe)

下载成功后打开 Zadig

在下拉栏中选择 GD32V， 替换驱动选择 WinUSB, 点击替换按钮，即可替换成功。
![](../../assets/dfu_zadig.png)
## DFU 图形界面下载

下载DFU工具：http://dl.sipeed.com/LONGAN/Nano/Tools/GD32_MCU_Dfu_Tool_V3.8.1.5784_1.rar

解压出两个文件夹：

GD32 MCU Dfu Drivers_v1.0.1.2316  和 GD32 MCU Dfu Tool_v3.8.1.5784

先进入driver文件夹，安装对应的驱动文件，注意使用管理员权限运行

![](../../assets/examples/how_to_install_dfu.png)

运行 GD32 MCU Dfu Tool.exe
将 Longan Nano 插到电脑，按住 Boot0 键，短按 Reset 键，再松开 Boot0 键，
可以看到 DFU 工具中识别到了 GD32VF 芯片

选择对应的固件文件，并勾选烧录后校验，点击OK，即可进行烧录

烧录完成之后不会自动复位，需要自己手工按下复位按键，查看运行效果

![](../../assets/examples/how_to_use_dfu.png)
