---
title: MaixUI 基础使用指导
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: MaixUI 基础使用指导
---


如何正确的食用 MaixUI 项目？

## 为什么要开发它？它的意义和存在价值是什么？

在任何芯片下永远存在对 UI 框架的基本需求，但由于 K210 无法在支持 Ai 功能的情况下继续使用 LVGL 环境，导致 UI 失去了本来存在的意义。

也就是在不能用 QT 也不能用 LVGL 的时候，又希望能够使用 Python 编写 UI 应用，所以才诞生了基于 image 的 MaixUI UI 框架。

## 对 MaixUI 的要求

在最新 MaixPy 固件的基础上 2020年10月7日 满足如下要求。

- 确保 MicroPython 的 GC 内存在任何时候都是使用可回收可控的。

- 确保 UI 组件代码独立，不包含在固件，可被调试修改。

- 确保系统稳定性，保证代码和硬件资源均可重入，不会出现 core dump 现象。

- 运行可重入，也就运行动态代码展示 UI 样式，类似 HTML5 / CSS 的设计。

- Python 的异常捕获实时反馈到屏幕上，快速定位出错行。

- UI 相关的绘制函数可被多处装饰使用，也可独立运行。

- 框架提供的所有 MicroPython 硬件驱动均可独立运行相应的单元测试。

- 框架运行时允许动态加载外部符合结构的 UI 应用，可以从 storage 或 network 上获取用户自定义应用。

所以在最基础的示例中，它将严格控制内存占用控制在 512k ~ 1M ，并将绘图性能保持 15 ~ 24fps 之间。

## 如何食用？

来，我们从最简单的入口代码开始说起，完整的代码在这里 [app_main.py](https://github.com/sipeed/MaixUI/blob/master/app/app_main.py) 。

```python
# This file is part of MaixUI
# Copyright (c) sipeed.com
#
# Licensed under the MIT license:
#   http://www.opensource.org/licenses/mit-license.php
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

分别是运行它所需要 import 的依赖代码，有如下依赖：

- from core import agent, system
  - 提供一个 agent 软定时器和一个全局实例 system 软定时器对象。
- from dialog import draw_dialog_alpha
  - 提供了一个圆角边框 MessageBox 控件的绘图操作。
- from ui_canvas import ui, print_mem_free
  - 提供了一个 UI 画布的基础接口，通过它来管理全局的统一绘图操作。
- from ui_container import container
  - 提供了一种运行 UI 应用的容器模块，可以通过它切换不同的 UI 应用。
- from wdt import protect
  - 看门狗，保证系统在出现 core dump 后能够重启恢复过来。
- from creater import get_time_curve
  - 一种基于时间或计数器的曲线生成函数，用来维持非线性动画效果。

这两段代码是用来 import 加载到不同区域（在 Flash/SD 的根目录或文件夹下）的代码，所以你知道怎么 import 代码了就行。

- 可以使用 MaixPy IDE 发送文件，也可以使用 [mpfshell-lite](https://github.com/junhuanchen/mpfshell-lite) put 文件到硬件的 flash 或 sd 中。
- 可以使用 SD 读卡器，把整个 maixui 仓库下的文件夹放到 SD 卡中启动即可。

### 定义 UI 应用

接着介绍一种典型的基础应用的案例，准备如下代码（class launcher 静态类）。

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

在这里， __class__ 类似于 实例类 中的 this 指针，可以通过它访问当前类的全局变量。

该静态类拥有有 load / free / event 三个生命周期函数用以提供给 UI 容器维持该 UI 应用的持续运行。

- load 只会执行一次，用于 UI 应用的初始化。
- free 只会执行一次，用于 UI 应用的释放。
- event 将会提供给 UI 容器循环执行其中的操作。
  - UI 容器指的是 [ui/ui_container.py](https://github.com/sipeed/MaixUI/tree/master/ui/ui_container.py) 。
  - 当然你也可以不通过 UI 容器来维持运行。

可以看到该 UI 应用在 load 的时候定义了 agent 软定时器和设置了绘图函数的期望执行周期为 20ms ，设置再小也不会低于真实运行的周期。

```python
    __class__.ctrl = agent()
    __class__.ctrl.event(20, __class__.draw)
```

然后在 event 函数中维持 软定时器 ctrl 拥有的分时事件（非阻塞 no-block），因此基于此设计你可以制作很多个不同定时的分时任务。

```python
    __class__.ctrl.cycle()
```

它可以周期执行，也可以用完删除，就如下示范。

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

接着我们看到具体的 UI 绘图事件，不同于按键/触摸等硬件驱动事件，但无论是哪类事件，我们都期望它能够尽快结束，交出运行核心。

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

在这里，我们有一个最基础的 draw() 绘图函数，也为它装饰了 5 个基础函数，事实上装饰只是好看，它实际上等效于如下代码，所以是否使用取决于你的喜好。

```python
  def draw():
    ui.blank_draw()    # 准备一个空白的 image 画布对象
    ui.grey_draw()     # 给 画布 画上灰色
    ui.bg_in_draw()    # 给 画布 画上内置的 背景图 一个 sipeed 的 logo 。
    ui.anime_in_draw() # 给 画布 加载四周水波动画效果
    ui.help_in_draw()  # 给 画布 画上 内置的 帮助说明。

    height = 100 + int(get_time_curve(3, 250) * 60) # 获取基于时间的正弦曲线值
    # 在指定位置画出 圆角边框的 MessageBox 的效果，并获取边框的 左上角起点 。
    pos = draw_dialog_alpha(ui.canvas, 20, height, 200, 20, 10, color=(255, 0, 0), alpha=200)
    # 在指定位置打印 "Welcome to MaixUI" 字符串。
    ui.canvas.draw_string(pos[0] + 10, pos[1] + 10, "Welcome to MaixUI", scale=2, color=(0,0,0))
    # 把当前的画布显示到屏幕上，多次执行也不影响，执行后会释放当前画布对象。
    ui.display()
```

接入其他按键/触摸/摄像头的事件亦如此，可以在此查看 UI 绘图的具体实现 [ui/ui_canvas.py](https://github.com/sipeed/MaixUI/tree/master/ui/ui_canvas.py)。

### 运行 UI 框架

在真正进入上述的业务逻辑之前，我们需要把 UI 框架跑起来，因此我们需要一个入口函数，如 `if __name__ == "__main__":` 中的代码。

```python

if __name__ == "__main__":
  container.reload(launcher)
  while True:
    container.forever()

```

讲解一下，我们看到使用 UI 容器 （container.reload(launcher)） 加载一个名为 launcher 的 UI 应用即可运行，可以在此查看 UI 容器的具体实现 [ui/ui_container.py](https://github.com/sipeed/MaixUI/tree/master/ui/ui_container.py)。

但仅仅这样写是不够稳定的，所以我们可以通过两个 while True 保持程序永远不会退出（除非系统 core dump 崩溃）。

并通过 last 与 当前 tick_ms 做差得到当前的 fps 值，建议非调试场合建议关闭 print 这个函数，它非常耗时（ms 级）。

```python
  while True:
    while True:
      last = time.ticks_ms() - 1
      while True:
        try:
          #time.sleep(0.1)
          print(1000 // (time.ticks_ms() - last), 'fps')
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

然后我们加强一下环境的稳定性，加入看门狗的维持（protect.keep()）和 GC 内存回收（gc.collect()），还有维持一个全局的软定时器（system.parallel_cycle()），用作全局的定时器线程。

```python

if __name__ == "__main__":
  container.reload(launcher)
  while True:
    while True:
      last = time.ticks_ms() - 1
      while True:
        try:
          #time.sleep(0.1)
          print(1000 // (time.ticks_ms() - last), 'fps')
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

- 你可以通过 time.sleep(0.1) 来降低 UI 容器的执行速率来观察 UI 的变化状态是否符合预期，有时候高于 15 fps 的变化人眼感知不到，就可以减少不必要的绘图过程，压缩绘图过程提高性能。
- 你可以通过 except Exception as e: 来保证任何异常都不会导致 UI 框架的崩溃，但调试的时候可以把这个注释，来捕获可能出现的异常。

> 默认情况下程序超过 10 秒没有执行 protect.keep() 重置看门狗，则系统自动重启，这从 import wdt 驱动的时候就开始计时了，详细可以看 [driver/wdt.py](https://github.com/sipeed/MaixUI/tree/master/driver/wdt.py) 驱动。

最后再加入捕获 KeyboardInterrupt 异常事件来保证程序可以在 IDE 或 Ctrl + C 输入后，停下来并被重新运行，并停下看门狗事件（protect.stop()），同时还要在 finally 中试图执行 ui.display() 防止绘图事件中存在异常导致没有释放画布，保证 image 画布对象永远都能在循环的最后被释放。

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

以上就是 MaixUI 框架最基础的示范，虽然 MaixUI 只会提供 Cube 和 Amigo 的应用案例，但只要基于 MaixPy 均可使用，或者说，支持 image 接口对象的 MicroPython 环境均可使用。

希望我们未来能会同步到 CPython 共用的，也就是可以在 CPython 上进行 UI 样式的开发同步到 MicroPython 环境中，这会高效率的完成开发的，但性能也不能落下。

### 最后

本文档介绍如何运行最基础的示例，如果想看更多示例，可以参考 [app_cube.py](https://github.com/sipeed/MaixUI/tree/master/app/app_cube.py) & [app_amigo.py](https://github.com/sipeed/MaixUI/tree/master/app/app_amigo.py) 两个案例。

> 截至目前 2020年10月7日 已经完成 MaixPy 的常见功能使用的 App 案例，不过这需要你亲自烧写一下体验看看了 XD ， 说明里只有一点简单的交互与动画展示。

目前 app_main.py 运行效果如下：

![](./image/app_main.gif)
