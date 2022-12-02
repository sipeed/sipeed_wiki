待更新！

<!-- ## Python API 编程

> 在 **20221125** 后更新的镜像内置了基于 ax-pipeline 的应用并支持可用 Python API 编程。

**ax_pipeline**：[点击查看相关仓库](https://github.com/junhuanchen/ax_pipeline_api)

使用之前需要替换最新 **20221125** 的镜像然后在终端安装 ax_pipeline_api 包。

```bash
pip3 install ax_pipeline_api -U
```
再使用以下命令行运行一下内置的 `pipeline.py` 即可在屏幕上看到效果

```bash
cd /home
python3 pipeline.py
```

关于如何修改摄像头型号、libxxx*so、model 之类的可以参考 readme 文档

### 支持 microbit 掌控板

连接 microbit 掌控版并使用 python 编程前需要准备好以下的材料。

- **microbit 掌控版以及 micro usb 数据线**
- **type-c usb 转接头**
- **Maix-III AXera-Pi 开发板以及 type-c 线** 
  
具体接线图待补充！

可在终端接入 `python3` 模式运行下方代码即可连接 microbit 掌控版并会看到 **hello world** 亮灯效果。

```bash
import time
from pinpong.board import Board,Pin
from pinpong.extension.microbit import *
Board("microbit","/dev/ttyACM0").begin()
display.show(Image.HEART)
while True:
    display.scroll("hello world")
```

![microbit](./../assets/microbit.jpg) -->