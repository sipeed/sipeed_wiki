---
title: 常见问题
keywords: Linux, Lichee, TH1520, SBC, RISCV, Debian, Desktop
update:
  - date: 2023-10-30
    version: v1.2
    author: ztd
    content:
      - Update official development docs.
  - date: 2023-10-23
    version: v1.1
    author: ztd
    content:
      - Update NPU's FAQ
  - date: 2023-09-22
    version: v1.0
    author: ztd
    content:
      - Release docs
---
## 开箱体验
- 供电注意事项：
  1. USB-C仅支持5V输入，保险起见不要使用带快充功能的充电宝或者充电头供电
  2. 排针的IO均为1.8V电平，请使用配送的串口小板或者支持1.8V的串口小板
  3. 电脑USB一般只有5V1A，带不起来板子，板子至少需要5V2A，推荐5V3A的适配器供电，或者使用12V DC供电
  4. USB 丝印旁的 LED 闪烁，说明电源不稳定或短路
- 正式版与内测版硬件差异、USB限流说明见[板卡硬件说明](https://en.wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/2_unbox.html#%E6%9D%BF%E5%8D%A1%E7%A1%AC%E4%BB%B6%E8%AF%B4%E6%98%8E)

## 镜像集合
- 20230721之前版本的镜像，在16+128的核心板上存在无法正确识别内存大小的问题，需要更新镜像版本。若为20230706之后的版本，也可参考[镜像集合相关章节](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/3_images.html#%E5%86%85%E5%AD%98%E9%97%AE%E9%A2%98%E4%BF%AE%E5%A4%8D%E8%AF%B4%E6%98%8E)进行修复。
- 使用镜像前请仔细阅读wiki中镜像集合的使用说明，以保证下载的是预期镜像，比如使用10.1寸触摸屏需要烧录带MIPI后缀压缩包中的镜像。
- 安卓13镜像目前暂未进行外设支持，烧录后只有HDMI显示等基础功能。

## 烧录镜像
- Windows系统下烧录，请先确认驱动是否按照正确安装。若正确安装驱动，烧录时还是没有反应，可尝试更换 USB 线，注意使用的 USB 线必须是能供电和传输数据的线，并且烧录时使用的 USB 口尽量不要使用主机前面板的 USB 口，也不要使用笔记本电脑中的数据口，否则会因为供电原因导致识别不到设备。
- 想要切换启动模式，比如切换为从 SD 卡启动，正式版底板可以通过拨码开关（注意需要制作专用镜像）来切换，非正式版也可以通过传递启动参数来切换，详见[烧录镜像的对应章节](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/4_burn_image.html#U-Boot)。

## 桌面系统基础使用
- 若桌面下方启动器的图标功能异常，可以自己手动配置为自己想要的方案，也可以使用如下命令恢复为默认配置，默认配置效果参考[桌面系统基础使用相关章节](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/5_desktop.html#%E6%B5%8F%E8%A7%88%E5%99%A8)：
	```shell
	cp /etc/xdg/xfce4/panel/default.xml /home/sipeed/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml
	chown sipeed:sipeed /home/sipeed/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml
	```
- 若安装软件时遇到报错，请更新到最新镜像或参考[软件安装](https://en.wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/5_desktop.html#%E8%BD%AF%E4%BB%B6%E5%AE%89%E8%A3%85)

## 外设使用
1. 若要使用 NPU，请使用0920及以上版本的镜像；
2. 使用 JTAG 需要自行飞线，并在板子上设置 pinmux，参考[JTAG](https://en.wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/6_peripheral.html#JTAG)
3. 在接入外设较多时（比如 HDMI，USB键鼠）尽量使用12V DC供电。电脑的USB口若本身接入外设较多，可能会没有多余的能力给开发板及开发板所连接的外设供电。
4. 在使用 NPU 进行推理时，第一次运行时会在板上进行一次优化，这个过程比较慢。之后会生成 shl.hhb.bm 文件，使用这个权重文件进行推理会比较快。

## 系统开发
### revyos

1. 构建 kernel/uboot/opensbi 前，请检查这些环境变量是否设置好了
	```shell
	export toolchain_tripe=riscv64-unknown-linux-gnu-
	export ARCH=riscv
	export nproc=12
	export GITHUB_WORKSPACE="~/th1520_build"
	export PATH="/opt/Xuantie-900-gcc-linux-5.10.4-glibc-x86_64-V2.6.1/bin:$PATH"
	```
	以上环境变量请根据自身实际配置、文件路径等进行调整。
	构建后，在安装相应文件时也请检查对应的文件夹是否创建了，以及路径是否正确，比如 `rootfs` ，`rootfs/boot` 目录是否创建。

2. 由于工具链版本不同，不同 SDK 下构建的二进制文件不能混用。
3. 构建完烧录后若USB等外设功能失效，请检查 Image 和 modules(模块目录放到板子上的/lib/modules目录下) 是否对上。

### THead Yocto

1. 截至该 SDK 的 1.1.2 版本，使用 Docker 搭建该 SDK 的开发环境时需要更改 Dockerfile，具体改动参考[THead Yocto相关章节](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/7_develop_thead.html#%E6%90%AD%E5%BB%BAYocto%E7%BC%96%E8%AF%91%E7%8E%AF%E5%A2%83)：
	注释 Dockerfile 中 182 - 186 行：
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

3. 在使用 `MACHINE=light-lpi4a bitbake thead-image-linux` 命令构建镜像时，如果遇到在执行 `compile` 任务时崩溃，可能是内存不够。建议至少 32G 内存。

4. 由于网络原因，可能会出现下载失败或下载很慢的情况，推荐使用代理下载。

5. 若遇到如下报错：
	```text
	Please use a locale setting which supports utf-8.
	Python can't change the filesystem locale after loading so we need a utf-8 when python starts or things won't work.
	```
	请按照以下步骤解决：
	首先安装相应的依赖
	```shell
	sudo apt-get install locales
	sudo dpkg-reconfigure locales 
	```
	然后在打印出来的列表中找到 `en_US.UTF8` 这一项（典型位置在第158项）,输入这一项对应的序号后回车，接下来也选择这一项后回车。  
	完成上述设置步骤后接着运行如下命令（也可考虑将下面的命令加入到docker的 `.bashrc` 中）
	```shell
	sudo locale-gen en_US.UTF-8
	sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
	export LANG=en_US.UTF-8
	```
	完成上述步骤后再编译就不会出现原来的报错。

5. 若遇到类似如下报错：
	```text
	please install them in order to proceed: lz4c pzstd zstd
	```
	是缺少相关依赖，直接安装即可
	```shell
	sudo apt update && sudo apt install -y zstd liblz4-tool
	```
### Android

1. 对于国内用户，使用 Android SDK 下载源码时，若运行`repo init -u https://gitee.com/thead-android/local_manifests.git -b main_2023_7_7`命令始终不成功，可以尝试运行以下命令后，再进行 `repo init`
	```
	export REPO_URL='https://mirrors.tuna.tsinghua.edu.cn/git/git-repo/'
	```

2. 使用 docker 环境编译时，可能会遇到如下报错：
	```shell
	Build sandboxing disabled due to nsjail error. 
	```
	这个报错可以暂时忽略，不影响后面的编译步骤。若想运行 nsjail，可以尝试升级内核版本至5.XX或者启动 docker 时传入这些参数 `--security-opt apparmor=unconfined --security-opt seccomp=unconfined --security-opt systempaths=unconfined` 或 `--privileged`。

## 开发文档

请在[该链接](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/09_Doc)中下载。