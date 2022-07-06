---
title: Tina sdk 目录结构

---

Tina Linux SDK 主要由构建系统、配置工具、工具链、host 工具包、目标设备应用程序、文档、脚本、linux 内核、bootloader 部分组成，下面是Tina主目录包含的文件和目录。

```
Tina-SDK/
├── build
├── config
├── Config.in
├── device
├── dl
├── lichee
├── Makefile
├── out
├── package
├── prebuilt
├── rules.mk
├── scripts
├── target
├── tmp
├── toolchain
└── tools
```

以下将对主要目录中包含的内容进行简单介绍。

## build
  
build 目录存放 Tina Linux 的构建系统文件，此目录结构下主要是一系列基于 Makefile 规格编写的 .mk 文件，主要的功能有：
1. 检测当前的编译环境是否满足 Tina Linux 的构建需求；
2. 生成 host 包编译规则；
3. 生成工具链的编译规则；
4. 生成 target 包的编译规则；
5. 生成 linux kernel 的编译规则；
6. 生成系统固件的生成规则。

## config
  
config 目录主要存放 Tina Linux 中配置菜单的界面以及一些固定的配置项，该配置菜单基于内核的 mconf 规格编写。

## device
  
devices 目录用于存放方案的配置文件，包括内核配置、env 配置、分区表配置、sys_config.fex（全志定制板级配置文件）、board.dts（linux标准设备树文件） 等。

> 这些配置在旧版本Tina（Tina3.0以前）上是保存于 target 目录下，现新版本均移到了 device 目录下，但 defconfig 仍保存在 target 目录下

## lichee
  
lichee 目录主要存放 bootloader、linux内核、DSP等代码，其中DSP代码及编译环境因涉及DSP供应商科声讯版权，需单独申请。lichee目录下结构如下：
```
Tina-SDK
    ├── brandy-2.0
    │   ├── build.sh
    │   ├── tools
    │   └── u-boot-2018
    └── linux-4.9
```

## package
  
package 目录存放Tina系统支持的软件包源码和编译规则，目录按照目标软件包的功能进行分类，该目录包含了Tina系统全平台（包括全志R/H/F/V/T系列）的软件包，但是并不是所有软件包都适配了R329方案，部分软件包需要开发者自行适配。

## prebuild
  
prebuild 目录存放预编译用的交叉编译器，主要包括aarch64的glibc和musl以及arm的glibc和musl。prebuild目录下结构如下：
```
Tina-SDK
└── linux-x86
    ├── aarch64
    │   ├── aarch64-toolchain.txt
    │   ├── toolchain-sunxi-glibc
    │   └── toolchain-sunxi-musl
    ├── arm
    │   ├── arm-toolchain.txt
    │   ├── toolchain-sunxi-glibc
    │   └── toolchain-sunxi-musl
    └── host
        └── host-toolchain.txt
```
## scripts
  
scripts 目录用于存放设备开发中用到的一些脚本。

## target
  
target目录用于存放开发板相关的配置以及 sdk 和 toolchain 生产的规格。

## toolchain
  
toolchain 目录用于存放交叉工具链构建配置、规则。

## tools
  
tools 目录用于存放 host 端工具的编译规则。

## out
  
out 目录用于保存编译相关的临时文件和最终镜像文件，编译后自动生成此目录，并生成对应的方案out目录，如开发板对应的R329-evb5方案目录结构如下：
```
Tina-SDK/out
├── host
└── r329-evb5
    ├── boot.img
    ├── compile_dir
    ├── image
    ├── md5sums
    ├── packages
    ├── r329-evb5-boot.img
    ├── r329-evb5-Image.gz
    ├── r329-evb5-uImage
    ├── rootfs.img
    ├── sha256sums
    ├── staging_dir
    └── tina_r329-evb5_uart0.img
```
其中 ：

- tina_r329-evb5_uart0.img 就是编译打包后生成的最终烧写到开发板上的固件；
- boot.img 为最终烧写到系统 boot 分区的数据；
- rootfs.img 为最终烧写到系统 rootfs 分区的数据；
- r329-evb5-uImage为内核的 uImage 格式镜像，若配置为 uImage 格式，则会拷贝成 boot.img；
- r329-evb5-boot.img为内核的 boot.img 格式镜像，若配置为 boot.img 格式，则会拷贝成 boot.img
- compile_dir 为 sdk 编译 host、target 和 toolchain 的临时文件目录，存有各个软件包的源码；
- packages 目录保存的是最终生成的 ipk 软件包。

另外 out 下的 host 目录用于存放 host 端的工具以及一些开发相关的文件。