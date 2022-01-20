| 更新时间 | 负责人 | 内容 | 备注 |
| --- | --- | --- | --- |
| 2022年12月4日 | Rui | 初次编写文档 | ---- |
| 2022年1月18日 | dalaoshu | 修改文档，增加效果图 | ---- |

# MaixPy3 播放视频

实际上它是由 ffmpeg + pyav 编译而来，它们分别是什么呢？

FFmpeg 是一套可以用来记录、转换数字音频、视频，并能将其转化为流的开源计算机程序。

https://pyav.org/docs/develop/

PyAV 是一个用于 FFmpeg 的 python 绑定。通过容器、流、包、编解码器和帧直接和精确地访问媒体。它公开了一些数据的转换，并帮助您从其他包(例如 Numpy 和 Pillow )获取数据。

https://pyav.org/docs/develop/

目前测试的视频格式有 mp4 和 avi，其他格式还没有进行测试，以下是我们提供的测试视频供确认效果。

<iframe src="//player.bilibili.com/player.html?aid=717126108&bvid=BV1dQ4y1f7RN&cid=385731209&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

共有3个[测试视频](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/example),将这里得到的视频存放到 Linux 系统的 root 目录中，将 `path_to_video` 的参数修改成所存放视频路径。

```python
from maix import display, camera
import pyaudio
import av
import threading
import time

class funation:
    status = 0
    def __init__(self,device=None):
        self.event = self.run
        display.show(camera.capture())
        self.tim = time.time()
        self.device = device
    def __del__(self):
        print("paly exit")
    def play(self):
        try:
            # recommend flv
            # ffmpeg -r 30 -i bad_apple.mp4 -s 240x240 output.mp4
            # adb push ./output.mp4 /mnt/UDISK/
            # adb push ./test.py / && adb shell 'python ./test.py'
            path_to_video = '/root/output.mp4'
            container = av.open(path_to_video)
            ai_stream = container.streams.audio[0]
            vi_stream = container.streams.video[0]
            fifo = av.AudioFifo()
            p = pyaudio.PyAudio()
            ao = p.open(format=pyaudio.paFloat32, channels=2, rate=22050, output=True)
            for frame in container.decode(video=0, audio=0):
                if 'Audio' in repr(frame):
                    frame.pts = None
                    fifo.write(frame)
                    for frame in fifo.read_many(4096):
                        ao.write(frame.planes[0].to_bytes())
                if 'Video' in repr(frame):
                    display.show(bytes(frame.to_rgb().planes[0]))
                if self.device.funaction_status == -1:
                    ao.stop_stream()
                    ao.close()
                    p.terminate()
                    return
        except Exception as e:
            print(e)
        finally:
            ao.stop_stream()
            ao.close()
            p.terminate()
    def run(self):
        if self.status == 0:
            threading.Thread(target=self.play).start()
            self.status = 1
        time.sleep(0.1)


if __name__ == "__main__":
    import signal
    def handle_signal_z(signum,frame):
        print("APP OVER")
        exit(0)
    signal.signal(signal.SIGINT,handle_signal_z)
    start = funation()
    while True:
        start.event()
```
