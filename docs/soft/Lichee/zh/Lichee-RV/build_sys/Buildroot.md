---
title: 使用Buildroot
keywords: debian, Rv, Problem, buildroot, img, sipeed
---
> 编辑于2022年3月16日

## 方式一：使用韦东山提供的Buildroot
### 准备工作
克隆Buildroot
```
git clone https://gitee.com/weidongshan/neza-d1-buildroot.git
```
进入Buildroot文件夹
```
cd neza-d1-buildroot/
```
### 配置和编译
加载配置文件
```
make neza-d1_defconfig
```
如果需要进一步配置（如添加/删除软件，添加WiFi网卡驱动），可以执行：
```
make menuconfig
```
如果你使用的是RV Dock WiFi版（出厂自带RTL8723DS），请前往Target packages下的Hardware handling勾选RTL8723DS。（建议连同Networking applications中的dhcpd和Network Manager中的nmtui勾选上）。如果你使用其他WiFi模块，需要根据WiFi模块所使用的芯片来选择相应的WiFi驱动。
其他软件包（如Vim，Qt5等）按需选择即可。
退出，保存，开始编译（编译时长取决于电脑性能，需要编译的软件数量和网速）。
```
make all
```
或
```
make all -j2
```
（视情况输入或调整使用的线程数，如果您的电脑性能较好可以试试`-j4`甚至更多）
如果出现以下内容:
```
INFO: hdimage(sdcard.img): adding partition 'boot0' from 'boot0_sdcard.fex' ...
INFO: hdimage(sdcard.img): adding partition 'boot-packages' from 'boot_package.fex' ...
INFO: hdimage(sdcard.img): adding partition 'env' (in MBR) from 'env.fex' ...
INFO: hdimage(sdcard.img): adding partition 'env-redund' (in MBR) from 'env.fex' ...
INFO: hdimage(sdcard.img): adding partition 'boot' (in MBR) from 'boot.vfat' ...
INFO: hdimage(sdcard.img): adding partition 'rootfs' (in MBR) from 'rootfs.ext4' ...
INFO: hdimage(sdcard.img): writing GPT
INFO: hdimage(sdcard.img): writing hybrid MBR
```
恭喜你，固件编译成功，这时候就可以使用Etcher来将该固件烧入SD卡里了。
### 调试
然后将开发板和串口模块连接起来，并使用串口调试软件进行调试。
**注意：只需要接RX、TX和GND即可，RX接TX，TX接RX，别接错了。**
如果按下回车键后有内容输出，并且能够正常使用命令，恭喜你，喜提属于你自己的Linux。
如果需要联网，请参考：
[联网教程](https://wiki.sipeed.com/hardware/zh/lichee/RV/user.html#%E6%97%A0%E7%BA%BF%E7%BD%91%E7%BB%9C)的使用Tina系统（udhcpc需要替换成dhcpd）
## 方式二：使用官方Buildroot/其他大佬的Buildroot（适合喜欢折腾Buildroot的人）
目前官方版本的Buildroot已经支持全志D1（截至2022.02），但是默认C语言标准库是uClibc-ng，就看个人喜好了，想要支持更多软件可以使用glibc，想要体积小一点的可以选uClibc-ng，当然你得自己去摸索了，比如软件库啥的。
其他大佬的Buildroot列表：
https://github.com/YuzukiHD/Buildroot-YuzukiSBC
（如果有其他的欢迎来补充）
