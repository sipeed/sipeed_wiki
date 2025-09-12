---
title: Advanced Applications
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool, PCIe
update:
  - date: 2025-8-26
    version: v0.1
    author: BuGu
    content:
      - Release docs
  - date: 2025-9-11
    version: v0.2
    author: iawak9lkm
    content:
      - Add new feature description
---

## Switching to PiKVM

In addition to running the NanoKVM framework, NanoKVM Pro is also compatible with the PiKVM software framework. You can switch between them as needed.

### Switching to PiKVM

By default, the NanoKVM Pro uses the NanoKVM framework. You can switch to PiKVM in `Settings` -> `About` -> `Switch Device`.

![](./../../../assets/NanoKVM/pro/extended/SwitchtoPiKVM.png)

After clicking, the system will automatically restart and boot into the PiKVM framework. This process takes about 30 seconds. If it does not switch automatically for a long time, please refresh the webpage manually.

![](./../../../assets/NanoKVM/pro/extended/PiKVMLogin.png)

The default username and password for the PiKVM framework are also `admin`, `admin`. However, the two platforms use their own usernames and passwords, which are not unified. It is strongly recommended to change them after logging in.

![](./../../../assets/NanoKVM/pro/extended/PiKVM-Setting.png)

> Some functions in the PiKVM framework require the use of a web terminal, such as Wi-Fi configuration and Tailscale setup.  
> When updating NanoKVM, the PiKVM framework will be updated simultaneously.

### Switching to NanoKVM

Switching back from the PiKVM system to NanoKVM is equally simple. Just go to `Options` -> `Switch to NanoKVM` and click `Switch Now`.

![](./../../../assets/NanoKVM/pro/extended/SwitchtoNanoKVM.png)

After clicking, the system will automatically restart and boot into the NanoKVM framework. This process takes about 30 seconds. If it does not switch automatically for a long time, please refresh the webpage manually.

## SSH & mDNS

### SSH

By default, NanoKVM-Pro disables SSH to ensure system security. If you need to enable the SSH service or use it when previewing new versions, you can turn it on as follows:

* **ATX/Desk**: From the web interface, go to `Settings` → `Device` → enable `SSH`
* **Desk**: From the screen, tap `Settings` → `SSH` to enable `SSH`

The default account is `root` with the password `sipeed`. If you change the web account password in the NanoKVM interface, the SSH password will be updated accordingly.

### mDNS

To enable or disable mDNS, use the following methods:

* **ATX/Desk**: From the web interface, go to `Settings` → `Device` → enable/disable `mDNS`
* **Desk**: From the screen, tap `Settings` → `mDNS` to enable/disable `mDNS`

## HDMI Input & Loop Out

> Currently, configuration is only supported on the Desk version’s screen.
> Support for ATX/Desk web interface will be added soon.

If HDMI functionality is not required, you can disable it to reduce power consumption. Operation:

On Desk: From the screen, tap `Settings` → `HDMI` to enter the HDMI configuration page, which has two options:

* **INPUT**: When disabled, Desk stops capturing HDMI input signals.
* **LOOP OUT**: When disabled, Desk stops outputting HDMI loop-out signals.

## Display Adjustment

### ATX

Currently, the OLED screen supports the following function:

* Short press the `USR` button to toggle the OLED display on or off.

### Desk

The LCD screen supports the following functions (all configured from the screen):

* Adjust backlight brightness: `Settings` → `Brightness`
* Standby clock: `Settings` → `Auto Clock`

  * When disabled, the LCD remains always on.
  * When enabled, the LCD switches to a clock display after a long period of inactivity.

## Factory Reset

### Quick Reset

* **ATX**: Long press the `USR` button until the screen shows `Reset`, then release.

  > Requires version ≥ `1.0.13`
* **Desk**: From the screen, tap `Settings` → `Help` to enter the Help page. Repeatedly tap the reset button until `0` appears, and the device enters recovery mode.

> **Note**: Do not perform any other operations until the device has fully restarted and refreshed the screen.

### Deep Reset

For details, see the [FAQ](https://wiki.sipeed.com/hardware/en/kvm/NanoKVM_Pro/faq.html#Image-Burning-Methods) section on `Image Burning Methods`.

## USB Expansion Features

### USB NCM

The NCM function allows the NanoKVM to simulate a USB network card, enabling users to log in directly via USB. To enable:

* **ATX/Desk**: From the web interface, go to `Settings` → `Device` → enable `Virtual Network`
* **Desk**: From the screen, tap `Settings` → `USB` → enable `NCM`

### USB Secondary Display

> **Supported only on NanoKVM-Desk**
> Currently, the USB secondary display function is supported only on Windows systems.

1. Download and extract the USB secondary display driver.

2. On Desk: From the screen, tap `Settings` → `USB` to enter the USB configuration page, then enable `Panel`.

3. On the controlled PC:

   * Open `Device Manager` → `Other devices`

   * Find `NanoKVMPro` → right-click `Properties` → `Driver` → `Update driver`

   * Choose `Browse my computer for drivers` → `Let me pick from a list of available drivers on my computer`

   * Double-click `Show all devices`

   * Under `Standard USB Host Controller` / `Standard system devices`, locate `USB Composite Device` → double-click to install

   > **Note**: Driver locations may vary depending on Windows version. Please search carefully.

4. After installation, a new `loop input to output` device will appear under `Other devices` in Device Manager.

5. Right-click this device → `Update driver` → `Browse my computer for drivers` → `Browse` → select the USB secondary display driver folder → `Next` → follow the prompts to complete installation.

6. Once installed, a new NanoKVM graphics device will appear under `Display adapters`.

7. On Desk, enter the secondary display page from the screen, select USB, and the Desk will function as a USB secondary display.

8. To disable, refer to step 2 to turn off `Panel`.

9. When re-enabling, some systems may require reinstalling the USB driver.

## Updates

NanoKVM Pro will periodically push new application versions that include new features and bug fixes. You can update the application version in `Settings` -> `Check for Updates`.

![](./../../../assets/NanoKVM/pro/extended/Update.png)

After clicking download, the new application installation package will be automatically downloaded, which includes `kvmcomm_x.x.x_arm64.deb`, `nanokvmpro_x.x.x_arm64.deb`, and `pikvm_x.x.x_arm64.deb`:

* `kvmcomm_x.x.x_arm64.deb` is responsible for driving the shared hardware in the NanoKVM and PiKVM frameworks;
* `nanokvmpro_x.x.x_arm64.deb` is the NanoKVM application software;
* `pikvm_x.x.x_arm64.deb` is the PiKVM application software.

Enabling the preview update feature will allow you to access the latest experimental application, which usually includes updated features but may lack stability. It is recommended to enable SSH before downloading preview updates.

You can also download specific versions and install them manually.

```shell
# Example of downloading version 1.0.10
# Download files
curl -L -o nanokvm_pro_1.0.10.tar.gz https://cdn.sipeed.com/nanokvm/pro/kvmcomm_1.0.10_arm64.deb
curl -L -o nanokvm_pro_1.0.10.tar.gz https://cdn.sipeed.com/nanokvm/pro/nanokvmpro_1.0.10_arm64.deb
curl -L -o nanokvm_pro_1.0.10.tar.gz https://cdn.sipeed.com/nanokvm/pro/pikvm_1.0.10_arm64.deb

sudo apt install ./*1.0.10*
```

## How to Use Serial Ports

NanoKVM Pro provides two available serial ports, UART1/UART2 (the ATX version does not expose them due to bracket specifications, retaining only internal pads).

* Connect to other serial terminal devices:

```shell
# Use UART1 at 115200 baud rate on the web terminal, exit with Ctrl+A+Q
picocom -b 115200 /dev/ttyS1
# Use UART2 at 115200 baud rate on the web terminal, exit with Ctrl+A+Q
# picocom -b 115200 /dev/ttyS2
```

* Send serial commands only:

```shell
# Set ttyS1 to 115200 baud rate
stty -F /dev/ttyS1 115200

# Send hexadecimal data 0x11, 0x22, 0x33
echo -n -e '\x11\x22\x33' > /dev/ttyS1
```

## How to Modify EDID

EDID (Extended Display Identification Data) is a set of data provided by a display device to the host, including device information, resolution and frame rate lists, color characteristics, audio capabilities, etc. The host adjusts the display settings based on the received EDID.

NanoKVM Pro supports modifying the EDID exposed by the virtual display. You can clone the EDID from a monitor or write your own EDID to achieve specific screen ratios, refresh rates, or color characteristics.

> Modifying the EDID may risk improper display functionality. Please proceed with caution. If issues arise, restore the default EDID.

Writing method:

```shell
# 1. Prepare the EDID file, typically 256 bytes, and scp it to the system
ls -l /root/customize.bin
# -rw-r--r-- 1 1000 1000 256 Aug 19 14:44 /root/customize.bin
# 2. Write the EDID
cat /root/customize.bin > /proc/lt6911_info/edid
# 3. Restore the default EDID:
cat /kvmcomm/edid/e18.bin > /proc/lt6911_info/edid
```
