---
title: SP_Ethernet 的使用
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: SP_Ethernet 的使用
---


<img src="../../../assets/hardware/module_spmod/sp_ethernet.png">

该模块采用 W5500作为主控芯片，这是一款集成全硬件 TCP/IP 协议栈的嵌入式以太网控制器。

## 参数

* 工作电压：2.6V~3.6V
* 工作电流：<132mA
* 休眠电流：<15mA
* 通讯接口：SPI
* 工作温度范围：-40℃ ~ 85℃

模块详细信息请参考[Ethernet 规格书](https://api.dl.sipeed.com/fileList/MAIX/HDK/Spmod_EN/SP-Ethernet%20Datasheet%20V1.0.pdf)

## 使用方法

1. 准备: 已烧录最新固件的开发板, sp_ethernet 模块， 网线。
2. 运行: 连接模块, 修改[示例代码](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/spmod/sp_ethernet)中 config 包围的配置, 运行后模块将打印通信数据。

程序如下：

```python
spi1 = SPI(4, mode=SPI.MODE_MASTER, baudrate=600 * 1000,
            polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=WIZNET5K_SPI_SCK, mosi=WIZNET5K_SPI_MOSI, miso = WIZNET5K_SPI_MISO)

#  create wiznet5k nic
nic = network.WIZNET5K(spi = spi1, cs = WIZNET5K_SPI_CS)
print("Static IP: ", nic.ifconfig())
```

* 创建 SPI 并使用 SPI 创建 WIZNET5K 有线网卡
* 打印当前 IP 信息

相关 API 参考: [wiznet5k API](../../api_reference/machine/network.html#wiznet5k)