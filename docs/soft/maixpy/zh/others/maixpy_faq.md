---
title: MaixPy 常见问题
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: MaixPy 常见问题
---



## MaixPy 与 C 开发有什么异同，我该怎么选择

MaixPy 是基于 Micropython 的脚本语言， 不需要编译，在运行时解析，编写起来更简单方便，只是运行时时实性不如 C 语言。
所以如果是快速验证、新手、只会 python、头发少等都可以用 MaixPy; 追求极限性能效率或者熟悉 C ，以及对 MaixPy 的长期运行的稳定性不太有信心的都可以使用 C 语言开发

## MaixPy IDE 无法成功连接开发板

**现象:**

​	开发板到手之后，一直无法连接 MaixPy IDE

* 检查固件是否支持 IDE， 早期的固件以及名字带`minimum`的固件都不支持
* 检查串口是否被占用（其它软件也打开了串口）
* 点击连接后，不用和终端工具同时使用，否则会出现串口占用无法打开
* 如果一直无法成功连接成功， 检查：
  * 请检查是否开发板型号选择错误；

  * 观察开发板屏幕是否有变化，如果没有反应可能是串口选择错误；

  * 尝试升级到最新的 [master 分支固件](http://cn.dl.sipeed.com/MAIX/MaixPy/release/master)， 以及最新的 MaixPy IDE 软件

    > MaixPy 版本号低于 0.5.0_v0 不支持连接 MaixPy IDE

## 文档网页打不开，速度慢

如果遇到有些页面无法访问， 请检查一下网址（路径）是否正确， 可以回到首页 (`maixpy.sipeed.com`) 重新进入即可。

比如这个网址就是由于点击过快导致的：
```
http://localhost:4000/zh/zh/get_started/how_to_read.html
```
正确的网址应该是：
```
http://localhost:4000/zh/get_started/how_to_read.html
```

另外，可以换个网络线路试试，比如挂代理，或者换手机流量试试， 国内也可以使用`cn.maixpy.sipeed.com`

## 下载站文件下载速度慢，文件无法下载

如果遇到在 dl.sipeed.com 下载站下载速度慢，可以使用国内的同步服务器 cn.dl.sipeed.com 下载，路径相同，每天同步一次；
部分文件提供了 CDN 下载链接，速度会比较快， 比如 IDE 在 readme.txt 中有说明

## Micro SD 卡读取不到


Micro SD 读取不到现象及解决方法:

1. 确认 SD 能否在电脑上正常使用，如果不能即 SD 已损坏，

2. 电脑能够正常使用，读取 SD，但 MaixPy 开发板无法使用：

  SD 卡未格式化为 MBR 分区 FAT32 格式

3. 电脑能够正常使用 SD 卡，也确认 SD 卡的磁盘格式为 FAT32，但 MaixPy 开发板依旧无法使用：

  可能存在的原因：部分 SD 出厂时，sd 中没有磁盘分区表，或者磁盘分区表类型不是 MBR

  解决的方法：使用第三方磁盘管理软件，将 sd 分区表类型转换为 MBR, 并且将 sd 格式格式化为 FAT32

> 这里使用 **Diskgenius** 来转换磁盘分区表格式

![Diskgenius](../../assets/other/diskgenius.png)


![GPT 类型转 MBR](../../assets/other/diskgenius_sd_gpt_to_mbr.png)

![MBR 类型](../../assets/other/diskgenius_sd.png)


3. SD 卡不支持 SPI 协议

目前硬件只能支持 SPI 协议读取， 尽量购买正规的卡

比如：下图左边两张卡 MaixPy 的驱动不支持， 中间和右边的都支持， 但是中间的 class10 卡速度最快（最高测过 128GB可用）
> 另外测试过网上购买的几张闪迪、金士顿、三星的卡，其中发现有一张三星的卡无法使用

![](../../assets/hardware/other/tf_sdcard.png)


## SD 卡支持多大容量

最大测试过 128GiB 可以使用

## 使用 SD 加载文件、模型不成功

现象：我们在使用过程中可能遇到加载模型提示错误，

可能存在的问题原因: sd 不兼容，挂载不成功

验证 sd 卡是否挂载方法:

```python
import os
print(os.listdir("/"))
>>['flash'] # 没有挂载 SD 卡

>>['flash', 'sd'] # 挂载 SD 卡成功
```

## 为什么连接了 IDE 帧率降低了很多

K210 没有 USB 外设， 因此只能使用串口与 IDE 通信， 速度不如 USB 设备快，因此会影响帧率， 可以关闭 IDE 的摄像头预览


## 为什么 IDE 上预览的摄像头图像很模糊

K210 没有 USB 外设， 因此只能使用串口与 IDE 通信， 速度不如 USB 设备快， 因此对图片进行了压缩，如果需要看清晰的图像请在开发板的屏幕上看，或者保存成图片传到电脑查看

所以 IDE 的图像预览功能主要是给教学和演示使用， 平时建议使用屏幕，
可以使用以下代码来设置预览图质量
```python
sensor.set_jb_quality(95)
```
这样就将预览图的质量设置为了 `95%`， 但是帧率会有明显降低


## 怎么提高摄像头帧率

* 换更好的摄像头，比如 `ov7740` 帧率会比 `ov2640` 高一点。 但前提是摄像头电路必须与开发板的电路兼容
* 增加摄像头时钟频率(`sensor.reset(freq=)`)，但是注意不要太高，太高会让画面变差
* 可以自己编译源码，打开摄像头双缓冲选项（默认打开），并且 `sensor.reset(dual_buff=True)`，帧率会有所增加，但是相应地，耗费的内存也会增加（大约为 384KiB ）


## IDE 帧缓冲区成像方向不正确，LCD 显示方向不正确

由于 MaixPy 支持的硬件型号较多，在使用 MaixPy IDE 或者 LCD 显示的时候会出现显示的方向不正确,那么这时候我们就需要对图像进行旋转了;
在修正显示方向之前,我们需要确认是 Sensor 方向旋转(MaixPy IDE 右上角的图像即为 Sensor 直接输出的图像)了，还是 LCD 方向旋转了
修正方法:

- sensor 方向修正：

```python
# 设置摄像头水平镜像
# `enable`: 1 表示开启水平镜像 0 表示关闭水平镜像
sensor.set_hmirror(enable)

# 设置摄像头垂直镜像
# `enable`: 1 表示开启垂直镜像 0 表示关闭垂直镜像
sensor.set_vflip(enable)
```

- lcd 方向修正：

```python
# 设置 `LCD` 屏幕方向
# 参数: `dir`: 取值范围 [0,3]， 从`0`到`3`依次顺时针旋转
# 返回值: 当前方向，取值[0,3]
lcd.rotation(dir)

# 设置 `LCD` 是否镜面显示
# 参数: `invert`： 是否镜面显示， `True` 或者 `False`
# 返回值: 当前设置，是否镜面显示，返回`True`或者`False`
lcd.mirror(invert)
```

## 烧录 MaixPy 之后，MaixPy 出现无法启动

现象：我们在使用过程中可能遇到烧录 MaixPy 之后，MaixPy 出现无法启动(表象为 无法点亮屏幕，白屏 等)，
问题原因: 出现这种现象很大一部分是内部文件系统中的配置文件读取出错，或者我们设置的系统配置值(如 gc heap 值过大)出错导致系统无法启动。

解决方法：擦除文件系统(擦除全部 flash)

使用 kflash_gui 右上角选择`擦除`功能，然后加载`MaixPy 文件系统`模板，地址变成`0xD00000`, 长度变为`3MiB`

或者下载擦除固件: erase.fpkg/flash_erase_16MB.bin/[erase_spiffs.kfpkg](https://cn.dl.sipeed.com/MAIX/MaixPy/release)


## 使用 JTAG 调试器一直无法接连 K210

现象：使用裸机开发 K210, JTAG 调试器一直无法接连 K210

可能的原因：
  1. OpenOCD 调试环境搭建有问题（细节这里不说明）
  2. 烧录过 ken_gen.bin 之后，将永久禁用 K210 的 JTAG 调试功能

## 下载，保存脚本到 MaixPy 内部flash 之后，板子无法更新固件，无法启动运行脚本

- 可能现象：下载，保存脚本到 MaixPy 内部flash 之后，板子无法更新固件，板子无法启动


> 问题可以从硬件和软件上面去定位:

可能的硬件原因：

​	TODO: 待更新

可能的软件原因：

  1. 程序中拉高了 GPIO16, 造成了自动下载点电路无法拉低 GPIO16,使 K210 进入 ISP 模式

## kflash 无法烧录/更新 MaixPy 固件

kflash_gui 配置选项

- 开发板型号
  - 开发板型号选错
- 烧录空间(SRAM/Flash)
  - 烧录空间选错
- 波特率&下载速度模式
  - 下载波特率过高
