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

## Development methods

Note:

- GOWIN IDE verision should over v1.9.7.01 Beta.
- The programmer application used for burning FPGA should be this one: [Click me](https://dl.sipeed.com/shareURL/TANG/programmer)
- Visit [Install-IDE](./../Tang-Nano-Doc/install-the-ide.md) to install IDE.

## Burn methods

Tang Nano 4K contains a on-board BL702 chip, used for burning GW1NSR-4C chip. Just connect this coard with computer and use this [GOWIN programmer](https://dl.sipeed.com/shareURL/TANG/programmer) to burn bitstream, not need extra debugger to download.

## Information

- [Examples](./../Tang-Nano-Doc/examples.md)
- [Schematic](https://dl.sipeed.com/shareURL/TANG/Nano%204K/HDK/02_Schematic)
- [Download center](https://dl.sipeed.com/shareURL/TANG/Nano%204K/)

## Addition

1. If you have trouble with this board, you can join our telegram (t.me/sipeed) or contact us on twitter (https://twitter.com/SipeedIO).

2. For Fpga burning we require using [this](https://dl.sipeed.com/shareURL/TANG/programmer) Programmer application. Because other version Programmer application may fail burning this board.

3. If you meet problems, please visit [problems](./../Tang-Nano-Doc/questions.md) first, normally most problems will be solved after using this programmer [Click me](https://dl.sipeed.com/shareURL/TANG/programmer).

4. For debugging Cortex-M3, we suggest to use serial-port debug way. If you are excellent enough you can try other ways to debug it.