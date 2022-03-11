---
title: R329主线armbian内核，系统，驱动开发方法
keywords: R329, maixsnse, MaixSense, Maixsense, armbian, build, kernel
---
本文需要一些[前置基础](./R329_SDK_编译与烧录.md)

准备环境:
* Ubuntu20.04
* [MaixSense](https://wiki.sipeed.com/hardware/zh/maixII/M2A/maixsense.html)
* 一张已经烧录`r329-armbian-maixpy3-0.4.0.img`的TF卡
* [Armbian_21.08.0-trunk_Maixsense_bullseye_edge_5.14.1.img.xz](https://eyun.baidu.com/s/3htTXfaG)镜像,网盘里对应的路径为`./MaixII-a/SDK`

##修改 boot.cmd 的方法
想要改变 uboot 的一些启动配置，就可以通过这个方式进行修改，修改 boot.cmd 后直接在系统里运行完成更新。
> mkimage -C none -A arm -T script -d /boot/boot.cmd /boot/boot.scr

主线 linux 都会有类似的配置供你使用，可能是文件可能是分区。

##Linux 内核、驱动、设备树的相关用法方法
可以参考[Lichee Pi](https://wiki.sipeed.com/soft/Lichee/zh/index.html)(特别详细)，armbian编译没有那么繁琐因此不再赘述。
准备环境`sudo apt install -y git wget make gcc flex bison libssl-dev bc kmod`
其他相关教程 
* [licheepi zero主线Kernel基础编译](https://wiki.sipeed.com/soft/Lichee/zh/Zero-Doc/System_Development/kernel_build.html)
* [licheepi nano主线Linux编译](https://wiki.sipeed.com/soft/Lichee/zh/Nano-Doc-Backup/build_sys/kernel.html)

##修改设备树配置的方法
使用`git clone -b r329-wip https://github.com/sipeed/linux.git` #完成后切到 `r329-wip` 分支
编译链工具可以用系统自带的`通用编译链`或`gcc-linaro`，本文使用的是`gcc-arm-8.3-2019.03-x86_64-aarch64-linux-gnu.tar.xz` [点我下载](https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu-a/8.3-2019.03/binrel/gcc-arm-8.3-2019.03-x86_64-aarch64-linux-gnu.tar.xz)。
[设备树简介：](https://wiki.sipeed.com/soft/Lichee/zh/Zero-Doc/Drive/Device_Tree_Intro.html)用户在设备树里定义并启用的树结点，就可以使用相应驱动。
MaixSense的设备树在`linux/arch/arm64/boot/dts/allwinner/`路径下，和r329相关的设备树有
* sun50i-r329-maix-iia.dtsi
* sun50i-r329-maixsense.dts
* sun50i-r329.dtsi

目前的主线配置`linux/arch/arm64/configs/defconfig`导入它。
输入`make ARCH=arm64 defconfig`开始完整编译
```
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- -j4
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- -j4 INSTALL_MOD_PATH=out modules
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- -j4 INSTALL_MOD_PATH=out modules_install
```
啥都不清楚的情况下，一路确认键按下去，直到开始编译，导出 modules 是非必要操作，但对应一些外置 ko 模块需要导出拷到 /lib/modules/ 目录中，在 menuconfig 中设置为 M 就可以编译出 ko 模块从外部插入系统。
编译成功后，生成文件所在位置：
- 内核`Image`文件: ./arch/arm64/boot/Image 对应 armbian 目录下的 boot/Image
- 设备树`dtb`文件: ./arch/arm64/boot/dts/allwinner/sun50i-r329-maixsense.dtb 到 boot/dtb/allwinner/
- `modules`文件夹: ./out/lib/modules

将`Image`与`dtb`文件放入`boot`目录下重启后即可自动完成内核的更新（armbian 特有）。

上述内容测试过后，你就可以开始自定义自己的主线内核了，但这个并不是主要目的，只是说一些基础用法。
单独编译`dtb`文件加入设备。
通常来说，在不了解如何编译整体的情况下，只需要通过简单的设备树替换就可以完成驱动适配。
`make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- dtbs -j4`
- 参考文章：[为R329添加i2c设备](https://www.cnblogs.com/USTHzhanglu/p/15500269.html)
- 参考文章：[总结一次为R329开启uart的经历](https://www.cnblogs.com/USTHzhanglu/p/15191052.html)

将编译得到的`dtb`文件复制到`/boot/dtb/`。

这里仅供学习参考，Sipeed 内部已经包含了`/usr/lib/modules/5.14.0-rc4-sun50iw11/kernel/drivers/net/wireless/rtl8723ds/8723ds.ko`模块。

上述方法出来的内核不是我们提供的，因为配置项的不同所以会缺少一些驱动，需要你自行加入；如`8723ds`非主线所使用的 wifi 模块。

`git clone https://github.com/Icenowy/rtl8723ds` #切换到newest-kernel
移动到`linux/drivers/net/wireless/realtek/`下
编辑`drivers/net/wireless/Kconfig`添加 `source "drivers/net/wireless/realtek/rtl8723ds/Kconfig"`，清除错误的语法，只留最简单的部分即可。
```
config RTL8723DS
	tristate "Realtek 8723D SDIO or SPI WiFi"
```
编辑`linux/drivers/net/wireless/realtek/Makefile`添加`obj-$(CONFIG_RTL8723DS) += rtl8723ds/`使得模块参与编译。
通过`make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- -j8 menuconfig` 按 `/` 搜索 `8723ds` 把它配上编译即可。
配好直接 `make` 编译就行，在 `sipeed` 的 `armbian` 这里不需要，仅告知如何加入非主线模块，如特殊的 `TP` 触摸屏、`ADC` 按键驱动、`I2C` 传感器驱动等。

##编译 `armbian` 系统
* 自行准备良好的网络环境，相关问题不做解答，默认懂得都懂，编不出来也很正常，不用太在意。

上述开发的内核模块在 `sipeed` 提供的 `armbian` 镜像中都是无用的，仅用于测试和确认开发环境，所以要进一步把 `armbian` 编译出来才是最终用户所用的环境。

有需要的可以看文档 https://docs.armbian.com/Developer-Guide_Build-Preparation 说明。

安装 `apt install -y dialog psmisc acl uuid-runtime curl gnupg gawk` 准备环境
获取 `https://github.com/sipeed/armbian-build.git` 切到 r329-wip 分支，然后通过 `compile.sh` 完成编译。

将根据以下配置在 armbian-build 中进行编译。
- config/boards/maixsense.wip
- config/bootscripts/boot-sun50iw11.cmd
- config/kernel/linux-sun50iw11-edge.config
- config/sources/families/sun50iw11.conf

运行 `./compile.sh` 选择会自动拉取所有相关的东西，即可编译出来，接下来就是漫长的等待。

注意 `maixsense` 并非为最终 `conf` 版本，你需要在 底下的 `show WIP` 中选择 `agree` 后就可以看到 `maixsense` 了,配置可以是 `bullseye` 和 `minimal` 就好。

编译期间会在 `armbian-build/cache/sources` 下 `git clone` 在 `config/sources/families/sun50iw11.conf` 指定的仓库和分支。

把 `https://github.com/Icenowy/rtl8723ds` 改为 `https://github.com/lwfinger/rtl8723ds` 。

把 `armbian-build/config/sources/families/sun50iw11.conf` 文件中 `KERNELBRANCH` （linux）的 `r329-wip-integrated` 改到 `r329-wip` 分支。

完成后输出如下：
```bash
[ o.k. ] Building kernel splash logo [ bullseye ]
[ .... ] Installing extras-buildpkgs [  hostapd htop mmc-utils sunxi-tools ]
[ o.k. ] Calling image customization script [ customize-image.sh ]
[ o.k. ] No longer needed packages [ purge ]
[ o.k. ] Unmounting [ /home/juwan/R329/armbian-build/.tmp/rootfs-c735dfca-9977-402a-a68b-b4529b5aac8f ]
[ o.k. ] Preparing image file for rootfs [ maixsense bullseye ]
[ o.k. ] Current rootfs size [ 780 MiB ]
[ o.k. ] Creating blank image for rootfs [ 984 MiB ]
[ .... ] dd:  984MiB [ 136MiB/s] [================================================================>] 100%
[ o.k. ] Creating partitions [ root: ext4 ]
[ .... ] Creating rootfs [ ext4 on /dev/loop40p1 ]
[ .... ] Copying files to [ / ]
[ .... ] Copying files to [ /boot ]
[ .... ] Updating initramfs... [ update-initramfs -uv -k 5.14.0-rc7-sun50iw11 ]
[ o.k. ] Updated initramfs. [ for details see: /home/juwan/R329/armbian-build/output/debug/install.log ]
[ .... ] Re-enabling [ initramfs-tools hook for kernel ]
[ o.k. ] Unmounting [ /home/juwan/R329/armbian-build/.tmp/mount-c735dfca-9977-402a-a68b-b4529b5aac8f/ ]
[ o.k. ] Free SD cache [ 8% ]
[ o.k. ] Mount point [ 91% ]
[ o.k. ] Writing U-boot bootloader [ /dev/loop40 ]
[ o.k. ] SHA256 calculating [ Armbian_21.08.0-trunk_Maixsense_bullseye_edge_5.14.0_minimal.img ]
[ warn ] GPG signing skipped - no GPG_PASS [ Armbian_21.08.0-trunk_Maixsense_bullseye_edge_5.14.0_minimal.img ]
[ o.k. ] Done building [ /home/juwan/R329/armbian-build/output/images/Armbian_21.08.0-trunk_Maixsense_bullseye_edge_5.14.0_minimal.img ]
[ o.k. ] Runtime [ 350 min ]
[ o.k. ] Repeat Build Options [ ./compile.sh  BOARD=maixsense BRANCH=edge RELEASE=bullseye BUILD_MINIMAL=yes BUILD_DESKTOP=no KERNEL_ONLY=no KERNEL_CONFIGURE=no COMPRESS_OUTPUTIMAGE=sha,gpg,img  ]
```
把 Armbian_21.08.0-trunk_Maixsense_bullseye_edge_5.14.0_minimal.img 拿来烧录就行。

以下是本次的配置：（如果你连这个都没编译出来就不要操作了）
```bash
# Allwinner R329 dual core 256M RAM WiFi USB-C
BOARD_NAME="MaixSense"
BOARDFAMILY="sun50iw11"
BOOTCONFIG="sipeed_maixsense_defconfig"
MODULES_BLACKLIST="lima"
DEFAULT_CONSOLE="serial"
BUILD_DESKTOP="no"
BOOT_LOGO="yes"
SERIALCON="ttyS0"
KERNEL_TARGET="edge"
OFFLINE_WORK="yes"
CLEAN_LEVEL=""


# ./compile.sh EXPERT=yes BUILD_STABILITY=stable BOARD=maixsense BRANCH=edge RELEASE=bullseye BUILD_MINIMAL=yes BUILD_IMAGE=yes BUILD_DESKTOP=no KERNEL_ONLY=no KERNEL_CONFIGURE=yes COMPRESS_OUTPUTIMAGE=sha,gpg,img CLEAN_LEVEL=""

# ./compile.sh OFFLINE_WORK="no" EXPERT=yes BUILD_STABILITY=stable BOARD=maixsense BRANCH=edge RELEASE=bullseye BUILD_MINIMAL=yes BUILD_IMAGE=no BUILD_DESKTOP=no KERNEL_ONLY=yes KERNEL_CONFIGURE=yes COMPRESS_OUTPUTIMAGE=sha,gpg,img CLEAN_LEVEL=""
```

>必须经过第一次完整编译才能用 OFFLINE_WORK 加快仓库的拉取检查。

###如何修改开机logo

> 看 BOOT_LOGO="yes" 和替换图片文件自动打包编译到二进制文件。

###配置开机启动服务脚本
因为系统默认不启动`/etc/rc.local`了，所以需要启动一下再往里面编辑脚本，一定要 & 挂在后台，不然就看不到交互终端了。

执行 `sudo nano /etc/systemd/system/rc-local.service` 后输入如下内容：
```
[Unit]
 Description=/etc/rc.local Compatibility
 ConditionPathExists=/etc/rc.local

[Service]
 Type=forking
 ExecStart=/etc/rc.local start
 TimeoutSec=0
 StandardOutput=tty
 RemainAfterExit=yes
 SysVStartPriority=99

[Install]
 WantedBy=multi-user.target
```
上述内容保存后执行以下命令
```
sudo systemctl enable rc-local #使能服务
chmod -x /etc/rc.local #更改文件权限
sudo systemctl start rc-local.service #启动服务
sudo systemctl status rc-local.service #查看服务运行状态
```
  
删除用户密码并关闭控制台输出到屏幕上和闪烁光标
查询服务 `systemctl status` 禁用服务 `systemctl disable getty@tty1.service` 即可关闭开机终端。
删除密码 `sudo passwd -d root` 之后输入 root 自动进入系统。
使用 `echo 0 > /sys/class/graphics/fbcon/cursor_blink` 关闭终端的光标闪烁`cursor_blink`，对应实现 `drivers/video/console/fbcon.c` 。

### 编译 aipu.ko 主线模块并加入 armbian 系统
需要结合上下两节食用。没有 linux 外部编译模块基础的，要先简单看过这篇 https://www.kernel.org/doc/Documentation/kbuild/modules.txt 来知道怎么添加外部模块参与编译（*.ko）。

这里提供了一份包含编译 aipu 的分支，你也可以在 linux 目录下外部编译 aipu.ko 模块出来。
将 `armbian-build/config/sources/families/sun50iw11.conf` 里的 KERNELSOURCE="`https://github.com/sipeed/linux`" 链接替换为`https://github.com/junhuanchen/linux/commits/r329-wip` 。即可采用新源进行 armbian 的编译。
偷懒就用临时配置好的 https://github.com/junhuanchen/armbian-build 仓库。

### 给镜像中添加自定义模块（deb）
kernel 的模块（.ko）由 kernel 添加，如果没有改变则删除 `armbian-build/output/debs/linux-image-edge-sun50iw11_21.08.0-trunk_arm64.deb` ，可手工可命令。

这里说一下 armbian 的 deb 手工打进去，因为有时候可能不是所有东西都需要，而云端下载太久，就需要提前下好包进去。

在 `armbian-build/config/cli/bullseye/main/config_cli_standard/packages.additional` 的末尾添加一下包就可以编译进去，其他的类似有 desktop 目录之类的。

打包某些 deb 包的时候经常会出现 `apt Hash Sum mismatch` 问题，设置成 `apt-get -o Acquire-by-hash=yes --fix-missing` 可以解决大部分问题。

### 常见问题后记
- boot 就不提了，看 https://github.com/sipeed/u-boot 就行，实际上全部交给 armbian-build 仓库就行，这样就具备了基础环境，要编辑的部分自然就很少了。

- 如果你发现模块加载不成功，可能是 `version magic '5.14.0-rc4-sun50iw11 SMP mod_unload aarch64' should be '5.14.0-rc7-01557-gd78f1b75fd69-dirty SMP preempt mod_unload aarch64'` 错误。这是模块加载不成功的常见 version magic 错误，简单的处理方法是修改 linux/include/linux/vermagic.h 直接怼到 `#define VERMAGIC_STRING "5.14.0-rc7-01557-gd78f1b75fd69-dirty"` 。
想要彻底解决上述这个问题，只能重新编译 armbian-build 导出镜像改变 kernel version 。