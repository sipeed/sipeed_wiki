---
title: 安装 MaixPy3
keywords: linux, MaixII-Dock, MaixSense, 安装MaixPy3
desc: maixpy doc: linux_x86_64 如何安装？
---

## 可适配平台

目前 MaixPy3 所能兼容的平台有 [MaixII-Dock](/hardware/zh/maixII/M2/introduce.html)、[MaixSense](/hardware/zh/maixII/M2A/R329.html)、Linux，后续会推出更加多可适配的平台



### MaixII-Dock 上安装 MaixPy3

在 MaixII-Dock 的最新[镜像](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/release)中是已已经将 MaixPy3 安装好，烧录即可使用。不一定是最新版本的 MaixPy3，需要手动[更新 MaixPy3](/hardware/zh/maixII/M2/tools/0.MaixII-Dock.html#%E6%9B%B4%E6%96%B0-MaixPy3).

也可以在[连接网络](/hardware/zh/maixII/M2/tools/0.MaixII-Dock.html#%E8%BF%9E%E6%8E%A5%E7%BD%91%E7%BB%9C)之后进行更新，通过 `pip install maixpy3` 进行安装，或者通过 `pip install -U Maixpy3` 进行更新

```shell
root@sipeed:/# pip install maixpy3 -U
Requirement already up-to-date: maixpy3 in /usr/lib/python3.8/site-packages (0.3.5)
Requirement already satisfied, skipping upgrade: Pillow in /usr/lib/python3.8/site-packages (from maixpy3) (7.2.0)
Requirement already satisfied, skipping upgrade: evdev in /usr/lib/python3.8/site-packages (from maixpy3) (1.4.0)
Requirement already satisfied, skipping upgrade: gpiod in /usr/lib/python3.8/site-packages (from maixpy3) (1.4.0)
Requirement already satisfied, skipping upgrade: pyserial in /usr/lib/python3.8/site-packages (from maixpy3) (3.4)
Requirement already satisfied, skipping upgrade: rpyc in /usr/lib/python3.8/site-packages (from maixpy3) (5.0.1)
Requirement already satisfied, skipping upgrade: spidev in /usr/lib/python3.8/site-packages (from maixpy3) (3.5)
Requirement already satisfied, skipping upgrade: zbarlight in /usr/lib/python3.8/site-packages (from maixpy3) (3.0)
Requirement already satisfied, skipping upgrade: plumbum in /usr/lib/python3.8/site-packages (from rpyc->maixpy3) (1.6.9)
WARNING: You are using pip version 20.1.1; however, version 21.3.1 is available.
You should consider upgrading via the '/usr/bin/python3 -m pip install --upgrade pip' command.
root@sipeed:/#
```

输出以上信息则是代表安装好了

### MaixSense 安装 MaixPy3

MaixSense 需要是烧录官方提供最新的 Armbian 镜像，旧的镜像在安装 MaixPy3 的时候会缺很多文件而导致的报错。
> MaixSense 的 Tina 没有做 MaixPy3 的移植，有需要的可以自行移植

```shell
root@maixsense:~# pip install maixpy3
Requirement already satisfied: maixpy3 in /usr/local/lib/python3.9/dist-packages (0.3.4)
Requirement already satisfied: Pillow in /usr/lib/python3/dist-packages (from maixpy3) (8.1.2)
Requirement already satisfied: zbarlight in /usr/local/lib/python3.9/dist-packages (from maixpy3) (3.0)
Requirement already satisfied: evdev in /usr/local/lib/python3.9/dist-packages (from maixpy3) (1.4.0)
Requirement already satisfied: spidev in /usr/local/lib/python3.9/dist-packages (from maixpy3) (3.5)
Requirement already satisfied: pyserial in /usr/local/lib/python3.9/dist-packages (from maixpy3) (3.5)
Requirement already satisfied: rpyc in /usr/local/lib/python3.9/dist-packages (from maixpy3) (5.0.1)
Requirement already satisfied: gpiod in /usr/local/lib/python3.9/dist-packages (from maixpy3) (1.5.0)
Requirement already satisfied: plumbum in /usr/local/lib/python3.9/dist-packages (from rpyc->maixpy3) (1.7.0)
root@maixsense:~# python
Python 3.9.2 (default, Feb 28 2021, 17:03:44)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import maix
>>>
```

### Linux 上安装MaixPy3

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


