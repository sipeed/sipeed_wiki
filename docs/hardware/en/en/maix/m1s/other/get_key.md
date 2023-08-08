---
title: M1s Machine Code
keywords: M1s DOCK ,BL808, M1s
update:
  - date: 2022-11-21
    version: v0.1
    author: wonder
    content:
      - New file
---

When we download models from [MaixHub](https://maixhub.com/), the machine code is required. Here we are talking about how to get the machine code.

If you did not get your machine code after doing the following steps, just see the end [Questions](#questions) chapter at the end of this page.

## Brief steps

Here are the steps:
- Connect the board with computer through USB UART port (2 UART Ports will appear in your computer)
- Run UART application to open the UART device, set the Baudrate 2000000 (one 2 and six 0), open the bigger UART port
- Press onboard `RST` key, and the log message is as following

```bash
# logs
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

- We can see the `CHIP KEY` in the end, which is our machine code.

> The `CHIP KEY` of each board is different, the actual `CHIP KEY` should be got by yourself

## Detailed Steps

1. Connect your board with your computer by Type-C cable through USB UART port
   ![uart_connect](./../../../../zh/maix/m1s/other/assets/get_key/uart_connect.png)

2. Run the UART application, set Baudrate 2000000 (one 2 and six 0), choose the bigger UART port
   <img src="./../../../../zh/maix/m1s/other/assets/get_key/baudrate_2000000.png" width=45% alt="baudrate_2000000">
   <img src="./../../../../zh/maix/m1s/other/assets/get_key/bigger_com_port.png" width=45% alt="bigger_com_port">

3. Open Serial port; Press the `RST` key on your board, then you will see your `CHIP KEY` in the log.

<table>
    <tr>
    <th>Click RST</th>
    <th>Chip KEY in logs</th>
    </tr>
    <tr>
    <td><img src="./../../../../zh/maix/m1s/other/assets/get_key/rst_key.png" alt="rst_key"></td>
    <td><img src="./../../../../zh/maix/m1s/other/assets/get_key/chip_key.png" alt="chip_key"></td>
    </tr>
</table>

The `CHIP KEY` is your machine code

## Questions

### Messy logs

Make sure your Baudrate is 2000000 (2M)

### No CHIP KEY in logs

This means you need upgrade your firmware, [Click me](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/7_Firmware/factory) to download the firmware, choose the file starts with `firmware`,and visit the **Download e907 firmware** [here](https://github.com/sipeed/M1s_BL808_example) (Github) to burn it.

### No two Serial port

visit the **Download bl702 firmware** [here](https://github.com/sipeed/M1s_BL808_example) (Github) to burn the onboard serial chip, and the firmware can be downloaded [here](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s_Dock/7_Firmware), choose the file starts with `usb2dualuart_bl702`.

### No Serial port

Make sure you have connected the computer with the UART port on the board first, then try to burn the onboard serial chip by following [No two Serial port](#no-two-serial-port)