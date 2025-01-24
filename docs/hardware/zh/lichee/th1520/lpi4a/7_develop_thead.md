---
title: Yocto Linux  
keywords: Linux, Lichee, TH1520, SBC, RISCV, Kernel, SDK, Develop
update:
  - date: 2023-07-17
    version: v1.2
    author: ztd
    content:
      - Update docs
  - date: 2023-05-12
    version: v1.1
    author: wonder
    content:
      - Depart docs
  - date: 2023-05-08
    version: v1.0
    author: wonder
    content:
      - Release docs
---

TH1520 的官方开发环境是平头哥的基于 yocto 的开发环境，大家可以在这里获取开发环境： https://gitee.com/thead-yocto/   

本节简单介绍如何搭建 Linux Yocto 环境并使用 Yocto 构建可在开发板上运行的完整镜像。
**建议机器配置：内存64G以上，磁盘空间250G以上，编译时间因网络情况差异很大，在使用代理的情况下编译典型 linux 系统配置（最小系统加上必要的相关基础组件）时间约为8小时（CPU 为 i5-11400，时间供参考）**
**不推荐没有 Yocto 使用经验的用户使用此 SDK**

## 搭建Yocto编译环境

Linux SDK 使用 Yocto 构建镜像。Yocto 编译环境使用 Ubuntu18.04，推荐在 Linux 上使用 Docker 部署,也可直接在 Ubuntu18.04 下搭建环境（见[T-Head曳影1520Yocto用户指南.pdf](https://gitee.com/thead-yocto/documents/blob/master/zh/user_guide/T-Head%E6%9B%B3%E5%BD%B11520Yocto%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)2.2）。

这里仅介绍 Linux 上使用 Docker 部署的方式。
- 使用官方脚本安装 docker
	```bash
	curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
	```

- 下载 dockerfile 并修改用户名和 ID
	点击下载 [linux-dev-master.7z](https://gitee.com/thead-yocto/documents/blob/master/linux-dev-master.7z) 并解压后，进入到 `linux-dev-master` 目录，打开 `Dockerfile`，找到如下语句

	```bash
	ENV DOCKER_USER2 "your the same user name asyour host"`
	ENV USER2_ID "your user id"
	```

	将 "your the same user name asyour host" 改为用户 host os 的用户名，"your user id" 的值填写一个纯数值，代表uid，可以填写为100。

- 构建 docker 镜像环境
	```bash
	docker build -t linux-dev-base:base .
	```
	构建时若遇到如下报错：  
	```shell
	Dockerfile:183
	--------------------
	182 |     # install npm
	183 | >>> RUN cd $WORK_PATH \
	184 | >>>  && curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
	185 | >>>  && apt install -y nodejs yarn \
	186 | >>>  && npm install aiot-vue-cli -g
	187 |     
	--------------------
	ERROR: failed to solve: process "/bin/sh -c cd $WORK_PATH  && curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -  && apt install -y nodejs yarn  && npm install aiot-vue-cli -g" did not complete successfully: exit code: 100
	```
	
	则注释 Dockerfile 中 182 - 186 行：
	```shell
	# install npm
	#RUN cd $WORK_PATH \
	# && curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
	# && apt install -y nodejs yarn \
	# && npm install aiot-vue-cli -g
	```

	再执行 
	```shell
	docker build -t linux-dev-base:base .
	```
	
	容器安装完毕后，进入容器，再执行如下命令:
	```shell
	sudo apt update
	sudo apt install npm
	sudo apt install nodejs
	```

	最后执行:  
	```shell
	npm -v
	nodejs -v
	```

	有相关版本号输出即可。

	该 docker 镜像可以编译 thead 发布的 buildroot、yocto 等 Linux SDK。用户 `thead` 默认密码为 `123`。

- 启动 docker
	```bash
	docker run -u thead -dt --name linux-dev-{your_name} -v {your_lock_home}:{your_home} linux-dev-base:base /bin/bash
	```
	{your_name} 为容器名称，起名时不要重名。
	通过 -v 选项可以挂载宿主机的目录，起到类似共享文件的作用，{your_lock_home} 为宿主机的本地路径，{your_home} 为挂载在 docker 里的路径。

- 查看启动的 docker 容器
	```bash
	docker ps | grep linux-dev-base
	```
就能够看到刚刚启动的 docker 容器。

- 登录 docker
	```bash
	docker exec -it linux-dev-{your_name} /bin/bash
	```

- 下载开源软件包（仅在第一次获取 SDK 时才需要下载）
	构建固件时会从网上下载开源软件包，若网络较差，下载时间会比较长。为了加速这一过程，可以先到 gitee 下载离线开源软件包（假设下载到用户目录）
	```bash
	cd ~
	git clone https://gitee.com/thead-yocto/yocto-downloads.git
	```

- 下载 Yocto 构建包
	```bash
	git clone https://gitee.com/thead-yocto/xuantie-yocto.git -b Linux_SDK_V1.1.2
	```

- 加载目标设备的配置文件和环境变量（编译前记得检查是否加载）
	```bash
	cd xuantie-yocto
	source openembedded-core/oe-init-build-env thead-build/light-fm
	```

- 将前面下载的开源软件包通过共享 downloads 目录的方式软链接到 SDK 目录
	```bash
	ln -s ~/yocto-downloads ../downloads
	```

- 使用 patch

由于写文档时 xuantie-yocto 的 commit-d296c2345fe2c2521eb0e1a2772bcba637029bc8 还未合并下述 patch 中的改动，所以需要手动打 patch 来同步这些改动再进行后续开发。patch 文件请在[下载站](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/06_Patch)下载，请使用最新版本的patch 压缩包。

### xuantie-yocto 的 patch

0001-Allow-download-without-logging-in-gitee.patch
允许在没有登录的情况下拉取 gitee仓库

使用方法：
在 xuantie-yocto 路径下使用 patch

### kernel 的 patch

0001-pca9557.patch
使用 pca9557 替换 pcal9554 扩展芯片
0002-cpufreq-to-2GHz.patch
修改电压频率表与 cpu_freq 驱动，调整频率上限到 2GHz
0003-remove-audio-pcal9554b.patch
删除一路 i2c 扩展芯片与 lpi4a 的改动同步
0004-sync-audio-patch.patch
同步音频设备改动
0005-8G-ddr.patch
调整内存地址范围以支持 8G DRAM
0006-set-cpu_max_frq-1.992GHz.patch
根据用户手册提供的频点调整频率(约有2成不能在该频率下稳定工作)
0007-set-cpu_max_frq-1.848GHz.patch
所有1520能通过压力测试的频率
0012-riscv-dts-thead-lpi4a-add-PWM-Fan.patch
增加 PWM 风扇支持
0016-drm-dc8200-disable-gamma-lut-now.patch
失能 gamma lut，解决依赖问题
0017-drm-verisilicon-fix-fbcon.patch
修复 fbcon
0018-riscv-dts-thead-lpi4a-change-fan-PWM-frequency.patch
修改PWM频率参数，改善风扇噪声问题
0019-add-mipi-screec-and-touch-support.patch
添加 mipi 720p 屏幕和触摸屏驱动支持
0020-add-hdmi-audio-support.patch
添加 HDMI 音频驱动支持
0021-enable-pwm-fan.patch
使能 PWM 风扇
0022-add-mipi-camera-ov5693-support.patch
添加 OV5693 摄像头设备树支持

使用方法：
注意：使用先需要构建一次固件，否则 xuantie-yocto/thead-build/light-fm/tmp-glibc 路径不存在
在 xuantie-yocto/thead-build/light-fm/tmp-glibc/work/light_lpi4a-oe-linux/linux-thead/5.10.y-r0/linux-5.10.y路径下使用 patch

### opensbi 的 patch

0001-lib-sbi_illegal_insn-Add-emulation-for-fence.tso.patch
0002-lib-sbi_illegal_insn-Fix-FENCE.TSO-emulation-infinit.patch
以上两个patch模拟实现 fence.tso 指令，修复llvm崩溃问题

使用方法：
注意：使用先需要构建一次固件，否则 xuantie-yocto/thead-build/light-fm/tmp-glibc 路径不存在
在 xuantie-yocto/thead-build/light-fm/tmp-glibc/work/light_lpi4a-oe-linux/opensbi/0.9-r0/git 下使用 patch

### uboot 的 patch

0001-ENV_SETTINGS.patch
删除第4-6个分区，为 rootfs 预留足够的空间，使用 systemd 启动系统;
0002-fix-fix-bootargs.patch
修复设置启动参数命令
0003-fix-ftbfs.patch
修复 ftbfs 中的变量定义问题，更改后编译不会报错

使用方法：
注意：使用先需要构建一次固件，否则 xuantie-yocto/thead-build/light-fm/tmp-glibc 路径不存在
在 xuantie-yocto/thead-build/light-fm/tmp-glibc/work/light_lpi4a-oe-linux/u-boot/1_2020.10-r0/git路径下使用 patch

### vi-sensor 的 patch

0001-add-OV5693-support.patch
添加OV5693摄像头驱动支持

使用方法：
注意：使用先需要构建一次固件，否则 xuantie-yocto/thead-build/light-fm/tmp-glibc 路径不存在
在 xuantie-yocto/thead-build/light-fm/tmp-glibc/work/riscv64-oe-linux/vi-sensor/1.0-r0/git 路径下使用patch

### roofs 的 patch
bluetooth_fix.zip 
修复蓝牙无法正常使用的问题，使用方法见压缩包内 readme.txt

至此，编译环境已经配置完成。

## Machine/Target支持列表

在上面的加载环境变量步骤中，设置完成后可看到以下信息

```bash
### Shell environment set up for builds. ###
You can now run 'bitbake <target>'
Common targets are:
    thead-image-linux
    thead-image-multimedia
    thead-image-gui
machines:
    light-beagle
    light-b-product
    light-a-val
    light-lpi4a
```

相关说明如下
target（SDK 支持的镜像列表）：

|命名|描述|
|---|---|
|thead-image-linux|典型linux系统配置，最小系统加上必要的相关基础组件|
|thead-image-multimedia|典型linux系统+视频视觉配置，加上视频子系统的组件（Gstreamer等）|
|thead-image-gui|加上GUI相关组件的完整配置版本，包括Gnome桌面、weston、QT等应用组件等等|

**目前 thead-image-gui 选项编译出来的 GUI 相关组件仅用于功能性验证，进入不了图形化桌面**

machines（SDK 支持的板级配置）：

|命名|描述|
|---|---|
|light-a-val|TH1520-A EVB板|
|light-b-product|TH1520-B EVB板|
|light-beagle|beagleV-Ahead开发板|
|light-lpi4a|Lichee Pi 4A开发板|

## 构建镜像

构建命令格式如下：

```bash
MACHINE={machine} bitbake {target}
```

将其中的 {machine} 和 {target} 部分替换为上面两个表格中对应的命名即可。例如，编译一个在 LicheePi 4A 开发板上运行的典型 Linux 镜像的命令如下：

```bash
MACHINE=light-lpi4a bitbake thead-image-linux
```
### 构建镜像时可能会出现的问题

- 由于网络原因，这一步可能仍会出现下载失败或下载很慢的情况，有条件的话推荐使用代理。
- 报错信息
	```bash
	Please use a locale setting which supports utf-8.
	Python can't change the filesystem locale after loading so we need a utf-8 when python starts or things won't work.
	```
	首先运行如下命令
	```bash
	sudo apt-get install locales
	sudo dpkg-reconfigure locales 
	```
	然后在打印出来的列表中找到`en_US.UTF8`这一项（大概在第158项）,输入这一项对应的序号后回车，接下来也选择这一项后回车。
	完成上述设置步骤后接着运行如下命令（也可考虑将下面的命令加入到docker的`.bashrc`中）
	```bash
	sudo locale-gen en_US.UTF-8
	sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
	export LANG=en_US.UTF-8
	```
	完成上述步骤后再编译就不会出现原来的报错。
- 报错信息
	```bash
	please install them in order to proceed: lz4c pzstd zstd
	```
	安装对应的依赖即可
	```bash
	sudo apt update && sudo apt install -y zstd liblz4-tool
	```
### 镜像打包

在 [light_deploy_images](https://gitee.com/thead-yocto/light_deploy_images/tree/master/tarball) 仓库中，包含了一些预发布镜像。对于刚刚编译好的镜像，可以利用这个仓库中的 `sdk.sh` 脚本来进行打包。
首先切换到已经编译好的镜像中的 `light-fm` 目录下，将该仓库中的 `sdk.sh` 移动到这里即可。直接运行该脚本 `./sdk.sh` 即可，打包后会生成相应的镜像，相应文件的位置以及镜像目录的结构参考 [light_deploy_images](https://gitee.com/thead-yocto/light_deploy_images/tree/master/tarball) 仓库。
最后，可以将 docker 编译好的镜像及相关文件复制到先前通过 -v 选项挂载的共享文件夹中，宿主机即可使用该文件进行烧录。

到这里，我们已经完成了编译和打包，得到了一个可以烧录到开发板中运行的镜像。
**使用该镜像时，需要手动到 uboot 中利用环境变量设置一个 MAC 地址，参考命令如下**
```shell
# 将下列两个地址替换为你的 MAC 地址，eth1addr 的值为ethaddr 的值+1
setenv ethaddr=XX:XX:XX:XX:XX:XX
setenv eth1addr=XX:XX:XX:XX:XX:XX
env save
```

简单介绍yocto中的常用概念和一些实用技巧。

### 基础概念

Yocto用来构建定制的Linux镜像，有广泛的硬件支持，它是一个集合了很多工具的开源项目。
先对Yocto在构建镜像时的大致工作流程简单介绍：
Fetch->Extract->Patch->Configure->Build->Install->Package
Fetch：在编译时获取需要的源码。
Extract：对获取到的源码进行解压。
Patch：应用补丁以修复bug和添加新功能。
Configure：配置开发环境。
Build：构建镜像，编译链接。
Install：拷贝文件到目标目录。
Package：镜像打包。
下图展示了流程中的一些具体步骤：

![yocto_flows](./assets/develop_thead/yocto_flows.png)

Yocto project的大概构成如下图，构建所用到的主要是OpenEmbedded构建系统（下文用OE简称），它的核心是任务执行器Bitbake。

![yocto_structure](./assets/develop_thead/yocto_structure.png)

常用到的一些概念如下：
recipes：以`.bb`结尾的文件，里面会包含下载软件包时需要的相关信息，如下载固定源码的文件位置，需要应用到该软件包的patch信息,编译需要的信息等。例如`xuantie-yocto`的中的`gnome-shell`，它的recipes文件存储在`/home/thead/xuantie-yocto/meta-openembedded/meta-gnome/recipes-gnome/gnome-shell`目录下。
build directory：该目录即为构建时的输出目录，同时也会存放一些环境配置文件，`source`命令指定编译环境时就会生成该目录，默认命名为`build`，也可在`source`时更改为其他名字，如`sourece oe-init-build-env mybuild`。
configurations：以`.conf`结尾的文件，主要是配置文件。比如存储在`build directory`的`conf`目录中的`local.conf`，在编译时可能会在根据需要更改其中一些参数。
layers：通常会在这里存储所需要的各种metadata(如，`.bb`文件，`patches`和一些其他的附加文件)，主要是用于告诉OE构建系统如何构建目标文件。将metadata按层分类有助于项目维护。
bitbake：OE构建系统中用来执行各种任务的任务执行器。

## 常用操作

### 常用task

Yocto以package为单位管理开源软件组件，如需要编译某个package，方法如下：
```shell
bitbake "package-name"
```
每个package都在recipes文件中定义支持的task，有些task如clean，是所有包通用的，可以用一下命令列出package支持的task：

```shell
bitbake "package-name" -c listtasks
```

### 查找编译后package的位置

Yocto集成了大量开源的package，这些 package 编译的时候的工作目录通常在以下目录：
- tmp-glibc/work/riscv64-oe-linux  
- tmp-glibc/work/${MACHINE} 

例如
```shell
thead@b9461db16a58:~/xuantie-yocto/thead-build/light-fm/tmp-glibc/work/light_lpi4a-oe-linux/u-boot$ tree -L 2
.
└── 1_2020.10-r0
    ├── 0001-no-strip-fw_printenv.patch
    ├── build
    ├── deploy-debs
```
可以通过`bitbake -e linux-thead | grep ^S=`命令查找package目录。例如，查看内核的编译目录
```shell
$ bitbake -e linux-thead | grep ^S=
S="/home/thead/xuantie-yocto/thead-build/light-fm/tmp-glibc/work/light_a_val-oe-linux/linux-thead/5.10.y-r0/linux-5.10.y"
```
编译完成后文件输出的位置，例如，镜像编译完成后相关的各类文件都位于`light-fm/tmp/glibc/work/light_lpi4a-oe-linux`下，例如镜像就位于该目录的`linux-thead`下，最后只需要打包即可。

### 编译时fetch包的速度过慢

在编译时，可能会遇到fetch包过慢问题，这是除了使用代理，也可以将包下载到本地，然后根据得到的包地址让fetch时直接使用本地的repo。例如：
```shell
WARNING: bzip2-native-1.0.8-r0 do_fetch: Failed to fetch URL git://sourceware.org/git/bzip2-tests.git;name=bzip2-tests;branch=master, attempting MIRRORS if available
```
那么可以使用如下命令找到包的下载地址
```shell
$ bitbake -e bzip2 | grep ^SRC_URI=
SRC_URI="https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz            git://sourceware.org/git/bzip2-tests.git;name=bzip2-tests;branch=master            file://configure.ac;subdir=bzip2-1.0.8            file://Makefile.am;subdir=bzip2-1.0.8            file://run-ptest            "
```
得到地址后，手动将该仓库`clone`下来，然后找到它对应的`.bb`文件
```shell
$ find -name bzip*.bb
./openembedded-core/meta/recipes-extended/bzip2/bzip2_1.0.8.bb
```
在该文件中找到`SRC_URI`这一项
```shell
SRC_URI = "https://sourceware.org/pub/${BPN}/${BPN}-${PV}.tar.gz \
           git://sourceware.org/git/bzip2-tests.git;protocol=file;name=bzip2-tests;branch=master \
           file://configure.ac;subdir=${BP} \
           file://Makefile.am;subdir=${BP} \
           file://run-ptest \
           "
```
加上`protocol`指定为`file`，若需要切换分支，直接在`clone`下来的本地repo中`checkout`到对应的分支即可，修改好后，直接fetch这个包即可。
```shell
bitbake bzip2 -c fetch
```
若编译速度过慢，找到`build_directory`的`conf`目录下的`local.conf`文件，修改相应的参数即可，参考[此文档](https://docs.yoctoproject.org/dev-manual/speeding-up-build.html?highlight=bb_numbers)，例如，增加下载和编译时的速度，可以在文件中增加如下代码，将并行数量调大（注意根据CPU具体参数来）
```
BB_NUMBER_THREADS = '16'
PARALLEL_MAKE = '-j 12'
```
yocto编译后对package有缓存机制，可以在后面编译时减少所花费的时间。
除此之外，也可在编译前提前下载好一些包，放入某个文件夹，然后在`build_directory`的`conf`文件夹的`local.conf`找到`DL_DIR`这一项，这就是共享文件夹，更改到指定目录或软链接共享即可。

### 单独构建u-boot

在编译时将源码下载到`light-fm/tmp-glibc/work/light_lpi4a-oe-linux/u-boot/1_2020.10-r0/git`路径下（倒数第二级目录名为版本号），修改源码后执行该命令即可：
```shell
bitbake u-boot -C compile
```
### 单独构建opensbi

在编译时将源码下载到`light-fm/tmp-glibc/work/light_lpi4a-oe-linux/opensbi/0.9-r0/git`路径下，修改源码后执行该命令即可：

```shell
bitbake opensbi -C compile
```
-----
编译完成后，为了简化打包流程，在`light_deploy_images`提供了打包脚本`sdk.sh`。编译完成后，在`light-fm`文件夹下创建一个`sdk`文件夹，将该镜像打包脚本下载到该文件夹下，运行即可。
打包后典型的目录结构应如下所示：

```shell
.
├── deb
│   ├── all
│   ├── light_lpi4a
│   └── riscv64
├── images
│   └── light-lpi4a
│       ├── boot.ext4
│       ├── light_fastboot_image_single_rank
│       │   └── u-boot-with-spl.bin
│       ├── rootfs.thead-image-linux.ext4
│       └── vmlinux
├── sdk.sh
└── tarball
    └── prebuild_light-lpi4a.tar.gz
```

烧录时主要是用`images`目录下的文件，如果少了哪个文件，也可以手动复制进去。`tarball`目录下为打包好的镜像文件的压缩包，`deb`目录下为软件包。
参考：
[bitbake官方文档](https://docs.yoctoproject.org/bitbake.html?highlight=bitbake)
[yocto官方文档](https://docs.yoctoproject.org/overview-manual/yp-intro.html)
[T-Head 曳影 1520 Yocto 用户指南](https://gitee.com/thead-yocto/documents/raw/master/zh/user_guide/T-Head%E6%9B%B3%E5%BD%B11520Yocto%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)


## 设备树解析

TODO  

## 其他参考资料

**light_deploy_images 仓库：**

- 包含已经构建好可烧录的 Linux Image，打包镜像脚本以及其他相关工具，详见仓库。
- 仓库地址：[https://gitee.com/thead-yocto/light_deploy_images](https://gitee.com/thead-yocto/light_deploy_images)

**documents 仓库：**

- 包含所有发布的 SDK 相关文档
- 仓库地址：[https://gitee.com/thead-yocto/documents](https://gitee.com/thead-yocto/documents)

欢迎投稿～ 投稿接受后可得￥5～150（$1~20）优惠券！
