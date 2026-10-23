# 快速上手

## 开箱准备

- MaixSense-D640 模组 × 1
- USB Type-C 数据线 × 1（需要数据线，非充电线）
- 电脑 × 1（Windows / Linux / macOS）

## 连接设备

1. 使用 USB-C 线将 D640 连接到电脑
2. 等待约 10 秒，设备自动初始化
3. 系统会识别到 4 个视频设备

**Linux 确认设备：**
```bash
v4l2-ctl --list-devices
# 应显示 4 个 /dev/videoN 节点
```

**Windows 确认设备：** 打开"设备管理器" → "照相机"，应看到 4 个 UVC 设备。

## 快速预览

### 方法一：系统自带工具

D640 是标准 UVC 设备，可用任意视频查看工具：

**Windows：**
- 打开"相机"应用，切换到 D640 的伪彩深度流
- 或使用 [PotPlayer](https://potplayer.daum.net/) 打开任意一路流

**Linux：**
```bash
# 查看伪彩深度
ffplay /dev/video1

# 查看左 IR
ffplay /dev/video2

# 使用 guvcview
guvcview -d /dev/video1
```

**macOS：**
- QuickTime Player → 文件 → 新建影片录制 → 选择 D640 设备
- 或使用 VLC

### 方法二：使用 GUI 应用（推荐）

GUI 提供完整的预览、配置和管理功能，详见 [GUI 使用指南](./gui.md)。

### 方法三：使用 SDK 命令行

```bash
# 编译 SDK
cd sdk && mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)

# 测量深度延迟
./msd-latency depth 10

# 测量 IR 延迟
./msd-latency left 10
```

## SSH 登录设备

D640 通过 USB 同时建立 NCM 网络连接，可 SSH 登录进行调试：

```bash
# Linux/macOS
ssh root@10.253.24.1
# 密码: sipeed
```

> Windows 用户需确认 NCM/RNDIS 网络适配器已正常识别。IP 地址取决于板子配置，常见为 `10.253.24.1`。

## 下一步

- [GUI 使用指南](./gui.md) — 桌面应用完整操作
- [SDK 开发指南](./sdk.md) — 集成深度数据到你的应用
