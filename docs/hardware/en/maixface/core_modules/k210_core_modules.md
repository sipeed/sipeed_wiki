# K210 core module

There are four AIOT modules developed based on K210: M1, M1w, M1n, MF0

- Feature description:

These four modules are based on Canaan Kanzhi Technology's edge intelligent computing chip K210 (RISC-V architecture). The main control chip has a built-in 64-bit dual-core high-performance low-power processor, each core has a floating-point unit (FPU), a convolutional artificial neural network intelligent hardware accelerator (KPU) and a fast Fourier transform accelerator (FFT) , Equipped with Field Programmable IO Array (FPIOA), supports a variety of mainstream AI programming frameworks.

### Maix AIOT module difference comparison

|                                               | M1                                                           | M1w                                                          | M1n                                                          | MF0                                                          |
| --------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Exterior                                      | ![M1 module](../../assets/mf_module/m1_m1w/sipeed_m1_module.png) | ![M1W module](../../assets/mf_module/m1_m1w/sipeed_m1w_module.png) | ![M1n module](../../assets/mf_module/m1n/sipeed_m1n_module.png) | ![MF0 module](../../assets/mf_module/mf0_mf0dock/sipeed_mf0_module.png) |
| size                                          | 25.4x25.4x3.3（mm）                                          | 25.4x25.4x3.3（mm）                                          | 25.0x22.0x2.7（mm）                                          | 20.0x20.0x4.5（mm）                                          |
| Voltage output (provided to the bottom board) | 1.8V and 3.3V                                                | 1.8V and 3.3V                                                | 1.8V and 3.3V                                                | 3.3V                                                         |
| Maximum power consumption (non-transient)     | 1.5W                                                         | 3W                                                           | 1.5W                                                         | 1.5W                                                         |
| WIFI                                          | None                                                         | K210 and ESP8285 are connected through SPI interface and serial port | None                                                         | None                                                         |
| Onboard camera connector                      | None                                                         | None                                                         | Yes (only compatible with single camera)                     | Yes (only compatible with single camera)                     |
| Pin form                                      | Stamp hole                                                   | Stamp hole                                                   | NGFF  B-KEY                                                  | 2.54mm pitch through pad + SMD pad                           |
| camera signal                                 | All leads                                                    | All leads                                                    | All leads                                                    | None                                                         |
| screen signal                                 | All leads                                                    | All leads                                                    | All leads                                                    | None                                                         |
| Lead out ordinary IO port                     | Quantity 48 (all lead out)                                   | Quantity 48 (all lead out)                                   | 44 (not drawn by IO0-3)                                      | 9                                                            |



## Module pin definition

Specific downloadable specifications

M1/M1w: https://dl.sipeed.com/MAIX/HDK/Sipeed-M1&M1W/Specifications

M1n: https://dl.sipeed.com/MAIX/HDK/Sipeed-M1n

MF0: https://dl.sipeed.com/MAIX/HDK/Sipeed-MF0/MF0-2802
