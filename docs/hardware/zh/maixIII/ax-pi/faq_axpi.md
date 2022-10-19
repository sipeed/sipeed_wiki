---
title: Maix-III 系列 AXera-Pi 常见问题（FAQ）
---

## Q：供电不足怎么办？

A：可以把两根 usb 口接上来供电，板子至少要 USB3.0 1A 的电流才能启动喔！（拉黑 USB2.0 500ma ）

## Q：被产品电了怎么办？

A：最近冬天静电来了，产品要注意接地喔。

## Q：如何更换 os04a10 摄像头？

A：一改参数，二改代码，以下述改动为例：

- 类似 sample_vin 这类命令改 `-c 0` 就可以启用 os04a10 摄像头，对应 `-c 2` 就是默认提供的 gc4653 摄像头。

- 类似于改代码里的 `COMMON_SYS_CASE_E eSysCase = SYS_CASE_SINGLE_GC4653;` ，详细可看[components/libmaix/lib/arch/axpi/libmaix_cam/libmaix_cam.cpp#L93](https://github.com/sipeed/libmaix/blob/release/components/libmaix/lib/arch/axpi/libmaix_cam/libmaix_cam.cpp#L93)

## Q：运行摄像头有关程序时报错 i2c_read: Failed to read reg: Remote I/O error.!？

A：检查摄像头配置是否与型号相匹配，命令行是否出错，

## Q：如何更换其他屏幕？

A：目前默认只提供 5 寸屏幕，支持其他屏幕需要自行修改驱动代码和设备树，以及对应的应用层显示代码。

## Q：如果使用 xxxx menuconfig 时遇到报错 locale.Error: unsupported locale setting ？

A：可以使用 `sudo localedef -i en_US -f UTF-8 en_US.UTF-8` 恢复一下配置即可。
