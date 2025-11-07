---
title: DIY应用
keywords: NanoKVM, Desk, Auxiliary Screen, DIY
update:
  - date: 2025-11-07
    version: v1.0
    author: bugu
    content:
      - initial docs
---

NanoKVM-Desk是Sipeed推出的IPKVM产品，拥有AX630为核心（双核A53@1.2GHz，内置3.2Tops NPU@INT8）配置了1G LPDDR4内存和32GeMMC，同时支持TF卡扩展，并有可选的wifi、POE配置，除了强大的远程控制功能外，其拥有一块1.47寸触摸显示屏和旋钮，作为桌面摆件的形态有无限的DIY想象空间。

在`1.2.1`版本中，我们新增了**APP Hub**功能。通过该功能，您可以便捷下载[开源应用仓库](https://github.com/sipeed/NanoKVM-UserApps)中的所有应用。

如果您有好的创意，也欢迎基于下方文档构建属于自己的应用并提交至开源仓库。我们会对提交的应用进行基础功能审核，一经通过，您开发的应用将可供所有NanoKVM-Desk用户下载使用！

## 如何构建你自己的应用

> 你可以将此文档发送给AI，来辅助生成你自己的应用！

### 项目文件夹的介绍

NanoKVM-Desk UserAPP会扫描 `/userapp` 目录下所有的文件夹，每一个文件夹就是一个APP，文件夹名称就是APP名称。文件夹内至少包含 `main.py` 和 `app.toml`。

`main.py` 是运行的代码，`app.toml` 是配置文件，其内容如下：

```toml
[application]
name = "XXX"                        # 使用文件夹名，启动时显示(必须且与目录名一致)
version = "1.0.0"                   # 用作版本升级，启动时显示(必须为SemVer格式子集 MAJOR.MINOR.PATCH)
descriptions = "Example"            # 用作App简短描述，在下载更新时显示(必须，用于用户快速了解app功能)

[author]
name = "Sipeed-xxx"                 # 填写作者名称，启动时显示(必须)
email = "xxx@sipeed.com"            # 方便用户联系作者(可选)

[interaction]
requires_user_input = false         # 是否需要开放触摸屏以及旋钮事件；若为true，要求程序内必须有主动退出机制(可选)
```

### 屏幕基础信息和使用方法

NanoKVM-Desk的屏幕分辨率为320*172，通过 `/dev/fb0` 访问。设备配备了一个172x320像素的RGB565彩色显示屏，可通过帧缓冲设备 `/dev/fb0` 访问。应用程序可以直接绘制到该显示设备上。

#### 显示特性
- **分辨率**: 172x320 像素（但逻辑屏幕是 320x172 - 见下面的旋转说明）
- **颜色深度**: 16 位 RGB565 格式 (红色 5 位，绿色 6 位，蓝色 5 位)
- **帧缓冲设备**: `/dev/fb0`
- **显示方向**: 物理显示屏为纵向模式，但应用程序通常创建横向图像 (320x172) 并逆时针旋转 90 度以供显示。

#### 基本显示用法

在 Python 应用程序中使用显示设备：

1. **设置物理显示尺寸的常量**:
   ```python
   PHYSICAL_WIDTH = 172
   PHYSICAL_HEIGHT = 320
   BPP = 16  # 每像素位数
   ```

2. **创建与帧缓冲区接口的显示类**:
   ```python
   import mmap
   import os
   import numpy as np
   from PIL import Image, ImageDraw

   class RGB565Display:
       def __init__(self, fb_device="/dev/fb0"):
           self.physical_width = PHYSICAL_WIDTH
           self.physical_height = PHYSICAL_HEIGHT
           self.bpp = BPP
           self.fb_size = self.physical_width * self.physical_height * (self.bpp // 8)

           # 打开帧缓冲设备
           self.fb_fd = os.open(fb_device, os.O_RDWR)
           self.fb_mmap = mmap.mmap(
               self.fb_fd, self.fb_size, mmap.MAP_SHARED, mmap.PROT_WRITE
           )
           self.fb_array = np.frombuffer(self.fb_mmap, dtype=np.uint16).reshape(
               (self.physical_height, self.physical_width)
           )

       def rgb_to_rgb565(self, r, g, b):
           """将 8 位 RGB 转换为 RGB565 格式"""
           return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)

       def clear_screen(self, color=0x0000):
           """使用指定颜色清屏"""
           self.fb_array.fill(color)

       def _display_image(self, logical_img):
           """旋转逻辑图像并在物理屏幕上显示"""
           # 将逻辑图像逆时针旋转 90 度以获得物理图像
           physical_img = logical_img.rotate(90, expand=True)

           # 转换为 RGB565 并复制到帧缓冲区
           rgb_array = np.array(physical_img)
           r = (rgb_array[:, :, 0] >> 3).astype(np.uint16)
           g = (rgb_array[:, :, 1] >> 2).astype(np.uint16)
           b = (rgb_array[:, :, 2] >> 3).astype(np.uint16)
           rgb565 = (r << 11) | (g << 5) | b

           # 直接复制整个数组到帧缓冲区
           self.fb_array[:, :] = rgb565

       def close(self):
           """关闭资源"""
           self.fb_mmap.close()
           os.close(self.fb_fd)
   ```

3. **在显示上绘制内容**:
   ```python
   def main():
       display = RGB565Display()
       
       try:
           # 创建逻辑横向图像 (320x172)
           logical_img = Image.new("RGB", (320, 172), (0, 0, 0))
           draw = ImageDraw.Draw(logical_img)

           # 绘制内容 (例如，矩形、文字)
           draw.rectangle([10, 10, 100, 100], fill=(255, 0, 0))  # 红色矩形
           
           # 显示图像
           display._display_image(logical_img)
           
           # 等待一段时间
           import time
           time.sleep(5)
           
       finally:
           display.close()

   if __name__ == "__main__":
       main()
   ```

#### 显示用法的最佳实践
- 始终将逻辑横向图像 (320x172) 逆时针旋转以匹配物理纵向显示 (172x320)
- 尽可能使用高效的绘图方法以减少渲染时间
- 在 `finally` 块或上下文管理器中正确关闭资源，以防止资源泄漏
- 在绘制频繁更新的内容时考虑性能 (例如，动画)

### 输入事件基础信息和使用方法

NanoKVM-Desk有旋钮旋转，按下和触摸三种输入事件。

> 如果要使用输入事件时，需要在 `app.toml` 中声明 `requires_user_input = true`，同时在你的程序中必须有明确的主动退出机制，否则无法退出至NanoKVM-UI；
> 若你的程序不需要触摸或旋钮的输入事件，配置字段 `requires_user_input = false` 或不写，NanoKVM-UI将会在点击屏幕或按下按钮后退出程序。

#### 输入设备位置

- **旋钮旋转事件**: `/dev/input/event0`
  ```shell
  root@kvm-72d6:~# evtest /dev/input/event0
  Input driver version is 1.0.1
  Input device ID: bus 0x19 vendor 0x0 product 0x0 version 0x0
  Input device name: "rotary@0"
  Supported events:
    Event type 0 (EV_SYN)
    Event type 2 (EV_REL)
      Event code 0 (REL_X)
  Properties:
  Testing ... (interrupt to exit)
  Event: time 1762504082.820148, type 2 (EV_REL), code 0 (REL_X), value 1
  Event: time 1762504082.820148, -------------- SYN_REPORT ------------
  Event: time 1762504082.861754, type 2 (EV_REL), code 0 (REL_X), value 1
  Event: time 1762504082.861754, -------------- SYN_REPORT ------------
  Event: time 1762504084.692300, type 2 (EV_REL), code 0 (REL_X), value -1
  Event: time 1762504084.692300, -------------- SYN_REPORT ------------
  Event: time 1762504084.714448, type 2 (EV_REL), code 0 (REL_X), value -1
  Event: time 1762504084.714448, -------------- SYN_REPORT ------------
  ```

- **旋钮按下、保持、抬起事件**: `/dev/input/event1`
  ```shell
  root@kvm-72d6:~# evtest /dev/input/event1
  Input driver version is 1.0.1
  Input device ID: bus 0x19 vendor 0x1 product 0x1 version 0x100
  Input device name: "gpio_keys"
  Supported events:
    Event type 0 (EV_SYN)
    Event type 1 (EV_KEY)
      Event code 28 (KEY_ENTER)
  Key repeat handling:
    Repeat type 20 (EV_REP)
      Repeat code 0 (REP_DELAY)
        Value    250
      Repeat code 1 (REP_PERIOD)
        Value     33
  Properties:
  Testing ... (interrupt to exit)
  Event: time 1762504201.120498, type 1 (EV_KEY), code 28 (KEY_ENTER), value 1
  Event: time 1762504201.120498, -------------- SYN_REPORT ------------
  Event: time 1762504201.371193, type 1 (EV_KEY), code 28 (KEY_ENTER), value 2
  Event: time 1762504201.721202, -------------- SYN_REPORT ------------
  Event: time 1762504201.724694, type 1 (EV_KEY), code 28 (KEY_ENTER), value 0
  Event: time 1762504201.724694, -------------- SYN_REPORT ------------
  ```

- **触摸屏事件**: `/dev/input/event2`
  ```shell
  root@kvm-72d6:~# evtest /dev/input/event2
  Input driver version is 1.0.1
  Input device ID: bus 0x18 vendor 0x0 product 0x0 version 0x0
  Input device name: "hyn_ts"
  Supported events:
    Event type 0 (EV_SYN)
    Event type 1 (EV_KEY)
      Event code 325 (BTN_TOOL_FINGER)
      Event code 330 (BTN_TOUCH)
    Event type 3 (EV_ABS)
      Event code 47 (ABS_MT_SLOT)
        Value      0
        Min        0
        Max        5
      Event code 48 (ABS_MT_TOUCH_MAJOR)
        Value      0
        Min        0
        Max      255
      Event code 50 (ABS_MT_WIDTH_MAJOR)
        Value      0
        Min        0
        Max      200
      Event code 53 (ABS_MT_POSITION_X)
        Value      0
        Min        0
        Max      172
      Event code 54 (ABS_MT_POSITION_Y)
        Value      0
        Min        0
        Max      320
      Event code 57 (ABS_MT_TRACKING_ID)
        Value      0
        Min        0
        Max        5
      Event code 58 (ABS_MT_PRESSURE)
        Value      0
        Min        0
        Max      255
  Properties:
    Property type 1 (INPUT_PROP_DIRECT)
  Testing ... (interrupt to exit)
  Event: time 1762504306.703328, type 1 (EV_KEY), code 330 (BTN_TOUCH), value 1
  Event: time 1762504306.703328, type 3 (EV_ABS), code 57 (ABS_MT_TRACKING_ID), value 25
  Event: time 1762504306.703328, type 3 (EV_ABS), code 57 (ABS_MT_TRACKING_ID), value 0
  Event: time 1762504306.703328, type 3 (EV_ABS), code 53 (ABS_MT_POSITION_X), value 71
  Event: time 1762504306.703328, type 3 (EV_ABS), code 54 (ABS_MT_POSITION_Y), value 165
  Event: time 1762504306.703328, type 3 (EV_ABS), code 48 (ABS_MT_TOUCH_MAJOR), value 1
  Event: time 1762504306.703328, type 3 (EV_ABS), code 50 (ABS_MT_WIDTH_MAJOR), value 1
  Event: time 1762504306.703328, type 3 (EV_ABS), code 58 (ABS_MT_PRESSURE), value 10
  Event: time 1762504306.703328, -------------- SYN_REPORT ------------
  Event: time 1762504306.749866, type 3 (EV_ABS), code 57 (ABS_MT_TRACKING_ID), value -1
  Event: time 1762504306.749866, type 1 (EV_KEY), code 330 (BTN_TOUCH), value 0
  Event: time 1762504306.749866, -------------- SYN_REPORT ------------
  ```

### 示例

[开源仓库的apps目录下](https://github.com/sipeed/NanoKVM-UserApps/tree/main/apps) 的两个示例，可能帮你更好的构建自己的应用：
- [hello](https://github.com/sipeed/NanoKVM-UserApps/tree/main/apps/hello): 基本显示功能
- [drawo](https://github.com/sipeed/NanoKVM-UserApps/tree/main/apps/drawo): 带有触摸屏支持的绘图应用程序

## 贡献到软件源

我们鼓励创建并上传自己的应用程序到[仓库](https://github.com/sipeed/NanoKVM-UserApps)！这作为 NanoKVM-Desk 的软件源，您的贡献使我们的生态系统更加丰富。

### 如何上传您的应用程序

1. 创建一个 pull request，将您的应用程序放入 `apps` 文件夹
2. 您的应用程序将经过简单的审核流程（作为开源社区，我们只审核基本功能；安全性由开发者保证）
3. 一经批准，您的应用程序将在 NanoKVM-Desk APP Hub 中提供

### 如何上报UserAPP的问题

请在[开源仓库](https://github.com/sipeed/NanoKVM-UserApps)的issus下报告问题，并@对应app下app.toml的作者
