---
title: SP_LORA 的使用
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: SP_LORA 的使用
---


<img src="../../../assets/hardware/module_spmod/sp_lora.png"/>

SP_LoRa 模块使用 M-XL8 模组, 其内置 LoRaTM 调制解调器和可调功率放大器的 LoRa 模块, 具有高性能和高可靠性.

## 参数

* 工作频段: 370MHz~1200Mhz
* 发射功率: 20dBm(最大)
* 通信接口: SPI
* 天线: 外置天线,IPEX 或焊接
* 接收灵敏度: -148dbm
* RSSI 动态范围: 127dB
* 工作电压: 1.8V~6.3V
* 工作温度: -40°C~80°C

模块详细信息请参考[LoRa 规格书与数据手册](https://api.dl.sipeed.com/fileList/MAIX/HDK/Spmod_EN/SP-LoRa%20Datasheet%20V1.0.pdf)

## 使用方法

1. 准备: 两块已烧录最新固件的开发板, 两个 sp_lora 模块.

2. 运行: 连接模块, 修改[示例代码](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/spmod/sp_lora)中 config 包围的配置, 两块开发板分别运行发送和接收函数, 即可在终端查看收发信息.

程序如下:

```python
# init
lora = SX127x(spi=spi1, pin_ss=cs)

# lora reset
rst.value(0)
time.sleep_ms(10)
rst.value(1)
time.sleep_ms(100)
lora.init()

####### receiver ###########
receive(lora)

######## sender ###########
# send(lora)

'''output
mpfs [/flash]> runfile lora_send.py
    transfer 6400 of 14576
    transfer 12800 of 14576
    transfer 14576 of 14576
[Warning] function is used by fm.fpioa.GPIOHS7(pin:23)
LoRa Sender
Sending packet:
Hello(0)

mpfs [/sd]> runfile lora_recv.py
    transfer 6400 of 14576
    transfer 12800 of 14576
    transfer 14576 of 14576
[Warning] function us used by fm.fpioa.GPIOHS7(pin:23)
LoRa Receiver
[Memory - free: 470080 allocated: 48064]
*** Received message ***
Hello(0)
with RSSI: <bound_method 800d19e0 <SX127x object at 800f5700>.<function packetRssi at 0x800d3180>>
'''
```

这里使用的调试运行工具为 mpfshell 方便同时打开两个终端运行脚本.

主要步骤为:

* 创建 LoRa 对象(参数为: SPI 对象, 片选脚)

* 复位(将复位引脚拉低有拉高), 初始化.
  
* 开始发送或接收.
