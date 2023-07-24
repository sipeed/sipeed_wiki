---
title: revyos SDK 
keywords: Linux, Lichee, TH1520, SBC, RISCV
update:
  - date: 2023-07-21
    version: v1.2
    author: ztd
    content: 
      - Update English docs
  - date: 2023-07-03
    version: v1.1
    author: ztd
---

The SDK used by Sipeed is the one in this document.
The SDK is built locally using `make` to configure the build environment. The following build process runs on ubuntu-22.04, so please reserve about 20 gigabytes of space.

## Build environment configuration

First, install the required packages and set the environment variables.

```bash
export xuetie_toolchain=https://occ-oss-prod.oss-cn-hangzhou.aliyuncs.com/resource//1663142514282
export toolchain_file_name=Xuantie-900-gcc-linux-5.10.4-glibc-x86_64-V2.6.1-20220906.tar.gz
export toolchain_tripe=riscv64-unknown-linux-gnu-
export ARCH=riscv
export nproc=12 #Please set according to their own CPU configuration, the document uses cpu i5-11400
mkdir th1520_build && cd th1520_build
export GITHUB_WORKSPACE="~/th1520_build" #The assumptions in this article are downloaded to the user's directory and can be changed according to your needs.
sudo apt update && \
              sudo apt install -y gdisk dosfstools g++-12-riscv64-linux-gnu build-essential \
                                  libncurses-dev gawk flex bison openssl libssl-dev tree \
                                  dkms libelf-dev libudev-dev libpci-dev libiberty-dev autoconf device-tree-compiler
              sudo update-alternatives --install \
                  /usr/bin/riscv64-linux-gnu-gcc riscv64-gcc /usr/bin/riscv64-linux-gnu-gcc-12 10
              sudo update-alternatives --install \
                  /usr/bin/riscv64-linux-gnu-g++ riscv64-g++ /usr/bin/riscv64-linux-gnu-g++-12 10
```
**Note: When clone the following repo, please check whether it is the corresponding branch:**
**kernel branch is lpi4a**
**uboot branch is lpi4a**.
**opensbi branch is lpi4a**
**Please use the latest version for all repositories**

## 构建kernel

First, please clone the used repo and create the corresponding folder (the following paths assume that the root directory is under the user directory).

```shell
git clone https://github.com/revyos/thead-kernel.git kernel
```

Configuring the compilation toolchain

```shell
wget ${xuetie_toolchain}/${toolchain_file_name}
tar -xvf ${toolchain_file_name} -C /opt
export PATH="/opt/Xuantie-900-gcc-linux-5.10.4-glibc-x86_64-V2.6.1/bin:$PATH"
```

Create the installation target directory

```shell
mkdir rootfs && mkdir rootfs/boot
```

Build the kernel

```shell
pushd kernel
make CROSS_COMPILE=${toolchain_tripe} ARCH=${ARCH} revyos_defconfig
make CROSS_COMPILE=${toolchain_tripe} ARCH=${ARCH} -j$(nproc)
make CROSS_COMPILE=${toolchain_tripe} ARCH=${ARCH} -j$(nproc) dtbs
if [ x"$(cat .config | grep CONFIG_MODULES=y)" = x"CONFIG_MODULES=y" ]; then
    sudo make CROSS_COMPILE=${toolchain_tripe}  ARCH=${ARCH} INSTALL_MOD_PATH=${GITHUB_WORKSPACE}/rootfs/ modules_install -j$(nproc)
fi
sudo make CROSS_COMPILE=${toolchain_tripe}  ARCH=${ARCH} INSTALL_PATH=${GITHUB_WORKSPACE}/rootfs/boot zinstall -j$(nproc)
sudo make CROSS_COMPILE=riscv64-unknown-linux-gnu- ARCH=riscv INSTALL_MOD_PATH=${GITHUB_WORKSPACE}/rootfs/ modules_install -j$(nproc)
sudo make CROSS_COMPILE=riscv64-unknown-linux-gnu- ARCH=riscv INSTALL_PATH=${GITHUB_WORKSPACE}/rootfs/boot zinstall -j$(nproc)
```

Build perf (build as needed)

```shell
make CROSS_COMPILE=riscv64-unknown-linux-gnu- ARCH=riscv LDFLAGS=-static NO_LIBELF=1 NO_JVMTI=1 VF=1 -C tools/perf/
sudo cp -v tools/perf/perf ${GITHUB_WORKSPACE}/rootfs/sbin/perf-thead
```

Record commit-id

```shell
git rev-parse HEAD > kernel-commitid
sudo cp -v kernel-commitid ${GITHUB_WORKSPACE}/rootfs/boot/
```

Install kernel, device tree to target directory

```shell
sudo cp -v arch/riscv/boot/Image ${GITHUB_WORKSPACE}/rootfs/boot
sudo cp -v arch/riscv/boot/dts/thead/*.dtb ${GITHUB_WORKSPACE}/rootfs/boot/
popd
```

After that, you only need to copy or overwrite the contents of the rootfs to the corresponding directory. Note that the kernel image and kernel module directories must correspond to each other, or else the peripheral functions will be disabled due to the missing kernel module.

## Building uboot

Note that at this point, you are still in the th1520_build directory and have already configured the environment variables and toolchain, refer to building the kernel for the steps.

```shell
git clone https://github.com/revyos/thead-u-boot.git uboot
```

Note that at this point, you are still in the th1520_build directory and have already configured the environment variables and toolchain, refer to building the kernel for the steps.

```shell
pushd uboot
make ARCH=${ARCH} CROSS_COMPILE=${toolchain_tripe} light_lpi4a_defconfig
make ARCH=${ARCH} CROSS_COMPILE=${toolchain_tripe} -j$(nproc)
find . -name "u-boot-with-spl.bin" | xargs -I{} cp -av {} ${GITHUB_WORKSPACE}/rootfs/u-boot-with-spl.bin
popd
```

Check the output files
```shell
tree ${GITHUB_WORKSPACE}/rootfs
```

## Build opensbi

Note that at this point, you are still in the th1520_build directory and have already configured the environment variables and toolchain, refer to building the kernel for the steps.

```shell
git clone https://github.com/revyos/thead-opensbi.git opensbi
```

Then start executing the compile command

```shell
pushd opensbi
make PLATFORM=generic ARCH=${ARCH} CROSS_COMPILE=${toolchain_tripe} 
sudo install -D -p -m 644 build/platform/generic/firmware/fw_dynamic.bin \
"${GITHUB_WORKSPACE}/rootfs/boot/"
popd
```

Checking the output files

```shell
tree ${GITHUB_WORKSPACE}/rootfs
```

Pack the kernel, uboot, opensbi related files from the current build into a zip archive.

```shell
tar -zcvf kernel.tar.gz rootfs
```

To use the build files, just replace the files in the zip package to the appropriate locations.
Delete the files to be replaced in boot.ext4, then the files under rootfs/boot/ are put into boot.ext4;
Replace rootfs/lib/modules/ with the /lib/modules/ directory in rootfs.ext4;
If you have built perf, replace the files under rootfs/sbin with the files under /sbin in rootfs.ext4;
Just burn uboot directly.