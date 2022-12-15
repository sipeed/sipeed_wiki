---
title: M0sense guide
keywords: M0sense
update:
  - date: 2022-12-15
    version: v0.1
    author: wonder
    content:
      - Create file
---

## Power On

The led lights up when M0sense is powered on, and the screen displays spectrum diagram of ambient sound.

<img src="./../../../zh/maixzero/sense/assets/start/m0sense_start.jpg" alt="m0sense_start" width="45%">
<img src="./../../../zh/maixzero/sense/assets/start/m0sense_start_screen.jpg" alt="m0sense_start_screen" width="45%">

## Burn by U-Disk

M0sense can be burned by draging and dropoing firmware to u-disk.

Hold BOOT key, then click RST key once, a removable disk is shown in computer.

![m0sense_udisk](./../../../zh/maixzero/sense/assets/start/m0sense_udisk.jpg)

Just drag the firmware you want to burn and drop it in the removable disk, the removable disk will be automatically removed and M0sense will be automatically burned with this firmware.

![m0sense_drag_burn](./../../../zh/maixzero/sense/assets/start/m0sense_drag_burn.gif)

Here are some demos [Click me](https://dl.sipeed.com/shareURL/Maix-Zero/Maix-Zero/7_Example_demos), just use them by draging and dropoing firmware to u-disk to see their result, the source codes are in [github](https://github.com/sipeed/M0sense_BL702_example).

And the result of each demo is as following:

### hello_world.uf2

Run serial application, and open the serial port, `Hello, World` is being printed.

![m0sense_hello_world](./../../../zh/maixzero/sense/assets/start/m0sense_hello_world.gif)

### blink_baremetal.uf2

Draging and dropoing this file to u-disk, then repower M0sense, LED flashes, open the serial port the LED states are printed.

- Open the serial port

![m0sense_blink_baremetal_uart](./../../../zh/maixzero/sense/assets/start/m0sense_blink_baremetal_uart.gif)

- LED flashes

![m0sense_blink_baremetal_led](./../../../zh/maixzero/sense/assets/start/m0sense_blink_baremetal_led.gif)

### blink_rtos.uf2

This demo is the same effect as the privious one, but this demo is based on RTOS.

- Open the serial port

![m0sense_blink_baremetal_uart](./../../../zh/maixzero/sense/assets/start/m0sense_blink_baremetal_uart.gif)

- LED flashes

![m0sense_blink_baremetal_led](./../../../zh/maixzero/sense/assets/start/m0sense_blink_baremetal_led.gif)

### lcd_flush.uf2

Burn this demo to M0sense, lcd background color flushes, and the color of screen is printed by serial port.

![m0sense_lcd_flush](./../../../zh/maixzero/sense/assets/start/m0sense_lcd_flush.gif)
![m0sense_lcd_flush_uart](./../../../zh/maixzero/sense/assets/start/m0sense_lcd_flush_uart.gif)

### imu.uf2

Burn this demo to board, the data of onboard 6 axi IMU is printed by serial port.

烧录进板子后，从串口可以看到板子上面 6 轴 IMU (惯性传感器)的数据。

![m0sense_imu_uart](./../../../zh/maixzero/sense/assets/start/m0sense_imu_uart.gif)

### single_button_control.uf2

Burn this demo to M0sense, press BOOT key, LED changes the color, and the state of LED is printed by serial port.

The detailed usage can be analysised by reading <a href="https://github.com/Sipeed/M0sense_BL702_example/blob/main/m0sense_apps/rtos_demos/single_button_control/main.c">source code</a>.

![single_button_control](./../../../zh/maixzero/sense/assets/start/single_button_control.gif)
![single_button_control_uart](./../../../zh/maixzero/sense/assets/start/single_button_control_uart.gif)

### audio_recording.uf2

Burn this demo to M0sense, the 16bit pcm format data of onboard microphone is printed by serial port.

![audio_recording](./../../../zh/maixzero/sense/assets/start/audio_recording.gif)

## SDK uasge

M0sense can be compiled in Linux.

### Get example

```bash
git clone https://github.com/Sipeed/M0sense_BL702_example.git
```

Then the file tree should be like this:

```bash
sipeed@DESKTOP:~$ tree -L 1 M0sense_BL702_example/
M0sense_BL702_example/
├── LICENSE           # License file
├── README.md         # guide
├── bl_mcu_sdk        # Folder of SDK
├── build.sh          # Compile script
├── m0sense_apps      # Folder of example codes
├── misc              # Other utils
└── uf2_demos         # Example demo
```

### Get SDK

Get sdk in the path of example folder.

It's about 400MB memory storage.

```bash
cd M0sense_BL702_example
git clone https://github.com/bouffalolab/bl_mcu_sdk
```

Then the file tree should be like this(The main folder and files):

```bash
sipeed@DESKTOP:~$ tree -L 2 M0sense_BL702_example/
M0sense_BL702_example/
├── LICENSE           # License file
├── README.md         # guide
├── bl_mcu_sdk        # Folder of SDK
│   ├── README.md     # SDK guide
│   ├── ReleaseNotes  # SDK history
│   ├── bsp
│   ├── cmake
│   ├── components
│   ├── docs
│   ├── drivers
│   ├── examples
│   ├── project.build
│   ├── tools
│   └── utils
├── build.sh          # Compile script
├── m0sense_apps      # Folder of example codes
├── misc              # Other utils
└── uf2_demos         # Example demo
```

### Get toolchain

Get toolchain in the path of example folder.

```bash
git clone https://github.com/wonderfullook/toolchain_gcc_sifive_linux
```

Then the file tree should be like this(The main folder and files):

```bash
sipeed@DESKTOP:~$ tree -L 2 M0sense_BL702_example/
M0sense_BL702_example/
├── LICENSE                       # License file
├── README.md                     # guide
├── bl_mcu_sdk                    # Folder of SDK
│   ├── README_zh.md              # SDK guide
│   ├── ReleaseNotes              # SDK history
│   ...
├── build.sh                      # Compile script
├── m0sense_apps                  # Folder of example codes
├── misc                          # Other utils
├── toolchain_gcc_sifive_linux    # Folder of toolchain
│   ├── bin                       # Folder of executable program
│   ├── lib                       # Folder of library
│   ...
└── uf2_demos                     # Example demo
```

### Put the patch

Make sure you are in `M0sense_BL702_example` dictionary.

Before put the patch, we need set username and email, just set what you like.

```bash
cd bl_mcu_sdk
git config user.email "m0sense@sipeed.com"
git config user.name "tinymaix"
```
Then put the patch.

```bash
cd ..
./build.sh patch
```

When it shows `Apply patch for you!`, we succeed doing this.

![m0sense_patch](./../../../zh/maixzero/sense/assets/start/m0sense_patch.jpg)

### Set toolcahin path

Everytime compling for M0sense, we need to set toolcahin path once.

First we need to know the path of `M0sense_BL702_example`:

```bash
sipeed@DESKTOP:~$ pwd
/home/lee/M0sense_BL702_example
```

We copy the result (the result of everyone is different) of `pwd` command, then add `/toolchain_gcc_sifive_linux/bin` in the end，run following command, then we finish setting the toolcahin path.

```bash
PATH=$PATH:/home/lee/M0sense_BL702_example/toolchain_gcc_sifive_linux/bin
```

Then we can use command `riscv64-unknown-elf-gcc -v` to test our toolcahin, here is the right result.

```bash
sipeed@DESKTOP:~$ riscv64-unknown-elf-gcc -v
Using built-in specs.
COLLECT_GCC=riscv64-unknown-elf-gcc
COLLECT_LTO_WRAPPER=/home/lee/M0sense_BL702_example/toolchain_gcc_sifive_linux/bin/../libexec/gcc/riscv64-unknown-elf/10.2.0/lto-wrapper
Target: riscv64-unknown-elf
```

If not set the path right, the command `riscv64-unknown-elf-gcc` will be shown not found, try to reset the toolcahin path.

![m0sense_toolchain_notfound](./../../../zh/maixzero/sense/assets/start/m0sense_toolchain_notfound.jpg)

### Compile demo

Before compiling demo first time, we need to compile the firmware conversion application on the computer for dragging  and burning firmware by u-disk.

Run followinf command in the dictionary of `M0sense_BL702_example` .

```bash
sudo apt install gcc # Install gcc
gcc -I libs/uf2_format misc/utils/uf2_conv.c -o uf2_convert # Compile the firmware conversion application
```

Then we can compile demo.

```bash
./build.sh m0sense_apps/blink/blink_baremetal
```

The demo of uf2 format which can be burned to M0sense by u-disk is in the uf2_demos folder, and the demo file is in bl_mcu_sdk/out folder.

## SDK Note

1. Compiling your own firmware conversion application if it's the first time compiling.
2. Everytime compiling the firmware, make sure you have [set the toolcahin path](#set-toolcahin-path)

## Burn bin file

Sometimes we need to burn bin file because of some reasons, here are the steps.

给 M0sense 烧录需要用到博流官方烧录工具，前往 https://dev.bouffalolab.com/download 下载名称为 `Bouffalo Lab Dev Cube` 的文件。解压后就得到了用来烧录板子的应用程序。

![bouffalo_cube](./../../maix/m1s/other/assets/start/bouffalo_cube.png)

解压后的文件夹中主要关注 `BLDevCube`、 `BLDevCube-macos` 和 `BLDevCube-ubuntu` 三个文件，用于在不同系统启动这个烧录工具。

![application](./../../maix/m1s/other/assets/start/application.png)

然后使用镊子或其他金属短接上板子上的 3.3V 引脚和 boot 引脚，然后在给板子通电，这样板子进入烧录模式了。可以在电脑设备管理器中看到出现了一个串口设备。

| 短接引脚                                   | 设备管理器中的串口设备                                |
| ------------------------------------------ | -------------------------------------------------- |
| ![boot_mode](./../../../zh/maixzero/sense/assets/start/boot_mode.jpg) | ![serial_device](./../../../zh/maixzero/sense/assets/start/serial_device.jpg) |

接着打开 `BLDevCube` 烧录软件（根据自己系统选择），选择 `BL702` 芯片，在打开的软件界面选择 MCU 模式，选择想要烧录进去的固件。默认的固件可以在这里下载到: [Click me](https://dl.sipeed.com/shareURL/Maix-Zero/Maix-Zero/7_Example_demos/default_firmware)

<table>
    <tr>
        <td><img src="./../../maix/m1s/other/assets/start/select_bl702.png" alt="select_bl702" style="transform:rotate(0deg);"></td>    
        <td><img src="./../../maix/m1s/other/assets/start/mcu_mode.png" alt="mcu_mode" style="transform:rotate(0deg);" width="70%"></td>
    </tr>
</table>

点击 `Refresh`，选择唯一的串口（如果看到的不是唯一串口，重新短接 boot 引脚和 3.3v 引脚），设置波特率 2000000， 点击下载烧录。

![burn_bl702](./../../maix/m1s/other/assets/start/burn_bl702.png)

烧录结束后，重新插拔一次 USB 来重新启动 bl702 以应用新的固件。

![finish_burn_702](./../../maix/m1s/other/assets/start/finish_burn_702.png)