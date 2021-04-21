---
title: 更新 MaixPy 固件
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 更新 MaixPy 固件
---


## 准备

硬件:

- USB Type-C 数据线
- MaixPy 开发板
- PC(电脑)

软件:

- MaixPy 开发板 USB 驱动程序
- kflash_gui

## 确认驱动已经正确安装

按照前面的说明安装好驱动，并且在电脑中能看到串口设备, `Linux` 和 `Mac OS` 执行 `ls /dev/` 即可看到设备号，比如名字是`ttyUSB0`和`ttyUSB1`; `Windows`在设备管理器中查看


## 获得升级工具

* 下载 [kflash_gui](https://github.com/sipeed/kflash_gui/releases), 会得到一个压缩包
> kflash_gui 是跨平台的，可以在多个系统下工作（包括 Windows、Linux、MacOS、甚至树莓派）
> 使用勘智（Kendryte）的`Windows`版本可能部分开发版无法下载成功，请使用 `kflash_gui` 这个软件来下载

* 解压到一个文件夹，双击 `kflash_gui.exe`(/`kflsh_gui`) 即可运行, `Windows`下建议右键`固定到开始页面` 或者`固定到任务栏`, `Linux` 下可以自己新建一个[kflash_gui.desktop](https://github.com/sipeed/kflash_gui/blob/master/kflash_gui.desktop), 修改文件地址, 使用管理员身份复制到`/usr/share/application`目录，然后在系统菜单界面就可以看到`kflash_gui`这款应用了

* 另外也可以使用命令行版本下载

```shell
pip3 install kflash
kflash --help
kflash -p /dev/ttyUSB0 -b 1500000 -B goE maixpy.bin
```

## 获得固件

* 发布版本的固件从 [github](https://github.com/sipeed/MaixPy/releases) 页面下载
* 最新提交的代码自动构建生成的固件下载： [master 分支](http://dl.sipeed.com/MAIX/MaixPy/release/master/)



固件为 `.bin` 结尾或者 `.kfpkg` 的文件
>`.kfpkg`其实就是多个`.bin`文件的打包版本, 可以使用`kflash_gui`打包或者[手动打包](http://blog.sipeed.com/p/390.html)

![MaixPy Firmware Type](../../assets/maixpy/firmware_type.png)

固件命名说明：

| 文件名                                              | 说明                                                         | 备注                       |
| --------------------------------------------------- | ------------------------------------------------------------ | -------------------------- |
| `maixpy_vx.y.z_x_xxx*.bin`                          | 默认版本的 MaixPy 固件，包含了大多数功能, 支持连接 `MaixPy IDE`, | 出厂默认固件版本           |
| `maixpy_vx.y.z_x_xxx*_m5stickv.bin`                 | 针对 M5Stickv 定制的固件, 支持连接 `MaixPy IDE`              | —                          |
| `maixpy_vx.y.z_x_xxx*_with_lvgl.bin`                | MaixPy 固件, 支持连接 `MaixPy IDE`, 带 LVGL 版本.(LVGL是嵌入式 GUI 框架, 写界面的时候需要用到) | —                          |
| `maixpy_vx.y.z_x_xxx*_minimum.bin`                  | MaixPy 固件最小集合，不支持 `MaixPy IDE`, 不包含`OpenMV`的相关算法和各种外设模块 | —                          |
| `maixpy_vx.y.z_x_xxx*_minimum_with_ide_support.bin` | MaixPy 固件最小集合, 支持连接 `MaixPy IDE`, 不包含`OpenMV`的相关算法和各种外设模块 | 运行各种模型，建议使用这个 |
| `elf_maixpy_vx.y.z_x_xxx*.7z`                       | elf 文件，普通用户不用关心，用于死机调试                     | —                          |
| `face_model_at_0x300000.kfpkg`                      | 人脸模型，放置在地址位 0x300000, 可以和`.bin`分开多次下载，不冲突 | —                          |



## 下载固件到开发板

* 打开 `kflash_gui` 应用

* 然后选择固件、设置选项, 点击下载即可, 更多特性介绍、使用说明见 [kflash_gui 项目主页](https://github.com/sipeed/kflash_gui)

使用时注意串口不能被其它软件占用，选择正确的开发板和串口号，可以适当降低波特率和使用低速模式来提高下载成功率

![](../../assets/kflash_gui/kflash_gui_download.png)




> 对于最早期的 `Maix Go`, 如果确认选项是对的，仍然无法下载, 可以尝试将三相拨轮按键拨向 `Down` 的位置并保持再下载

### Sipeed RV JATG 调试器

[Sipeed USB-JTAG/TTL RISC-V调试器 STLINK V2 STM8/STM32模拟器](https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-21231188706.40.505a5d544ooyDY&id=595953803239)


**烧录常见问题FAQ**

如果在使用 `kflash_gui` 烧录出现以下等问题

![Upgrade Error](../../assets/kflash_gui/kflash_gui_upgrade_error.png)

可以按照以下顺序进行排查

* 检查`PC`是否有权限打开端口，对于 `win10`，需要以管理员身份运行 `kflash_gui`  。
* 检查端口是否选择正确（如果出现两个设备端口，通常选择端口号小的那一个）。
* 检查端口是否被其他应用占用（如`Maixpy IDE`，`putty`等），应当关闭其他程序占用。
* 检查设备是否选择正确，对于 `Maix Bit2.0`（包括M1n模块），应该选择 `Maix Bit ( with Mic )`。

> 补充说明：对于Maix Bit 2.0两个串口端口的问题
>
> * 只有其中一个串口端口有效，用于串口通信与ISP下载程序。
> * Maix Bit与PC采用串口通信，通过CH552T芯片实现USB虚拟串口功能，而该芯片可以虚拟出两个串口，在Maix Bit（M1n模块底板）中，我们只用到了一个串口，不过有些k210产品两个串口都使用了。
