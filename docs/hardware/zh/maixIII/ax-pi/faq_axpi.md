---
title: Maix-III 系列 AXera-Pi 常见问题（FAQ）
---

## Q：供电不足怎么办？

A：可以把两根 usb 口接上来供电，板子至少要 USB3.0 1A 的电流才能启动喔！（拉黑 USB2.0 500ma）

## Q：被产品电了怎么办？

A：最近冬天静电来了，产品要注意接地喔。

## Q：如何更换 os04a10 摄像头？

A：**一改参数，二改代码，以下述改动为例**：

- 类似 sample_vin_vo 这类命令改 `-c 0` 就可以启用 os04a10 摄像头，对应 `-c 2` 就是默认提供的 gc4653 摄像头。
- 如果是类似 [IPCDemo](./basic_usage.md#ipcdemo) 的话更改相对应后缀 gc4653 为 `gc4653_config.json`、os04a10 为 `os04a10_config.json`。
  ![ipc_demo_json](./../../../en/maixIII/ax-pi/assets/flash_system/ipc_demo_json.jpg)
- 像[RSTP](./basic_usage.md#rtsp) 这种脚本运行的示例，可以通过编辑里面的摄像头注释来改变摄像头配置。
  ![rtsp_stream_shell](./../../../en/maixIII/ax-pi/assets/flash_system/rtsp_stream_shell.jpg)

- 可以编辑 C 代码里设置默认摄像头的代码 `COMMON_SYS_CASE_E eSysCase = SYS_CASE_SINGLE_GC4653;` 来切换摄像头，详细可看[components/libmaix/lib/arch/axpi/libmaix_cam/libmaix_cam.cpp#L93](https://github.com/sipeed/libmaix/blob/release/components/libmaix/lib/arch/axpi/libmaix_cam/libmaix_cam.cpp#L93)
<div>
  <img src="./../../../en/maixIII/ax-pi/assets/qa/qa_switcg_os04a10_1.jpg" alt="qa_switcg_os04a10_1" width="45%">
  <img src="./../../../en/maixIII/ax-pi/assets/qa/qa_switcg_os04a10_2.jpg" alt="qa_switcg_os04a10_2" width="45%">
</div>

## Q：运行摄像头有关程序时报错 i2c_read: Failed to read reg: Remote I/O error.!？

A：摄像头接线是否正确、检查摄像头配置是否与型号相匹配、参数是否修改、启动命令行输入是否出错、以及摄像头是否启动；如果以上都是正确的话，摄像头依旧报错就是硬件问题了。

## Q：如何更换其他屏幕？

A：目前默认只提供 5 寸屏幕，支持其他屏幕需要自行修改驱动代码和设备树，以及对应的应用层显示代码。

## Q：运行 xxxx menuconfig 时遇到报错 locale.Error: unsupported locale setting !?

A：可以使用 `sudo localedef -i en_US -f UTF-8 en_US.UTF-8` 恢复一下配置即可。

## Q：运行 IPC ODM 命令时报错 VCEncInit:ERROR codecFormat NOT support by HW !?

A：试着按复位键或者是插拔重启设备即可。

## Q：运行程序后屏幕显示花屏？

![faq_display](./../assets/faq_display.jpg)
A：查看摄像头型号参数是否配置正确。

## Q：摄像头、屏幕画面反了倒过来了怎么解决？

A：这是批次问题，物理旋转即可解决。

![faq_video_a](./../assets/faq_video_a.jpg)

有装配外壳的 AXera-Pi 可参考以下图例：

<html>
      <img src="./../assets/faq_video_b.jpg" width=48%>
      <img src="./../assets/faq_video_c.jpg" width=48%>
</html>

## Q：运行命令后报错：Bus Error！？

![faq_bus](./../assets/faq_bus.jpg)

A：这种情况是 SD 卡质量问题导致掉卡，也就是镜像卡里面的程序崩掉了无法读取到。

- 更换质量好一点的 SD 卡或官方购买镜像卡，可参照 `SD` 卡测试选购合适的卡[点击前往查看](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/flash_system.html#%E5%A6%82%E4%BD%95%E9%80%89%E6%8B%A9-SD-%E5%8D%A1%EF%BC%9F)。

## Q：使用 `ifconfig -a` 查看后没有 eth0 ip 地址？

A：没有联网的话会直接看不到 ip 地址，查看下网线是否有接入、是否接稳了。
   - 或使用 `dhclient eth0` 手动启动或参考文档[传送门](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/basic_usage.html#%E6%9C%89%E7%BA%BF%E4%BB%A5%E5%A4%AA%E7%BD%91%EF%BC%88eth0%EF%BC%89%E9%85%8D%E7%BD%AE%E6%96%B9%E6%B3%95)重新配置 ip 获取地址。

## Q：运行 uvc 命令后一直报错读取不到设备？

A：这种情况一般会少数出现在 Windows 环境上，查看设备管理器是不是有什么显示异常驱动，卸载后即可使用。

## Q：运行 uvc 命令后出现卡住现象？

A：重启即可

## Q：开机 ifconfig 不显示 wlan0 ？

A：可能是核心板与底板衔接松了，重新插拔核心板与底板可！

A：**20230103** 后的新版底板更换了 WiFi 模组物料，默认的系统镜像里面所使用的 Wifi 模组型号为`rtl8189fs`，因此对于之前所搭载的 `rtl8723bs` Wifi 模组的底板需要执行下面的命令来并执行 `reboot` 命令来重启设备以重新适配 Wifi 硬件。具体更改差别可前往[更改说明](#q硬件物料更改说明) 查看。

```bash
ls /boot/
cp kernel.img.rtl8723bs kernel.img #cp /boot/kernel.img.rtl8189fs kernel.img  
```

A：重新插拔核心板且执行上述命令后仍然不显示 wlan0 的话，重新烧录镜像来解决未知的系统问题(极少见)。

## Q：使用 ssh 登陆后断开报错：packet_write_wait: Connection to 10.xxx.xxx.xxx port 22: Broken pipe！

A: 运行一下`python3 -c "import os, binascii; os.system('sed -i \'/iface eth0 inet dhcp/ahwaddress ether {}\' /etc/network/interfaces'.format(binascii.hexlify(bytes.fromhex(open('/proc/ax_proc/uid').read().split('0x')[1][:-5]),':').decode('iso8859-1'))) if os.system('grep \'hwaddress ether\' /etc/network/interfaces -q') != 0 else exit();"` 后重启即可。


## Q：开机画面出现锯齿或以下画面怎么解决？
## Q：屏幕出现烧屏情况？

<html>
      <img src="./../assets/faq_sawtooth.jpg" width=48%>
      <img src="./../assets/faq_dth.jpg" width=48%>
</html>

A：屏幕批次不同导致的原因，因设备树版本的不同导致可能会出现烧屏情况，参考[更改说明](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/faq_axpi.html#Q：硬件物料更改说明)区分版本及时更换以下 `/boot/ dtb ` 设备树的文件即可。

```bash
ls /boot/
cp /boot/dtb.img.lcd20220830 dtb.img #dtb.img.lcd20221025 dtb.img
```

## Q：运行 opencv 相关后报错：can't open camera by index.

A：查询一下摄像头设备号是否与代码内调用设备号的一致。

## Q：烧录后启动失败显示 XERA-UBOOT=>

A：进入 uboot 模式了输入 boot 后即可启动。

![faq_boot](./../assets/faq_boot.jpg)

## Q：硬件物料更改说明

因为某些原因板卡更换了部分硬件，下面来说明更换的地方。

- **新旧版底板区别**

1. 在新版本的底板上我们标注了设备号：`v3768`，用户也可以根据版本号来确认新旧版本。
   
2. WiFi 模块更换：`旧 RTL8723BS` -> `新 RTL8189FTV`，遇到 wlan0 不现实的情况的话需要替换驱动，可以执行下面的命令来替换，或者 [查看没有 wlan0](#q开机-ifconfig-不显示-wlan0) 来了解更多。

```bash
ls /boot/
cp kernel.img.rtl8723bs kernel.img #cp /boot/kernel.img.rtl8189fs kernel.img  
```
  
3. 底板摄像头 FPC 连接座更换，主要就是固定方向改变，但是接线方向未变。
![faq_borad](./../assets/faq_board.jpg)

- **新旧版摄像头区别**

新版摄像头线序方向发生了变化，可参考示例进行接线，防止接反导致烧坏排线或板卡，接线示例指路[点击](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/flash_system.html#%E5%A6%82%E4%BD%95%E8%BF%9E%E6%8E%A5%E5%A4%96%E8%AE%BE%E5%92%8C%E9%85%8D%E4%BB%B6%EF%BC%9F)查看。

![faq_sensor](./../assets/faq_sensor.jpg)

- **新旧版屏幕区别**

新旧版的屏幕设备树不同，根据屏幕的日期区分并在使用时替换 `/boot` 目录下对应设备树驱动即可，请及时更换否则会导致烧屏，更换方法指路[点击](https://wiki.sipeed.com/hardware/zh/maixIII/ax-pi/faq_axpi.html#Q%EF%BC%9A%E5%B1%8F%E5%B9%95%E5%87%BA%E7%8E%B0%E7%83%A7%E5%B1%8F%E6%83%85%E5%86%B5%EF%BC%9F)查看。

![faq_newdisplay](./../assets/fqa_newdisplay.jpg)
  
