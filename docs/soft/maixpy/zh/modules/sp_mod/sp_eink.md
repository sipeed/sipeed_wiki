---
title: SP_EINK 的使用
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: SP_EINK 的使用
---


<img src="../../../assets/hardware/module_spmod/sp_eink.png"/>

SP_EINK 模块所采用的 GDEW0154M09 是一款 1.54”, 拥有 24P FPC(0.5mm 间距)接口的电子墨水屏.

## 参数

* 屏幕大小: 1.54 英寸
* 有效显示区域: 27.6mm * 27.6mm
* 色彩: 黑/白/红显示
* 通信接口: SPI
* 工作温度: -40°C~85°C
* 工作电压: 2.3V~3.6V

模块详细信息请参考[EINK 规格书与数据手册](https://api.dl.sipeed.com/fileList/MAIX/HDK/Spmod_EN/SP-EINK%20Datasheet%20V1.0.pdf)

## 使用方法

1. 准备: 已烧录最新固件的开发板, sp_eink 模块.

2. 运行: 连接模块, 修改[示例代码](https://github.com/sipeed/MaixPy_scripts/tree/master/modules/spmod/sp_eink)中 config 包围的配置, 运行后模块将显示图片.

程序如下:

```python
# init
epd = SPEINK(spi1, cs, dc, rst, busy, EPD_WIDTH, EPD_HEIGHT)
epd.init()

# create red image
img_r = image.Image()
img_r = img_r.resize(EPD_WIDTH, EPD_HEIGHT)
img_r.draw_line(0, 0, 100, 100)

# create black/white image
img_bw = image.Image()
img_bw = img_bw.resize(EPD_WIDTH, EPD_HEIGHT)
img_bw.draw_line(100, 50, 200, 100)

# display
epd.display(img_r, img_bw)

# sleep mode
epd.sleep()
```

主要步骤如下:

* 创建 SPEINK 对象(参数为: SPI 对象, 片选脚, 复位脚, 忙标志脚, 横向分辨率, 纵向分辨率, 屏幕旋转角度(0, 90, 180, 270)), 初始化.

* 创建红色和黑色图像, 设置为屏幕大小并填充图像.

* 调用 display(参数依次为: 红色图像, 黑色图像), 此时屏幕将会闪烁并显示图像.
  
* 进入睡眠状态.
