---
title: Solutions
tags: Tang
keywords: Programmer
desc: 
update:
  - date: 2023-05-18
    version: v0.3
    author: wonder
    content:
      - Add some informations
---


  <!-- - date: 2022-10-19
    version: v0.1
    author: wonder
    content:
      - Rewrite some solutions
  - date: 2023-02-23
    version: v0.2
    author: wonder
    content:
      - Add extra information about programmer -->

Here are some normal questions.

## Programmer 

Make sure there are 2 `converter` and `COM` device, this means the debugger works well.

![tang_bl702_device_convertor](./../../../zh/tang/Tang-Nano-Doc/assets/qusetions/tang_bl702_device_convertor.png)

The debugger can be used for Jtag and UART, when using its uart function, Jtag is disabled. To solve this, replug the TypeC cable of your board to disconnect the uart connection.

### No `COM` devices

If there is no `COM` device but 2 `converter` devices, right click `converter B` -> `Properties` -> `Advanced` -> `Load VCP` , then Click `OK` and reconnect your USB device.

![tang_bl702_device_convertor_load_vcp](./../../../zh/tang/Tang-Nano-Doc/assets/qusetions/tang_bl702_device_convertor_load_vcp.png)

### No `convertor` device

It takes 10 seconds for debugger loading the driver. And you can install the driver manually. [Click me to download driver](https://dl.sipeed.com/shareURL/TANG/programmer)

![no_convertor_install_driver](./../../../zh/tang/Tang-Nano-Doc/assets/qusetions/no_convertor_install_driver.png)

### Download frequency

Make sure the frquency is equal or lower than `2.5MHz`, otherwise it may lead some troubles like burnning bitstream file really slow or failed burnning bitstream file.

<img src="./../../../zh/tang/assets/questions/cable.png">

Choose Frequency equal to or lower than 2.5MHz

<img src="./../../../zh/tang/assets/questions/frequency.png" >

Then cilck Save

### Error found

This error means the Programmer application does detect debugger or your driver is wrong. 
Visit [this programmer](https://dl.sipeed.com/shareURL/TANG/programmer) compressed file, download it and extract it, replace the programmer folder install with GOWIN IDE by this extracted file.
If you don't know how to replace the programmer folder, just excute the programmer application in the extracted folder to download bisdtream file instead of the programmer application installed with GOWIN IDE.

If this problem still occurs after you use our recommended programmer application, try to rerun this application. If all attemps fail, see the begin of this documents about `converter`.

### Cable lost

Reflash bitstream to solve this. This occurs when flashing bitsteram, board and computer does not well disconneted.

### Cabel open failed

![cable_open_failed](./../../../zh/tang/Tang-Nano-Doc/assets/qusetions/cable_open_failed.png)

This means the programmer application does not detect the debugger, try this programmer application mentioned in [Error found](#error-found).

If this problem still occurs after you use our recommended programmer application, try to rerun this application. If all attemps fail, see the begin of this documents about `converter`.

<!-- 
After finishing replacing **programmer** as mentioned previously,Do following steps in programmer application.

Click Edit->Cable Setting->Cable->Query in the top menu bar,then save.

<details>
  <summary><font color="#4F84FF">Click to see steps by pictures</font></summary>
  <img src="./../../../zh/tang/assets/questions/cable.png">
  <p>Click Query in the following picture</p>
  <img src="./../../../zh/tang/assets/questions/click_query.png" >
  <p>Click Save</p>
</details> 
-->

### No Gowin devices found

![no_gowin_device_found](./../../../zh/tang/Tang-Nano-Doc/assets/qusetions/no_gowin_device_found.png)

This means the debugger does not detect the FPGA chip, you can use the latest [GOWIN Programmer](http://www.gowinsemi.com.cn/faq.aspx) to slove this problem.

![gowin_programmer_download](./assets/questions/gowin_programmer_download.png)

#### Nano 9K

Because the FPGA JTAG_SEL pin is routed to Key S2, from the GOWIN mannual we can see when JTAGSEL_N=0 (Active low), Jtag is enabled.

![gw1nr_9c_jtag_sel](./assets/questions/gw1nr_9c_jtag_sel.png)

For Nano 9K, hold S2 key to solve the trouble caused by JTAGSEL_N and JTAG pins are being used as I/O.

#### Primer 20K

For 20K Dock kits, it's necessary to enable the core board before using debugger debug the chip, just put the 1 switch on the dip switch down, otherwise this error occurs.

| Enable Core Board | Disable state | Additional comments |
| --- | --- | --- |
|<img src="./../../../zh/tang/tang-primer-20k/assets/start/switch_1_on.png" alt="switch_1_on" width=100%>|<img src="./../../../zh/tang/tang-primer-20k/assets/start/reset_led_on.png" alt="reset_led_on" width=100%> | When disabled, the LDE0 and LED1 is on, and core board doesn't work.|

When using RV Debugger Plus burnning firmware into 20K core board this error occurs, possibly the order of connectting wire is wrong, make sure your connectting order is same as following sheet, or you can check your core board jtag connector inside pins, make sure none of them are crooked(One time we get problem connecting Debugger with core board and finnaly check out that there is a crooked pin in the jtag connector, this maybe because of doing wrong connection operations when connecting)

The JTAG pin orders can be found in the back of 20K core board.

<table>
    <tr>
        <td>Core Board</td>
        <td>5V0</td>
        <td>TMS</td>
        <td>TDO</td>
        <td>TCK</td>
        <td>TDI</td>
        <td>RX</td>
        <td>TX</td>
        <td>GND</td>
    </tr>
    <tr>
        <td>Debugger</td>
        <td>5V0</td>
        <td>TMS</td>
        <td>TDO</td>
        <td>TCK</td>
        <td>TDI</td>
        <td>TX</td>
        <td>RX</td>
        <td>GND</td>
    </tr>
</table>

![cable_connect](./../../../../../news/others/20k_lite_start/assets/cable_connect.png)

### ID code mismatch

![id_code_mismatch](./../../../zh/tang/Tang-Nano-Doc/assets/qusetions/id_code_mismatch.png)

This means the selected device in the project mismatch your burnning chip. All that refers chip model(The project device, pin constrain, IP modules and programmer device choose) need to be reset.

| Board name | Series | Device | Package | Speed |
| --- | --- | --- | --- | --- |
| Tang Nano | GW1N | GW1N-1 | QN48 | C6/I5 |
| Tang Nano 1K | GW1NZ | GW1NZ-1 | QN48 | C6/I5 |
| Tang Nano 4K | GW1NSR | GW1NSR-4C | QN48P | C6/I5 or C7/I6 |
| Tang Nano 9K | GW1NR | GW1NR-9C | QN88P | C6/I5 |
| Tang Nano 20K | GW2AR | GW2AR-18C | QN88 | C8/I7 |
| Tang Primer 20K | GW2A | GW2A-18C | PBGA256 | C8/I7 |

<!-- For Nano 9K it should be choose as follow: -->
<!-- 
<details>
  <summary><font color="#4F84FF">Click to see the choice of 9K</font></summary>
  <img src="./../../../zh/tang/Tang-Nano-9K/nano_9k/Tang_nano_9k_Device_choose.png">
</details>

For other boards, just make sure your device selection corresponds to the laser mark on chip package. -->

### spi flash selected mismatch

The board using GOWIN Semiconductor LittleBee product family (Series of chip names beginning with GW1N) incorporates embedded FLASH in main chip, so when burning firmware we burn into embedded FLASH, and reagrd the external FLASH as a peripheral. 

The board using GOWIN Semiconductor Arora product family (Series of chip names beginning with GW1N) does not incorporate embedded FLASH, so when burning firmware we burn into external FLASH, and the operations are as followed . 

<table>
  <tr>
    <td rowspan="2"><img src="./../../../zh/tang/tang-primer-20k/examples/assets/led_assets/flash_mode.png" alt="flash_mode"></td>
    <td style="white-space:nowrap">Operation is<br><code>exFlash Erase,Program thru GAO-Bridge</code></td>
  </tr>
  <tr>
    <td>Flash Device we choose <code>Generic Flash</code></td>
  </tr>
</table>

### Download slowly

Don't choose Operation containing Verify

![never_choose_verify](./../../../zh/tang/assets/questions/never_choose_verify.png)

Make sure the frquency is equal or lower than `2.5MHz`, normally `2.5MHz` everything is ok.

<img src="./../../../zh/tang/assets/questions/cable.png">

Choose Frequency equal to or lower than 2.5MHz

<img src="./../../../zh/tang/assets/questions/frequency.png" >

Then cilck Save

### Directory *** has null character.

Error character of the project path.

- Close IDE.
- Check projrct path, only English works and `_` are Ok, take care of the blank character ` ` in the path.
- Reopen the project, clean and rerun your project.

### Can't find bistream file

Normally the bistream file with extension name `.fs` is in the impl/pnr folder under the project path.

<img src="./../../../zh/tang/assets/questions/fs_path.png">

From the picture above we can know the  of this bistream file path is `fpga_project1/impl/pnr/fpga_project1.fs`

The fpga_project1 is the project directory, the impl folder is generated by IDE, and the download is in the pnr folder.

The file  with extension name `.fs` is the firmware we will burn into fpga.

## IDE

### See IP manual

In the IP Core generate interface of IDE, click your target IP, then choose your language reference to see the IP manual.

<details>
  <summary><font color="#4F84FF">Click to see instructions</font></summary>
    <img src="./../../../zh/tang/assets/ip-reference.png">
</details>

### Reconfigure generated IP

In the IP Core generate interface of IDE, click the folder icon next to device selection at the top to open the generated IP configuration interface.

<details>
  <summary><font color="#4F84FF">Click to see instructions</font></summary>
    <img src="./../../../zh/tang/assets/ip-reconfigure.png">
</details>

### Set top module

For project containning muti-projects, if you succeed generating your module, right-click the module you want to set as the top module IDE -> Hierarchy interface.

![set_top_module](./../../../zh/tang/Tang-Nano-Doc/assets/set_top_module.png)

If your Hierarchy interface is the same as what is in the left picture, this means there are logic errors in the code, such as syntax errors or generate errors. Click 'RTL Anakysis Error' in the upper right corner then you can see the error type code and location of the error in the dialog box that pops up, as shown in the right picture in the following table.

<table>
<tr>
<td align="center">RTL Analysis Error</td>
<td align="center">Error type and details</td>
</tr>
<tr>
<td><img src="./../../../zh/tang/Tang-Nano-Doc/assets/top_error.png" alt="top_module_error" ></td>
<td><img src="./../../../zh/tang/Tang-Nano-Doc/assets/error_detail.png" alt="error_detail"  ></td>
</tr>
</table>

### Using GAO

GAO is Gowin Analyzer Oscilloscope, its document can be found in the path like what is shown below

![gao](./assets/gao.png)

Using this [programmer application](https://dl.sipeed.com/shareURL/TANG/programmer) instead of the programmer application installed with, then you can use GAO.(GAO need run by IDE, so you need to replace the Programmer bin folder by your downloaded one)