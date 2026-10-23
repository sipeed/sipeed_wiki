# MaixSense-D640

|    时间    | 负责人 |    更新内容    |
| :--------: | :----: | :------------: |
| 2026.10.23 |        | 初次编写文档   |

## 产品概述

**MaixSense-D640** 是 Sipeed 推出的双目立体深度相机模组，基于 AX620Q 视觉 SoC，搭载两颗 SC035HGS 全局快门传感器，通过 NPU 实时推理输出密集视差/深度图。

### 主要特性

- **分辨率**：深度图 640×384 @12fps（NPU 实时推理），双目 IR 640×480 @30fps
- **接口**：USB 2.0 Type-C（UVC 即插即用，免驱）
- **输出格式**：
  - Raw Depth（Z16/D16/Y16，毫米级 16bit 深度）
  - 伪彩深度（MJPEG，可视化）
  - 左/右 IR 灰度（MJPEG）
- **测量范围**：0.2m ~ 5m（取决于基线和标定）
- **SoC**：爱芯元智 AX620Q（双核 Cortex-A7 + 3.2TOPS NPU）
- **传感器**：2× 思特威 SC035HGS（全局快门，850nm IR 优化）
- **基线**：长基线 ~99mm / 短基线 ~32mm（不同硬件版本）

### 资料汇总

| 资料 | 链接 |
| :--- | :--- |
| SDK 下载 | [GitHub](https://github.com/sipeed/MaixSense-D640-SDK) |
| 硬件资料 | [下载站](https://dl.sipeed.com/shareURL/MaixSense/MaixSense_D640) |

## 快速上手

### 准备工作

- MaixSense-D640 模组 × 1
- USB Type-C 数据线 × 1（建议使用高质量线材）
- Windows 10/11 或 Linux PC × 1

### 连接设备

1. 使用 USB-C 线将 D640 连接到电脑
2. 设备上电后自动启动固件，约 10 秒后完成初始化
3. 系统会识别到 4 个 UVC 视频设备：

| 设备节点 (Linux) | 流 | 格式 | 分辨率 | 帧率 |
| :--- | :--- | :--- | :--- | :--- |
| /dev/video0 | Raw Depth | Z16/D16/Y16 | 640×384 | 12fps |
| /dev/video1 | 伪彩深度 | MJPEG | 640×384 | 12fps |
| /dev/video2 | 左 IR | MJPEG | 640×480 | 30fps |
| /dev/video3 | 右 IR | MJPEG | 640×480 | 30fps |

> **Windows 用户**：设备免驱，即插即用。在"相机"应用或任意 UVC 查看工具中可看到 4 个视频源。
>
> **Linux 用户**：通过 `v4l2-ctl --list-devices` 可列出所有设备节点。

### 快速预览

#### 方法一：使用任意 UVC 查看工具

D640 是标准 UVC 设备，可使用以下工具直接查看：

- **Windows**：[PotPlayer](https://potplayer.daum.net/)、VLC、系统相机应用
- **Linux**：`guvcview`、`vlc`、`ffplay`
- **macOS**：QuickTime Player、VLC

```bash
# Linux 快速查看伪彩深度流
ffplay /dev/video1

# 查看 IR 流
ffplay /dev/video2
```

#### 方法二：使用 SDK 测量延迟和查看深度数据

```bash
# 编译 SDK
cd sdk && mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)

# 查看深度延迟
./msd-latency depth 10

# 查看 IR 延迟
./msd-latency left 10
```

## SDK 开发指南

### 安装 SDK

```bash
git clone https://github.com/sipeed/MaixSense-D640-SDK.git
cd MaixSense-D640-SDK
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
```

依赖：`libusb-1.0-dev`、`libuvc-dev`（Linux）或 WinUSB（Windows）。

### 核心 API

SDK 提供 C API（`msd_` 前缀），头文件 `#include <maix_stereo_depth/sdk.h>`。

#### 打开设备

```c
#include <maix_stereo_depth/sdk.h>

msd_context *ctx = NULL;
msd_context_create(&ctx);

msd_device *device = NULL;
msd_status status = msd_device_open(ctx, NULL, &device);  // NULL = 自动查找
if (status != MSD_STATUS_OK) {
    printf("打开设备失败: %s\n", msd_status_string(status));
    return -1;
}

// 获取固件信息
msd_firmware_info info;
msd_device_get_firmware_info(device, &info);
printf("固件版本: %s\n", info.version);
```

#### 获取深度帧

```c
msd_stream *stream = NULL;
msd_stream_config config = {
    .type = MSD_STREAM_DEPTH,
    .format = MSD_PIXEL_FORMAT_Z16,
};
msd_stream_open(device, &config, &stream);
msd_stream_start(stream);

while (running) {
    msd_frame frame;
    status = msd_stream_read(stream, &frame, 1000);  // 1000ms 超时
    if (status == MSD_STATUS_OK) {
        // frame.data 指向 640×384 的 uint16_t 深度数据（单位：毫米）
        uint16_t *depth = (uint16_t *)frame.data;
        printf("中心点深度: %u mm\n", depth[192 * 640 + 320]);
        msd_frame_release(&frame);
    }
}

msd_stream_stop(stream);
msd_stream_close(stream);
```

#### 获取 IR 灰度帧

```c
msd_stream_config ir_config = {
    .type = MSD_STREAM_LEFT_IR,
    .format = MSD_PIXEL_FORMAT_MJPEG,
};
msd_stream_open(device, &ir_config, &ir_stream);
```

#### 获取设备时钟（延迟测量）

```c
msd_device_clock clock;
msd_device_get_clock(device, &clock);
printf("设备 PTS: %lu us, 设备 monotonic: %lu us\n",
       clock.device_pts_us, clock.device_monotonic_us);
// 可用于对齐设备帧时间戳与主机时钟，计算端到端延迟
```

#### 上传固件/标定

```c
// 上传固件包
msd_device_upload_file(device, MSD_UPLOAD_FIRMWARE_PACKAGE,
                       "maixsense_d640-v1.0.tar.gz", 0, NULL, NULL);

// 上传标定文件
msd_device_upload_file(device, MSD_UPLOAD_CALIBRATION_PACKAGE,
                       "calibration.tar.gz", 0, NULL, NULL);

// 下载当前标定
msd_device_download_file(device, MSD_DOWNLOAD_CALIBRATION,
                         "current_calib.tar.gz", NULL, NULL);
```

### 编译选项

| CMake 选项 | 默认 | 说明 |
| :--- | :--- | :--- |
| `BUILD_EXAMPLES` | ON | 编译示例程序 |
| `BUILD_SHARED_LIBS` | ON | 编译为动态库 |

### 示例程序

| 程序 | 说明 |
| :--- | :--- |
| `msd-latency` | 延迟测量工具（支持 depth/left/right 流） |
| `msd-upload` | 固件和标定文件上传工具 |

## 固件更新

### 通过 USB 上传（推荐）

```bash
# 使用 SDK 工具
./msd-upload firmware maixsense_d640-v1.0.tar.gz --restart
```

设备会自动完成：解压 → 校验 SHA256 → 替换文件 → 重启服务。固件更新**不会覆盖标定数据**。

### 通过 SSH（开发调试）

设备通过 USB 建立 NCM 网络连接（IP 默认 `10.253.24.1`，密码 `sipeed`）：

```bash
ssh root@10.253.24.1

# 手动部署
scp maixsense_d640_live root@10.253.24.1:/opt/maixsense-d640/
ssh root@10.253.24.1 "systemctl restart maixsense-d640"
```

### 固件目录结构

```
/opt/maixsense-d640/
├── maixsense_d640_live          # 主固件
├── VERSION                      # 版本号
├── models/620E.axmodel          # 深度 NPU 模型
├── calibration/                 # 标定数据（固件更新不覆盖）
│   ├── stereo_calib.ini         # 内参与投影矩阵
│   ├── stereo_calib_left_mesh.bin
│   └── stereo_calib_right_mesh.bin
├── scripts/
│   ├── maixsense-d640-start.sh  # 启动脚本
│   ├── maixsense-d640-stop.sh   # 停止脚本
│   └── maixsense-d640.service   # systemd 服务单元
└── lib/                         # 运行时库
```

## 常见问题

### 连接后没有识别到设备

1. 确认 USB 线是数据线而非充电线
2. 设备上电后需要约 10 秒完成初始化
3. Linux 下运行 `lsusb` 确认设备出现（Vendor ID: Sipeed）
4. 检查 `dmesg` 中是否有 USB 枚举错误

### 深度图帧率只有 12fps

这是正常的。深度帧率由 NPU 推理速度决定（AX620Q 800MHz NPU 约 75ms/帧 ≈ 13fps），描述符声明 12fps。IR 流可达 30fps。

### 深度图有黑色区域

黑色像素表示该区域深度值无效（置信度低或超出测量范围），常见原因：
- 物体表面反光或透明
- 距离超出测量范围
- 双目遮挡区域（靠近基线边缘）

### 如何获取毫米级深度值

使用 Z16 格式打开 Raw Depth 流，每个像素是 `uint16_t` 类型，单位为毫米。值为 0 表示无效。

### SSH 连接不上设备

- 确认 USB NCM 网络接口已获取到 IP 地址
- Linux：`ip addr` 查看是否有 `usb0` 或 `enx*` 接口
- Windows：设备管理器中查看"网络适配器"是否出现 RNDIS/NCM 设备
- 设备 IP 默认为 `10.253.24.1`，密码 `sipeed`

### 标定数据丢失或需要重新标定

```bash
# 从设备下载当前标定
./msd-upload fetch-calibration current_calib.tar.gz

# 上传新标定
./msd-upload calibration new_calib.tar.gz --restart
```

标定数据在固件更新时不会被覆盖。

### 设备发热正常吗

AX620Q SoC 在持续运行 NPU 推理时会有一定发热，属于正常现象。建议保持通风良好，避免密封环境长时间运行。

## 技术规格

| 参数 | 规格 |
| :--- | :--- |
| SoC | 爱芯元智 AX620Q (2× Cortex-A7 + 3.2 TOPS NPU) |
| 传感器 | 2× 思特威 SC035HGS (全局快门, 640×480) |
| 深度分辨率 | 640×384 |
| 深度帧率 | 12fps (NPU bound) |
| IR 帧率 | 30fps |
| 测量范围 | 0.2m ~ 5m |
| 接口 | USB 2.0 Type-C (UVC + NCM) |
| 输出协议 | UVC (即插即用，免驱) |
| 供电 | USB 5V, 典型功耗 ~1.5W |
| 基线 | 长基线 ~99mm / 短基线 ~32mm |
| 视场角 | ~70°(H) × 50°(V) (取决于镜头) |
| 工作温度 | 0°C ~ 50°C |

## 延迟指标

| 指标 | 典型值 |
| :--- | :--- |
| 设备侧延迟 (capture→send) | 126ms avg, 98ms min |
| USB 传输延迟 | 27ms avg |
| 端到端延迟 (capture→host receive) | 153ms avg |
| IR 端到端延迟 | 50ms avg |
