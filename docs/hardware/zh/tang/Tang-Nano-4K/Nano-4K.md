# Tang Nano 4K 

## Tang Nano 4K 开发板

Tang Nano 4K是基于[高云半导体](http://www.gowinsemi.com.cn/)的小蜜蜂系列 GW1NSR-LV4C 设计的简约型开发板。开发板设计小巧精致，将芯片的所有资源都引出，板载Type-C、USB-JTAG、DVP、HDMI座子及其电路等，并把所有IO资源引出，方便开发者拓展使用，非常适用于小型数字逻辑的设计和实验。

![Tang Nano 4K](./../Tang-Nano/assets/4k-1.jpg)
![Tang Nano 4K](./../Tang-Nano/assets/4k-2.jpg)

## 产品参数

Tang Nano 4K开发板板载的GW1NSR-LV4C，是一款系统级封装芯片，内部集成了GW1NS系列可编辑逻辑器件产品和PSRAM存储芯片。

- 下表为与前代同系列产品对比图

| 型号             | Tang Nano           | Tang Nano 4K      |
| ---------------- | ------------------- | ----------------- |
| FPGA芯片         | GW1N-1-LV           | GW1NSR-LV4C       |
| 逻辑单元         | 1152                | 4608              |
| 寄存器           | 864                 | 3456              |
| 硬核处理器       | 无                  | Coetex M3         |
| Block SRAM(bits) | 72K                 | 180K              |
| 用户闪存(bits)   | 96K                 | 256K              |
| 锁相环PLL        | 1                   | 2                 |
| I/O Bank 总数    | 4                   | 4                 |
| 最多用户I/O数    | 41                  | 44                |
| 显示屏接口       | 标准40P RGB LCD接口  | HDMI接口          |
| 摄像头接口       | None                | 常见的DVP顺序接口 |
| 尺寸             | 58.4mm\*21.3mm      | 60mm\*22.86mm     |
| 下载接口         | USB Type-C接口      | USB Type-C接口    |

### 引脚图

![Pinmap](./../Tang-Nano/assets/Tang_nano_4K_0813.png)

## 开发环境

特别注意：
使用ide的时候版本需要>= v1.9.7.01 Beta；烧录软件要求使用我们所提供的 [Programmer](https://dl.sipeed.com/shareURL/TANG/programmer)
- 安装IDE的方法[参考](./../Tang-Nano-Doc/get_started/install-the-ide.md)

## 下载方式

Tang Nano 4K 开发板板载 BL702 芯片，为 GW1NSR-4C 提供 JTAG 调试功能，开发板可以直接连接电脑使用 [GOWIN programmer](https://dl.sipeed.com/shareURL/TANG/programmer) 进行下载比特流，不需要额外准备下载器。

## 资料

- [相关例程](./../Tang-Nano-Doc/examples.html)
- [Schematic](https://dl.sipeed.com/shareURL/TANG/Nano%204K/HDK/02_Schematic)
- [Tang Nano 4K 资料库](https://dl.sipeed.com/shareURL/TANG/Nano%204K)

## 补充

1. 如果有什么疑问，欢迎加群 `834585530`, 或者去[论坛](bbs.sipeed.com)发帖。
2. 下载 FPGA 是要求使用 [这里](https://dl.sipeed.com/shareURL/TANG/programmer) 的 Programmer 软件。不然有极大概率不能下载固件到板子。
3. 有问题的话先去 [常见问题](./../Tang-Nano-Doc/questions.md) 自查，通常来说使用 [这里](https://dl.sipeed.com/shareURL/TANG/programmer) 的 Programmer 软件能解决 99% 问题。
4. 对于 Cortex-M3 硬核建议使用串口来打印调试信息来纠错，或者有能力的可以选择其他方式。