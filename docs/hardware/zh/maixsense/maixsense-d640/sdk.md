---
title: SDK 开发指南
keywords: MaixSense, D640, SDK, 深度相机
update_open: false
update:
  - date: 2026-10-27
    version: v0.1
    author: lxowalle
    content: 初版
---

MaixSense D640 SDK 提供 C/C++ 封装的用于编程连接相机的开发工具包，用于读取深度与左右红外图、获取同步帧组、处理点云和控制设备。

下面以 Linux 的 USB 采集为例，完成从构建到保存第一组数据的过程。

同步帧组指同一次采集对应的深度/伪彩图与左右红外图，相同帧组 ID 用于确认三张图的对应关系。

## SDK 能做什么

| 功能 | 用途 |
| :--- | :--- |
| 设备发现与热插拔监听 | 按稳定序列号区分设备，查询可用图像配置 |
| 原始深度与左右红外采集 | 保存毫米深度和原始图像，供算法处理 |
| 深度处理与点云 | 伪彩、空间/时间滤波、空洞处理及 XYZ 点云生成 |
| 设备控制 | 在支持的平台和固件上读取内参、调整曝光与设备滤波、传输固件和标定文件 |
| 桌面及机器人集成 | 可选 OpenCV、Open3D、PCL 示例，以及 [ROS 2 主机驱动](./ros2.md) |

各平台支持范围以 SDK 发行说明为准。以下命令和同步采集说明只针对 Linux 系统。

下载并解压[最新 SDK 源码包](https://cdn.sipeed.com/maixsense/d640/latest/maixsense_d640_sdk_source.tar.gz)，再执行下面的安装和构建步骤。

## 准备环境

Debian / Ubuntu 可安装：

```bash
sudo apt update
sudo apt install build-essential cmake ninja-build
```

## 构建核心 SDK

在 SDK 根目录执行：

```bash
cmake --preset core
cmake --build --preset core
```

构建成功后，`build/core` 中应出现 `msd-enumerate` 和 `msd-capture`。需要桌面算法或点云查看器时，再按 SDK 包中的 README 安装可选依赖并使用相应配置。

## 检查设备

1. 按[快速上手](./quick-start.md)配置 Linux 权限并连接相机。
2. 关闭上位机、浏览器和其他采集程序。
3. 枚举设备，确认输出包含相机序列号和可用图像配置：

```bash
./build/core/msd-enumerate
```

`msd-enumerate` 即使扫描到零台设备也可能正常退出，因此需要检查输出中的设备数量。示例默认使用首台设备，多设备程序应按序列号选择。

## 采集并保存同步图像

```bash
./build/core/msd-capture --mode depth --frames 10 --output ./demo-depth
```

程序等待 **10 个完整同步帧组，只将最后一组写入输出目录**，不会保存连续 10 组图片。在新的输出目录中，应得到三个非空文件，文件名中的帧组 ID 相同。下面的 `<frame_set_id>` 会替换成实际编号：

```text
demo-depth/
├── depth_<frame_set_id>.pgm
├── left_ir_<frame_set_id>.jpg
└── right_ir_<frame_set_id>.jpg
```

两张 JPEG 可直接查看。PGM 是 16 位深度图，像素值单位为毫米。PGM 文件按规范使用大端序，SDK 原始 Depth16 数据为小端序，自己解析时需要区分。保存的 PGM 中无效深度为 0。

设备端伪彩采集示例：

```bash
./build/core/msd-capture --mode pseudo --frames 10 --output ./demo-pseudo
```

此时第一份文件变为 `pseudo_<frame_set_id>.jpg`，不包含原始毫米深度。两种模式均同时采集左右红外。缺少完整同步组时示例会报错，不会用不匹配的图像凑齐三路。

常见退出码：`0` 表示成功，`1` 表示采集、同步或文件写入失败，`2` 表示参数错误或未找到兼容设备。超时时先检查权限、固件与 SDK 是否配套，以及其他程序是否占用设备。

## 在自己的程序中使用

从 SDK 包内 `examples/capture.cpp` 开始，结合公开头文件 `include/maixsense_d640/sdk.h` 使用。需要对应同次采集的深度与双目图时，使用完整帧组接口 `msd_pipeline_wait_for_frame_set()`。不要用电脑收到图像的先后顺序或时间戳自行猜配。

点云由 SDK 在主机端根据深度图和对应内参生成。可选的 OpenCV 查看器、Open3D/PCL 点云工具和 ROS 2 驱动，分别参见包内 `examples/README.zh-CN.md` 与 `ros2/README.zh-CN.md`。可选依赖缺失时，部分示例不会构建。

## 下一步

- 无需编程即可测距、抓图和录制：[上位机软件指南](./gui.md)
- 了解深度数据的测量条件：[测量精度](./accuracy.md)
- 连接和同步异常：[常见问题](./faq.md)
