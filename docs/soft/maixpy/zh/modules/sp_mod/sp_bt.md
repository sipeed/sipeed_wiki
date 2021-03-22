---
title: SP_BT 的使用
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: SP_BT 的使用
---


<img src="../../../assets/hardware/module_spmod/sp_bt.png"/>

SP_BT 是一款蓝牙串口透传模块， 具备超低功率特性和高可靠性， 使用 AT 指令进行控制， 蓝牙版本为 BLE 5.0(兼容BLE4.0, BLE4.2), 默认串口波特率为9600.

## 参数

* 接收灵敏度: -97dm
* 发射功率: 4db(最大)
* 通信接口: UART
* 天线: 板载天线
* 主从支持: 从机
* 工作频段: 2.4G
* 工作温度: -40°C~85°C
* 工作电压: 1.8V~3.6V

模块详细信息请参考[BT 规格书与数据手册](https://api.dl.sipeed.com/fileList/MAIX/HDK/Spmod_EN/SP-BT%20Datasheet%20V1.0.pdf)

## 使用说明

1. 准备: 已烧录最新固件的开发板, sp_bt 模块, 蓝牙调试助手.

2. 运行: 连接模块, 修改[示例代码](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/spmod/sp_bt)中 config 包围的配置, 运行后使用蓝牙调试助手连接并发送数据, 即可在终端查看收发信息.

程序如下:

```python
# set uart rx/tx func to io_6/7
fm.register(TX, fm.fpioa.UART1_TX)
fm.register(RX, fm.fpioa.UART1_RX)
# init uart
uart = UART(UART.UART1, 9600, 8, 1, 0, timeout=1000, read_buf_len=4096)

set_name(uart, name)
print("wait data: ")
while True:
  read_data = uart.read()
  if read_data:
      print("recv:", read_data)
      uart.write(read_data)  # send data back
      print("wait data: ")
```

主要步骤为:

* 初始化串口(波特率为模块默认波特率9600)

* 设置模块广播名

* 等待连接, 接收数据打印后发送回去

## 连接过程

* 模块初始化后处于未连接状态(指示灯: ACT 闪烁, STA 常灭).
  
* 蓝牙调试助手连接后模块变为已连接(指示灯: ACT 常亮, STA 常亮).
  
* 连接后蓝牙调试助手会显示的服务如下图:
  
  <img src="../../../assets/hardware/module_spmod/sp_bt_screenshot.png" alt="bt_server"/>
  
  上图中可以看到有一个 UUID 为 ffe0 的服务有两个特征, 打开透传(ffe1)的 Write, Notify, 便可以开始发送/接收数据.
