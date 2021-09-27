# 主线Linux编译


## 源码下载


完整下载命令为：

    git clone https://gitee.com/LicheePiNano/Linux.git

git拉取有时速度很慢，建议做如下配置：


完整拉取linux极大，建议只拉取单层分支，减少等待时间：

    git clone --depth=1 -b master https://gitee.com/LicheePiNano/Linux.git

## 配置

使用./arch/arm/configs/f1c100s_nano_linux_defconfig配置文件

	make ARCH=arm f1c100s_nano_linux_defconfig


## 进行编译


> 编译工具链为 arm-linux-gnueabi，工具链的安装请参考 uboot 编译部分

```
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- -j8	#请自行修改编译线程数
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- -j8 INSTALL_MOD_PATH=out modules	#请自行修改编译线程数
make ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- -j8 INSTALL_MOD_PATH=out modules_install	#请自行修改编译线程数
```

编译成功后，生成文件所在位置：
+ 内核img文件：./arch/arm/boot/zImage
+ 设备树dtb文件:./arch/arm/boot/dts/suniv-f1c100s-licheepi-nano.dtb
+ modules文件夹：./out/lib/modules

将zImage与dtb文件放入nano第一分区．

