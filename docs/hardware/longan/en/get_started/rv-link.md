Using RV-LINK
=========

## What is RV-LINK

**RV-LINK** is a simulation-based firmware development board RISC-V, by programming **RV-LINK** firmware can be **Sipeed Longan Nano** development board into a jtagdebugger for debugging another piece Longan or other development support jtag debugging board. RV-LINK project address: [https://gitee.com/zoomdy/RV-LINK](https://gitee.com/zoomdy/RV-LINK)

## Burn RV-LINK firmware

### Using the PlatformIO project to burn a key
* Download RV-LINK source code

    Project source code download address: [http://dl.sipeed.com/LONGAN/Nano/Tools/RV-LINK-pio-src-v0.1.zip](http://dl.sipeed.com/LONGAN/Nano/Tools/RV-LINK-pio-src-v0.1.zip)

    It can also be downloaded from the official RV-LINK project: [https://gitee.com/zoomdy/RV-LINK](https://gitee.com/zoomdy/RV-LINK)

* Open the project directory with VSCODE

    Extract the source code downloaded above into a separate folder and open the source folder using VSCODE

    As shown below:
    ![](../../assets/pio_open_rvlink.png)

    The firmware is usually burned using the DFU method, and the configuration file **does not need to be** modified.

    If you need to change the programming mode, you can modify `platformio.ini` to modify the file, please refer to the specific configuration:[modify the project configuration file](blink.md/#project-configuration-file)

* Burn firmware with PIO

    After connecting the development board, after the development board enters the burning mode, click the arrow symbol in the lower left corner to burn.

    After the programming is successful, you can see the green light flashing on the development board. After connecting the development board to the USB port of the computer, you can see that there is one more serial device in the device manager. At this point the Longan board successfully became the RV-LINK debugger.

### Other burning methods

Reference Document:  [Turning the Longan Nano Development Board into a RISC-V Emulator](https://gitee.com/zoomdy/RV-LINK/wikis/%E5%B0%86%20Longan%20Nano%20%E5%BC%80%E5%8F%91%E6%9D%BF%E5%8F%98%E6%88%90%20RISC-V%20%E4%BB%BF%E7%9C%9F%E5%99%A8)

## Debugging with RV-LINK

### Connecting the development board

Connect the development board that brushes the RV-LINK firmware to the jtag of the development board to be debugged.

| RV-LINK | To be debugged development board |
| :----: | :----: |
|  JTDO  |  JTDO  |
|  JTDI  |  JTDI  |
|  JTCK  |  JTCK  |
|  JTMS  |  JTMS  |
|  3V3   |  3V3   |
|  GND   |  GND   |

### Using RV-LINK in the PlatformIO IDE

RV-LINK in the PlatformIO IDE can support one-button boot debugging just like any other debugger.

Only in the project `platformio.ini` configuration file, specify the debug options and debug port option.

Sample code

```ini
[env:sipeed-longan-nano]
platform = gd32v
framework = gd32vf103-sdk
board = sipeed-longan-nano
monitor_speed = 115200
upload_protocol = rv-link ; rv-link download option
debug_tool = rv-link ; rv-link debug option
debug_port = COM2    ;  Required with rv-link Required debugger serial port
```

### Using RV-LINK on other platforms

Reference [RV-LINK WIKI](https://gitee.com/zoomdy/RV-LINK/wikis/)
