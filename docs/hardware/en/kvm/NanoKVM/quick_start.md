---
title: Quick Start
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-7-4
    version: v0.1
    author: BuGu
    content:
      - Release docs
update:
  - date: 2024-8-15
    version: v0.1
    author: BuGu
    content:
      - Update docs
---

## Unboxing

![](./../../../assets/NanoKVM/unbox/full_ubox.png)

The Full version includes NanoKVM (with case, with card), KVM-B board, 2 USB A to C cables, and Dupont cables.

![](./../../../assets/NanoKVM/unbox/lite_ubox.png)

The Lite version includes NanoKVM (without case and TF card) and a heatsink.

## Interface Introduction

![](./../../../assets/NanoKVM/unbox/Interface.png)

+ **The Full version features three USB Type-C interfaces with the following names and functions**

  + HID Interface (also called PC-USB), located below the HDMI interface, is used to connect the host, simulate keyboard and mouse, USB drive, and RNDIS devices.
  + AUX Interface, located above the HDMI interface, provides auxiliary power supply.
  + KVM-B Interface (also called ATX-Power), located above the Ethernet port, connects to KVM-B for power control functions.

## Power Supply

+ NanoKVM supports 5V power supply via regular USB, with a power consumption of about 1W. Some older motherboard models may have insufficient current, requiring additional power supply through the AUX interface.

![](./../../../assets/NanoKVM/unbox/U-I-W.jpg)

+ Some motherboards' BIOS settings may default to turning off USB power when shut down. To ensure NanoKVM remains powered, please provide an additional 5V power supply through the AUX interface.

+ NanoKVM's USB CC interface features a 5.1K pull-down resistor, allowing the use of standard PD chargers. Some low-quality power supplies may output 12V directly without negotiation, which can damage NanoKVM.

Note: The first batch of internal test versions of the AUX interface does not include a CC pull-down resistor and cannot use C-C PD chargers. Please use a conventional 5V USB power adapter.

## Wiring

The wiring diagram for the NanoKVM-Full version is as follows. The Lite version only includes USB-C, HDMI, and Ethernet ports, and can refer to the Full version for wiring.

+ Use a USB C to A data cable to connect the remote host to the PC USB interface of NanoKVM (located below the HDMI interface).

+ Connect an HDMI (standard size) cable between the remote host and the HDMI interface of NanoKVM.

  ![](./../../../assets/NanoKVM/unbox/hdmi.png)

+ Connect NanoKVM to a router/switch using an Ethernet cable.

+ Use another USB C to A data cable to connect the KVM-B board to the ATX interface of NanoKVM (located above the Ethernet port).

  The official KVM-B board features a standard 9-pin header interface compatible with most motherboards, allowing direct connection. The case's power button and Power LED can be connected to the KVM-B header, as shown in the diagram (only the power button is connected here):

  ![](./../../../assets/NanoKVM/unbox/new-ATX-B.png)

  The wiring diagram for the internal test version of the KVM-B board and the host's 9-pin interface is shown below. The double-row headers are interconnected, allowing the connection of the case's power button and Power LED to the other row.

  ![](./../../../assets/NanoKVM/unbox/old-ATX-B.png)
  ![](./../../../assets/NanoKVM/unbox/old-ATX-B-w.png)

## Updates

### Update Image

> **The Lite version requires preparing a TF card and flashing the image before use!**

The Full version comes with a pre-flashed image and can skip this step.

Images are updated periodically. It is recommended to update to the latest version for the best experience.

For detailed instructions, please refer to [Flashing Image](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/flashing.html).

### Update Application

New applications often bring more features or fix important bugs. It is recommended to update NanoKVM applications to the latest version. For detailed instructions, please refer to [Updating Application](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/updating.html).

## Basic Operations

### How to Obtain an IP Address

The Full version of NanoKVM has an OLED display that shows the IP address on the first line when connected to the network.

![](./../../../assets/NanoKVM/unbox/oled.jpg)

Lite version users, please refer to [Obtaining IP](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/updating.html#%E8%8E%B7%E5%8F%96-IP).

### Viewing Remote Desktop

Open a browser and enter the obtained IP address to access the login page. The default username and password are admin/admin. After logging in, it is recommended to **check for updates** (Settings -> Check for Updates). Detailed steps can be found in [Updating Application](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/updating.html).

For Lite version users, or Full version users who re-flashed the card and see no remote screen on the login page, please upgrade the application and refresh the webpage to start using.

![](./../../../assets/NanoKVM/unbox/frist_update.png)

### Changing Account Password

**For security, please change the account password after confirming the functions are working properly.**

![](./../../../assets/NanoKVM/unbox/unbox_9.png)

### ATX Power Control

The Full version package includes NanoKVM-A/B boards for controlling and viewing the host's power status.

+ The 5V LED (blue) on the top board indicates the power status of NanoKVM.
+ The PWR LED (green) indicates the power status of the host.
+ The POWER button functions as the host's power button, controlling the power on/off.
+ The RESET button acts as the host's reset button, forcing a restart when pressed while powered on.
+ Power status can also be viewed and controlled via the web interface. Refer to the [User Guide](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/user_guide.html) for details.
