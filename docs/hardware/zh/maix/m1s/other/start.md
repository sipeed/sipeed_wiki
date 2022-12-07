---
title: M1s DOCK 上手
keywords: M1s DOCK ,BL808, M1s
update:
  - date: 2022-11-23
    version: v0.1
    author: wonder
    content:
      - 初次编辑
---

M1s Dock 设计精巧，可以用来所很多有意思的事，这里简单说明一下一些使用方法。

## 初见

首次对 M1s Dock 板子上电，屏幕会显示摄像头所拍摄到的内容，且按两侧的按键显示屏上的数字会有变化。

![default_firmware](./assets/start/default_firmware.jpg)

通过 OTG 口连接 PC 的话会有一个大小为 3M 的 U 盘

![default_udisk](./assets/start/default_udisk.jpg)

通过 UART 口连接 PC 会显示有两个串口设备

![dual_uart](./assets/start/dual_uart.jpg)

## U 盘烧录

推荐使用这种方法来进行烧录，主要用来给板子上的 C906 核心烧录运行程序。

先使用 TypeC 数据线将电脑与板子的 OTG 口连接起来，再同时按住板子上面两侧的按键（已经在下面图片中指明），然后按一下板子上的 RST 键就可以进入 U 盘烧录模式。

<table>
    <tr>
        <td><img src="./assets/start/udisk_burn.png" alt="udisk_burn" style="transform:rotate(0deg);"></td>    
        <td>同时按住两侧的按键然后按一下 RST 键来复位板子，并让它进入 U 盘烧录模式</td>
    </tr>
</table>

另外，按住两侧按键的时候，从板子的 OTG 口板子给板子通电来启动板子也可以进入 U 盘下载模式。

<img src="./assets/start/udisk_in_computer.png" alt="udisk_in_computer" style="transform:rotate(0deg);">

板子成功进入 U 盘烧录模式后在电脑上会显示出一个容量很小的磁盘，直接把固件 <a href="https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/7_Firmware/demo_bin">点我跳转部分例程固件</a> 拖拽进去即可完成烧录。。

<img src="./assets/start/udisk_burn.gif" alt="udisk_burn" style="transform:rotate(0deg);">

文件存放进去后数秒后板子会重启，U 盘被弹出，表示烧录完成，看不到效果的话可以给板子重新插拔板子 USB 来完全重启一次再来查看烧录结果。

## 串口烧录

上面的 U 盘烧录方法适用于给 C906 核心烧录代码，当板子出现固件错误或者需要进行固件升级等操作时，我们需要通过串口来给板子烧录固件。

### 给 M1s 烧录

使用 TypeC 数据线将电脑与板子的 UART 口连接起来，此时电脑上会出现两个串口 （如果出现鼠标不能动的现象请拔掉 USB 并且查看 [更新板载 bl702 固件](#给板载-bl702-进行烧录) 相关内容来修复问题)。

给 M1s 烧录需要用到博流官方烧录工具，前往 https://dev.bouffalolab.com/download 下载名称为 `Bouffalo Lab Dev Cube` 的文件。解压后就得到了用来烧录板子的应用程序。

![bouffalo_cube](./assets/start/bouffalo_cube.png)

解压后的文件夹中主要关注 `BLDevCube`、 `BLDevCube-macos` 和 `BLDevCube-ubuntu` 三个文件，用于在不同系统启动这个烧录工具。

![application](./assets/start/application.png)

启动软件后选择 bl808 ，紧着这软件的 IOT 页面选择分区表文件[点我下载](https://dl.sipeed.com/fileList/MAIX/M1s/M1s_Dock/7_Firmware/partition/partition_cfg_16M_m1sdock.toml)（图里②）。

<table>
    <tr>
        <td><img src="./assets/start/chip_selection.png" alt="chip_selection" style="transform:rotate(0deg);"></td>    
        <td><img src="./assets/start/choose_partition.png" alt="choose_partition" style="transform:rotate(0deg);" width="70%"></td>
    </tr>
</table>

选择完上面的分区表文件后，烧录工具的可选项就变多了，主要关注 `boot2`, `firmware`, `d0fw` 三项。

<img src="./assets/start/firmware_choose.png" alt="firmware_choose" style="transform:rotate(0deg);">

上图中，`boot2` 是固定的，位于 `BLDevCube\chips\bl808\builtin_imgs\boot2_isp_bl808_v6.4_rc6` 目录下，就是在解压的烧录程序文件夹的子目录里面；`firmware` 是 E907 核心运行的固件 ；`d0fw`是 C906 核心运行的固件，前面的 U 盘烧录里面的固件就是给这个核心烧录的。E907 的固件文件和 C906 的固件文件均可以通过 [M1s_dock example](https://gitee.com/sipeed/M1s_BL808_example) 来编译得到。

默认固件可以在 [这里下载到](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/7_Firmware/factory)。

正确的选择固件后，在窗口右侧点击一下 `Refresh` 来刷新串口，正常情况有两个串口号相邻的串口可供选择，如果没有两个串口请参考下面的 [烧录 BL702](#给板载-bl702-进行烧录)来查看解决方法。在双串口中需要选择串口号较大的那个。设置波特率 2000000。

![burn_steps](./assets/start/burn_steps.png)

点击下载后按住板子上的 BOOT 键和 RST 键， 然后先松开 RST 键再松开 BOOT 键来给板子烧录固件。

<table>
    <tr>
        <td><img src="./assets/start/boot_rst.jpg" alt="boot_rst" style="transform:rotate(0deg);"></td>    
        <td><img src="./assets/start/finish_burning.png" alt="finish_burning" style="transform:rotate(0deg);" width="70%"></td>
    </tr>
</table>

### 给板载 bl702 进行烧录

一般来说板子出问题才进行这里的烧录。

在给板子通电前按住板子上的 BOOT 按键，然后通过板子上的 UART USB 接口连接电脑，此时板载 bl702 进入下载模式，打开 `BLDevCube` 烧录软件，选择 `BL702` 芯片，在打开的软件界面选择 MCU 模式，接着可以在 [这里](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/7_Firmware) 下载到 bl702 的固件，名称为 `usb2dualuart_bl702` 开头的就是我们需要烧录的文件。

<table>
    <tr>
        <td><img src="./assets/start/select_bl702.png" alt="select_bl702" style="transform:rotate(0deg);"></td>    
        <td><img src="./assets/start/mcu_mode.png" alt="mcu_mode" style="transform:rotate(0deg);" width="70%"></td>
    </tr>
</table>

点击 `Refresh`，选择唯一的串口（如果看到的不是唯一串口，记得是先按住 BOOT 键，再给板子上电），设置波特率 2000000， 点击下载烧录。

![burn_bl702](./assets/start/burn_bl702.png)

烧录结束后，重新插拔一次 USB 来重新启动 bl702 以应用新的固件。

![finish_burn_702](./assets/start/finish_burn_702.png)

## SDK 编译

M1s 需要在 Linux 环境下进行编译

### 获取例程仓库

```bash
git clone https://gitee.com/Sipeed/M1s_BL808_example.git
```

最终结构树如下

```bash
sipeed@DESKTOP:~$ tree -L 1 M1s_BL808_example/
M1s_BL808_example/
├── LICENSE           # 许可证文件
├── assets            # 资源文件
├── c906_app          # C906 核心例程
├── e907_app          # E907 核心例程
├── partition         # 分区表文件
└── readme.md         # 仓库说明
```

### 获得 SDK 仓库

仓库很大，120M 以上。

```bash
git clone https://gitee.com/sipeed/M1s_BL808_SDK.git
```

最终结构树如下

```bash
sipeed@DESKTOP:~$ tree -L 1 
.
├── M1s_BL808_example   # 例程文件夹
└── M1s_BL808_SDK          # SDK 文件夹
```

### 在 SDK 仓库文件夹下，获取编译工具链

根据例程仓库里面的 readme 的要求，工具链应存放在 M1s_BL808_SDK/toolchain 目录下

```bash
mkdir -p M1s_BL808_SDK/toolchain
cd M1s_BL808_SDK/toolchain
git clone https://gitee.com/wonderfullook/m1s_toolchain.git
```

修改工具链的名称为 `Linux_x86_64` ，然后返回到上两级目录

```bash
mv m1s_toolchain Linux_x86_64
cd ../../
```

这时得到的结构树应如下(截取部分)：

```bash
sipeed@DESKTOP:~$ tree -L 2
.
├── M1s_BL808_example     # 例程仓库文件夹
│   ├── LICENSE           # 许可证文件
│   ├── assets            # 资源文件
│   ├── c906_app          # C906 核心例程
│   ├── e907_app          # E907 核心例程
│   ├── partition         # 分区表文件
│   └── readme.md         # 仓库说明
└── M1s_BL808_SDK            # SDK 仓库文件夹
    ├── toolchain         # 编译工具链
    ...
```


### 配置编译工具链路径

以后每次开始编译都需要执行一次这个来配置下编译工具链路径。

首先确定 `M1s_BL808_SDK` 文件夹所在的路径：

```bash
sipeed@DESKTOP:~$ cd M1s_BL808_SDK
sipeed@DESKTOP:~/M1s_BL808_SDK$ pwd
/home/lee/bl808/M1s_BL808_SDK
```

我们复制上面执行 `pwd` 后的结果（每个人的会不一样），然后执行下面的命令就可以成功进行交叉编译了。

```bash
export BL_SDK_PATH=/home/lee/bl808/M1s_BL808_SDK
```

### 编译 demo

执行 M1s_BL808_example/c906_app 目录下的 build.sh ，后面追加上想要编译的 demo 就可以完成了

```bash
cd M1s_BL808_example/c906_app
./build.sh lvgl_demo
```

然后编译出来的固件就会在 M1s_BL808_example/c906_app/build_out 目录下，名称为 `d0fw.bin`，通过虚拟 U 盘拖拽烧录即可。

### 常见问题

1. 执行完 build.sh 后提示 `Makefile:14: *** BL_SDK_PATH not found, please enter: export BL_SDK_PATH={sdk_path}.  Stop.`，查看 [配置编译工具链路径](#配置编译工具链路径) 来配置自己的 BL_SDK_PATH。

2. 编译出错

确定自己所执行的编译命令时 `./build.sh demo_name`，而不是 `./build.sh demo_name/`，注意两者结尾处 `/` 符号。