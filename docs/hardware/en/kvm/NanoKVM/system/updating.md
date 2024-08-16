---
title: Update Application
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-8-13
    version: v0.1
    author: xwj
    content:
      - Release docs
---

## Power On

1. Connect the NanoKVM's wired network port with an Ethernet cable.
2. Use a standard HDMI cable to connect the remote host to the NanoKVM's HDMI port.
3. Use a USB C to A data cable to connect the remote host to the NanoKVM's PC USB port.

Once all cables are connected, the NanoKVM will automatically power on. It takes about one to two minutes to boot up.

## Obtain IP Address

The NanoKVM Full version will display the IP address on the screen after booting, so you can skip this step. The NanoKVM Lite version can obtain the IP address using the following methods.

### Check on the Router or Switch

The NanoKVM will obtain an IP address via DHCP after booting. You can find the IP address assigned to the NanoKVM on your router or switch.

### Check via Serial Port

Connect to the NanoKVM using a serial tool to get its IP address.

### Check via USB RNDIS Network Interface

> If the remote host is running Windows, refer to [usb rndis network interface](https://wiki.sipeed.com/hardware/zh/lichee/RV_Nano/5_peripheral.html#usb-rndis-网口) for driver installation.

1. Open a terminal on the remote host.
2. Execute the `ifconfig` command (or `ipconfig` on Windows).
3. Find the IPv4 address starting with 10 in the network list, as shown below:

    ![ipconfig](../../../../assets/NanoKVM/updating/ipconfig.png)

4. SSH into the NanoKVM using: `ssh root@10.223.155.1` (note, not 10.223.155.100), with the password `root`:

    ![ipconfig](../../../../assets/NanoKVM/updating/ssh.png)

5. After entering the NanoKVM, execute `ifconfig` and find the address of the `eth0` network card. This is the NanoKVM's IP address:

    ![ipconfig](../../../../assets/NanoKVM/updating/ifconfig.png)

6. Once you have the IP address, you can use it to access the NanoKVM.

## Check for Updates

1. Use any computer connected to the same network as the NanoKVM.
2. Open a browser (Chrome is recommended) and enter the obtained IP address in the address bar.
3. You will be directed to a login page. Enter the default username `admin` and password `admin` to log in:

    ![ipconfig](../../../../assets/NanoKVM/updating/login.png)

4. After logging in, click on check for updates:

    ![ipconfig](../../../../assets/NanoKVM/updating/check_for_update.png)

5. If there is an update available, click start update:

    ![ipconfig](../../../../assets/NanoKVM/updating/update.png)

6. Wait for the application update to complete. The browser will automatically refresh and return to the login page. Log in again.

## Update Complete

Congratulations! The image and application are now updated to the latest versions. You can now control the remote host by entering the NanoKVM's IP address in your browser.