Zero的开发环境分类
=========================================

.. contents:: 本文目录

Camdriod 官方SDK
-----------------------------------------

Camdriod是V3S的官方开发环境，又被称为“坑卓”。

此坑卓非彼安卓，不能运行原生安卓apk，请不要妄想在64MB内存上跑安卓。。

坑卓 linux内核版本为3.4，系统配置方法是使用fex文件，对摄像头支持较好。

需要开发行车记录仪方案的，可以尝试使用坑卓。

荔枝派目前不提供对坑卓的技术支持。（有偿的也不提供）。

坑卓SDK下载：

| camdriod 本体： http://pan.baidu.com/s/1miQN1Ra
| Lichee Linux：http://pan.baidu.com/s/1eRJrViy
   
   芯片资料和坑卓开发说明：http://pan.baidu.com/s/1pLQbwuB

下载后解压，把两个文件夹放在同一目录下，按照坑卓开发说明开发即可。

主线Uboot + Bsp 内核
-----------------------------------------

如果不想被坑卓坑， 又想比较好地使用摄像头，可以使用主线Uboot加Bsp内核方案， 系统配置为fex文件配置。

| 主线uboot： https://github.com/Lichee-Pi/u-boot

   bsp内核即前面的lichee linux： http://pan.baidu.com/s/1eRJrViy

主线Uboot + 主线linux
-----------------------------------------

如果想使用主线的特性，可以使用 主线Uboot + 主线linux 开发环境。系统配置为dts设备树配置。

| 主线uboot： https://github.com/Lichee-Pi/u-boot
   
   主线linux： https://github.com/Lichee-Pi/linux

Docker开发环境
-----------------------------------------

如果不想自己配置繁琐的开发环境，请使用docker开发环境，免去所有配置烦恼。

Zero的文件系统
-----------------------------------------

主要分为buildroot/LEDE，emdebian两类，前者较小，可以在spi flash(16/32MB)或者小容量TF卡（64/128MB）上运行。
