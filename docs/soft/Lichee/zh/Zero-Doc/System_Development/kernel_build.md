

---

title: 主线Kernel基础编译
---

## 安装依赖

 `sudo apt install git wget make gcc flex bison libssl-dev bc kmod `     

## 安装交叉编译器

下载地址：<https://releases.linaro.org/components/toolchain/binaries/6.3-2017.05/arm-linux-gnueabihf/>

```
wget https://releases.linaro.org/components/toolchain/binaries/6.3-2017.05/arm-linux-gnueabihf/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf.tar.xz
tar xvf gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf.tar.xz
mv gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf /opt/
vim /etc/bash.bashrc
export PATH="$PATH:/opt/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/bin"
source /etc/bash.bashrc
arm-linux-gnueabihf-gcc -v
```

## 下载编译linux源码

(默认是zero-5.2.y分支)：--depth 1 指拉取最近一次更改，不然会拉取所有更改（警告，数据量爆炸！）

```
git clone -b zero-5.2.y --depth 1 https://github.com/Lichee-Pi/linux.git
```

修改makefile文件

```
cd linux
vim Makefile
[364]ARCH            = arm
[365]CROSS_COMPILE   = arm-linux-gnueabihf-
[366]INSTALL_MOD_PATH = out
```

分别是指定架构，交叉编译器，MOD安装位置。

如果涉及到多个编译链版本，可以不用写入环境变量，在这里直接绝对路径指定。

```
[365]CROSS_COMPILE   = /opt/gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf/bin/arm-linux-gnueabihf-
```

然后开始编译

```
cd linux

make licheepi_zero_defconfig
make menuconfig   #一般不用修改，需要时单独改
make -j16
make  -j16 modules #编译模块
make -j16 modules_install #安装模块
make dtbs #编译设备树
```

编译完成后，zImage在arch/arm/boot/下，驱动模块在out/lib下，设备树在arch/arm/boot/dts下。

然后把zImage，sun8i-v3s-licheepi-zero-dock.dtb放到第一分区

modules文件夹放入文件系统的lib下s

使用`modprobe xxx`加载模块。

编译过程中可能遇到以下问题：

> /usr/bin/ld: scripts/dtc/dtc-parser.tab.o:(.bss+0x20): multiple definition of `yylloc'; scripts/dtc/dtc-lexer.lex.o:(.bss+0x0): first defined here
> collect2: error: ld returned 1 exit status
> make[1]: *** [scripts/Makefile.host:99: scripts/dtc/dtc] Error 1

解决办法：

```
vim scripts/dtc/dtc-parser.tab.h
修改extern XXX yylloc 为yyloc
vim scripts/dtc/dtc-lexer.l
修改XXX yylloc 为 extern XXX yylloc
```



