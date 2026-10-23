# SDK 开发指南

MaixSense-D640 SDK 提供 C/C++ API，用于将深度数据集成到你的应用中。

## 安装

### 依赖

| 平台 | 依赖 |
| :--- | :--- |
| Linux (Ubuntu/Debian) | `sudo apt install libusb-1.0-0-dev libuvc-dev cmake build-essential` |
| Windows | CMake + Visual Studio，WinUSB 自动安装 |
| macOS | `brew install libusb cmake` |

### 编译

```bash
git clone https://github.com/sipeed/MaixSense-D640-SDK.git
cd MaixSense-D640-SDK
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
```

编译产物：
- `libmaix_stereo_depth.so` — 动态库
- `msd-latency` — 延迟测量工具
- `msd-upload` — 固件/标定上传工具

## API 概览

所有公开函数使用 `msd_` 前缀，头文件位于 `include/maix_stereo_depth/sdk.h`。

### 设备发现与打开

```c
#include <maix_stereo_depth/sdk.h>

// 创建上下文
msd_context *ctx = NULL;
msd_context_create(&ctx);

// 打开设备（NULL = 自动查找第一个）
msd_device *device = NULL;
msd_status status = msd_device_open(ctx, NULL, &device);
if (status != MSD_STATUS_OK) {
    printf("error: %s\n", msd_status_string(status));
    return -1;
}

// 获取固件信息
msd_firmware_info info;
msd_device_get_firmware_info(device, &info);
printf("firmware: %s\n", info.version);
```

### 获取深度帧

```c
msd_stream *stream = NULL;
msd_stream_config config = {
    .type = MSD_STREAM_DEPTH,
    .format = MSD_PIXEL_FORMAT_Z16,   // 16bit 毫米深度
};
msd_stream_open(device, &config, &stream);
msd_stream_start(stream);

while (running) {
    msd_frame frame;
    status = msd_stream_read(stream, &frame, 1000);  // 1000ms 超时
    if (status == MSD_STATUS_OK) {
        uint16_t *depth = (uint16_t *)frame.data;
        // depth[y * 640 + x] = 距离(mm)，0 表示无效
        printf("center depth: %u mm\n", depth[192 * 640 + 320]);
        msd_frame_release(&frame);
    }
}

msd_stream_stop(stream);
msd_stream_close(stream);
```

### 获取 IR 灰度帧

```c
msd_stream_config ir_config = {
    .type = MSD_STREAM_LEFT_IR,       // 或 MSD_STREAM_RIGHT_IR
    .format = MSD_PIXEL_FORMAT_MJPEG,
};
msd_stream *ir = NULL;
msd_stream_open(device, &ir_config, &ir);
msd_stream_start(ir);

msd_frame frame;
if (msd_stream_read(ir, &frame, 1000) == MSD_STATUS_OK) {
    // frame.data = JPEG 数据, frame.size = 字节数
    save_jpeg("ir_left.jpg", frame.data, frame.size);
    msd_frame_release(&frame);
}
```

### 深度滤波配置

```c
msd_depth_filter_config filter = {
    .confidence_threshold = 0.5f,    // 置信度阈值 [0,1]
    .min_depth_mm = 300.0f,          // 最小深度 300mm
    .max_depth_mm = 2000.0f,         // 最大深度 2000mm
    .spatial_filter_delta_q4 = 0,    // 空间滤波（0=关闭）
};
msd_device_set_depth_filters(device, &filter);
```

### 曝光控制

```c
// 读取当前曝光
msd_exposure_state exposure;
msd_device_read_exposure(device, &exposure);
printf("shutter: %u us, gain: %.2fx\n", exposure.shutter_us, exposure.analog_gain);

// 设为手动曝光
msd_exposure_config manual = {
    .mode = MSD_EXPOSURE_MANUAL,
    .shutter_us = 5000,
    .analog_gain = 1.0f,
};
msd_device_apply_exposure(device, &manual);

// 恢复自动曝光
msd_exposure_config auto_exp = { .mode = MSD_EXPOSURE_AUTO };
msd_device_apply_exposure(device, &auto_exp);
```

### 设备时钟（延迟测量）

```c
msd_device_clock clock;
msd_device_get_clock(device, &clock);
// clock.device_pts_us — 设备 AX PTS 时钟（微秒）
// clock.device_monotonic_us — 设备 CLOCK_MONOTONIC（微秒）
// clock.host_before_ns / host_after_ns — 主机请求前后时间戳
// 用于对齐帧 PTS 和主机时钟，计算端到端延迟
```

### 固件/标定上传

```c
// 上传固件
msd_device_upload_file(device, MSD_UPLOAD_FIRMWARE_PACKAGE,
                       "maixsense_d640-v1.0.tar.gz", 0, NULL, NULL);

// 上传标定
msd_device_upload_file(device, MSD_UPLOAD_CALIBRATION_PACKAGE,
                       "calibration.tar.gz", 0, NULL, NULL);

// 下载标定
msd_device_download_file(device, MSD_DOWNLOAD_CALIBRATION,
                         "current_calib.tar.gz", NULL, NULL);
```

### 清理

```c
msd_device_close(device);
msd_context_destroy(ctx);
```

## 命令行工具

### msd-latency

测量帧延迟：

```bash
# 测深度流延迟（采集 10 秒）
./msd-latency depth 10

# 测 IR 延迟
./msd-latency left 10

# 逐帧详情
./msd-latency depth 10 --per-frame
```

输出示例：
```
device    min    98  avg   126  p95   148  max   222 ms
transfer  min    22  avg    27  p95    33  max    35 ms
total     min   123  avg   153  p95   176  max   255 ms
```

### msd-upload

固件和标定文件管理：

```bash
# 上传固件
./msd-upload firmware maixsense_d640-v1.0.tar.gz --restart

# 上传标定
./msd-upload calibration calib.tar.gz --restart

# 下载当前标定
./msd-upload fetch-calibration output.tar.gz
```

## 延迟指标

| 指标 | 深度流 | IR 流 |
| :--- | :--- | :--- |
| 设备侧延迟 | 126ms avg, 98ms min | 40ms avg |
| USB 传输 | 27ms avg | 11ms avg |
| 端到端 | 153ms avg | 50ms avg |

## 注意事项

- 同一设备同时只能有一个进程打开（UVC 设备独占）
- 深度帧率由 NPU 决定（~12fps），无法通过 SDK 调整
- macOS 上厂商控制（滤波/曝光/时钟）走 NCM 网络通道，需要 USB 网络连接可用
