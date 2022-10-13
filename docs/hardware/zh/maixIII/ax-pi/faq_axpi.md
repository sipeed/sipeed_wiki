---
title: Maix-III 系列 AXera-Pi 常见问题（FAQ）
---

## Q：如何更换 os04a10 摄像头？

A：一改参数，二改代码，以下述改动为例：

- 类似 sample_vin 这类命令改 `-c 0` 就可以启用 os04a10 摄像头，对应 `-c 2` 就是默认提供的 gc4653 摄像头。

- 类似于改代码里的 `COMMON_SYS_CASE_E eSysCase = SYS_CASE_SINGLE_GC4653;` ，详细可看[components/libmaix/lib/arch/axpi/libmaix_cam/libmaix_cam.cpp#L93](https://github.com/sipeed/libmaix/blob/release/components/libmaix/lib/arch/axpi/libmaix_cam/libmaix_cam.cpp#L93)

## Q：如何更换其他屏幕？

A：目前默认只提供 5 寸屏幕，支持其他屏幕需要自行修改驱动代码和设备树，以及对应的应用层显示代码。
