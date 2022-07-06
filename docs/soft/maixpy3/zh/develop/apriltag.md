## apriltag

开发原型时间： maixpy3 0.4.0 以上

预计开发时间： 2022年 Q1 结束。

开发目标：官方 apriltag 而非 openmv 版本

## 相关视频

<iframe src="//player.bilibili.com/player.html?aid=850839110&bvid=BV1wL4y1t7hc&cid=487534380&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

<iframe src="//player.bilibili.com/player.html?aid=677488628&bvid=BV1wm4y197Jf&cid=464634360&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

## 进度

- libmaix 实现分支 https://github.com/sipeed/libmaix/blob/apriltag/examples/camera/main/src/main.c

## 开发情况

参考 https://book.openmv.cc/image/apriltag.html

官网 https://april.eecs.umich.edu/software/apriltag.html

## 性能指标记录

V831 libmaix AprilTag tag36h11 SP2305 QVGA 30fps ~ OV7251 QQGVA 60fps

采用 opencv 绘图，直出 yuv 取 y 做灰度识别，效果理想。

