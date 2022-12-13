---
title: M1s DOCK guides
keywords: M1s DOCK ,BL808, M1s
update:
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

The M1s Dock can be used for a variety of interesting things by its delicate design. Here we tell the usages about this device. Note that the default baudrate is 2000000.

There are two Serial Devices if connecting the board through UART USB port with computer. The smaller number serial port is connected with C906 core，and the bigger number serial port is connected with E907 core.

![dual_uart](./../../../../zh/maix/m1s/other/assets/start/dual_uart.jpg)

## Power On

First time to start M1s Dock, screen displays what the camera captures, and the number on the screen which is the LED brightness changes when you press the keys on the side.

![default_firmware](./../../../../zh/maix/m1s/other/assets/start/default_firmware.jpg)

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

After succeed dragging the firmware bin into removable disk, the board will reboot and the u-disk is removed. Try to repower on this board if its not working well after burnning firmware.

### lvgl_demo

[LVGL](https://lvgl.io/) (Light and Versatile Graphics Library) is a free open source graphics library suitable for mcu graphical interfaces.

After burning into M1s Dock, the screen displays the lvgl test. And then sets the baudrate to 2000000, the serial port with the smaller serial port number prints the last touch screen position.

<img src="./../../../../zh/maix/m1s/other/assets/start/example_lvgl.gif" alt="example_lvgl" width="45%"> 
<img src="./../../../../zh/maix/m1s/other/assets/start/example_lvgl.jpg" alt="example_lvgl" width="45%"> 

### image_processing_demo

A simple image processing example.

Burning into M1s Dock, screen displays what is the camera captured, press the side key to change image operator. Set the baudrate to 2000000, to see the image operator state by the small serial port.

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

Connect this board by its TypeC UART port with computer, 2 serial port will be shown on your computer (If your mouse doesn't work after connecting board with computer, please disconnect board with computer and visit [Burn onboard bl702](#burn-onboard-bl702) to solve this problem).

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

After select the partition file, we have more choice in this page. We just need `boot2`, `firmware` and  `d0fw` these optitions.

<img src="./../../../../zh/maix/m1s/other/assets/start/firmware_choose.png" alt="firmware_choose" style="transform:rotate(0deg);">

In the picture abuve, `boot2` is never changed, and it's in this dictionary: `BLDevCube\chips\bl808\builtin_imgs\boot2_isp_bl808_v6.4_rc6`, under where the path if this burning application is. `firmware` is the firmware file for E907 cpre, and `d0fw` is C906 core file, the previous [Burn with u-disk](#burn-with-u-disk) operation can also burn firmware for this core. 

The firmware file for E907 or C906 can be gotten by compiling [M1s_dock example](https://gitee.com/sipeed/M1s_BL808_example).

First time burning, both `firmware` and `boot2` are needed, after this you just need tick what you want to burn not all.

The default firmware can be downloaded [here](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/7_Firmware/factory).

After choose the firmware, click the `Refresh` in the righr to refresh the serial port, then we can see 2 serial ports. If there are not 2 serial ports, visit [Burn onboard bl702](#burn-onboard-bl702) to solve this. We choose the bigger number serial port, and set uartrate 2000000 .

![burn_steps](./../../../../zh/maix/m1s/other/assets/start/burn_steps.png)

Press BOOT key and RST key on the board, then release RST key first, then release BOOT key in order to make M1s Dock into UART burning mode.

<img src="./../../../../zh/maix/m1s/other/assets/start/boot_rst.jpg" alt="boot_rst" style="transform:rotate(0deg);" width="40%">

Click `Create & Download`, then we can see the following meaasge where the arrow points at, before this we should make M1s Dock into UART burning mode.

![burn_press_boot](./../../../../zh/maix/m1s/other/assets/start/burn_press_boot.jpg)

Then it will burn M1s Dock if it `shake hand success`

<img src="./../../../../zh/maix/m1s/other/assets/start/burn_press_boot_success.jpg" alt="burn_press_boot_success" style="transform:rotate(0deg);" width="70%">
<img src="./../../../../zh/maix/m1s/other/assets/start/finish_burning.png" alt="finish_burning" style="transform:rotate(0deg);" width="70%">

Reburn this if it `SHAKEHAND FAIL`. Try to release the keys in order (Release RST key first then release BOOT key, I mean when release RST key, the BOOT key is being pressed) to make the board into UART burning mode, otherwise the burning software will will show error because of timeout burning.

<img src="./../../../../zh/maix/m1s/other/assets/start/burn_press_boot_failed.jpg" alt="burn_press_boot_failed" style="transform:rotate(0deg);" width="70%">

### Burn onboard bl702

Generally speaking, we do this only when there is some trouble with our board.

Hold BOOT key before power this device, then connect this board ti==with computer by the UART TypeC USB port, after this the onboard is in download mode. Run `BLDevCube`, choose `BL702`, then in MCU page, choose the firmware. Here we have provided the [firmware](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/7_Firmware), download the file whose name starts with `usb2dualuart_bl702`.

<table>
    <tr>
        <td><img src="./../../../../zh/maix/m1s/other/assets/start/select_bl702.png" alt="select_bl702" style="transform:rotate(0deg);"></td>    
        <td><img src="./../../../../zh/maix/m1s/other/assets/start/mcu_mode.png" alt="mcu_mode" style="transform:rotate(0deg);" width="70%"></td>
    </tr>
</table>

Click `Refresh`，choose the serial port (there is only one port, if you can't see this port, make sure you have hold BOOT key before power this device), set UartRate 2000000, click `Create & Diwnload`.

![burn_bl702](./../../../../zh/maix/m1s/other/assets/start/burn_bl702.png)

After finishing burning, repower this board to use the new firmware.

![finish_burn_702](./../../../../zh/maix/m1s/other/assets/start/finish_burn_702.png)

## SDK Compile


## Linux Demo

[点我](https://dl.sipeed.com/fileList/MAIX/M1s/M1s_Dock/7_Firmware/m1sdock_linux_20221116.zip) 下载 Linux 例子，按照压缩包里面 `steps.md` 操作步骤完成 Linux 系统烧录。

![linux_opensbi](./assets/start/linux_opensbi.jpg)

使用 `root` 登录
![linux_login](./assets/start/linux_login.jpg)

查看 CPU 信息
![linux_cpuinfo](./assets/start/linux_cpuinfo.jpg)