---
title: F&Q
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
---

## Exception Fixes

**The following solutions are based on the latest application version. If you encounter issues, please update the application first. If you cannot update via the web interface, please follow the steps below for a forced update:**

1. Refer to [this link](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/updating.html#%E8%8E%B7%E5%8F%96-IP) to connect the development board.
2. Execute: `python /etc/kvm/update-nanokvm.py`
   > Users outside of China may experience download failures due to DNS issues. Please add `nameserver 119.29.29.29` or `nameserver 223.5.5.5` to `/etc/resolv.conf` and try again.
   > Earlier versions of the application may not have this script file. Please download [here](https://github.com/user-attachments/files/16939944/update-nanokvm.py.zip), extract it, and grant execute permissions before trying again.

### About Password

   1. After updating to version 2.1.5, if you haven't set a web password before, you will be prompted to change the password upon logging in. When you change the password, the backend `root` password will also be synchronized to the web password. If you have already changed the web password before, the backend `root` password will not be changed automatically. You can modify it using `passwd` in the terminal or click "Reset Password" in the web settings.
   2. If the application version is greater than 2.1.5 and you forget the password, you can press the `BOOT` button on the device for more than 10 seconds (the BOOT button for the NanoKVM-Cube is located next to the USB-HID interface, while the PCIe version can be found on the panel. Older versions of the NanoKVM Full may not have a hole in the corresponding location and require disassembly).
   3. If holding down the button does not reset the password, it may be because the application version is less than 2.1.5. Please refer to [here](https://wiki.sipeed.com/hardware/en/kvm/NanoKVM/system/flashing.html) to reflash the image. Note that reflashing the image will erase all configuration information.

### HID Keyboard and Mouse Not Working
1. Use the "Reset HID" feature in the web interface.
2. Some host systems have high requirements for USB keyboards and mice, needing to use "HID Only" mode. In this mode, USB only simulates keyboard and mouse devices. Please switch to this mode using the mouse icon in the web interface.
3. Some motherboard systems require HID keyboard and mouse devices to have a BIOS identifier. NanoKVM can create a BIOS in `/boot` to enable this feature. Execute `touch /boot/BIOS && restart`.
4. Check if the USB connection is stable. You can see if the HID icon on the OLED is lit, or use `cat /sys/class/udc/4340000.usb/state` in the web terminal. If it shows "not connected," then the USB cable may be faulty. Please replace the USB cable and try again.

### BIOS Does Not Recognize HID Keyboard and Mouse
1. Some host systems have high requirements for USB keyboards and mice, needing to use "HID Only" mode. In this mode, USB only simulates keyboard and mouse devices that support BIOS. Please switch to this mode using the mouse icon in the web interface.
2. Use the "Reset HID" feature in the web interface.

### Incorrect Key Mapping for Non-English Keyboards
+ The keyboard layout needs to be modified in the controlled host system settings. For example, to modify a French keyboard in Ubuntu:
  Settings -> Keyboard -> Input Sources -> ‘+’ -> Add -> Search "French," then add.

### STA LED Not Flashing Normally

The STA LED indicates the operating status of the NanoKVM. When functioning properly, the STA LED should flash irregularly. If the STA LED is continuously on or off, or exhibits regular intermittent extinguishing, the NanoKVM may be malfunctioning.

1. If the STA LED intermittently extinguishes after powering on: The system did not detect the system on the TF card. Please check if the TF card is properly inserted and reflash the TF image.
2. If the STA LED is off for an extended period: This is usually due to a lack of power. Please check the power supply status.

   > If powered only by USB-HID, the USB power may disconnect when the computer is shut down. Please refer to relevant documentation to set USB to always supply power in the BIOS, or use auxiliary power.
   > Connecting to an unconventional power supply may damage the NanoKVM and cause the STA LED to extinguish.

3. If the STA LED remains on for an extended period without flashing: This situation generally should not occur with the official system and applications. If custom functions are configured within the NanoKVM system, there is a chance it may cause the system to freeze, leaving the STA LED lit. It is recommended to reflash the image.

### Unable to Obtain IP Address

1. Lite users should first check if a TF card is inserted. The Lite version is shipped without a card by default, so users need to provide their own TF card. Please follow the instructions [here](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/flashing.html) to flash the card and retry.
2. Check if the network switch supports 100M. Some newer switches do not support 100M connections; please replace the switch and try again.
3. The NanoKVM Cube (including NanoKVM Full and NanoKVM Lite) may be unable to obtain an IP address when connecting to certain power sources/HDMI. Please confirm the following:
   > Disconnect all interfaces and power the device using a power bank, then connect the network cable to see if an IP can be obtained.
   > If an IP can be obtained, reconnect HDMI/computer USB to check if the IP exists.
   > If the IP exists only when powered by the power bank, but disappears after connecting HDMI/computer USB, this indicates the issue. Please contact customer service to purchase an isolator to resolve it.

### No Display After Logging into the Browser Interface
1. The controlled host may be in sleep mode. Try pressing any key on the keyboard to wake it up.
2. Non-Chrome browsers may experience issues with H264 not displaying, while MJPEG mode works normally. Please try again using Chrome.
3. For the PCIe version, try clicking the reset HDMI option under the "Video" icon.
4. For the Cube version, you can try unplugging and replugging the HDMI cable after opening the webpage.
5. Check the resolution on the OLED or enter `echo "$(cat /kvmapp/kvm/width) * $(cat /kvmapp/kvm/height)"` in the web terminal, and compare it with the resolution of the controlled host. If they differ, you can manually set the resolution using `echo xxx > /kvmapp/kvm/width && echo xxx > /kvmapp/kvm/height`.
   > If the host system is Windows, the resolution shown in display settings may not match the actual resolution. Check in Advanced -> Active Signal Resolution.
6. The early test version of Full NanoKVM uses standard cables to connect to the HDMI capture board, which may not detect the HDMI signal due to poor connections. You can reconnect the cable as shown in the image below or contact customer service to purchase dedicated cables.
   [](./../../../assets/NanoKVM/guide/Old_fix.png)
7. Try restarting to resolve the issue: execute `reboot` in the web terminal.
8. If the above methods do not identify the problem, execute `cat /proc/cvitek/vi_dbg` in the web terminal.
   > If `VIDevFPS` is 0, it means NanoKVM cannot get HDMI input. Check the following issues: Is the host outputting a video signal? Is the HDMI cable damaged? Is the Cube an early version with possible connection issues?
   > If `VIDevFPS` is not 0 and `VIFPS` is 0, it indicates that NanoKVM is not correctly configured for HDMI parameters. The Cube can replug the HDMI to auto-detect, while PCIe can click `Reset HDMI` under `Video` to auto-detect.
   > Check if `VIInImgWidth` and `VIInImgHeight` match the actual HDMI resolution. If they are different, it means NanoKVM did not auto-detect the correct HDMI parameters. Manually configure the resolution parameters as described in point 4.

### Serious screen delay in internal network environment

1. Try replacing the switch or power supply
2. If it is invalid, please contact after-sales service

### OLED Displaying Information Normally, But Unable to Open Webpage

1. Please force update the application.

### OLED Not Lighting Up

The NanoKVM Full and PCIe versions come with an OLED to display information such as IP. If the OLED does not light up, please follow these steps to troubleshoot:

1. Version `2.1.4` added an OLED sleep function; pressing the BOOT button can temporarily turn on the OLED.
2. If the STA LED is flashing abnormally, first check whether the system is booting normally, and follow the steps outlined in “STA LED Not Flashing Normally” to troubleshoot.
3. Try a forced update or reflash the system.

### About Memory

1. The total memory (RAM) space of NanoKVM is 256MB, with a dedicated ion memory area used for video image processing. The memory viewed in user space will be less than 256MB.
2. Firmware versions lower than 1.3.0 reserve only 128MB of memory for user space. All images from version 1.3.0 and later increase the memory size to 158MB, which is beneficial for Tailscale to run for long periods. Users in need should update the image according to the steps [here].
3. Enable "Memory Optimization" in the settings.

### Host Abnormal Restart
+ In the early beta version, when the Full NanoKVM ATX board is connected to the host's RESET pin, the host may restart when the NanoKVM is rebooted. Please disconnect the RESET jumper or contact customer service to purchase stable version accessories.

### Current Backflow
+ The early beta version of the Full NanoKVM has a current backflow issue: When the host is powered off and the USB has no power output, current will flow back into the host when connecting the auxiliary power supply.
  1. It is recommended to set the USB to remain powered after the host is shut down.
  2. For Full version users: Use a soldering iron to disconnect the 5V resistor or header short-circuit at the indicated position in the image below, supplying power only through the auxiliary power port.
      ![](./../../../assets/NanoKVM/guide/fix2.png)
      
### Try Power Cycling to Solve Unknown Issues

### If there are network disconnections or other abnormal situations during the update, it may lead to a failed update. Please refer to the following solutions:  

1. Refer to [here](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/updating.html#%E8%8E%B7%E5%8F%96-IP) to connect the development board.  
2. Execute `rm -r /kvmapp && cp -r /root/old/ / && mv /old/kvmapp && reboot` to restore the previous version.  
3. Manually force the update using the method outlined above.  
4. Reflash the system.

### If the Above Methods Do Not Resolve the Issue, Please Describe Your Model and Problems Encountered in the Forum, GitHub, or QQ Group. We Will Respond Patiently.
+ When providing feedback, please specify the version of your NanoKVM, the environment in which you are using it (motherboard model, system name, etc.), and the system configuration (e.g., image version 1.4.0; application version 2.2.5; H264; 1080P; high quality; frame rate 30). This information will help us reproduce and resolve the issue.
+ If there is a problem with no image display, please execute the following commands during the anomaly and paste the output logs into the issue:
  ```shell
  cat /etc/kvm/hw
  cat /etc/kvm/hdmi_version
  cat /etc/kvm/hdmi_mode
  ```
+ Some issues require collecting runtime application logs. Please follow these steps:
  ```shell
  # Enable SSH functionality in the web interface (Settings -> Devices -> SSH)
  # Log in to SSH using the password set in the web interface. If no password is set, the default password is root.
  ssh root@xxx.xxx.xxx.xxx
  # Change the log level: /etc/kvm/server.yaml -> logger -> level: info to debug
  vi /etc/kvm/server.yaml
  # Use ‘i’ to edit; use ‘Esc’ + :wq to exit
  # Restart the KVM service
  /etc/init.d/S95nanokvm restart
  # Copy the log
  ```

## Feedback Methods

* MaixHub Forum: [https://maixhub.com/discussion/nanokvm](https://maixhub.com/discussion/nanokvm)
* GitHub: [https://github.com/sipeed/NanoKVM](https://github.com/sipeed/NanoKVM)
* QQ Group: 703230713