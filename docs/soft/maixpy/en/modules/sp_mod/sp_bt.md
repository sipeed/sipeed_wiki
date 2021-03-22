---
title: Use of SP_BT
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: use of SP_BT
---


<img src="../../../assets/hardware/module_spmod/sp_bt.png"/>

SP_BT is a Bluetooth serial port transparent transmission module with ultra-low power characteristics and high reliability. It is controlled by AT commands. The Bluetooth version is BLE 5.0 (compatible with BLE4.0, BLE4.2) and the default serial port baud rate is 9600.

## Parameters

* Receiving sensitivity: -97dm
* Transmitting power: 4db (maximum)
* Communication interface: UART
* Antenna: Onboard antenna
* Master-slave support: slave
* Working frequency: 2.4G
* Working temperature: -40°C~85°C
* Working voltage: 1.8V~3.6V

For detailed module information, please refer to [BT Specification and Data Manual](http://api.dl.sipeed.com/shareURL/MAIX/HDK/sp_mod/sp_bt)

## Instructions for use

1. Preparation: The development board with the latest firmware, sp_bt module, Bluetooth debugging assistant.

2. Run: Connect the module, modify the configuration surrounded by config in [Sample Code](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/spmod/sp_bt), use the Bluetooth debugging assistant to connect and send after running Data, you can view the received and sent information on the terminal.

The procedure is as follows:

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
      uart.write(read_data) # send data back
      print("wait data: ")
```

The main steps are:

* Initialize the serial port (the baud rate is 9600 by the module default baud rate)

* Set the module broadcast name

* Wait for connection, send back after receiving the data and printing

## Connection process

* After the module is initialized, it is not connected (indicator: ACT flashes, STA is always off).
  
* After the Bluetooth debugging assistant is connected, the module becomes connected (indicators: ACT is always on, STA is always on).
  
* The services displayed by the Bluetooth debugging assistant after connection are as follows:
  
  <img src="../../../assets/hardware/module_spmod/sp_bt_screenshot.png" alt="bt_server"/>
  
  In the above figure, you can see that there is a service with a UUID of ffe0 that has two characteristics.Turn on the Write and Notify of the transparent transmission (ffe1) to start sending/receiving data.
