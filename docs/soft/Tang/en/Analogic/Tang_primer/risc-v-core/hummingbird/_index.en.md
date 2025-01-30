---
title: "Hummingbrid Core"
date: 2019-02-23T13:51:21+05:30
weight: 5
draft: false
---

## Download the SDK

We have assembled an All-In-One SDK that includes SiRV-SDK Toolchain, and OpenOCD. You can download the SDK from given link below.

<i class="fas fa-download"></i> [sirv-e-sdk.tar.lrz](https://github.com/kprasadvnsi/tang-doc/releases/download/1.0.0/sirv-e-sdk.tar.lrz)

## Configuring the working environment

Extract the downloaded archive to the current working directory.

```
lrzuntar sirv-e-sdk.tar.lrz 
```


> You will need **lrzip** for the above command to work. Install it using the following command.
> `sudo apt-get install lrzip`


## Compile the demo program

We are going to Compile a GPIO demo that Blinks the Onboard LED on Tang Primer.

Use the following cammand to compile the Demo.

```
cd sirv-e-sdk

make software PROGRAM=demo_gpio BOARD=sirv-e203-lichee
```

## Upload Demo to the board

We need to first setup proper permissions to access USB Debugger.

Add your username to plugdev group. Replace `<username>` with your present working system's username.

```
sudo usermod -a -G plugdev <username>
```

Set udev rules to enable Tang Primer to be accessed by the plugdev group,

Execute the following command in terminal to create a new udev rules file.

```
sudo nano /etc/udev/rules.d/45-dt2232.rules
```
Copy the following code into the text editor and save it, as shown in the following image.

```
SUBSYSTEMS=="usb", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6010", \
  GROUP="plugdev", \
  MODE="0660"
```

Execute the following command in terminal to restart the udev service.

```
sudo service udev restart
```

Press `ctrl+x` to save the file

Connect Tang Primer with RV Debugger as shown below.

|   Tang Primer   | RV Debugger |
| --------------- | ----------- |
| U0_RX (Pin H13) | TX          |
| U0_TX (Pin J13) | RX          |
| E_TMS (Pin C9)  | TMS         |
| E_TDI (Pin B6)  | TDI         |
| E_TCK (Pin C5)  | TCK         |
| E_TDO (Pin A4)  | TDO         |
| GND   (Pin G)   | GND         |


> Pin locations on the Tang board can be found in [Pinout Diagram](/en/hardware-overview/lichee-tang/#pinouts).


Execute the following command in “sirv-e-sdk” folder to upload demo into the board.

```
make upload PROGRAM=demo_gpio BOARD=sirv-e203-lichee
```

## Debugging the Demo

OpenOCD provides us a nice way to debug our programs.

Run the OpenOCD GDB server with the following command and leave it running.

```
make run_openocd PROGRAM=demo_gpio BOARD=sirv-e203-lichee
```

In the other Terminal run the following command to debug your code using familiar GDB Debugger.

```
make run_gdb PROGRAM= demo_gpio BOARD=sirv-e203-lichee
```