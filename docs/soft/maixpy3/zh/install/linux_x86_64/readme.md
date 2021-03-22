---
title: linux_x86_64
keywords: MaixPy, MaixPy3, Python, Python3, MicroPython
desc: maixpy doc: linux_x86_64 如何安装？
---

> 2021年02月21日 在 ubuntu20 与 manjaro20 上测试通过。

通过 `pip3 install maixpy3` 安装。

```bash
juwan@juwan-N85-N870HL:~/Desktop/v831_toolchain_linux_x86/MaixPy3$ pip3 install .Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Processing /home/juwan/Desktop/v831_toolchain_linux_x86/MaixPy3
Requirement already satisfied: Pillow in /usr/lib/python3/dist-packages (from MaixPy3==0.2.9) (7.0.0)
Requirement already satisfied: evdev in /home/juwan/.local/lib/python3.8/site-packages (from MaixPy3==0.2.9) (1.4.0)
Requirement already satisfied: gpiod in /home/juwan/.local/lib/python3.8/site-packages (from MaixPy3==0.2.9) (1.4.0)
Requirement already satisfied: numpy in /home/juwan/.local/lib/python3.8/site-packages (from MaixPy3==0.2.9) (1.19.4)
Requirement already satisfied: opencv-python in /home/juwan/.local/lib/python3.8/site-packages (from MaixPy3==0.2.9) (4.5.1.48)
Requirement already satisfied: pyserial in /usr/local/lib/python3.8/dist-packages (from MaixPy3==0.2.9) (3.4)
Requirement already satisfied: rpyc in /home/juwan/.local/lib/python3.8/site-packages (from MaixPy3==0.2.9) (5.0.1)
Requirement already satisfied: spidev in /home/juwan/.local/lib/python3.8/site-packages (from MaixPy3==0.2.9) (3.5)
Requirement already satisfied: plumbum in /home/juwan/.local/lib/python3.8/site-packages (from rpyc->MaixPy3==0.2.9) (1.6.9)
Building wheels for collected packages: MaixPy3
  Building wheel for MaixPy3 (setup.py) ... done
  Created wheel for MaixPy3: filename=MaixPy3-0.2.9-cp38-cp38-linux_x86_64.whl size=115611 sha256=54f70f181ccc629f1eaf470bf30eccd20389c6333814d7145e16a31db7f6cdcd
  Stored in directory: /tmp/pip-ephem-wheel-cache-9bf1q3wt/wheels/53/7d/47/6cd374fab930089f96a0a3185f5677e52a9b71dbbee769935d
Successfully built MaixPy3
Installing collected packages: MaixPy3
  Attempting uninstall: MaixPy3
    Found existing installation: MaixPy3 0.2.8
    Uninstalling MaixPy3-0.2.8:
      Successfully uninstalled MaixPy3-0.2.8
Successfully installed MaixPy3-0.2.9
```

现在你安装好后，可以在 python3 中复制粘贴如下代码运行。

```python
from maix import display, camera
display.show(camera.capture())
```

现在你可以看到系统唤起了图像浏览器显示的摄像头捕获的图像。

![./asserts/dalaoshu.png](./asserts/dalaoshu.png)

> 它借助了 opencv-python 和 PIL 的接口功能实现的。

## 想要图像推流？

请查阅左侧【常用开发工具】> [pyqt_rtsp](../../tools/pyqt_rtsp.md) 的使用方法。

## 关于 AI 功能

2021年02月21日 由于在 PC 机上有很多选择，还未确定要接入的 AI 框架。

## 关于其他用法？

还未想到有哪些什么用法是需要在 PC 机上特别说明的。

欢迎提供你的想法！

## 想知道更多？请往左侧目录的【一些使用案例】上前进吧！
