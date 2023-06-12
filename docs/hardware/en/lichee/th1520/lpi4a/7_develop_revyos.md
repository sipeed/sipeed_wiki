## revyos SDK 
Sipeed所使用的SDK是该文档中的SDK。
该SDK在本机配置编译环境使用`make`构建。且下述构建流程运行于ubuntu-22.04系统，请预留约20G空间。
### 编译环境配置
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
**gpu驱动模块分支为master**
**uboot分支为lpi4a**
**opensbi分支为lpi4a**
**各仓库请使用最新版本**
### 构建kernel
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
编译驱动模块
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
### 提示
第一次修改源码编译后，若只替换内核部分可能会导致USB hub无法正常工作，因为USB是模块，还需要将编译出来的/lib/modules这个目录整个替换进去，并且替换时注意编译后使用的内核版本是否对应这里的版本（可在kernel中使用uname -r查看你现在所使用的版本信息）