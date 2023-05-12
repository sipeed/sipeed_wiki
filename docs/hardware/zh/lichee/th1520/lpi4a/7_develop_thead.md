---
title: 系统开发
keywords: Linux, Lichee, TH1520, SBC, RISCV, Kernel, SDK, Develop
update:
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

## Yocto Linux  

TH1520 的官方开发环境是平头哥的基于 yocto 的开发环境，大家可以在这里获取开发环境： https://gitee.com/thead-yocto/   

本节简单介绍如何搭建 Linux Yocto 环境并使用 Yocto 构建可在开发板上运行的完整镜像。

### 搭建Yocto编译环境

Linux SDK 使用 Yocto 构建镜像。Yocto 编译环境使用 Ubuntu18.04，推荐在 Linux 上使用 Docker 部署,也可直接在 Ubuntu18.04 下搭建环境（见[T-Head曳影1520Yocto用户指南.pdf](https://gitee.com/thead-yocto/documents/blob/master/zh/user_guide/T-Head%E6%9B%B3%E5%BD%B11520Yocto%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)2.2）。

这里仅介绍 Linux 上使用 Docker 部署的方式。**建议编译机器预留200G磁盘空间，内存为4G以上，编译时间因网络情况差异很大，在使用代理的情况下编译典型linux系统配置（最小系统加上必要的相关基础组件）时间约为1.5h（CPU为i5-11400，时间供参考）**。
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
	将 "your the same user name asyour host" 改为用户 host os 的用户名，"your user id" 的值对应该用户的密码。
- 构建 docker 镜像环境
	```bash
	docker build -t linux-dev-base:base .
	```
	这里下载的软件包的时候可能会有些报错，可以在 Dockerfile 中进行相应的修改，等到创建好 docker 后登录到 docker 中再进行下载。这个 docker 镜像可以编译 thead 发布的 buildroot、yocto 等 Linux SDK。默认密码为 `123`。
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

至此，搭建环境已经完成。

### Machine/Target支持列表

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

machines（SDK 支持的板级配置）：

|命名|描述|
|---|---|
|light-a-val|TH1520-A EVB板|
|light-b-product|TH1520-B EVB板|
|light-beagle|beagleV-Ahead开发板|
|light-lpi4a|Lichee Pi 4A开发板|

### 构建镜像

构建命令格式如下：

```bash
MACHINE={machine} bitbake {target}
```

将其中的 {machine} 和 {target} 部分替换为上面两个表格中对应的命名即可。例如，编译一个在 LicheePi 4A 开发板上运行的典型 Linux 镜像的命令如下：

```bash
MACHINE=light-lpi4a bitbake thead-image-linux
```
#### 构建镜像时可能会出现的问题

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

### 设备树解析

TODO  

### 其他参考资料

**light_deploy_images 仓库：**

- 包含已经构建好可烧录的 Linux Image，打包镜像脚本以及其他相关工具，详见仓库。
- 仓库地址：[https://gitee.com/thead-yocto/light_deploy_images](https://gitee.com/thead-yocto/light_deploy_images)

**documents 仓库：**

- 包含所有发布的 SDK 相关文档
- 仓库地址：[https://gitee.com/thead-yocto/documents](https://gitee.com/thead-yocto/documents)

<!-- ## Mainline Linux

TODO  

## OpenWRT

TODO

## Andriod 
TODO  

## OpenHarmony  
TODO 


                    {
                      "label":"THead Yocto",
                      "file":"lichee/th1520/lpi4a/7_develop_thead.md"
                    },
                    {
                      "label":"Mainline Linux",
                      "file":"lichee/th1520/lpi4a/7_develop_mainline.md"
                    },
                    {
                      "label":"Andriod",
                      "file":"lichee/th1520/lpi4a/7_develop_andriod.md"
                    },
                    {
                      "label":"Other",
                      "file":"lichee/th1520/lpi4a/7_develop_other.md"
                    }
-->

## Others

简单介绍在本机配置编译环境并使用`make`构建。该构建流程运行于ubuntu-22.04系统，请预留约20G空间。
首先安装所需的软件包并设置好环境变量就配置好了构建所需环境
```
export xuetie_toolchain=https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1663142514282
export toolchain_file_name=Xuantie-900-gcc-linux-5.10.4-glibc-x86_64-V2.6.1-20220906.tar.gz
export toolchain_tripe=riscv64-unknown-linux-gnu-
export ARCH=riscv
export nproc=12 #请根据自身CPU配置设置，该文档使用cpu为i5-11400
mkdir th1520_build && cd th1520_build
export GITHUB_WORKSPACE="~/th1520_build" #本文假设均下载到用户目录下，可根据自身需要更改
sudo apt update && \
              sudo apt install -y gdisk dosfstools g++-12-riscv64-linux-gnu build-essential \
                                  libncurses-dev gawk flex bison openssl libssl-dev tree \
                                  dkms libelf-dev libudev-dev libpci-dev libiberty-dev autoconf device-tree-compiler
              sudo update-alternatives --install \
                  /usr/bin/riscv64-linux-gnu-gcc riscv64-gcc /usr/bin/riscv64-linux-gnu-gcc-12 10
              sudo update-alternatives --install \
                  /usr/bin/riscv64-linux-gnu-g++ riscv64-g++ /usr/bin/riscv64-linux-gnu-g++-12 10
```
#### 构建kernel
首先请clone用到的repo，并建立好对应文件夹（下列路径均假设根目录为用户目录下）
```shell
git clone https://github.com/revyos/thead-kernel.git kernel
git clone https://github.com/revyos/gpu_bxm_4_64-kernel.git img_module
```
配置编译工具链
```shell
mkdir rootfs && mkdir rootfs/boot
wget ${xuetie_toolchain}/${toolchain_file_name}
tar -xvf ${toolchain_file_name} -C /opt
export PATH="/opt/Xuantie-900-gcc-linux-5.10.4-glibc-x86_64-V2.6.1/bin:$PATH"
```
编译内核
```shell
pushd kernel
make CROSS_COMPILE=${toolchain_tripe} ARCH=${ARCH} light_defconfig
make CROSS_COMPILE=${toolchain_tripe} ARCH=${ARCH} -j$(nproc)
make CROSS_COMPILE=${toolchain_tripe} ARCH=${ARCH} -j$(nproc) dtbs
if [ x"$(cat .config | grep CONFIG_MODULES=y)" = x"CONFIG_MODULES=y" ]; then
sudo make CROSS_COMPILE=${toolchain_tripe} ARCH=${ARCH} INSTALL_MOD_PATH=${GITHUB_WORKSPACE}/rootfs/ modules_install -j$(nproc)
fi
sudo make CROSS_COMPILE=${toolchain_tripe} ARCH=${ARCH} INSTALL_PATH=${GITHUB_WORKSPACE}/rootfs/boot zinstall -j$(nproc)
```
初步打包内核、设备树文件
```shell
sudo cp -v arch/riscv/boot/Image ${GITHUB_WORKSPACE}/rootfs/boot/
sudo cp -v arch/riscv/boot/Image.gz ${GITHUB_WORKSPACE}/rootfs/boot/
sudo cp -v arch/riscv/boot/dts/thead/*.dtb ${GITHUB_WORKSPACE}/rootfs/boot/
popd
```
编译模块
```shell
export PVR_BUILD_DIR=thead_linux
export PVR_ARCH=rogue
export RGX_BVNC=36.52.104.182
export RGX_BNC=36.52.104.182
export CROSS_COMPILE=${toolchain_tripe}

pushd img_module/rogue_km
export KERNELDIR=${GITHUB_WORKSPACE}/kernel/
make
for kernel_version in $(ls ${GITHUB_WORKSPACE}/rootfs/lib/modules/);
do
	  sudo install -D -p -m 644 binary_thead_linux_wayland_release/target_riscv64/kbuild/drm_nulldisp.ko \
"${GITHUB_WORKSPACE}/rootfs/lib/modules/${kernel_version}/extra/drm_nulldisp.ko"
	sudo install -D -p -m 644 binary_thead_linux_wayland_release/target_riscv64/kbuild/pvrsrvkm.ko \
"${GITHUB_WORKSPACE}/rootfs/lib/modules/${kernel_version}/extra/pvrsrvkm.ko"
	sudo depmod -a -b "${GITHUB_WORKSPACE}/rootfs" "${kernel_version}"
done
popd
```
查看编译生成的文件
```shell
tree ${GITHUB_WORKSPACE}/rootfs
```
### 构建uboot
注意，此时仍在th1520_build目录下，且已经配置好环境变量和工具链，步骤参考构建kernel。
```shell
git clone https://github.com/revyos/thead-u-boot.git uboot
```
然后开始执行编译命令
```shell
pushd uboot
sed -i "s/YYLTYPE yylloc;/extern YYLTYPE yylloc;/" scripts/dtc/dtc-lexer.l
make ARCH=${ARCH} CROSS_COMPILE=${toolchain_tripe} light_lpi4a_defconfig
make ARCH=${ARCH} CROSS_COMPILE=${toolchain_tripe} -j$(nproc)
find . -name "u-boot-with-spl.bin" | xargs -I{} cp -av {} ${GITHUB_WORKSPACE}/rootfs/boot/u-boot-with-spl-lpi4a.bin
popd
```
上述过程中，可能会遇到重复定义`YYLTYPE yylloc`问题，按照报错信息找到重复定义的那一行删掉多余的`extern`即可，典型文件位置如下`uboot/scripts/dtc/dtc-lexer.lex.c`。
检查输出的文件
```shell
tree ${GITHUB_WORKSPACE}/rootfs
```
### 构建opensbi
注意，此时仍在th1520_build目录下，且已经配置好环境变量和工具链，步骤参考构建kernel。
```shell
git clone https://github.com/revyos/thead-opensbi.git opensbi
```
然后开始执行编译命令
```shell
pushd opensbi
make PLATFORM=generic ARCH=${ARCH} CROSS_COMPILE=${toolchain_tripe} 
sudo install -D -p -m 644 build/platform/generic/firmware/fw_payload.bin \
"${GITHUB_WORKSPACE}/rootfs/boot/"
popd
```
检查输出的文件
```
tree ${GITHUB_WORKSPACE}/rootfs
```
将目前构建好的kernel, uboot, opensbi相关文件打包为压缩包
```shell
tar -zcvf kernel.tar.gz rootfs
```
完成上述步骤后仍可以继续使用yocto来进行开发，yocto使用技巧可参考thead-yocto相关介绍。

欢迎投稿～ 投稿接受后可得￥5～150（$1~20）优惠券！
