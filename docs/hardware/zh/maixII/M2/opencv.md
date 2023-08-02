---
title: Maix-II DOCK 使用 OpenCV
update:
  - date: 2023.08.02
    author: neucrack
    content: 新建文档，添加 C/C++ 和 Python 使用 OpenCV 方法
---

有两种使用方式，C/C++ 或者 Python 语言使用

## Maix-II-Dock C/C++ 使用 OpenCV

使用 [libmaix + opencv](https://github.com/sipeed/libmaix/tree/release/examples/camera_opencv)。
这里写好了 opencv 的最小例程，根据你的情况开发即可。
> OpenCV 开发的好处是需要啥都能搜到例子，另外还能用 MaixPy3 用的一些接口，比如 find_blobs 寻找色块，在[这里](https://github.com/sipeed/MaixPy3/blob/c6b5c419a9c547f1f42c686020eb0e4cdb3f93cf/ext_modules/_maix_image/py_maix_image.cpp#L105)查找你要的 API， 然后根据指向的函数，比如`.def("binary", &maix_image::_binary,`指向[_binary](https://github.com/sipeed/MaixPy3/blob/c6b5c419a9c547f1f42c686020eb0e4cdb3f93cf/ext_modules/_maix_image/_maix_image.cpp#L926)函数，照着这个函数写就好了！是不是自由度巨大，不用受限于 MaixPy3 的 API 更新啦
>
> libmaix + opencv 为 m2dock 编译指导：请参考 [libmaix 的 readme 文档](https://github.com/sipeed/libmaix/blob/release/README.md)

修改例程中的 OpenCV 操作即可，例程是一个边缘检测：
```c++
void opencv_ops(cv::Mat &rgb)
{
    cv::Mat gray;
    cv::cvtColor(rgb, gray, cv::COLOR_RGB2GRAY);
    cv::Canny(gray, gray, 100, 255, 3, false);
    cv::cvtColor(gray, rgb, cv::COLOR_GRAY2RGB);
}
```

## Python 使用 OpenCV

Maix-II-Dock 使用 OpenCV 参考[给 M2Dock 安装 Python Opencv](https://wiki.sipeed.com/news/others/v831_opencv/v831_opencv.html) 这篇文章给 M2Dock 安装 Python Opencv 包，然后在 Python 代码里面`import cv2`就可以开始使用啦！

不过由于 Maix-II-Dock 内存资源有限，同时使用模型的话可能内存会比较紧张，根据自己的需求使用就好，如果内存不足，则建议使用 C/C++ 开发。

