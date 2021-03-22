---
title: 第一个程序: 使用屏幕和摄像头
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 第一个程序: 使用屏幕和摄像头
---


开发板有配套的摄像头和屏幕，请在上电前检查硬件连接是否正确（**按照排线标有的一号引脚对齐**）

然后上电，打开串口终端， 按键盘`Ctrl+E`,然后粘贴以下代码：
```python
import sensor, lcd

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)
sensor.skip_frames()

lcd.init(freq=15000000)

while(True):
    lcd.display(sensor.snapshot())

```
按键盘`Ctrl+D`来开始运行代码

会发现屏幕被点亮了，而且显示出了摄像头拍到的画面

如果显示`reset fail`， 则是摄像头没有连接好，或者摄像头已经损坏，或者检查是不是使用了不支持的摄像头

上面的程序都可以在 API 手册中查到含义， 在左边目录中可以找到， 也可以使用左上角的搜索框进行搜索。
现在解释上面的程序：
* `import sensor, lcd`: 首先导入内置的`sensor`（摄像头）库和`lcd`（屏幕）库
* `sensor.reset()`: 初始化摄像头，这里失败需要检查硬件
* `sensor.set_pixformat(sensor.RGB565)`: 设置摄像头为`RGB565`格式，默认都是用`RGB565`即可
* `sensor.set_framesize(sensor.QVGA)`: 分辨率为`QVGA`，即`320x240`
* `sensor.run(1)`: 开始运行，在现在的版本中也可以不调用，在上面设置完成后，摄像头会自动开始运行
* `sensor.skip_frames()`: 摄像头刚启动时，图像质量还没稳定，所以跳过一些图像
* `lcd.init(freq=15000000)`: 初始化 LCD， 这里传了一个参数叫`freq`即频率， 是指定驱动 LCD 的时钟频率，这里是`15MHz`，可以根据硬件性能调整
* `while(True)`: 这是一个循环，循环里面的代码会被不停地运行
* `sensor.snapshot()`:从摄像头取一帧图像数据，返回值是一张图像的对象
* `lcd.display()`： 显示图像到 LCD
*  `lcd.display(sensor.snapshot())`: 这里就是先执行括号里的获取图像，返回值直接作为参数给 LCD 进行显示



