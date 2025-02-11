---
title: Update debugger 
keywords: Sipeed, Gowin, Tang, FPGA, Nano, Primer, Mega
update:
  - date: 2025-02-10
    version: v0.8
    author: Serika
    content:
      - First release
---
## Overview

All Sipeed Tang series have onboard debugger (except standalone SOM). The debuggers are separate MCUs with their own firmware. Users could update the firmware for these debuggers to get feature updates and bug fixes.

We need to use the [**BouffaloLabDevCube**](https://dev.bouffalolab.com/download/) to program these onboard debugger chips,  and documentation about the ***chips & tools*** can be found [here](https://dev.bouffalolab.com/document/).

- Download and install the corresponding edition of the ***tools*** according to your OS.
- Get the updated debugger firmware for your board from [**Sipeed Download Station**](https://dl.sipeed.com/shareURL/TANG/Debugger/onboard).
- Refer to the official documentation of [**BouffaloLabDevCube**](https://dev.bouffalolab.com/download/) to update the firmware of the onboard debugger.
- For Windows users, there are detailed step-by-step tutorial below. Also, the steps for other operating systems are similar.

***

## Tutorial
  ### Preparation for Hardware

  To put the onboard debugger into **DFU mode**, press the ***Update Button*** or short the corresponding ***Test Points*** before power on the board or connecting the board's debug USB port with a cable. 
  
  Please refer to the below for the corresponding ***Update Button*** and ***Test Points***.

  #### Tang nano series
  
  - Tang nano 1k

    The 2 **`Test Points`** is in the upper left corner of the board **TOP** side, behind the `KEY-B`.

  ![nano1k_update](./assets/hardware/nano1k_update.png)
  
  - Tang nano 4k

    The 2 **`Test Points`** is in the upper left corner of the board **TOP** side, behind the USB-C connector.
  
  ![nano4k_update](./assets/hardware/nano4k_update.png)
  
  - Tang nano 9k

    The 2 **`Test Points`** is in the middle left of the board **TOP** side, behind the USB-C connector.
  
  ![nano9k_update](./assets/hardware/nano9k_update.png)
  
  - Tang nano 20k
    
    The **`Update Button`** behind the HDMI connector on the **TOP** side has the silkscreen **`UPDATE`**.
  
  ![nano20k_update](./assets/hardware/nano20k_update.png)

  #### Tang Primer series
  
  - Tang Primer 25k Dock

    The 2 **`Test Points`** is in the upper left corner of the board **BOT** side, marked as `3V3` & `TDO`.
  
  ![Primer25k_update](./assets/hardware/Primer25k_update.png)
  
  - Tang Primer 20k Dock

    The white **`Update Button`** is on the lower right side of the TOP side of the Dock board between USB-C debug port and HDMI port, marked as **`702-BOOT`**
  
  ![Primer20k_update](./assets/hardware/Primer20k_update.png)
  
  - ~~Tang Primer 15k Dock~~ (**Not yet released**)
  
    TBD

  #### Tang Mega series(include Tang Console)
  
  - Tang Mega Neo Dock(inclede Tang Mega 138K Dock)

    The **`Update Button`** is blow the USB-C connector marked as **DEBUG-USB2** on the **TOP** side.

  ![Mega-neo_update](./assets/hardware/Mega-neo_update.png)

  - Tang Mega 138K Pro Dock

    The **`Update Button`** is on the left of the USB-C connector marked as **JATG|UART** on the **TOP** side.

  ![Mega-138kpro_update](./assets/hardware/Mega-138kpro_update.png)
  
  - Tang Console
  
    The **`Update Button`** is on the other side the USB-C connector on the **TOP** side, the shorter of the 2 buttons marked ad **`BOOT`**.

  ![Mega-console_update](./assets/hardware/Mega-console_update.png)

  ***

  ### Preparation for Software

  - First, download **BouffaloLabDevCube** from [**BouffaloLab Official Website**](https://dev.bouffalolab.com/download/), The latest version is **`1.9.0`** (February 10, 2025).
 
  ![download_BLDevCube](./assets/download_bldc.png)
  
  - Unzip the downloaded content and execute the corresponding executable file, for Windows this is **`BLDevCube.exe`**
  
  ![run_BLDevCube](./assets/run_bldc.png)


  - In the pop-up window, select Chip model as BL616/618.
  
  ![model-sel_BLDevCube](./assets/model-sel_bldc.png)

  - In the new window, check the **`Enable`** checkbox in blow the ***Single download option***. Click the **`Browse`** button to select the firmware file to be updated.
    
  ![mainwindow_BLDevCube](./assets/mainw_bldc.png)

  - Let the onboard debugger into **DFU mode**, it should be a CDC-ACM device for both BL702 or BL616. On Windows, this registers a new COM port, in this example is **`COM12`**. For Linux users, CDC-ACM usual register as `/dev/ttyACMx`. For macOS users, it may register as `/dev/tty.usbmodemxxxx` or `/dev/cu.usbmodemxxxx`. (Each `x` represents a digit)
  
  ![new_com-port](./assets/new_com-port.png)

  - Now, set the **BLDevCube** up as shown below. Set the firmware file location, the port for DFU mode, then click **`Open UART`**, and finally click **`Create & Download`**.

  ![setting_BLDevCube](./assets/set_bldc.png)

  - Wait for the download to complete as shown in the image below.

  ![download_complete](./assets/complete_bldc.png)

  ***

  ### Confirm the results

  After completing the above steps, we need to confirm that the firmware of the onboard debugger is successfully burned. Usually replug the USB cable or re-poweron the board will confirm it.

  - In Windows, you can see two new devices in the device manager: **`USB Converter A`** and **`USB Converter B`**.

  ![dual_usbconverter](./assets/ftdi_dual.png)

  - To confirm the debugger firmware version, double-click any **`USB Converter`** and go to the Details tab. Then select **`Parent`** Options from the drop-down menu:

  ![detail_usbconverter](./assets/detail_usbconverter.png)

  - As shown in the figure below, the last 10 digits **`2025102315`** are the serial number of the debugger firmware version. Linux & macOS users could use command **`dmesg`** to check the serial number in kernel log.

  ![serialnum_usbconverter](./assets/serialnum_usbconverter.png)

  ### Latest firmware

  The latest firmware serial numbers of all Tang series onboard debuggers are recorded here:


  | Board         | MCU model  | Download                                                                                                     |Serial num.|  Firmware SHA256 Checksum                                                                                                                     |
  | ------------- | ---------- | -------------------------------------------------------------------------------------------------------------| --------- |-----------------------------------------------------------------------------------------------------------------------------------------------|
  | nano 1K       | BL702      | N/A                                                                                                          | N/A       |N/A                                                                                                                                            |
  | nano 4K       | BL702      | N/A                                                                                                          | N/A       |N/A                                                                                                                                            |
  | Nano 9K       | BL702      | N/A                                                                                                          | N/A       |N/A                                                                                                                                            |
  | Primer 20K    | BL702      | N/A                                                                                                          | N/A       |N/A                                                                                                                                            |
  |               |            |                                                                                                              |           |                                                                                                                                               |
  | nano 20K      | BL616      | [Click](https://api.dl.sipeed.com/TANG/Debugger/onboard/BL616/202501231x/bl616_fpga_partner_20kNano.bin)     |2025012315 |[bl616_fpga_partner_20kNano.sha256](https://api.dl.sipeed.com/TANG/Debugger/onboard/BL616/202501231x/bl616_fpga_partner_20kNano.sha256)        |
  | Primer 25K    | BL616      | [Click](https://api.dl.sipeed.com/TANG/Debugger/onboard/BL616/202501231x/bl616_fpga_partner_25kDock.bin)     |2025012315 |[bl616_fpga_partner_25kDock.sha256](https://api.dl.sipeed.com/TANG/Debugger/onboard/BL616/202501231x/bl616_fpga_partner_25kDock.sha256)        |
  | Mega NEO      | BL616      | [Click](https://api.dl.sipeed.com/TANG/Debugger/onboard/BL616/202501231x/bl616_fpga_partner_NeoDock.bin)     |2025012315 |[bl616_fpga_partner_NeoDock.sha256](https://api.dl.sipeed.com/TANG/Debugger/onboard/BL616/202501231x/bl616_fpga_partner_NeoDock.sha256)        |
  | Mega 138K Pro | BL616      | [Click](https://api.dl.sipeed.com/TANG/Debugger/onboard/BL616/202501231x/bl616_fpga_partner_138kproDock.bin) |2025012315 |[bl616_fpga_partner_138kproDock.sha256](https://api.dl.sipeed.com/TANG/Debugger/onboard/BL616/202501231x/bl616_fpga_partner_138kproDock.sha256)|
  | Console       | BL616      | [Click](https://api.dl.sipeed.com/TANG/Debugger/onboard/BL616/202501231x/bl616_fpga_partner_Console.bin)     |2025012319 |[bl616_fpga_partner_Console.sha256](https://api.dl.sipeed.com/TANG/Debugger/onboard/BL616/202501231x/bl616_fpga_partner_Console.sha256)        |

  











  ### Troubleshooting
  If you encounter any problems during use, or have any comments or suggestions on the document, please feel free to give us your feedback. Contact details are below.
  
  In most cases, BouffaloLab's official documentation is sufficient for troubleshooting. Click [here](https://dev.bouffalolab.com/document/) to get them.

  #### FAQ
  - TBD, waiting for feedback to be collected before adding.

  #### Communication Methods
  - **Reddit** : [reddit.com/r/GowinFPGA/](reddit.com/r/GowinFPGA/)
  - **Telegram** : [t.me/sipeed](t.me/sipeed)
  - Discussion forum: [maixhub.com/discussion](https://maixhub.com/discussion)
  - QQ discussion group: [834585530](https://jq.qq.com/?_wv=1027&k=wBb8XUan)
  - Leave a message directly below this page
  - Business email : [support@sipeed.com](support@sipeed.com)










