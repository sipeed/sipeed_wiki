# MaixPy3 播放视频

| 更新时间 | 负责人 | 内容 | 备注 |
| --- | --- | --- | --- |
| 2021年12月4日 | Rui | 初次编写文档 | ---- |
| 2022年1月18日 | dalaoshu | 修改文档，增加效果图 | ---- |
| 2022年4月24日 | Coty | 修改视频播放代码,修改了提供视频的尺寸 | ---- |

实际上它是由 ffmpeg + pyav 编译而来，它们分别是什么呢？

FFmpeg 是一套可以用来记录、转换数字音频、视频，并能将其转化为流的开源计算机程序。

https://pyav.org/docs/develop/

PyAV 是一个用于 FFmpeg 的 python 绑定。通过容器、流、包、编解码器和帧直接和精确地访问媒体。它公开了一些数据的转换，并帮助您从其他包(例如 Numpy 和 Pillow )获取数据。

目前测试的视频格式有 mp4 和 avi，其他格式还没有进行测试，以下是我们提供的测试视频供确认效果。

<p align="center">
  <iframe src="//player.bilibili.com/player.html?aid=717126108&bvid=BV1dQ4y1f7RN&cid=385731209&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:640px; max-height:480px;"> </iframe>
</p>

## 如何播放视频？

这里使用的是转换后的 output_240_240.mp4 [测试视频](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/example)，从这里获得视频后存放到 Linux 系统的 root 目录中，将 `path_to_video` 的参数修改成所存放视频路径，如：`'/root/output_240_240.mp4'`，其他视频同理，需要注意的是 v831 的性能很弱，可能最高就播放到软解 h264 30fps 了，硬解资源不被 FFmpeg 所提供。

> ffmpeg 转换命令 ffmpeg -r 30 -i badapple_240_60fps.mp4 -vf scale=240:240,setdar=1:1 output.mp4

```python
import pyaudio, av, os
from maix import display, camera, image
# ffmpeg -r 30 -i badapple_240_60fps.mp4 -vf scale=240:240,setdar=1:1 output.mp4
# adb push ./output.mp4 /root/
path_to_video = '/root/output_240_240.mp4'
if os.path.exists(path_to_video):
    try:
        container = av.open(path_to_video)
        ai_stream = container.streams.audio[0]
        vi_stream = container.streams.video[0]
        fifo = av.AudioFifo()
        p = pyaudio.PyAudio()
        ao = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)
        for frame in container.decode(video=0, audio=0):
            if 'Audio' in repr(frame):
                frame.pts = None
                fifo.write(frame)
                for frame in fifo.read_many(4096):
                    ao.write(frame.planes[0].to_bytes())
            if 'Video' in repr(frame):
                img = image.load(bytes(frame.to_rgb().planes[0]), (vi_stream.width, vi_stream.height))
                display.show(img)
    finally:
        ao.stop_stream()
        ao.close()
        p.terminate()
```

## 如何录制视频？

2022年07月26日 根据 pyav.org 文档加源码整理如下代码，从录制编码到播放（x264 支持手机预览但解码性能低），注意该代码只在 av 9.2.0 版本的库可用，需要更新 0.5.2 系统底包的（av 8.0.3）喔（这种需要编译的包 pip 是得不到的）。

```python

from maix import display, image

path_to_video = 'test.mp4'

import av

duration, fps = 4, 10
total_frames = duration * fps
container = av.open(path_to_video, mode='w')
stream = container.add_stream('h264', rate=fps) # h264 or mpeg4
stream.width = 320
stream.height = 240
stream.pix_fmt = 'yuv420p'

for frame_i in range(total_frames):
    img = image.new(size=(stream.width, stream.height), mode='RGB')
    import time
    img.draw_string(0, 0, str(time.time()), 2)
    frame = av.VideoFrame(img.width, img.height, 'rgb24')
    frame.planes[0].update(img.tobytes())
    for packet in stream.encode(frame):
        container.mux(packet)

#Flush stream
for packet in stream.encode():
    container.mux(packet)

#Close the file
container.close()

#Play the video

container = av.open(path_to_video)
stream = container.streams.video[0]
for frame in container.decode(video=0):
    if 'Video' in repr(frame):
        img = image.load(bytes(frame.to_rgb().planes[0]), (stream.width, stream.height))
        display.show(img)
```

试试吧，可以看到录制的是我们填充的 image 图像，打印了时间字符串。
