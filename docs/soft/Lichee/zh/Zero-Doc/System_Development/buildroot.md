# licheepi buildroot根文件系统

buildroot可用于构建小型的linux根文件系统。

大小最小可低至2M，与内核一起可以放入最小8M的spi flash中。

buildroot中可以方便地加入第三方软件包（其实已经内置了很多），省去了手工交叉编译的烦恼。

美中不足的是不支持包管理系统，没有gcc等。

## 下载安装

首先安装一些依赖，比如linux头文件：

```
apt-get install linux-headers-$(uname -r)
apt-get install libncurses5-dev
apt-get install wget
apt-get install gcc automake autoconf libtool make
```

然后下载安装：

```none
wget https://buildroot.org/downloads/buildroot-2017.08.tar.gz
tar xvf buildroot-2017.08.tar.gz
cd buildroot-2017.08/
make menuconfig
```

## 配置

看下ubootroot的目录结构

 ```
 .
 ├── arch: #存放CPU架构相关的配置脚本，如arm/mips/x86,这些CPU相关的配置，在制作工具链时，编译uboot和kernel时很关键.
 ├── board
 ├── boot
 ├── CHANGES
 ├── Config.in
 ├── Config.in.legacy
 ├── configs: #放置开发板的一些配置参数. 
 ├── COPYING
 ├── DEVELOPERS
 ├── dl: #存放下载的源代码及应用软件的压缩包. 
 ├── docs: #存放相关的参考文档. 
 ├── fs: #放各种文件系统的源代码. 
 ├── linux: #存放着Linux kernel的自动构建脚本. 
 ├── Makefile
 ├── Makefile.legacy
 ├── output: #是编译出来的输出文件夹. 
 │   ├── build: #存放解压后的各种软件包编译完成后的现场.
 │   ├── host: #存放着制作好的编译工具链，如gcc、arm-linux-gcc等工具.
 │   ├── images: #存放着编译好的uboot.bin, zImage, rootfs等镜像文件，可烧写到板子里, 让linux系统跑起来.
 │   ├── staging
 │   └── target: #用来制作rootfs文件系统，里面放着Linux系统基本的目录结构，以及编译好的应用库和bin可执行文件. (buildroot根据用户配置把.ko .so .bin文件安装到对应的目录下去，根据用户的配置安装指定位置)
 ├── package：#下面放着应用软件的配置文件，每个应用软件的配置文件有Config.in和soft_name.mk。
 ├── README
 ├── support
 ├── system
 ├── toolchain
 └── utils               # 实用工具
 ```

一般通过make xxx_defconfig来选择一个defconfig，这个文件在configs目录下。

当configs中不存在对应的开发板时，我们就要手动从头配置一遍。

使用`make config`进入配置界面。

```
Target options  --->选择目标板架构特性。
Build options  --->配置编译选项。
Toolchain  ---> 配置交叉工具链，使用buildroot工具链还是外部提供。
System configuration  --->
Kernel  --->
Target packages  --->
Filesystem images  --->
Bootloaders  --->
Host utilities  --->
Legacy config options  --->
```

### 选中Target options以选择licheepi对应的架构

licheepi用的v3s cpu 参数如下

```
CPU
ARM Cortex A7 @ 1.2GHz
Support NEON Advanced SIMD instruction
VFPv4 Floating Point Unit
```

选择相应的参数

```
Target Architecture (ARM (little endian))  --->
Target Binary Format (ELF)  --->
Target Architecture Variant (cortex-A7)  ---> 
Target ABI (EABIhf)  ---> 
Floating point strategy (VFPv4-D16)  ---> 
ARM instruction set (ARM)  --->
```

### Build options主要配置以下一些内容

- 配置文件保存位置，将配置文件保存的好处是，在重新构建时，只需要调用make <xxx_defconfig>然后make,而不必重新全部配置。

  示例：`$(CONFIG_DIR)/condigs/LicheePi_Zero_defconfig `,。然后`make savedefconfig`保存配置文件。

- 配置下载位置，因为系统构建的时候需要从网络上抓起很多软件报的代码进行编译构建。这个一般不需要修改。

- strip target binaries建议使能，这样会使文件尺寸变小。

- 对于其他的选项基本可以不做修改。

### Toolchain 配置交叉工具链

因为之前开发uboot和内核都用到了自己下载的工具链，所以这里也配置成外部工具链。没有的话先配置工具链

```
wget https://releases.linaro.org/components/toolchain/binaries/6.3-2017.05/arm-linux-gnueabihf/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf.tar.xz
tar xvf gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf.tar.xz
mv gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf /opt/
vim /etc/bash.bashrc
# add: PATH="$PATH:/opt/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/bin"
source /etc/bash.bashrc
arm-linux-gnueabihf-gcc -v
```

出现以下信息则配置成功。

```
Thread model: posix
gcc version 6.3.1 20170404 (Linaro GCC 6.3-2017.05) 
```

- 配置成外部工具链

```
Toolchain type (External toolchain)  --->
x   ( ) Buildroot toolchain
x   (X) External toolchain
```

- 在本机上外部工具链配置为：
  **/opt/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/**

  选中`() Toolchain path (NEW)`，填入path

  ```
  (/opt/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/) Toolchain path
  ```

- Toolchain prefix前缀是： **arm-linux-gnueabihf**

  

- External toolchain gcc version：我们使用的是6.3版本,选中6.x

- External toolchain kernel headers series：是在
  **arm-linux-gnueabihf/libc/usr/include/linux/version.h**
  里读取内核版本信息。本机的版本是4.6(263680=0x040600, 即4.6.0)

  ```
  cat /opt/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/arm-linux-gnueabihf/libc/usr/include/linux/version.h 
  #define LINUX_VERSION_CODE 263680
  ```

- External toolchain C library还是选择传统的glibc。需要小体积可以选uclibc（需要自行编译安装）。然后勾选上 `[] Toolchain has C++ support?`

### System configuration 配置系统参数

- System hostname：根据需要定义一个字符串，是控制台前面的提示符xxx@vsi，这里改为 `(licheepi) System hostname`
-  Init system：这里选择busybox，轻量级使用非常广泛。可选的有systemV,systemd.
- Root password配置登录密码。

### Target package

用于配置一些软件包，例如QT5

```
Target packages  --->
x  Graphic libraries and applications (graphic/text)  --->
xx   [*] Qt5  ---> 
```

有时候下载速度慢，可以复制make时打印的下载链接，使用迅雷等下载好后，拷贝到dl目录下，会自动识别。

## Ⅲ、编译

make.注意还要安装一下依赖，

  ```
  apt-get install g++ patch cpio python unzip rsync bc
  ```

不然会报：

```
You may have to install 'g++' on your build machine
You must install 'patch' on your build machine
You must install 'cpio' on your build machine
You must install 'python' on your build machine
You must install 'unzip' on your build machine
You must install 'rsync' on your build machine
You must install 'bc' on your build machine
```

如果编译busybox时出现

```
arm-linux-gnueabihf-gcc: error: unrecognized argument in option '-march=i586'
```

并且make clean后仍然报错的，可以试试make clean all（不知道啥原理但是好使了）

编译完成后会在output/images下生成rootfs.tar, 解压到第二分区后就能使用了。

默认失能串口登录，需要修改 **/etc/inittab** :

```none
tyS0::respawn:/sbin/getty -L ttyS0 115200 vt100 # GE
```

