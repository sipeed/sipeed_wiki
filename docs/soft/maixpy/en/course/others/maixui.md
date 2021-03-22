---
title: MaixUI basic usage guide
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: MaixUI basic usage guide
---


How to consume MaixUI items correctly?

## Why develop it? What is its meaning and existence value?

There is always a basic requirement for the UI framework under any chip, but because the K210 cannot continue to use the LVGL environment while supporting the Ai function, the UI loses its original meaning.

That is, when you can't use QT or LVGL, you want to be able to use Python to write UI applications, so the image-based MaixUI UI framework was born.

## Requirements for MaixUI

Based on the latest MaixPy firmware, the following requirements will be met on October 7, 2020.

- Ensure that MicroPython's GC memory is recyclable and controllable at all times.

- Ensure that the UI component code is independent, not included in the firmware, and can be debugged and modified.

- Ensure system stability, ensure that code and hardware resources can be re-entered, and no core dump phenomenon will occur.

- Run reentrant, which means running dynamic code to show UI style, similar to HTML5 / CSS design.

- Python's exception capture is fed back to the screen in real time to quickly locate the error line.

- UI-related drawing functions can be used in multiple decorations or run independently.

- All MicroPython hardware drivers provided by the framework can independently run corresponding unit tests.

- When the framework is running, it allows dynamic loading of external UI applications that conform to the structure, and user-defined applications can be obtained from storage or network.

So in the most basic example, it will strictly control the memory usage to 512k ~ 1M and keep the drawing performance between 15 ~ 24fps.

## How to eat?

Here, let’s start with the simplest entry code, the complete code is here [app_main.py](https://github.com/sipeed/MaixUI/blob/master/app/app_main.py).

```python
# This file is part of MaixUI
# Copyright (c) sipeed.com
#
# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license.php
#

import time, gc, math, sys

try:
  from core import agent, system
  from dialog import draw_dialog_alpha
  from ui_canvas import ui, print_mem_free
  from ui_container import container
  from wdt import protect
  from creater import get_time_curve
except ImportError as e:
  sys.print_exception(e)
  from lib.core import agent, system
  from lib.dialog import draw_dialog_alpha
  from ui.ui_canvas import ui, print_mem_free
  from ui.ui_container import container
  from driver.wdt import protect
  from lib.creater import get_time_curve

```

They are the dependent code of import required to run it, and the following dependencies are:

- from core import agent, system
  - Provide an agent soft timer and a global instance system soft timer object.
- from dialog import draw_dialog_alpha
  - Provides drawing operations for a rounded border MessageBox control.
- from ui_canvas import ui, print_mem_free
  - Provides a basic interface of UI canvas, through which to manage the overall unified drawing operation.
- from ui_container import container
  - Provides a container module for running UI applications, which can be used to switch between different UI applications.
- from wdt import protect
  - Watchdog, to ensure that the system can restart and recover after a core dump occurs.
- from creater import get_time_curve
  - A curve generation function based on time or counter to maintain non-linear animation effects.

These two pieces of code are used to import the code loaded into different areas (under the root directory or folder of Flash/SD), so you only need to know how to import the code.

- You can use MaixPy IDE to send files, or use [mpfshell-lite](https://github.com/junhuanchen/mpfshell-lite) to put files to the flash or sd of the hardware.
- You can use an SD card reader, put the entire folder under the maixui warehouse into the SD card and start it.

### Define UI application

Then introduce a typical basic application case, prepare the following code (class launcher static class).

```python

class launcher:

  def load():
    __class__.ctrl = agent()
    __class__.ctrl.event(20, __class__.draw)

  def free():
    __class__.ctrl = None

  @ui.warp_template(ui.blank_draw)
  @ui.warp_template(ui.grey_draw)
  @ui.warp_template(ui.bg_in_draw)
  @ui.warp_template(ui.anime_in_draw)
  @ui.warp_template(ui.help_in_draw)
  #@ui.warp_template(taskbar.time_draw)
  #@ui.warp_template(taskbar.mem_draw)
  #@catch # need sipeed_button
  def draw():
    height = 100 + int(get_time_curve(3, 250) * 60)
    pos = draw_dialog_alpha(ui.canvas, 20, height, 200, 20, 10, color=(255, 0, 0), alpha=200)
    ui.canvas.draw_string(pos[0] + 10, pos[1] + 10, "Welcome to MaixUI", scale=2, color=(0,0,0))
    ui.display()

  def event():
    __class__.ctrl.cycle()

```

Here, __class__ is similar to the this pointer in the instance class, through which the global variables of the current class can be accessed.

The static class has three life cycle functions of load / free / event to provide to the UI container to maintain the continuous operation of the UI application.

- load will only be executed once and is used to initialize the UI application.
- free will only be executed once, for the release of UI applications.
- The event will be provided to the UI container to perform its operations in a loop.
  - UI container refers to [ui/ui_container.py](https://github.com/sipeed/MaixUI/tree/master/ui/ui_container.py).
  - Of course, you can also keep running without the UI container.

You can see that the UI application defines the agent soft timer and sets the expected execution cycle of the drawing function to 20ms when it is loaded, and the setting will not be lower than the actual running cycle.

```python
    __class__.ctrl = agent()
    __class__.ctrl.event(20, __class__.draw)
```

Then maintain the time-sharing event (non-blocking no-block) owned by the soft timer ctrl in the event function, so based on this design you can make many time-sharing tasks with different timings.

```python
    __class__.ctrl.cycle()
```

It can be executed periodically, or it can be used up and deleted, as shown below.

```python
    self.ctrl = agent()
    # loop
    self.ctrl.event(5, self.draw)
    # once
    def into_launcher(self):
      container.reload(launcher)
      self.remove(into_launcher)
    self.ctrl.event(2000, into_launcher)
```

Then we see specific UI drawing events, which are different from hardware-driven events such as buttons/touches, but no matter what kind of events, we expect it to end as soon as possible and hand over to the core of operation.

```python
  @ui.warp_template(ui.blank_draw)
  @ui.warp_template(ui.grey_draw)
  @ui.warp_template(ui.bg_in_draw)
  @ui.warp_template(ui.anime_in_draw)
  @ui.warp_template(ui.help_in_draw)
  #@ui.warp_template(taskbar.time_draw)
  #@ui.warp_template(taskbar.mem_draw)
  #@catch # need sipeed_button
  def draw():
    height = 100 + int(get_time_curve(3, 250) * 60)
    pos = draw_dialog_alpha(ui.canvas, 20, height, 200, 20, 10, color=(255, 0, 0), alpha=200)
    ui.canvas.draw_string(pos[0] + 10, pos[1] + 10, "Welcome to MaixUI", scale=2, color=(0,0,0))
    ui.display()
```

Here, we have one of the most basic draw() drawing functions, and five basic functions are decorated for it. In fact, the decoration is just good-looking, it is actually equivalent to the following code, so whether to use it depends on your preference.
```python
  def draw():
    ui.blank_draw() # prepare a blank image canvas object
    ui.grey_draw() # Draw gray on the canvas
    ui.bg_in_draw() # Draw a sipeed logo on the canvas with a built-in background image.
    ui.anime_in_draw() # Load the animation effect of surrounding water waves on the canvas
    ui.help_in_draw() # Draw the built-in help instructions on the canvas.

    height = 100 + int(get_time_curve(3, 250) * 60) # Get time-based sine curve value
    # Draw the effect of the MessageBox with a rounded border at the specified position, and get the starting point of the upper left corner of the border.
    pos = draw_dialog_alpha(ui.canvas, 20, height, 200, 20, 10, color=(255, 0, 0), alpha=200)
    # Print the string "Welcome to MaixUI" at the specified location.
    ui.canvas.draw_string(pos[0] + 10, pos[1] + 10, "Welcome to MaixUI", scale=2, color=(0,0,0))
    # Display the current canvas on the screen, and multiple executions will not affect it. After execution, the current canvas object will be released.
    ui.display()
```

The same is true for events connected to other buttons/touches/cameras. You can view the specific implementation of UI drawing here [ui/ui_canvas.py](https://github.com/sipeed/MaixUI/tree/master/ui/ui_canvas. py).

### Run UI framework

Before actually entering the above business logic, we need to run the UI framework, so we need an entry function, such as the code in `if __name__ == "__main__":`.

```python

if __name__ == "__main__":
  container.reload(launcher)
  while True:
    container.forever()

```

To explain, we see that the UI container (container.reload(launcher)) is used to load a UI application named launcher to run. You can view the specific implementation of the UI container here [ui/ui_container.py](https:// github.com/sipeed/MaixUI/tree/master/ui/ui_container.py).

But just writing in this way is not stable enough, so we can use two while True to keep the program never exiting (unless the system core dump crashes).

And the current fps value is obtained by the difference between last and the current tick_ms. It is recommended to close the print function in non-debugging situations. It is very time-consuming (ms level).

```python
  while True:
    while True:
      last = time.ticks_ms()-1
      while True:
        try:
          #time.sleep(0.1)
          print(1000 // (time.ticks_ms()-last),'fps')
          last = time.ticks_ms()
        except Exception as e:
          gc.collect()
          print(e)
        finally:
          try:
            ui.display()
          except:
            pass

```

Then we strengthen the stability of the environment, adding watchdog maintenance (protect.keep()) and GC memory collection (gc.collect()), and maintaining a global soft timer (system.parallel_cycle()) , Used as a global timer thread.

```python

if __name__ == "__main__":
  container.reload(launcher)
  while True:
    while True:
      last = time.ticks_ms()-1
      while True:
        try:
          #time.sleep(0.1)
          print(1000 // (time.ticks_ms()-last),'fps')
          last = time.ticks_ms()

          gc.collect()
          container.forever()
          system.parallel_cycle()

          protect.keep()
          #gc.collect()
          #print_mem_free()
        except KeyboardInterrupt:
          protect.stop()
          raise KeyboardInterrupt
        #except Exception as e:
          #gc.collect()
          #print(e)
        finally:
          try:
            ui.display()
          except:
            pass

```

- You can use time.sleep(0.1) to reduce the execution rate of the UI container to observe whether the change state of the UI is in line with expectations. Sometimes changes higher than 15 fps are not perceived by the human eye, which can reduce unnecessary drawing processes. Compress the drawing process to improve performance.
- You can use except Exception as e: to ensure that any exception will not cause the UI framework to crash, but you can comment this out to catch possible exceptions when debugging.

> By default, if the program does not execute protect.keep() for more than 10 seconds to reset the watchdog, the system will automatically restart. This starts when the wdt driver is imported. For details, please see [driver/wdt.py](https ://github.com/sipeed/MaixUI/tree/master/driver/wdt.py) driver.

Finally, add catching KeyboardInterrupt exception events to ensure that the program can be stopped and re-run after IDE or Ctrl + C input, and stop the watchdog event (protect.stop()), and also try to execute in finally ui.display() prevents the canvas from being released due to an exception in the drawing event and ensures that the image canvas object can always be released at the end of the loop.

```python
  try:
    protect.keep()
  except KeyboardInterrupt:
    protect.stop()
    raise KeyboardInterrupt
  except Exception as e:
    gc.collect()
    print(e)
  finally:
    try:
      ui.display()
    except:
      pass
```

The above is the most basic demonstration of the MaixUI framework. Although MaixUI will only provide Cube and Amigo application cases, it can be used as long as it is based on MaixPy, or in other words, the MicroPython environment that supports image interface objects can be used.

I hope that we will be able to synchronize to CPython in the future, that is, we can synchronize UI-style development on CPython to the MicroPython environment. This will complete the development efficiently, but the performance will not drop.

### At last

This document describes how to run the most basic examples. If you want to see more examples, you can refer to [app_cube.py](https://github.com/sipeed/MaixUI/tree/master/app/app_cube.py) & [app_amigo .py](https://github.com/sipeed/MaixUI/tree/master/app/app_amigo.py) Two cases.

> As of now on October 7, 2020, the App case for MaixPy's common functions has been completed, but this requires you to personally write and experience XD. The description only has a little simple interaction and animation display.

The current running effect of app_main.py is as follows:

![](./image/app_main.gif)
