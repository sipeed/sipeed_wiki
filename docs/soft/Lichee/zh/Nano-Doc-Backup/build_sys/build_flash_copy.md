# spi_flash编译


## 创建工作文件夹

```
mkdir ~/LicheePi_Nano
cd ~/LicheePi_Nano
```

## 安装交叉编译链
此处为获取7.2.1版本，您可获取其他版本或者通过链接直接下载
    
```
wget http://releases.linaro.org/components/toolchain/binaries/7.2-2017.11/arm-linux-gnueabi/gcc-linaro-7.2.1-2017.11-x86_64_arm-linux-gnueabi.tar.xz

tar -vxJf gcc-linaro-7.2.1-2017.11-x86_64_arm-linux-gnueabi.tar.xz

sudo cp -r ./gcc-linaro-7.2.1-2017.11-x86_64_arm-linux-gnueabi /opt/

sudo vim /etc/bash.bashrc
```

在文件末尾 添加以下内容

    PATH="$PATH:/opt/gcc-linaro-7.2.1-2017.11-x86_64_arm-linux-gnueabi/bin"

使路径生效

    source /etc/bash.bashrc

此时可用 arm-linux-gnueabi-gcc -v 进行测试；若普通用户状态下没有成功，通过 sudo su 切换到root用户再尝试；

## 安装必要的库

```
sudo apt-get install build-essential subversion git-core libncurses5-dev zlib1g-dev gawk flex quilt libssl-dev xsltproc libxml-parser-perl mercurial bzr ecj cvs unzip lib32z1 lib32ncurses5 lib32bz2-1.0 -y

sudo apt-get install vim flex bison texinfo u-boot-tools lib32stdc++6 -y

sudo apt-get install libusb-1.0-0-dev

sudo apt-get install mtd-utils
```

## 安装sunxi-tools下载工具

获取源码

    git clone https://gitee.com/LicheePiNano/sunxi-tools.git

查看分支

    git branch -a

切换到 Nano 分支

    git checkout f1c100s-spiflash

## 编译并安装工具

```
cd sunxi-tools

make && sudo make install
```

## 编译UBOOT

### UBOOT下载

```
cd ~/LicheePi_Nano

git clone -b nano-lcd800480 https://gitee.com/LicheePiNano/u-boot.git

cd ~/LicheePi_Nano/u-boot
```

### UBOOT编译

```
make ARCH=arm f1c100s_nano_uboot_defconfig

make ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- -j8
```

## 编译Linux

### Linux下载
```
cd ~/LicheePi_Nano

git clone https://gitee.com/LicheePiNano/Linux.git

cd ~/LicheePi_Nano/Linux
```
### Linux编译
```
make ARCH=arm f1c100s_nano_linux_defconfig

make ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- -j8

make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- -j16 INSTALL_MOD_PATH=out modules

make ARCH=arm CROSS_COMPILE=arm-linux-gnueabihf- -j16 INSTALL_MOD_PATH=out modules_install
```
## 编译Buildroot

### Buildroot下载

```
cd ~/LicheePi_Nano

wget https://buildroot.org/downloads/buildroot-2021.02.4.tar.gz

tar xvf buildroot-2021.02.4.tar.gz

cd ~/LicheePi_Nano/buildroot-2021.02.4
```

### Buildroot安装依赖

sudo apt-get install linux-headers-$(uname -r)

### Buildroot编译

make menuconfig

### Buildroot配置

- Target options
  - Target Architecture (ARM (little endian))
  - Target Variant arm926t
- Toolchain
  - C library (musl) # 使用musl减小最终体积
- System configuration
  - Use syslinks to /usr .... # 启用/bin, /sbin, /lib的链接
  - Enable root login # 启用root登录
  - Run a getty after boot # 启用登录密码输入窗口

make

## 制作烧录镜像

下载脚本[nano_flash_dd.sh](https://dl.sipeed.com/shareURL/LICHEE/Nano/SDK)

更改脚本权限

```
sudo su

chmod +x nano_flash_dd.sh
```
启动脚本

./nano_flash_dd.sh

执行烧录

sudo sunxi-fel -p spiflash-write 0 flashimg.bin
