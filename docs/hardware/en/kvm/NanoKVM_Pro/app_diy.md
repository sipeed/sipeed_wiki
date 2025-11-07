---
title: DIY Applications
keywords: NanoKVM, Desk, Auxiliary Screen, DIY
update:
  - date: 2025-11-07
    version: v1.0
    author: bugu
    content:
      - initial docs
---

NanoKVM-Desk is an IPKVM product launched by Sipeed, featuring an AX630 core (dual-core A53@1.2GHz, with a built-in 3.2Tops NPU@INT8), configured with 1G LPDDR4 memory and 32G eMMC storage, while also supporting TF card expansion. It offers optional wifi and POE configurations. Beyond its powerful remote control capabilities, it includes a 1.47-inch touch display and a rotary knob. Its form factor as a desktop accessory offers limitless possibilities for DIY imagination.

In version `1.2.1`, we introduced the **APP Hub** feature. Through this feature, you can conveniently download all applications from the [Open Source Application Repository](https://github.com/sipeed/NanoKVM-UserApps).

If you have great ideas, you are also welcome to build your own applications based on the documentation below and submit them to the open-source repository. We will conduct a basic functionality review on submitted applications. Once approved, the applications you develop will be available for download and use by all NanoKVM-Desk users!

## How to Build Your Own Application

> You can send this document to an AI to assist in generating your own application!

### Project Folder Introduction

The NanoKVM-Desk UserAPP scans all folders under the `/userapp` directory; each folder represents an APP, and the folder name is the APP name. Each folder must contain at least `main.py` and `app.toml`.

`main.py` is the code that runs, and `app.toml` is the configuration file with the following content:

```toml
[application]
name = "XXX"                        # Use the folder name, displayed on startup (must match the directory name)
version = "1.0.0"                   # Used for version upgrades, displayed on startup (must be a subset of SemVer format MAJOR.MINOR.PATCH)
descriptions = "Example"            # Used as a brief description of the App, displayed during download/update (required, helps users quickly understand the app's functionality)

[author]
name = "Sipeed-xxx"                 # Fill in the author's name, displayed on startup (required)
email = "xxx@sipeed.com"            # Allows users to contact the author easily (optional)

[interaction]
requires_user_input = false         # Whether touchscreen and rotary knob events need to be enabled; if true, the program must have an active exit mechanism (optional)
```

### Screen Basic Information and Usage

The NanoKVM-Desk screen resolution is 320*172, accessed via `/dev/fb0`. The device is equipped with a 172x320 pixel RGB565 color display, accessible via the framebuffer device `/dev/fb0`. Applications can draw directly to this display device.

#### Display Characteristics
- **Resolution**: 172x320 pixels (but the logical screen is 320x172 - see rotation note below)
- **Color Depth**: 16-bit RGB565 format (Red 5 bits, Green 6 bits, Blue 5 bits)
- **Framebuffer Device**: `/dev/fb0`
- **Display Orientation**: The physical display is in portrait mode, but applications typically create a landscape image (320x172) which is rotated 90 degrees counter-clockwise for display.

#### Basic Display Usage

Using the display device in Python applications:

1. **Set constants for the physical display dimensions**:
   ```python
   PHYSICAL_WIDTH = 172
   PHYSICAL_HEIGHT = 320
   BPP = 16  # Bits per pixel
   ```

2. **Create a display class interfacing with the framebuffer**:
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

           # Open the framebuffer device
           self.fb_fd = os.open(fb_device, os.O_RDWR)
           self.fb_mmap = mmap.mmap(
               self.fb_fd, self.fb_size, mmap.MAP_SHARED, mmap.PROT_WRITE
           )
           self.fb_array = np.frombuffer(self.fb_mmap, dtype=np.uint16).reshape(
               (self.physical_height, self.physical_width)
           )

       def rgb_to_rgb565(self, r, g, b):
           """Convert 8-bit RGB to RGB565 format"""
           return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)

       def clear_screen(self, color=0x0000):
           """Clear the screen with the specified color"""
           self.fb_array.fill(color)

       def _display_image(self, logical_img):
           """Rotate the logical image and display it on the physical screen"""
           # Rotate the logical image 90 degrees counter-clockwise to get the physical image
           physical_img = logical_img.rotate(90, expand=True)

           # Convert to RGB565 and copy to the framebuffer
           rgb_array = np.array(physical_img)
           r = (rgb_array[:, :, 0] >> 3).astype(np.uint16)
           g = (rgb_array[:, :, 1] >> 2).astype(np.uint16)
           b = (rgb_array[:, :, 2] >> 3).astype(np.uint16)
           rgb565 = (r << 11) | (g << 5) | b

           # Copy the entire array directly to the framebuffer
           self.fb_array[:, :] = rgb565

       def close(self):
           """Close resources"""
           self.fb_mmap.close()
           os.close(self.fb_fd)
   ```

3. **Draw content on the display**:
   ```python
   def main():
       display = RGB565Display()
       
       try:
           # Create a logical landscape image (320x172)
           logical_img = Image.new("RGB", (320, 172), (0, 0, 0))
           draw = ImageDraw.Draw(logical_img)

           # Draw content (e.g., rectangle, text)
           draw.rectangle([10, 10, 100, 100], fill=(255, 0, 0))  # Red rectangle
           
           # Display the image
           display._display_image(logical_img)
           
           # Wait for some time
           import time
           time.sleep(5)
           
       finally:
           display.close()

   if __name__ == "__main__":
       main()
   ```

#### Best Practices for Display Usage
- Always rotate your logical landscape image (320x172) counter-clockwise to match the physical portrait display (172x320)
- Use efficient drawing methods whenever possible to reduce rendering time
- Properly close resources in a `finally` block or context manager to prevent resource leaks
- Consider performance when drawing frequently updated content (e.g., animations)

### Input Event Basics and Usage

The NanoKVM-Desk has three types of input events: knob rotation, knob press, and touch.

> If you want to use input events, you must declare `requires_user_input = true` in `app.toml`, and your program must have a clear, active exit mechanism; otherwise, it cannot exit back to NanoKVM-UI.
> If your program does not require touch or knob input events, set the configuration field `requires_user_input = false` or omit it. NanoKVM-UI will then exit the program when the screen is touched or the button is pressed.

#### Input Device Locations

- **Knob Rotation Event**: `/dev/input/event0`
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

- **Knob Press, Hold, Release Events**: `/dev/input/event1`
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

- **Touchscreen Event**: `/dev/input/event2`
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

### Examples

The two examples in the [apps directory of the open-source repository](https://github.com/sipeed/NanoKVM-UserApps/tree/main/apps) might help you better build your own application:
- [hello](https://github.com/sipeed/NanoKVM-UserApps/tree/main/apps/hello): Basic display functionality
- [drawo](https://github.com/sipeed/NanoKVM-UserApps/tree/main/apps/drawo): A drawing application with touchscreen support

## Contributing to the Software Repository

We encourage you to create and upload your own applications to the [repository](https://github.com/sipeed/NanoKVM-UserApps)! This serves as the software repository for NanoKVM-Desk, and your contributions make our ecosystem richer.

### How to Upload Your Application

1. Create a pull request to place your application in the `apps` folder
2. Your application will go through a simple review process (as an open-source community, we only review basic functionality; security is guaranteed by the developer)
3. Once approved, your application will be available in the NanoKVM-Desk APP Hub

### How to Report UserAPP Issues

Please report issues under the [Issues section of the open-source repository](https://github.com/sipeed/NanoKVM-UserApps) and mention (@) the author specified in the `app.toml` file of the corresponding app.