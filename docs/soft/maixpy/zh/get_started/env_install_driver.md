---
title: 安装 USB 驱动
keywords: maixpy, k210, AIOT, 边缘计算, maixpy入门
desc: maixpy  安装 USB 驱动
---


正式使用 MaixPy 之前，我们需要先安装好串口驱动，才可进行下一步的开发与使用；因为板子是通过 USB 转串口设备与电脑连接（K210 没有 USB 硬件支持功能）。
根据板子的 USB 转串口芯片型号装驱动。

> 在 `Linux` 或者 `Mac` 下操作串口， 如果不想每次都使用 `sudo` 命令， 执行 `sudo usermod -a -G dialout $(whoami)` 将自己添加到 `dialout` 用户组即可，可能需要注销或者重启才能生效


- 现有开发板板载的 USB 转串口 IC 说明

| 开发板型号   | USB 转串口 IC           | 说明           | 安装教程                                   |
| ------------ | ----------------------- | -------------- | ------------------------------------------ |
| Maix Go      | STM32                   | STM32 USB 驱动 | [Go](./install_driver/go.md)               |
| Maix Dock    | CH340                   |                | [Dock](./install_driver/dock.md)           |
| Maix Duino   | CH552                   | CH552 USB 驱动 | [Duino](./install_driver/duino.md)         |
| Maix Bit     | CH552(新版)/CH340(旧版) | CH552 USB 驱动 | [Bit](./install_driver/bit.md)             |
| Maix Cube    | GD32(新版)/CH552(旧版)  | CH552 USB 驱动 | [Cube](./install_driver/cube.md)           |
| Maix Amigo   | GD32                    | GD32  USB 驱动 | [Amigo](./install_driver/amigo.md)         |
| Maix Nano    | CH552                   | CH552 USB 驱动 | [Nano](./install_driver/nano.md)           |
| Grove AI HAT | GD32                    | GD32  USB 驱动 | [Grove AI HAT](./install_driver/ai_hat.md) |

> 使用 CH340 IC 的板子直接装 CH340 的驱动即可，其他的板子需要安装特定的 USB 驱动

## 关于 USB 串口的疑难杂症排查

如果没有看到串口，请按如下顺序排查硬件问题。

- 插入电脑，是否存在叮咚一声，如插入 U 盘时USB 驱动加载的声音，没有表示硬件上的串口芯片出问题了。
- 更换线材重试，更换电脑 USB 口重试，仍然加载不出来，更换电脑确认。

如果没有办法烧录固件，请按如下顺序排查硬件问题。

- 使用串口工具查看硬件当中是否存在 maixpy 固件
- 设置 115200 波特率连接串口，按复位键（RST）接收到芯片的数据，不管是什么都表示串口芯片工作正常，如果没有则表示硬件异常。
- 基于上述再进行烧录固件，烧录前，按硬件的 BOOT 键后按复位，再松开 BOOT 键，此时烧录正常进行，如果没有则表示 Flash 受损，可以尝试烧录到 SRAM ，如果烧录失败，则表示串口芯片异常。
- 如果到这里了，还是不能解决问题，则硬件确实存在缺陷

### K210 的烧写机制介绍

我们常把这个称为一键下载电路，表示能够轻松的通过控制 串口的 RST 和 DTR 的完成对 BOOT 和 RST 引脚的控制进入烧录模式，如上描述的期望硬件电路自动完成最初由人按下 BOOT 后按 RST 的操作，这与硬件实现强相关，基于此，再进行 TX 和 RX 的数据传输，所以实际上我们需要用到 UART 串口的功能引脚。

在 Kflash 中分多种版型多种烧写方式的触发，我们可以简单分为几类，低速的 115200 和 高速的 1500000 波特率，以这两类波特率所匹配的烧录方式为差异点，如果发现下载过程中失败，可以适当的降低波特率，这是由于串口芯片工作不稳定导致，而工具中对版型选择只是会影响第一段烧录模式的触发，而在这之后的烧写固件中就会采取配置的波特率进行烧写，通常不超过与flash的通信烧录速度，常见于 50~60 KB/S。

如果发现无论如何更换烧录模式都无法进入，要么是烧录版型不匹配，要么是串口芯片的 DTR RST 引脚出了问题（物理上的）。


