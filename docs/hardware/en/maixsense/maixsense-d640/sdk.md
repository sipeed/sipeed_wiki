---
title: SDK Guide
keywords: MaixSense, D640, SDK, depth camera, C, C++
update_open: false
update:
  - date: 2026-10-27
    version: v0.1
    author: lxowalle
    content: Initial release
---

The MaixSense D640 SDK provides C and C++ interfaces for reading depth and infrared images, receiving synchronized frame sets, generating point clouds, and controlling the camera.

This guide walks through building the SDK and saving a first image set over USB on Linux. A synchronized frame set contains matching depth or pseudocolor, left IR, and right IR images. The frame-set ID identifies which images belong together.

## SDK capabilities

| Capability | Use |
| :--- | :--- |
| Discovery and hotplug monitoring | Identify cameras by serial and query available image profiles |
| Depth and stereo infrared capture | Save millimetre depth and images for your algorithms |
| Depth processing and point clouds | Generate pseudocolor and XYZ clouds, apply spatial/temporal filters, and fill holes |
| Device control | Read calibration, adjust exposure and device filters, and transfer firmware or calibration on supported platforms and firmware |
| Desktop and robot integration | Optional OpenCV, Open3D, and PCL examples, plus the [ROS2 driver](./ros2.md) |

Check the SDK release notes for platform support. The commands below apply to Linux USB capture.

Download and extract the [latest SDK source package](https://cdn.sipeed.com/maixsense/d640/latest/maixsense_d640_sdk_source.tar.gz) before following the installation and build steps.

## Prepare the environment

On Debian or Ubuntu:

```bash
sudo apt update
sudo apt install build-essential cmake ninja-build
```

## Build the core SDK

Run from the SDK root directory:

```bash
cmake --preset core
cmake --build --preset core
```

After a successful build, `build/core` contains `msd-enumerate` and `msd-capture`. For desktop algorithms or point cloud viewers, install the optional dependencies and select the build configuration described in the SDK README.

## Check the camera

1. Configure [Linux permissions](./quick-start.html#linux-access) and connect the camera.
2. Close the desktop app, browser preview, and other capture programs.
3. Enumerate devices and check the listed serial and image profiles:

```bash
./build/core/msd-enumerate
```

Enumeration may exit normally even when it finds no devices. Check the reported device count. The example captures the first device. Applications using multiple cameras should select by serial.

## Capture a synchronized image set

```bash
./build/core/msd-capture --mode depth --frames 10 --output ./demo-depth
```

The example waits for **10 complete frame sets and saves only the last set**. It does not save ten sets of files. The new output folder should contain three nonempty files sharing one frame-set ID:

```text
demo-depth/
├── depth_<frame_set_id>.pgm
├── left_ir_<frame_set_id>.jpg
└── right_ir_<frame_set_id>.jpg
```

The JPEG files can be opened directly. The PGM contains 16-bit millimetre depth values, with zero for invalid depth. PGM stores samples in big-endian order, while the SDK's in-memory Depth16 data is little-endian. Account for this if you parse it yourself.

To capture device-generated pseudocolor instead:

```bash
./build/core/msd-capture --mode pseudo --frames 10 --output ./demo-pseudo
```

The first file becomes `pseudo_<frame_set_id>.jpg` and contains no metric depth. Both modes also capture left and right infrared. If a complete synchronized set is unavailable, the example fails rather than combining mismatched images.

Exit codes:

| Code | Meaning |
| :--- | :--- |
| `0` | Success |
| `1` | Capture, synchronization, or file-write failure |
| `2` | Invalid arguments or no compatible device |

For a timeout, check permissions, SDK/firmware compatibility, and competing capture programs.

## Use the SDK in your program

Start with `examples/capture.cpp` and the public header `include/maixsense_d640/sdk.h`. Use `msd_pipeline_wait_for_frame_set()` when you need matching depth and stereo images. Do not pair images by arrival order or by guessing from timestamps.

The SDK generates point clouds on the computer using depth and the corresponding calibration. See `examples/README.zh-CN.md` and `ros2/README.zh-CN.md` in the SDK for optional viewers and ROS2 integration. Some examples are not built when optional dependencies are missing.

## Next steps

- Measure, save images, and record without programming: [Desktop App Guide](./gui.md).
- Understand depth measurement conditions: [Measurement Accuracy](./accuracy.md).
- Resolve connection or synchronization problems: [FAQ](./faq.md).
