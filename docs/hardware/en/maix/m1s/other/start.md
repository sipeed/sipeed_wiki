---
title: M1s DOCK guides
keywords: M1s DOCK ,BL808, M1s
update:  - date: 2022-12-20
    version: v0.3
    author: wonder
    content:
      - Add contents about blai
  - date: 2022-12-13
    version: v0.1
    author: wonder
    content:
      - Add content
  - date: 2022-12-03
    version: v0.1
    author: wonder
    content:
      - Create file
---

The M1s Dock can be used for a variety of interesting things by its delicate design. Here we tell the usages of this device. Note that the default baudrate is 2000000.

There are two Serial Devices if connecting the board through UART USB port with computer. The smaller number serial port is connected with C906 core，and the bigger number serial port is connected with E907 core.

![dual_uart](./../../../../zh/maix/m1s/other/assets/start/dual_uart.jpg)

## Power On

the first time to start M1s Dock, screen displays what the camera captures, and the number on the screen which is the LED brightness changes when you press the keys on the side.

![default_firmware](./../../../../zh/maix/m1s/other/assets/start/default_firmware.jpg)
![led_brghtness](./../../../../zh/maix/m1s/other/assets/start/led_brghtness.jpg)

A virtual removable disk whose storage capacity is 3M will be shown on your computer if you connect this board with your computer by TypeC OTG port on this board.

![default_udisk](./../../../../zh/maix/m1s/other/assets/start/default_udisk.jpg)

Two serial devides will be shown on your computer if you connect this board with your computer by TypeC UART port on this board.

![dual_uart](./../../../../zh/maix/m1s/other/assets/start/dual_uart.jpg)

Set baudrate to 2000000，open the two serial ports, you will see different information.

Open the small serial port and you can see that the messages are being printed:

![start_smaller_uart](./../../../../zh/maix/m1s/other/assets/start/start_smaller_uart.jpg)

Open the big serial port for command-line interaction:

![start_bigger_uart](./../../../../zh/maix/m1s/other/assets/start/start_bigger_uart.jpg)

## Burn with u-disk

It's suggested using this way to burn firmware, by which we can burn the program for C906 core in the chip.

Connect this board by its TypeC OTG port with computer, hold the 2 sides keys (which have been marked on the following figure) of M1s Dock, then press RST button to make this board into u-disk burn mode.

<table>
    <tr>
        <td><img src="./../../../../zh/maix/m1s/other/assets/start/udisk_burn.png" alt="udisk_burn" style="transform:rotate(0deg);"></td>    
        <td>Hold 2 side keys and press RST，make M1s Dock into u-disk burn mode</td>
    </tr>
</table>

Besides, when 2 side keys are being pressed, power on this board can make this board into u-disk burn mode too.

<img src="./../../../../zh/maix/m1s/other/assets/start/udisk_in_computer.png" alt="udisk_in_computer" style="transform:rotate(0deg);">

A removable disk with tiny storage capacity will be shown on your computer if this board is in u-disk burn mode. Just drag the firmware <a href="https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/7_Firmware/demo_bin"> Here are some demo bins </a> into the removable disk to burn the firmware.

<img src="./../../../../zh/maix/m1s/other/assets/start/udisk_burn.gif" alt="udisk_burn" style="transform:rotate(0deg);">

After succeed dragging the firmware bin into removable disk, the board will reboot and the u-disk is removed. Try to repower this board if its not working well after burnning firmware.

### lvgl_demo

[LVGL](https://lvgl.io/) (Light and Versatile Graphics Library) is a free open source graphics library suitable for mcu graphical interfaces.

After burning into M1s Dock, the screen displays the lvgl test. And then sets the baudrate to 2000000, the serial port with the smaller serial port number prints the last touch screen position.

<img src="./../../../../zh/maix/m1s/other/assets/start/example_lvgl.gif" alt="example_lvgl" width="45%"> 
<img src="./../../../../zh/maix/m1s/other/assets/start/example_lvgl.jpg" alt="example_lvgl" width="45%"> 

### image_processing_demo

A simple image processing example.

Burning into M1s Dock, screen displays what the camera captured, press the side key to change image operator. Set the baudrate to 2000000, to see the image operator state by the small serial port.

<img src="./../../../../zh/maix/m1s/other/assets/start/example_image_processing_demo.jpg" alt="example_image_processing_demo" width="45%"> 
<img src="./../../../../zh/maix/m1s/other/assets/start/example_image_processing_demo_uart.jpg" alt="example_image_processing_demo_uart" width="45%"> 

### tinymaix_mnist_demo

[TinyMaix](https://github.com/sipeed/TinyMaix) is a tiny inference Neural Network library specifically for microcontrollers (TinyML), can run lightweight deep learning model on any Single Chip Microcomputer.

Burning into M1s Dock, recognizing number through the red box in the center of screen. Set the baudrate to 2000000, to see the process and result by the small serial port.

<img src="./../../../../zh/maix/m1s/other/assets/start/example_tinymaix_mnist_demo.jpg" alt="example_tinymaix_mnist_demo" width="45%"> 
<img src="./../../../../zh/maix/m1s/other/assets/start/example_tinymaix_mnist_demo_uart.jpg" alt="example_tinymaix_mnist_demo_uart" width="45%"> 

### pikascript_demo

[PikaScript](http://pikascript.com/) is a cross-platform, ultra-lightweight embedded Python engine.

Burning into M1s Dock, the screen is white. Set the baudrate to 2000000, open the small serial port for command-line interaction:

Use these commands:
```bash
arc = lv.arc(lv.scr_act())
arc.set_end_angle(200)
arc.set_size(150, 150)
arc.center()
```

![example_pikascript_demo_uart](./../../../../zh/maix/m1s/other/assets/start/example_pikascript_demo_uart.jpg)

Then the screen displays as shown(Ignore the bad shoot):

![example_pikascript_demo_uart](./../../../../zh/maix/m1s/other/assets/start/example_pikascript_demo_screen.jpg)

## Burn with UART

The u-disk burnning method above is used to burn firmware for C906 core, and if there are some trouble with firmware or when we need to upgrade the whole firmware, we need to burn this board by UART.

### Burn M1s

Connect this board by its TypeC UART port with computer, 2 serial ports will be shown on your computer (If your mouse doesn't work after connecting board with computer, please disconnect board with computer and visit [Burn onboard bl702](#burn-onboard-bl702) to solve this problem).

#### Burn with graphical application

To burn for M1s, we need bouffalolab official burning application, visit https://dev.bouffalolab.com/download and download the file named `Bouffalo Lab Dev Cube`. Decompress the downloaded file then we get the application to burn the board.

![bouffalo_cube](./../../../../zh/maix/m1s/other/assets/start/bouffalo_cube.png)

We mainly use `BLDevCube`, `BLDevCube-macos` and `BLDevCube-ubuntu` these three files, by which to burn our board with graphical interface on different OS.

![application](./../../../../zh/maix/m1s/other/assets/start/application.png)

Run the application, choose bl808, then we put this [partition file](https://dl.sipeed.com/fileList/MAIX/M1s/M1s_Dock/7_Firmware/partition/partition_cfg_16M_m1sdock.toml) in partition table (marked with ②) in IOT page.

<table>
    <tr>
        <td><img src="./../../../../zh/maix/m1s/other/assets/start/chip_selection.png" alt="chip_selection" style="transform:rotate(0deg);"></td>    
        <td><img src="./../../../../zh/maix/m1s/other/assets/start/choose_partition.png" alt="choose_partition" style="transform:rotate(0deg);" width="70%"></td>
    </tr>
</table>

After selecting the partition file, we have more choice in this page. We just need `boot2`, `firmware` and  `d0fw` these options.

<img src="./../../../../zh/maix/m1s/other/assets/start/firmware_choose.png" alt="firmware_choose" style="transform:rotate(0deg);">

In the picture above, `boot2` stays the same, and it's in this directory: `BLDevCube\chips\bl808\builtin_imgs\boot2_isp_bl808_v6.4_rc6`, under where the path if this burning application is. `firmware` is the firmware file for E907 core, and `d0fw` is C906 core file, the previous [Burn with u-disk](#burn-with-u-disk) operation can also burn firmware for this core. 

The firmware file for E907 or C906 can be gotten by compiling [M1s_dock example](https://gitee.com/sipeed/M1s_BL808_example).

First time burning, both `firmware` and `boot2` are needed, after this you just need tick what you want to burn not all.

The default firmware can be downloaded [here](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/7_Firmware/factory).

After choose the firmware, click the `Refresh` in the righr to refresh the serial port, then we can see 2 serial ports. If there are not 2 serial ports, visit [Burn onboard bl702](#burn-onboard-bl702) to solve this. We choose the bigger number serial port, and set uartrate 2000000 .

![burn_steps](./../../../../zh/maix/m1s/other/assets/start/burn_steps.png)

Press BOOT key and RST key on the board, then release RST key first, then release BOOT key in order to make M1s Dock into UART burning mode.

<img src="./../../../../zh/maix/m1s/other/assets/start/boot_rst.jpg" alt="boot_rst" style="transform:rotate(0deg);" width="40%">

Click `Create & Download`, then we can see the following message where the arrow points at, before this we should make M1s Dock into UART burning mode.

![burn_press_boot](./../../../../zh/maix/m1s/other/assets/start/burn_press_boot.jpg)

It will burn M1s Dock if it shows `shake hand success`

<img src="./../../../../zh/maix/m1s/other/assets/start/burn_press_boot_success.jpg" alt="burn_press_boot_success" style="transform:rotate(0deg);" width="70%">
<img src="./../../../../zh/maix/m1s/other/assets/start/finish_burning.png" alt="finish_burning" style="transform:rotate(0deg);" width="70%">

Reburn this if it `SHAKEHAND FAIL`. Try to release the keys in order (Release RST key first then release BOOT key, I mean when release RST key, the BOOT key is being pressed) to make the board into UART burning mode, otherwise the burning software will show error because of timeout burning.

<img src="./../../../../zh/maix/m1s/other/assets/start/burn_press_boot_failed.jpg" alt="burn_press_boot_failed" style="transform:rotate(0deg);" width="70%">

#### Burn with command-line

We can burn M1s Dock by command-line through serial port on this board.

In `BLDevCube` folder, there is `bflb_iot_tool` application, `bflb_iot_tool`、 `bflb_iot_tool-macos` and `bflb_iot_tool-ubuntu` are used for different OS.

Here I take Windows as example, and for other OS you need to change the commands by yourself.

In this command, `firmware` is the bin file for E907 Core, the default bin file can be downloaded from [here](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/7_Firmware/factory). `pt` is the partition file, it's in the `M1s_BL808_example\partition` folder, you can also [Click me](https://dl.sipeed.com/fileList/MAIX/M1s/M1s_Dock/7_Firmware/partition/partition_cfg_16M_m1sdock.toml) to get it.`boot2` is in `BLDevCube\chips\bl808\builtin_imgs\boot2_isp_bl808` folder. Set baudrate 2000000 to burn this board fast. `port` is the bigger port number.

```bash
.\bflb_iot_tool.exe --chipname=bl808 --port=COM38 --baudrate=2000000 --firmware="firmware_20221212.bin" --pt="M1s_BL808_example\partition\partition_cfg_16M_m1sdock.toml" --boot2="BLDevCube\chips\bl808\builtin_imgs\boot2_isp_bl808\boot2_isp_debug.bin"
```

Of course, make sure you have make this board into UART burning mode: Press BOOT key and RST key, then release RST key first then release BOOT key.

![command_burn_flash](./../../../../zh/maix/m1s/other/assets/start/command_burn_flash.jpg)

After burning these, you can burn the bin file for C906 core according to [Burn with u-disk](#burn-with-u-disk). You can also burn this board based on the adderss, from `partition_cfg_16M_m1sdock.toml` file you can know the burn address and modify it.

#### Erase flash

We need advanced mode first.

![erase_advanede_mode](./../../../../zh/maix/m1s/other/assets/start/erase_advanede_mode.jpg)

Then in FLASH interface, we choose the bigger serial port, tick Whole Chip. Make this board into UART burning mode: Press BOOT key and RST key, then release RST key first then release BOOT key. Click `Erase Flash` to erase the chip

![erase_configurations](./../../../../zh/maix/m1s/other/assets/start/erase_configurations.jpg)

There is no progress bar when erasing, and there is `SUCCESS` when it finished erasing.

![erase_success](./../../../../zh/maix/m1s/other/assets/start/erase_success.jpg)

### Burn onboard bl702

We do this only when there is some trouble with our board.

Hold BOOT key before power this device, then connect this board ti==with computer by the UART TypeC USB port, after this the onboard is in download mode. Run `BLDevCube`, choose `BL702`, then in MCU page, choose the firmware. Here we have provided the [firmware](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/7_Firmware), download the file whose name starts with `usb2dualuart_bl702`.

<table>
    <tr>
        <td><img src="./../../../../zh/maix/m1s/other/assets/start/select_bl702.png" alt="select_bl702" style="transform:rotate(0deg);"></td>    
        <td><img src="./../../../../zh/maix/m1s/other/assets/start/mcu_mode.png" alt="mcu_mode" style="transform:rotate(0deg);" width="70%"></td>
    </tr>
</table>

Click `Refresh`，choose the serial port (there is only one port, if you can't see this port, make sure you have hold BOOT key before powering this device), set UartRate 2000000, click `Create & Diwnload`.

![burn_bl702](./../../../../zh/maix/m1s/other/assets/start/burn_bl702.png)

After finishing burning, repower this board to use the new firmware.

![finish_burn_702](./../../../../zh/maix/m1s/other/assets/start/finish_burn_702.png)

## SDK Compile

M1s can be compiled in Linux.

### Get example

```bash
git clone https://github.com/Sipeed/M1s_BL808_example.git
```

Then the file tree should be like this:

```bash
sipeed@DESKTOP:~$ tree -L 1 M1s_BL808_example/
M1s_BL808_example/
├── LICENSE           # License file
├── assets            # folder for assets for readme.md
├── c906_app          # folder for C906 core example
├── e907_app          # folder for E907 core example
├── partition         # folder for partition file
└── readme.md         # guide
```

### Get SDK

It's about 120MB memory storage.

```bash
git clone https://github.com/sipeed/M1s_BL808_SDK.git
```

Then the file tree should be like this:

```bash
sipeed@DESKTOP:~$ tree -L 1 
.
├── M1s_BL808_example   # Folder of example
└── M1s_BL808_SDK       # Folder of SDK
```

### Get toolchain

According to the `readme.md` in example folder, we need to put the toolchain in M1s_BL808_SDK/toolchain

```bash
mkdir -p M1s_BL808_SDK/toolchain
cd M1s_BL808_SDK/toolchain
git clone https://github.com/wonderfullook/m1s_toolchain.git
```

Rename the toolchain folder name to `Linux_x86_64`, and return to the previous two levels of directories.

```bash
mv m1s_toolchain Linux_x86_64
cd ../../
```

Then the file tree should be like this(The main folder and files):

```bash
sipeed@DESKTOP:~$ tree -L 2
.
├── M1s_BL808_example     # Folder of example
│   ├── LICENSE           # License file
│   ├── assets            # folder for assets for readme.md
│   ├── c906_app          # folder for C906 core example
│   ├── e907_app          # folder for E907 core example
│   ├── partition         # folder for partition file
│   └── readme.md         # guide
└── M1s_BL808_SDK         # Folder of SDK
    ├── toolchain         # Folder of toolchain
    ...
```

### Set toolcahin path

Everytime compling for M1s, we need to set toolcahin path once.

First we need to know the path of `M1s_BL808_SDK`:

```bash
sipeed@DESKTOP:~$ cd M1s_BL808_SDK
sipeed@DESKTOP:~/M1s_BL808_SDK$ pwd
/home/lee/bl808/M1s_BL808_SDK
```

We copy the result (the result of everyone is different) of `pwd` command, then run following commamd to set toolcahin path.

```bash
export BL_SDK_PATH=/home/lee/bl808/M1s_BL808_SDK
```

Note that this is `M1s_BL808_SDK` ，not `M1s_BL808_SDK/`，normally this error is made by automatic string completion.

### Compile demo

Run `build.sh` which is in the folder of M1s_BL808_example/c906_app, add the `demo` in the end you want to try to compile.

Demos（Edited in 2022-12-13）：

```bash
c906_app
├── audio_recording
├── blai_mnist_demo
├── camera_bypass_lcd
├── camera_dump
├── camera_streaming_through_wifi
├── cli_demo
├── flash_demo
├── gpio_demo
├── hello_world
├── i2c_touch
├── image_processing_demo
├── lfs_demo
├── lvgl_demo
├── pikascript_demo
├── play_with_gba
├── proj_config.mk
├── pwm_demo
├── spi_lcd
├── tinymaix_mnist_demo
└── uvc_demo
```

```bash
cd M1s_BL808_example/c906_app
./build.sh lvgl_demo
```

Then the compiled bin file is in M1s_BL808_example/c906_app/build_out folder, and its name is `d0fw.bin`, we can burn it by [u-disk](#burn-with-u-disk).

### Compile firmware

Run `build.sh` which is in the folder of M1s_BL808_example/e907_app, add `firmware` in the end to compile.

```bash
cd M1s_BL808_example/e907_app
./build.sh firmware
```

Then the compiled bin file is in M1s_BL808_example/e907_app/build_out folder, and its name is `firmware.bin`, we can burn it with the burning application provided by Bouffalo.

### Questions

1. Run command `build.sh` and get error `Makefile:14: *** BL_SDK_PATH not found, please enter: export BL_SDK_PATH={sdk_path}.  Stop.`, Visit [Set toolcahin path](#set-toolcahin-path) to set `BL_SDK_PATH` correctly.

2. Failed compiling

Make sure you run `./build.sh demo_name` command, not `./build.sh demo_name/` command. Note the symbol `/` in the end.

## Linux Demo

[Click me](https://dl.sipeed.com/fileList/MAIX/M1s/M1s_Dock/7_Firmware/m1sdock_linux_20221116.zip) to download Linux demo, and following the `steps.md` in the compressed file to finish burning Linux image.

![linux_opensbi](./../../../../zh/maix/m1s/other/assets/start/linux_opensbi.jpg)

Login in with `root`
![linux_login](./../../../../zh/maix/m1s/other/assets/start/linux_login.jpg)

Visit CPU information
![linux_cpuinfo](./../../../../zh/maix/m1s/other/assets/start/linux_cpuinfo.jpg)

## Using Jtag

The jtag debugger is sold in [Sipeed aliexpress store](https://sipeed.aliexpress.com/store/1101739727), you can buy one if you need.

![cklink_appearence](./../../../../zh/maix/m1s/other/assets/start/cklink_appearence.jpg)

### Connect to device

Insert the jtag convertor board into the TF card slot on M1s Dock, then the convertor board is connected and fixed on the board.

And it's look like as follows:

![cklink_connect_side](./../../../../zh/maix/m1s/other/assets/start/cklink_connect_side.jpg)
![cklink_connect_top](./../../../../zh/maix/m1s/other/assets/start/cklink_connect_top.jpg)

Both jtag and M1s Dock are need to be connected with computer, and we need to make sure the UART port on M1s Dock is connected with computer, by which we can enable the core jtag and ensure that the jtag will not be very hot because of heavy power supply to M1s Dock.

### Install driver

Visit [Download station](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/9_Driver/cklink) to download the driver for your OS.

#### Windows

Unzip `T-Head-DebugServer-windows`, run `Setup` to install driver.

![cklink_windows_install_driver](./../../../../zh/maix/m1s/other/assets/start/cklink_windows_install_driver.jpg)

It's suggested not to change the default installation path, to avoid it remove all child directory when uninstalling it.

![cklink_windows_driver_path](./../../../../zh/maix/m1s/other/assets/start/cklink_windows_driver_path.jpg)

Install all compoents, which we may need in the future.

![cklink_windows_driver_components](./../../../../zh/maix/m1s/other/assets/start/cklink_windows_driver_components.jpg)

Finish installing this, and we can see there is `CKlink-Lite` in Windows device manager if we have connected the debugger.

![cklink_windows_driver_device_manager](./../../../../zh/maix/m1s/other/assets/start/cklink_windows_driver_device_manager.jpg)

There is an icon of the debug software.

![cklink_windows_driver_desktop_icon](./../../../../zh/maix/m1s/other/assets/start/cklink_windows_driver_desktop_icon.jpg)

#### Linux

Download driver：[Click me](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/9_Driver/cklink)

![cklink_linux_list_file](./../../../../zh/maix/m1s/other/assets/start/cklink_linux_list_file.jpg)

Unzip the downloaded file.

```bash
tar xvf T-Head-DebugServer*
```

Then there is a new script file.

![cklink_linux_list_shell_file](./../../../../zh/maix/m1s/other/assets/start/cklink_linux_list_shell_file.jpg)

Run this script, then its usages are shown, by which we can know that add with command `-i` to install driver or with `-u` to remove it in the end of command.

```
./T-Head-DebugServer-linux-x86_64-V5.16.5-20221021.sh
```

![cklink_linux_script_help](./../../../../zh/maix/m1s/other/assets/start/cklink_linux_script_help.jpg)

Install driver：

```
sudo ./T-Head-DebugServer-linux-x86_64-V5.16.5-20221021.sh -i
```

![cklink_linux_installation](./../../../../zh/maix/m1s/other/assets/start/cklink_linux_installation.jpg)

We need enter `yes` two times when installing it, and for as for `Set full installing path` we can just press Enter on the keyboard to use the default installation path or set your own installation path by yourself.

Finishing installing the driver, use command `lsusb` to see there is `CKlink-Lite` if we have connected the debugger.

![cklink_linux_lsusb](./../../../../zh/maix/m1s/other/assets/start/cklink_linux_lsusb.jpg)

### Debug denive

Before debugging, we need to enable core debug. Connect computer with UART port on M1s Dock, and open the bigger serial port.

![cklink_jtag_serial_choice](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_serial_choice.jpg)
![cklink_jtag_choice](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_choice.jpg)

We can know there are two jtag choices, run command `jtag_cpu0` to debug C906 Core or run command `jtag_m0` to debug E907 Core.

![cklink_jtag_c906](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_c906.jpg)
![cklink_jtag_e907](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_e907.jpg)

#### Windows

Run T-HeadDebugServer software on the desktop, if it shows following message, try following steps:

- Make sure you have enabled core debug in serial connection
- There is `CKlink-Lite` in Windows device manager, if there is no `CKlink-Lite`, check the connection of debugger or reinstall the driver 
- Debugger is occupied by other T-HeadDebugServer application

![cklink_jtag_windows_no_target](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_windows_no_target.jpg)

Click the triangle icon to connect device.

![cklink_jtag_windows_run_debugger](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_windows_run_debugger.jpg)

If there shows Failed about port, set another port and then rerun connecting device.

![cklink_jtag_windows_no_port](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_windows_no_port.jpg)

Click Socket Setting, set a port.

![cklink_jtag_windows_set_socket](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_windows_set_socket.jpg)
![cklink_jtag_windows_set_socket_1](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_windows_set_socket_1.jpg)

If succeed connecting, the triangle icon will change into circle icon.

![cklink_jtag_windows_success_connection](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_windows_success_connection.jpg)

Up to now we have connected device, and the picture above is we usr command `jtag_m0` to debug E907 Core, you can also run `jtag_cpu0` to debug C906 Core.

And we can use software like gdb to debug the chip.

![cklink_jtag_windows_gdb_debug](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_windows_gdb_debug.jpg)

Besides, in the directory where we install this software, we can run `DebugServerConsole` to connect debugger by command-line.

![cklink_jtag_windows_debugserverconsole](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_windows_debugserverconsole.jpg)

Run it by command-line to see its usages.

```bash
.\DebugServerConsole.exe -h
```

![cklink_jtag_windows_debugserverconsole_help](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_windows_debugserverconsole_help.jpg)

```bash
.\DebugServerConsole.exe -port 65535
```

![cklink_jtag_windows_debugserverconsole_port](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_windows_debugserverconsole_port.jpg)

Then we can debug it with port number 65535.

#### Linux

Run command`DebugServerConsole -h` to see help.

![cklink_jtag_linux_debugserverconsole_help](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_linux_debugserverconsole_help.jpg)

Run following command to debug M1s Dock with port number 12345.

```bash
DebugServerConsole -port 12345
```

![cklink_jtag_linux_debugserverconsole](./../../../../zh/maix/m1s/other/assets/start/cklink_jtag_linux_debugserverconsole.jpg)

## blai npu

### Supported operators

<table>
<thead>
<tr>
  <th>Type</th>
  <th>Operators</th>
  <th>Applicable Subset Spec.</th>
  <th>Processor</th>
</tr>
</thead>
<tbody>
<tr>
  <td rowspan="10">Convolution</td>
  <td rowspan="4">Conv </td>
  <td>Kernel: 1x1,3x3,5x5,7x7</td>
  <td rowspan="4">:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Stride: 1x1, 2x2</td>
</tr>
<tr>
  <td>Dilation: 1x1, 2x2</td>
</tr>
<tr>
  <td>Pad: same</td>
</tr>
<tr>
  <td rowspan="4">Depthwise Conv</td>
  <td>Kernel: 1x1,3x3 (5x5, 7x7 TBD)</td>
  <td rowspan="4">:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Stride: 1x1, 2x2</td>
</tr>
<tr>
  <td>Dilation: 1x1 (2x2 TBD)</td>
</tr>
<tr>
  <td>Pad: same</td>
</tr>
<tr>
  <td rowspan="2">Transpose Conv</td>
  <td>Kernel: 3x3</td>
  <td rowspan="2">strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Stride: 2x2</td>
</tr>
<tr>
  <td rowspan="4">Pooling</td>
  <td rowspan="2">MaxPool (NPU TBD)</td>
  <td>Kerenl: 2x2</td>
  <td rowspan="2">DSP</td>
</tr>
<tr>
  <td>Stride: 2x2</td>
</tr>
<tr>
  <td rowspan="2">MaxPool</td>
  <td>Kerenl: 3x3</td>
  <td rowspan="2">:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Stride: 1x1, 2x2</td>
</tr>
<tr>
  <td rowspan="2">Activation</td>
  <td>Relu</td>
  <td></td>
  <td>:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Relu 6</td>
  <td></td>
  <td>:strong:<code>NPU</code></td>
</tr>
<tr>
  <td rowspan="5">Other processing</td>
  <td>BatchNormalization</td>
  <td>fused with conv</td>
  <td>:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Add (shortcut)</td>
  <td></td>
  <td>:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Concat (route)</td>
  <td>Channel wise (AXIS 3 in BHWC)</td>
  <td>:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Fully Connected</td>
  <td></td>
  <td>:strong:<code>NPU</code></td>
</tr>
<tr>
  <td>Upsample</td>
  <td>Nearest</td>
  <td>:strong:<code>NPU</code></td>
</tr>
</tbody>
</table>

### blai_mnist_demo

Burning it into M1s Dock, we have told that the each compiled demo bin is named `d0fw.bin`, and it's in `M1s_BL808_example/c906_app/built_out` folder.

```
#c906_app
./build.sh blai_mnist_demo
```

![udisk_burn](./../../../../zh/maix/m1s/other/assets/start/udisk_burn.gif)

After burning this firmware (when the u-disk is automatically removed it means we have finished burning this firmware), press RST key to reset M1s Dock and reload firmware, then open the smaller serial port (with baudrate 2000000) we can see it shows failed loading model.

![blai_mnist_demo_no_model](./../../../../zh/maix/m1s/other/assets/start/blai_mnist_demo_no_model.jpg)

So we need upload model into M1s Dock, from source code we can know we need to save model in flash.

![blai_mnist_demo_fopen](./../../../../zh/maix/m1s/other/assets/start/blai_mnist_demo_fopen.jpg)

Connect computer with OTG port on M1s Dock we can see there is a u-disk with nearly 7M storge memory.

![blai_mnist_demo_flash_disk](./../../../../zh/maix/m1s/other/assets/start/blai_mnist_demo_flash_disk.jpg)

Follow the source code, in the u-disk (which is the flash of M1s Dock indeed), we create a folder named `models`, and save [mnist.blai](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/7_Firmware/demo_bin/blai_mnist_demo) into the newly created folder.

```bash
models
└── mnist.blai
```

Press RST key again,  open the smaller serial port we can see we succeed loading model, and the recognition results are printed.

Screen displays camera contents, and show recognition result.

![blai_mnist_demo_uart](./../../../../zh/maix/m1s/other/assets/start/blai_mnist_demo_uart.jpg)

![blai_mnist_demo_recognition](./../../../../zh/maix/m1s/other/assets/start/blai_mnist_demo_recognition.jpg)
