---
title: Maix-III AXera-Pi Q&A
---

## Q：Device not work

A: Try to plug connect the 2 USB on m3axpi, by this m3axpi can get enough power to boot. m3axpi comsume 5V*1A maximum.

## Q：How to switch to os04a10 camera？

A：**Change the parameter, or edit code**

- For examples like [`sample_vin_vo`](./basic_usage.md#video), we can change the parameter `-c 2` into `-c 0` to switch camera.
- Like to edit the code `COMMON_SYS_CASE_E eSysCase = SYS_CASE_SINGLE_GC4653;`, visit [github libmaix](https://github.com/sipeed/libmaix/blob/release/components/libmaix/lib/arch/axpi/libmaix_cam/libmaix_cam.cpp) to know more.

<div>
    <img src="./assets/qa/qa_switcg_os04a10_1.jpg" alt="qa_switcg_os04a10_1" width="45%">
    <img src="./assets/qa/qa_switcg_os04a10_2.jpg" alt="qa_switcg_os04a10_2" width="45%">
</div>

## Q：Error `i2c_read: Failed to read reg: Remote I/O error.!` when using camera

A: Make sure you have connected the camera and board correctly, and run the command correctly, like using the mismatched camera parameters or wrong parameters in command. If these are all right but this error still occurs, there are some errors on the device.

## Q：How to use the other screen？

A：Up to now we only provide screen with 5 inches, and for other screens you need to build the driver, edit the device tree and the application codes to display.

## Q：Error `locale.Error: unsupported locale setting !` when running `xxxx menuconfig`

A: Run `sudo localedef -i en_US -f UTF-8 en_US.UTF-8` to restore the configuration to slove this.

## Q：Error `VCEncInit:ERROR codecFormat NOT support by HW !` when running `IPC ODM`

A: Try to reboot device by pressing the RST key onboard or replug device.

## Q：Screen display wrong

![faq_display](./../../../zh/maixIII/assets/faq_display.jpg)

A: Check if you have set the correct camera parameters.

## Q：Screen shows opposite camera content

A: This occurs because of the different batches of products, connecting them with 180° rotation.

![faq_video_a](./../../../zh/maixIII/assets/faq_video_a.jpg)

Those who have shell for AXera-Pi can connect them like in the following pictures:

<html>
      <img src="./../../../zh/maixIII/assets/faq_video_b.jpg" width=48%>
      <img src="./../../../zh/maixIII/assets/faq_video_c.jpg" width=48%>
</html>

## Q：Error `Bus Error！`

![faq_bus](./../../../zh/maixIII/assets/faq_bus.jpg)

A：This happens when data in the tf card system is broken because of the bad quality of tf card.

- Try to use a good tf card, like what we sell, and you can choose your tf card based on our test: [Choose tf card](./flash_system.md#choose-tf-card)

## Q：No eth0 ip address after running `ifconfig -a`

A：There is no ip address if the ethernet is not connected to the Internet, check your ethernet connection. Or use command `dhclient eth0` to get the ip address mannaly or visit [config eth0](./basic_usage.md#config-eth0) to know more.

## Q：Device not found after running uvc

A：This might happen on Windows. Check if there is an error in Windows device manager, remove the incorrect device then this error will be solved.

## Q：The device is stuck after running uvc

A：Reboot the board

## Q：No wlan0 shown in result after running command `ifconfig`

A：
- Maybe the bad connection between Core Model and ext-board because of the express, reconnect them to fix this bad connection.
- The wireless module is changed in `20221219`, so it's need to change the configration file, run the following command:

```bash
ls /boot/
cp /boot/kernel.img.rtl8189fs kernel.img
```

## Q：Error `packet_write_wait: Connection to 10.xxx.xxx.xxx port 22: Broken pipe！` after login by ssh

A: Reboot device after run Run command `python3 -c "import os, binascii; os.system('sed -i \'/iface eth0 inet dhcp/ahwaddress ether {}\' /etc/network/interfaces'.format(binascii.hexlify(bytes.fromhex(open('/proc/ax_proc/uid').read().split('0x')[1][:-5]),':').decode('iso8859-1'))) if os.system('grep \'hwaddress ether\' /etc/network/interfaces -q') != 0 else exit();"` in serial port.

## Q：The screen is blurred after booting.
## Q：Sticking Image on screen

<html>
      <img src="./../../../zh/maixIII/assets/faq_dth.jpg" width=48%>
      <img src="./../../../zh/maixIII/assets/faq_sawtooth.jpg" width=48%>
</html>

A：Because of the because of the different batches of products, the configuration for screen is different, replace the `dtb` file in `/boot/` folder.

```bash
ls /boot/
cp /boot/dtb.img.lcd20220830 dtb.img #dtb.img.lcd20221025 dtb.img
```

## Q：Error `can't open camera by index` when running opencv.

A：Check if the camera in the code matches the camera you use. [switch camera](#qhow-to-switch-to-os04a10-camera)

## Q：`XERA-UBOOT=>` is shown from serial port.

A：This happens when autoboot is canceled when booting device, use command `boot` to start system.

![faq_boot](./../../../zh/maixIII/assets/faq_boot.jpg)