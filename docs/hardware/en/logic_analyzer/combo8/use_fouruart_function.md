---
title: Using as Serial Module
keywords: LogicAnalyzer, debugger, link, RISCV, tool
---

SLogic Combo8 has 4 independent high-speed serial port functionalities. The first two ports based on UART can achieve a super-high speed baud rate of up to 20Mbps simultaneously, while the latter two ports can reach up to 1Mbps through IO simulation. It is highly suitable for scenarios such as batch programming and production testing.

## Enable Serial Module Functionality

Press the toggle button to switch the indicator light to red.

![](../../../zh/logic_analyzer/assets/slogic_led_red.png)

> To verify if Serial Module functionality is enabled:
>
> Linux: Use the lsusb command to check if the UARTx4 HS USB device appears.

![](../../../zh/logic_analyzer/assets/slogic_linux_equipment_uart.png)

## Getting Started

### Hardware Connection

SLogic Combo8 has a total of 4 serial ports. UART0 and UART1 support a maximum baud rate of 20M, while UART3 and UART4 support a maximum baud rate of 1M. Refer to the panel pinout diagram and connect any UART's TX, RX, and GND to the RX, TX, and GND pins of the target device (note that RX and TX need to be crossed).

Note：
1. Ensure that the module and the target device share a common ground to prevent issues such as garbled data.
2. The device numbers on Windows may be in random order, so manual trial-and-error may be required to find the corresponding serial port.

### Linux

Please note: Due to system reasons, Linux may consider the device as a modem when it has more than one ttyACM. This may temporarily occupy the device for sending AT commands. In this situation, you may not be able to open the serial port, and it may report "Resource busy" due to device being occupied. This is normal, and it will return to normal after a while. To solve this problem, you can add a udev rule to avoid this issue. Please refer to the following commands:

```shell
sudo touch /etc/udev/rules.d/49-sipeed.rules
sudo echo "ATTRS{idVendor}==\"359f\", ATTRS{idProduct}==\"3101\", ENV{ID_MM_DEVICE_IGNORE}=\"1\"" > /etc/udev/rules.d/49-sipeed.rules
sudo udevadm control --reload
```


### Data Transmission and Reception

For Linux, you can use **picocom** or **minicom** as the serial communication tool. Install it using the following commands:

```Bash
sudo apt install picocom
sudo apt install minicom
```

For example, to use **minicom** with UART0 to communicate with the test device, open the Linux terminal using **CTRL+ALT+T**, enter the installation commands, and enter the administrator user password when prompted. Wait for the package installation to complete.

![](../../../zh/logic_analyzer/assets/minicom_install_uart.png)

After installation, communicate with the test device using UART0. In the terminal, enter the command:

```Bash
sudo minicom -b 2000000 -D /dev/ttyACM0
```

The **-b** parameter specifies the desired baud rate, which should be the same as the UART baud rate setting of the test device.

The **-D** parameter specifies the port to listen to.

![](../../../zh/logic_analyzer/assets/minicom_uart.png)

After entering the command, you can communicate with the test device, receive and print messages in the terminal, and send data to the test device.



#### Serial Loopback Test：

![](../../../zh/logic_analyzer/assets/uart_line_uart.jpg)
(Above: Serial module wiring diagram)

Loopback test result:
![](../../../zh/logic_analyzer/assets/minicom_test_uart.png)


### Windows

In the Windows system, you can use serial port tools like SSCOM and MobaXterm for serial communication. Here, we will take [SSCOM](http://www.daxia.com/) as an example to demonstrate how to conduct serial communication tests

1. Firstly, download and extract SSCOM.The software is open source software, please download it from Google.

2. After the download is complete, extract and launch the serial port tool. You will see the following interface:

   ![SSCOM Interface](../../../zh/logic_analyzer/assets/sscom_gui_en.png)

3. Connect the module to your PC. Then, in the Windows Device Manager (shortcut `Win + X + M`), check if the connection is successful and obtain the port number information

   ![Device Manager](../../../zh/logic_analyzer/assets/sscom_device_manage.png)

   Due to the characteristics of the Windows system, the serial port numbers might be in random order. Therefore, you can follow these steps to test the corresponding serial port numbers:

   - Connect the TX* and RX* pins of the module (* can be 0-3).
   - Set the baud rate, usually using 115200.
   - Open the serial port.
   - Sequentially try different port device numbers, click the "Send" button, and check if data is received to confirm the corresponding serial port for each

   ![Confirm Port](../../../zh/logic_analyzer/assets/sscom_determine_port.png)

4. After confirming the serial port numbers for each port, you can input the data you want to send in the data input window. Additionally, received data will also be displayed in the window

#### Send and Receive Testing

Using the SLogic 4xUART module for serial communication testing, the maximum speed for the first two virtual serial ports is 20Mbps. Here's an example of testing performance using SSCOM

##### Test 1Mbps (256kbps, 512kbps)

1. Connect TX2 and RX3.
2. Start two instances of SSCOM, connecting them to the respective serial ports
3. Set the baud rate to 1000000 and open the serial port
4. Create a 256KB text document with repeated common characters
5. Utilize SSCOM's file transmission feature, select the created text document and send it
6. The other instance of SSCOM will receive the data and confirm the received file content

The following is the result of the 1Mbps test. When checking the file size and data content and confirming 1Mbps, the test of sending and receiving 256kb data is successful

![](../../../zh/logic_analyzer/assets/uart_sscom_1mbps_256kb.png)

Increase the data of the text file to 512KB, and repeat the test, and confirm that at 1Mbps, the test of receiving and sending 512kb data is successful

![](../../../zh/logic_analyzer/assets/uart_sscom_1mbps_512kb.png)


##### Test 20Mbps (256kbps)

1. Connect TX0 and RX1.
2. Start two instances of SSCOM, connecting them to the respective serial ports
3. Set the baud rate to 20000000 and open the serial port
4. Create a 256KB text document with repeated common characters
5. Utilize SSCOM's file transmission feature, select the created text document and send it
6. The other instance of SSCOM will receive the data and confirm the received file content

Below is a screenshot of the test results. You can confirm the success of the test by checking the file size and data content.

![20Mbps Test](../../../zh/logic_analyzer/assets/uart_sscom_20mbps_256kb.png)

