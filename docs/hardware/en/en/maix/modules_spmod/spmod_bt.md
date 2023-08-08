# SPMOD - BT


## Overview

<img src="../../assets/spmod/spmod_bt/sp_bt.png" alt="XXX" style="zoom:40%;" />

SPMOD-BT(Bluetooth module) uses YDJ-23.

## SPMOD - BLE Introduction

- Using **Sipeed-SPMOD** interface(2.54mm * 8PIN )，unified MaixPy board interface
- Using SP-MOD UART to communicate with Bluetooth module
- JDY-23 Bluetooth module:Support BLE 5.0(Compatible with BLE4.0、BLE4.2).Communication interface adopts UART interface. The module supports AT command control. It has ultra-low power design and high reliability design.
- Two built-in LED，making module status easier to see.
- Size:25.6\*20.2\*3.2mm

### JDY-23 Introduction:

| Features: | --- |
| --- | -- |
| Working Frequency:| 2.4GHz|
| Transmission Power:| 4db(maixmun) |
| Communication Interface:| UART |
| Supply voltage of external power supply :| 1.8V~3.6V |
| Range of working temperature :| -40℃ - 80℃ |
| Antenna:| Built-in PCB antenna
| Reception Sensitivity:| -97dbm |
| Support master-slave: | Slave |
| Bluetooth Version:| BLE 5.0(Compatible with BLE4.0、BLE4.2) |
| Awakening Current State:| 800uA(Transmission) |
| Sleep Status of Current:| <50uA (Transmission) |
| Deep Sleep of Current:| 9uA (Not transmission) |
| Default baud rate:| 9600 |

### SPMOD_BT pin description :

| Pin | Name | Type | Description |
| -------- | -------- | ---- | --- |
| 1 | GND | G | Ground |
| 2 | AWK | I/O | Sleep wake-up pin (active low) |
| 3 | STA | I/O |  The status of the pin connection |
| 4 | RX | I | Serial input pin (TTL level) |
| 5 | 3V3 | V |  Power supply(3.3V) |
| 6 | --- | NC | Not connected |
| 7 | RST | I/O | Reset (active low) |
| 8 | TX  | O | Serial output pin (TTL level) |

<img src="../../assets/spmod/spmod_bt/back.jpg" height="250" />

- Mode of connection:

| MCU:FUN(IO) | SP_BT |
| :---------: | :---: |
| UART:TX(IO_7) | RX |
| USRT:RX(IO_6) | TX |
| 1.8-3.3V | 3.3V |
| GND | GND |

<img src="../../assets/spmod/spmod_bt/connection.png" height="250">

### AT instruction list:

| Order | Description |
| --- | --- |
|AT+POWR | Get transmit power |
|AT+RST	| Soft reset |
|AT+MAC	| Display MAC address |
|AT+NAME | Display Transmission name |
|AT+HOSTEN | Slave mode or IBEACON work mode |
|AT+IBUUID | UUID of IBEACON |
|AT+DISC | Disconnect |
|AT+SLEEP | Configures the Sleep mode |
|AT+MTU | Set the serial port for the APP to send a long number of packets |

*See [JDY-23-V2.1.pdf](https://cn.dl.sipeed.com/shareURL/MAIX/HDK/sp_mod/sp_bt) for more information*

## Usage

* Process
  1. Send AT instruction
  2. Receive the reply
  3. Determines whether the setup was successful

### C :

  ```c
  // set uart rx/tx func to io_6/7
  fpioa_set_function(6, FUNC_UART1_RX + UART_NUM * 2);
  fpioa_set_function(7, FUNC_UART1_TX + UART_NUM * 2);
  uart_init(UART_DEVICE_1);
  uart_configure(UART_DEVICE_1, 9600, 8, UART_STOP_1, UART_PARITY_NONE);

  //change the name of sp_bt module to MAIXCUBE
  uart_send_data(UART_NUM, "AT+NAMEMAIXCUBE\r\n", strlen("AT+NAMEMAIXCUBE\r\n")); //send AT order
  msleep(100);
  ret = uart_receive_data(UART_NUM, rcv_buf, sizeof(rcv_buf)); //receive response
  if(ret != 0 && strstr(rcv_buf, "OK"))
  {
     printk(LOG_COLOR_W "set name success!\r\n");
  }

  // get the name of sp_bt module
  uart_send_data(UART_NUM, "AT+NAME\r\n", strlen("AT+NAME\r\n")); //send AT order
  msleep(100);
  ret = uart_receive_data(UART_NUM, rcv_buf, sizeof(rcv_buf)); //receive response
  if(ret != 0 && strstr(rcv_buf, "NAME"))
  {
     printk(LOG_COLOR_W "get name success!\r\n");
  }
  ```

### MaixPy :

  ```python
    # set uart rx/tx func to io_6/7
  fm.register(6,fm.fpioa.UART1_RX)
  fm.register(7,fm.fpioa.UART1_TX)
  uart = UART(UART.UART1,9600,8,1,0,timeout=1000, read_buf_len=4096)

  #change the name of sp_bt module to MAIXCUBE
  uart.write("AT+NAMEMAIXCUBE\r\n") #send AT order
  time.sleep_ms(100)
  read_data = uart.read() #receive response
  if read_data:
      read_str = read_data.decode('utf-8')
      count = read_str.count("OK")
      if count != 0:
          uart.write("set name success\r\n")

  # get the name of sp_bt module
  uart.write("AT+NAME\r\n") #send AT order
  time.sleep_ms(100)
  read_data = uart.read() #receive response
  if read_data:
      read_str = read_data.decode('utf-8')
      count = read_str.count("NAME")
      if count != 0:
          uart.write("get name success\r\n")
  ```

*Note that you must add \r\n after sending AT instruction*

### Result:

  Using [BLE Utility](../../tools/bledebugger.apk) to connect the device to do the send and receive test results are as follows:


  <center class="third">
      <img src="../../assets/spmod/spmod_bt/res.png" height="250"/><img src="../../assets/spmod/spmod_bt/res1.png" height="250"/>
  </center>

### Runtime environments:

  |  Language  |  Board  | SDK/Firmware version |
  | :----: | :------: | :----------------------------- |
  |   C    | MaixCube | kendryte-standalone-sdk v0.5.6 |
  | MaixPy | MaixCube | maixpy v0.5.1                  |

## Outlook

- SPMOD_BLE Size drawing:

<img src="../../assets/spmod/spmod_bt/sipeed_spmod_bt.png" height="250" />


## Resource Link

| Resource | --- |
| --- | --- |
| Website | www.sipeed.com |
| Github | [https://github.com/sipeed](https://github.com/sipeed) |
| BBS | [http://bbs.sipeed.com](http://bbs.sipeed.com) |
| Wiki | [http://maixpy.sipeed.com](http://wiki.sipeed.com/maixpy) |
| Sipeed model shop | [https://maixhub.com/](https://maixhub.com/) |
| SDK Relevant information | [dl.sipeed.com/MAIX/SDK](dl.sipeed.com/MAIX/SDK) |
| HDK Relevant information | [dl.sipeed.com/MAIX/HDK](dl.sipeed.com/MAIX/HDK) |
| E-mail(Technical Support and Business Cooperation) | [Support@sipeed.com](mailto:support@sipeed.com) |
| telgram link | [https://t.me/sipeed](https://t.me/sipeed) |