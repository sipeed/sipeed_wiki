---
title: revyos SDK 
keywords: Linux, Lichee, TH1520, SBC, RISCV
update:
  - date: 2023-07-03
    version: v1.1
    author: ztd
---

Sipeed所使用的SDK是该文档中的SDK。
该SDK在本机配置编译环境使用`make`构建。且下述构建流程运行于ubuntu-22.04系统，请预留约20G空间。

## 编译环境配置

首先安装所需的软件包并设置好环境变量

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
**注意，clone下面的repo时请检查是否为对应分支：**
**kernel分支为lpi4a**
**uboot分支为lpi4a**
**opensbi分支为lpi4a**
**各仓库请使用最新版本**

## 构建kernel

首先请clone用到的repo，并建立好对应文件夹（下列路径均假设根目录为用户目录下）

```shell
git clone https://github.com/revyos/thead-kernel.git kernel
```
配置编译工具链

```shell
wget ${xuetie_toolchain}/${toolchain_file_name}
tar -xvf ${toolchain_file_name} -C /opt
export PATH="/opt/Xuantie-900-gcc-linux-5.10.4-glibc-x86_64-V2.6.1/bin:$PATH"
```

创建安装目标目录
```shell
mkdir rootfs && mkdir rootfs/boot
```

编译内核

```shell
pushd kernel
make CROSS_COMPILE=${toolchain_tripe} ARCH=${ARCH} revyos_defconfig
make CROSS_COMPILE=${toolchain_tripe} ARCH=${ARCH} -j$(nproc)
make CROSS_COMPILE=${toolchain_tripe} ARCH=${ARCH} -j$(nproc) dtbs
if [ x"$(cat .config | grep CONFIG_MODULES=y)" = x"CONFIG_MODULES=y" ]; then
    sudo make CROSS_COMPILE=${toolchain_tripe}  ARCH=${ARCH} INSTALL_MOD_PATH=${GITHUB_WORKSPACE}/rootfs/ modules_install -j$(nproc)
fi
sudo make CROSS_COMPILE=${toolchain_tripe}  ARCH=${ARCH} INSTALL_PATH=${GITHUB_WORKSPACE}/rootfs/boot zinstall -j$(nproc)
```

构建perf（根据需要构建）

```shell
make CROSS_COMPILE=riscv64-unknown-linux-gnu- ARCH=riscv LDFLAGS=-static NO_LIBELF=1 NO_JVMTI=1 VF=1 -C tools/perf/
sudo cp -v tools/perf/perf ${GITHUB_WORKSPACE}/rootfs/sbin/perf-thead
```

记录 commit-id

```shell
git rev-parse HEAD > kernel-commitid
sudo cp -v kernel-commitid ${GITHUB_WORKSPACE}/rootfs/boot/
```

安装内核、设备树到目标目录

```shell
sudo cp -v arch/riscv/boot/Image ${GITHUB_WORKSPACE}/rootfs/boot/
sudo cp -v arch/riscv/boot/dts/thead/light-lpi4a.dtb ${GITHUB_WORKSPACE}/rootfs/boot/
popd
```

之后只需要把rootfs中内容拷贝或覆盖到对应目录即可，注意内核Image和内核module目录一定要对应，不然会因缺失内核模块导致外设功能失效。

### 构建uboot
注意，此时仍在th1520_build目录下，且已经配置好环境变量和工具链，步骤参考构建kernel。

```shell
git clone https://github.com/revyos/thead-u-boot.git uboot
```

然后开始执行编译命令

```shell
pushd uboot
make ARCH=${ARCH} CROSS_COMPILE=${toolchain_tripe} light_lpi4a_defconfig
make ARCH=${ARCH} CROSS_COMPILE=${toolchain_tripe} -j$(nproc)
find . -name "u-boot-with-spl.bin" | xargs -I{} cp -av {} ${GITHUB_WORKSPACE}/rootfs/u-boot-with-spl.bin
popd
```

检查输出的文件

```shell
tree ${GITHUB_WORKSPACE}/rootfs
```

## 构建opensbi

注意，此时仍在th1520_build目录下，且已经配置好环境变量和工具链，步骤参考构建kernel。

```shell
git clone https://github.com/revyos/thead-opensbi.git opensbi
```

然后开始执行编译命令

```shell
pushd opensbi
make PLATFORM=generic ARCH=${ARCH} CROSS_COMPILE=${toolchain_tripe} 
sudo install -D -p -m 644 build/platform/generic/firmware/fw_dynamic.bin \
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
要使用构建的文件，则将压缩包中文件替换到相应位置即可。
将boot.ext4中要替换的文件删掉，然后rootfs/boot/下的文件放到boot.ext4中；
将rootfs/lib/modules/替换掉rootfs.ext4中的/lib/modules/目录；
若构建了perf了，将rootfs/sbin下的文件替换掉rootfs.ext4中/sbin下的文件；
uboot直接烧录即可。
