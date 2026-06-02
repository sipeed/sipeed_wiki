# Sipeed TN160 热成像固件

Sipeed TN160（固件仓库名 `pico_tn160`）是基于 RP2350 的 160×120 热成像采集与 USB UVC 输出固件。当前固件使用 TinyUSB、PIO、DMA 和双核缓冲处理完成传感器采集、图像处理、自动 FFC、运行期 NUC 和 USB 视频输出。

> [!NOTE]
> 当前页面提供的是 TN160 开发验证固件。已放入 wiki 的 UF2 为 `2026-05-28` 日期版本，仍需以实际上板验证结果作为最终发布依据。

## 主要特性

- 采集 `160x120` 热成像数据。
- 通过 USB UVC 输出免驱视频流。
- UVC 基线参数为 `160x120`、`YUY2`、`10fps`、full-speed Bulk UVC。
- 支持 Windows、Linux/V4L2 和 `guvcview` 兼容性验证基线。
- 支持 UART 调试输出、双点校准、自动 FFC、运行期 NUC 和 Flash 校准数据加载。

## 固件下载

当前固件下载与烧录说明见 [固件下载](firmware.md)。

## UVC 使用

烧录固件后，将 TN160 通过 USB 连接到主机。系统会把设备识别为标准 UVC 摄像头，可使用 Windows 相机、OBS、VLC，或 Linux 下的 `guvcview`、`v4l2-ctl` 等工具预览。

Linux 下可先确认设备节点和格式：

```bash
v4l2-ctl --list-devices
v4l2-ctl -d /dev/videoX --list-formats-ext
```

其中 `/dev/videoX` 需要替换为实际设备节点。如遇到权限问题，请使用 `sudo` 或调整当前用户的视频设备权限。
