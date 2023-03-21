# Tang Nano 4K 

> Edit on 2022.08.16

## Introduction

Tang Nano 4K is a development board designed based on [Gowin](https://www.gowinsemi.com/en/) little-bee GW1NSR-LV4C FPGA chip. The board is equipped with camera interface and HDMI interface. There is also an onboard USG-JTAG debugger, which make it convinent for users to use. Its Cortex-M3 hardcore can help users study mcu.

![Tang Nano 4K](./assets/4k-1.jpg)
![Tang Nano 4K](./assets/4k-2.jpg)

## Specs

- The sheet below shows difference with previous product

| model               | Tang Nano             | Tang Nano 4K   |
| ------------------- | --------------------- | -------------- |
| FPGA chip           | GW1N-1-LV             | GW1NSR-LV4C    |
| logic units         | 1152                  | 4608           |
| Register            | 864                   | 3456           |
| Hard core           | none                  | Coetex m3      |
| Block SRAM(bits)    | 72K                   | 180K           |
| User flash(bits)    | 96K                   | 256K           |
| Number of PLL       | 1                     | 2              |
| Number of I/O Bank  | 4                     | 4              |
| Number of users I/O | 41                    | 44             |
| Screen interface    | 40P RGB LCD interface | HDMI interface |
| camera interface    | None                  | DVP interface  |
| Size                | 58.4mm\*21.3mm        | 60mm\*22.86mm  |

### Pinmap

![Pinmap](./../../../zh/tang/Tang-Nano/assets/Tang_nano_4K_0813.png)

## Development software

Visit [install ide](https://wiki.sipeed.com/hardware/en/tang/Tang-Nano-Doc/install-the-ide.html) to setup your programming environment.

## Burn firmware

Tang Nano 4K uses the onboard BL702 for jtag, with which to burn bitstream.

Run the Programmer in Gowin IDE to download firmware into FPGA.

## Information

- [Examples](https://wiki.sipeed.com/hardware/en/tang/Tang-Nano-Doc/examples.html)
- [Schematic](https://dl.sipeed.com/shareURL/TANG/Nano%204K/HDK/02_Schematic)
- [Download center](https://dl.sipeed.com/shareURL/TANG/Nano%204K/)

## Addition

1. If you have trouble with this board, you can join our telegram (t.me/sipeed) or contact us on twitter (https://twitter.com/SipeedIO). Leaving message below is also OK.
2. Visit [Tang questions](https://wiki.sipeed.com/hardware/en/tang/Tang-Nano-Doc/questions.html) first if you have any trouble.
3. Debugging Cortex-M3, we suggest to use serial-port debug way. If you are excellent enough you can try other ways to debug it.
4. THe HDMI ports are multiplexed as IO and routed to the pin headers. The actual results of the IO which are multiplexed with HDMI pins on the pin headers may not be consistent with what you want because of the external pull up.
    ![nano_4k_hdmi_io](./../../../zh/tang/Tang-Nano-4K/assets/nano_4k_hdmi_io.png)