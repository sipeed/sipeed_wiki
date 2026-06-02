# TN160 固件下载

本页提供 TN160 当前开发验证固件。该固件来自 `pico_tn160` 项目的 `docs/pico_tn160_2026-05-28.elf.uf2`，用于验证 160×120 热成像采集和 full-speed Bulk UVC 输出。

> [!IMPORTANT]
> 该 UF2 已完成构建校验，但页面写入时仍标记为“待上板完整验证”。量产或对外稳定发布前，应以实际 Windows、Linux/V4L2、`guvcview` 和长时间热漂测试结果为准。

## 当前固件

| 项目 | 内容 |
| :--- | :--- |
| 文件 | [pico_tn160_2026-05-28.elf.uf2](assets/firmware/pico_tn160_2026-05-28.elf.uf2) |
| 大小 | `438272` bytes |
| SHA256 | `55a8776114e4696c2f3f3eb363b05777e9362523250b743c10192abc77e38885` |
| 输出模式 | USB UVC，`160x120`，`YUY2`，`10fps` |
| USB 传输 | full-speed Bulk UVC |
| 状态 | 构建通过，待上板完整验证 |

## 烧录方法

1. 断开 TN160 与电脑的 USB 连接。
2. 按住板上的 `BOOT` / `BOOTSEL` 按键后接入 USB，使 RP2350 进入 UF2 下载模式。
3. 电脑会出现一个 RP2350/RPI-RP2 类似名称的 U 盘。
4. 将上方 UF2 文件复制到该 U 盘根目录。
5. 等待复制完成，设备会自动重启并运行新固件。

## 验证建议

烧录后建议至少确认以下项目：

- Windows 可以识别到 UVC 摄像头并出画面。
- Linux 下可通过 `v4l2-ctl` 连续抓取多帧。
- `guvcview` 可以选择并显示 `160x120`、`YUY2`、`10fps` 画面。
- 静态场景运行 8 到 10 分钟，观察画面和温漂表现是否稳定。

Linux 抓帧示例：

```bash
v4l2-ctl -d /dev/videoX --stream-mmap --stream-count=5 --stream-to=/tmp/tn160.yuyv
```

其中 `/dev/videoX` 需要替换为实际设备节点。
