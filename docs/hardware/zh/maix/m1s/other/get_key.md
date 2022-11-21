---
title: M1s 获取机器码
keywords: M1s DOCK ,BL808, M1s
update:
  - date: 2022-11-10
    version: v0.1
    author: wonder
    content:
      - 初次编辑
---

在 [MaixHub](https://maixhub.com/) 下载模型的时候会要求输入机器码，这里说明一下怎么获得机器码。

如果进行下面步骤后没有得到机器码的话，查看[常见问题](#常见问题)

## 简述

简述步骤如下：
- 将开发板通过 UART 串口与电脑连接（电脑设备管理器中会出现两个串口）
- 使用任意串口工具，设置波特波特率为 2000000 （1 个 2 和 6 个 0），打开开发板在电脑中所显示的较大的串口号
- 按下开发板上的 RST 按键，在打印的串口信息如下（仅作示例）

```bash
# 省略若干
[MTD] >>>>>> Hanlde info Dump >>>>>>
      name D0FW
      id 0
      offset 0x00100000(1048576)
      size 0x00200000(2048Kbytes)
      xip_addr 0x580f0000
[MTD] <<<<<< Hanlde info End <<<<<<
D0FW addr:0x580f0000 size:0x200000
MM CPU select PLL--->MM CPU select 400Mhz
UART CLK select MM XCLK--->XCLK select XTAL
I2C CLK select MM XCLK--->XCLK select XTAL
SPI CLK select 160Mhz
MM BUS CLK select 160Mhz
XCLK select XTAL
irq handle: 3 reset ev

------------------------ CHIP KEY --------------------------
key:57F80642C3F97E2655772C48AF17455EC9E79BBF76C16EED4E0EC1096D664435
------------------------------------------------------------
```

- 可以从最后面的 `CHIP KEY` 得到下载模型所需要的机器码了

> 每块板子的 `CHIP KEY` 都不一样，上面仅作示范参考，实际 `CHIP KEY` 根据每个人操作来获得。

## 详述

1. 将板子的 UART 口通过 Type-C 数据线与电脑连接起来
   ![uart_connect](./assets/get_key/uart_connect.png)

2. 打开电脑串口工具（根据自己的串口软件自行更改），设置波特率为 2000000 （1 个 2 和 6 个 0），打开开发板在电脑上显示的较大串口号
   <img src="./assets/get_key/baudrate_2000000.png" width=45% alt="baudrate_2000000">
   <img src="./assets/get_key/bigger_com_port.png" width=45% alt="bigger_com_port">

3. 打开串口；按下板子上面的 RST 按键。在串口打印信息的最后看到 `CHIP KEY` 。

<table>
    <tr>
    <th>按一下 RST 按键再松开</th>
    <th>串口软件显示出来机器码</th>
    </tr>
    <tr>
    <td><img src="./assets/get_key/rst_key.png" alt="rst_key"></td>
    <td><img src="./assets/get_key/chip_key.png" alt="chip_key"></td>
    </tr>
</table>

## 常见问题

### 串口乱码

确认自己设置的波特率为 2000000 （2M）

### 复位后的信息中没有 CHIP KEY

这种情况可以通过更新为最新固件来解决，[点我跳转到最新固件下载地址](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/7_Firmware)，选择文件名为 `firmware_m1sdock` 开头的文件，烧录方法请参考[该网页](https://github.com/sipeed/M1s_BL808_example) (Github) 里面的 **Download e907 firmware**

### 没有显示出两个串口

可以参考[该网页](https://github.com/sipeed/M1s_BL808_example) (Github) 里面的 **Download bl702 firmware** 重新烧录一次串口固件，双串口固件下载地址为 [这里](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/7_Firmware)，其名称以 `usb2dualuart_bl702.bin` 开头

### 没有显示出任何串口

首先应当确认自己所接通的是 UART 口，然后可以根据本篇所述的[没有显示出两个串口](#没有显示出两个串口)重新烧录一下串口固件