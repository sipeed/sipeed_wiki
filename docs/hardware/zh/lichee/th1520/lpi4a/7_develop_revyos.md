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

```bash
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
#sudo make CROSS_COMPILE=${toolchain_tripe}  ARCH=${ARCH} INSTALL_PATH=${GITHUB_WORKSPACE}/rootfs/boot zinstall -j$(nproc)
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
sudo cp -v arch/riscv/boot/dts/thead/{light-lpi4a.dtb,light-lpi4a-16gb.dtb} ${GITHUB_WORKSPACE}/rootfs/boot/
popd
```

之后只需要把rootfs中内容拷贝或覆盖到对应目录即可，注意内核Image和内核module目录一定要对应，不然会因缺失内核模块导致外设功能失效。
从 commit `c56347a43e850de287a2249d3d9118910718527b` 开始，内核中默认包含 16GB 内存设备树，故 8G/16G 是共用一个 kernel，仅 uboot 有所区别。

## 构建uboot
注意，此时仍在th1520_build目录下，且已经配置好环境变量和工具链，步骤参考构建kernel。

```shell
git clone https://github.com/revyos/thead-u-boot.git uboot
```

然后开始执行编译命令。
需要注意的是，8G 与 16G 内存版本使用的 uboot 不同，所以对应的构建命令也不同，基于此仓库构建命令如下：

```shell
pushd uboot
# 构建16G内存版本使用的uboot
make light_lpi4a_16g_defconfig
make CROSS_COMPILE=${toolchain_tripe} ARCH=${ARCH} -j$(nproc)
find . -name "u-boot-with-spl.bin" | xargs -I{} cp -av {} ${GITHUB_WORKSPACE}/rootfs/u-boot-with-spl-lpi4a-16g.bin
make clean
# 构建8G内存版本使用的uboot
make light_lpi4a_defconfig
make CROSS_COMPILE=${toolchain_tripe} ARCH=${ARCH} -j$(nproc)
find . -name "u-boot-with-spl.bin" | xargs -I{} cp -av {} ${GITHUB_WORKSPACE}/rootfs/u-boot-with-spl-lpi4a.bin
make clean
popd
```

烧录时注意烧录和你所使用的开发板所对应的 uboot。在烧录时请注意使用的命令，若使用的镜像版本为 `0912` 及以上版本，升级 uboot 只需要运行：
```shell
sudo ./fastboot flash uboot u-boot-with-spl-lpi4a-16g.bin
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

```shell
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

## 支持 PTG omxil 库的 GStreamer 播放器适配文档

### 概述
PTG 的 OpenMAX IL 库（下称 vpu-omxil）可使 LicheePi 4A 能够流畅硬解码 4k 60fps 的视频，那么具体应该如何使用该库呢？本文将主要介绍 LicheePi 4A 开发板上 Parole 播放器的集成与使用，用户可根据本文来了解在 LicheePi 4A 上的适配过程 以 h264 的硬解为例，视频硬解的工作流程如图所示
```text
                +-------------------------------------------+
                |    +------------+       +------------+    |   +--------+
video stream----+--->| omxh264dec +------>| video-sink +----+-->| player |
                |    +------+-----+       +------------+    |   +--------+
                |           |     GStreamer                 |
                +-----------+-------------------------------+
                            |
                      +-----v-----+
                      | vpu-omxil |
                      +-----+-----+
                            |
                            |
                    +-------v-------+
                    | kernel module |
                    |    (driver)   |
                    +-------+-------+
                            |
                            v
                        hardware
```
1. 视频流（video stream）由 GStreamer 读入后经过一系列预处理，送到 GStreamer 的解码器 `omxh264dec` 中
2. omxh264dec 调用动态库，即 PTG 提供的 vpu-omxil 库，该库通过驱动访问硬件（kernel module）进行硬解
3. 解码后的流传输到 GStreamer 的 video-sink 中，并由播放器（player）呈现

### GStreamer omxh264dec 解码测试
将 omxh264 解码的部分单独拎出来，大体的结构如下

```text
  +---+------------+----+
  |   +------------+    |
  |   | omxh264dec |    |
  |   +------------+    |
  |      GStreamer      |
  +----------+----------+
             |
  +----+-----v-----+----+
  |    +-----------+    |
  |    | vpu-omxil |    |
  |    +-----------+    |
  |  libomxil-bellagio  |
  +----------+----------+
             |
+------------v------------+
|  - memalloc   - vc8000  |
|  - hantrodec  - vidmem  |
|      kernel modules     |
+------------+------------+
             |
             v
          hardware
```
我们依照自底向上的顺序构建图示的链条。本节的主要目的是使 omxh264dec 解码器能够运行，并不涉及到输出屏幕等内容。

#### 1. 驱动编译、安装以及硬件访问权限的设置
硬解码需要访问硬件，而访问硬件又需要驱动，所以需要编译并安装驱动

##### 1.1 编译驱动
PTG 提供的驱动源：

https://gitee.com/thead-yocto/vpu-vc8000e-kernel

https://gitee.com/thead-yocto/vpu-vc8000d-kernel

https://gitee.com/thead-yocto/video_memory

##### 1.2 安装驱动
```shell
# depmod 分析可载入模块的依赖关系，在 /lib/modules/<kernel-version>中添加modules.dep文件，以便后续 modprobe 使用
sudo depmod -a
sudo modprobe vidmem vc8000 hantrodec memalloc

## 如果 modprobe 安装有问题的话，可以尝试使用 insmod 安装
#cd /usr/lib/modules/$(uname -r)
#sudo insmod $(find . -name *vidmem.ko*)
#sudo insmod $(find . -name *vc8000.ko*)
#sudo insmod $(find . -name *hantrodec.ko*)
#sudo insmod $(find . -name *memalloc.ko*)

# 可选：设置开机加载模块
echo -e "\nvidmem\nhantrodec\nmemalloc\nvc8000\n" | sudo tee -a /etc/modules > /dev/null
```

##### 1.3 设置硬件访问权限

安装内核模块后，/dev 目录下会出现 hantrodec vidmem vc8000 三个设备文件。默认情况下，用户对其没有访问权限，如果不修改权限的话，非 root 用户在打开 omxil 库时会报错。
```shell
# 生效一次
cd /dev
sudo chmod 666 hantrodec vidmem vc8000

# 长期生效
cat << EOF | sudo tee /lib/udev/rules.d/70-hantro.rules > /dev/null
KERNEL=="vidmem", MODE="0666"
KERNEL=="hantrodec", MODE="0666"
KERNEL=="vc8000", MODE="0666"
EOF
```

##### RevyOS 适配记录

如果要获取 RevyOS 特定版本的内核模块，可进入 [revyos/thead-kernel](https://github.com/revyos/revyos/wiki/%E6%94%AF%E6%8C%81-PTG-omxil-%E5%BA%93%E7%9A%84-GStreamer-%E6%92%AD%E6%94%BE%E5%99%A8%E9%80%82%E9%85%8D%E6%96%87%E6%A1%A3)，并在 GitHub CI 中下载 artifacts

#### 2. 安装 vpu-omxil 并调整配置

首先，请将 vpu-omxil 下载并解压到 /usr/lib/omxil/ 中：[vpu-omxil_1.2.1.tar.gz](https://drive.google.com/file/d/1pYgCVI7WltfpskltJ-RqzVUCEC21FS56/edit?pli=1)。如下图所示，需要：

1. 将 vpu-omxil 中的 OpenMax 组件注册到 libomxil-bellagio 中
2. gst-omx（该包提供了 omxh264dec 解码器） 调用 libomxil-bellagio 的时候也需要知道调用的组件名称

```text
+---------+   +-------------------+   +-----------+
| gst-omx +-->| libomxil-bellagio +-->| vpu-omxil |
+---------+   +-------------------+   +-----------+
```

##### 2.1 将 vpu-omxil 中的组件注册到 libomxil-bellagio 中

```shell
sudo apt install libomxil-bellagio-bin libomxil-bellagio0
# 注册组件
omxregister-bellagio -v /usr/lib/omxil/
```

##### 2.2 调整 gstomx.conf 的设置

调整 gstomx.conf 的设置以使解码器 omxh264dec 调用正确的组件，具体请查看针对 gst-omx 的补丁：

[gst-omx-01-add-libomxil-config.patch](https://gist.github.com/Sakura286/26777ea8204c1819885e093806a4f7ca#file-gst-omx-01-add-libomxil-config-patch)

#### 3. 添加 dmabuf 补丁

请查看 PTG 提供的针对 gst-omx 的 dmabuf 补丁：

[gst-omx-02-set-dec-out-port-dmabuf.patch](https://gist.github.com/Sakura286/26777ea8204c1819885e093806a4f7ca#file-gst-omx-02-set-dec-out-port-dmabuf-patch)

#### 4. GStreamer 解码初步测试

```shell
sudo apt install gstreamer1.0-omx-generic gstreamer1.0-omx-bellagio-config gstreamer1.0-plugins-bad gstreamer1.0-plugins-base gstreamer1.0-gl gstreamer1.0-plugins-good gstreamer1.0-tools

# 1 基本解码
gst-launch-1.0 filesrc location=<test.mp4> ! qtdemux !  h264parse ! omxh264dec  ! videoconvert ! fakesink  sync=false
# 2 在终端中显示 fps
# 参考：https://stackoverflow.com/questions/73948308
gst-launch-1.0 filesrc location=<test.mp4> ! qtdemux !  h264parse ! omxh264dec  ! videoconvert ! fpsdisplaysink video-sink=fakesink  text-overlay=false sync=false -v 2>&1
```

`fakesink`会把前面的视频流全部吞掉，不输出画面（因而不会在 video-sink 这一环节损失性能），但是结合fpsdisplaysink可以读取到解码的速度。正常日志如下：
```shell
Setting pipeline to PAUSED ...[DBGT]
vc8kdec compiled without trace support (ENABLE_DBGT_TRACE switch not enabled)
Pipeline is PREROLLING ...
Redistribute latency...
OMX  ! decoder_get_parameter OMX_ErrorNoMore (2)
Pipeline is PREROLLED ...
Setting pipeline to PLAYING ...
New clock: GstSystemClockRedistribute latency...
0:01:39.5 / 0:01:49.4 (90.9 %)
```

**【TIP】**
如果有 [omxh264dec-omxh264dec0: Could not initialize supporting library.](https://gist.github.com/Sakura286/015fae6792e160268db7ad8a697dd2df) 等字样的报错，可以安装`gst-omx`、`libomxil-bellagio`与`libc6`相关的 `debug-symbol` 包，使用 `gdb` 启动上述命令进行调试。调试时，先断 `DWLInit`，然后再断 `open`，具体看是打开哪个地方的时候出错了。

##### RevyOS 适配记录

RevyOS 适配过程中对于初始化动态库失败找到了如下三种原因：

1. 编译 vpu-omxil 时使用的工具链与当前系统不兼容
2. 未使用`omxregister-bellagio`注册 vpu-omxil
3. 未调整 `/dev` 目录下 `hantrodec` `vc8000` `vidmem` 等设备的权限

### B. 选用合适的 GStreamer video-sink

`video-sink` 是视频流在整个 [GStreamer pipeline](https://gstreamer.freedesktop.org/documentation/tutorials/basic/concepts.html) 中的最后一步，其作用一般是将视频流输出到屏幕上。
前文中`fakesink`只是测试解码器是否正常工作的特殊 `video-sink`，[可选的 video-sink](https://gstreamer.freedesktop.org/documentation/tutorials/basic/platform-specific-elements.html?gi-language=c)非常多，常见的有 `autovideosink`，`ximagesink`，`xvimagesink`，`fbdevsink`，`waylandsink`，`glimagesink`，`gtkglsink`等，它们各在不同的插件包里，需要酌情安装：

| **video-sink** | **所属包名** |
| --- | --- |
| waylandsink | gstreamer1.0-plugins-bad |
| fbdevsink | gstreamer1.0-plugins-bad |
| autovideosink | gstreamer1.0-plugins-good |
| gtkglsink | gstreamer1.0-plugins-good |
| ximagesink \| xvimagesink | gstreamer1.0-plugins-base |
| glimagesink | gstreamer1.0-plugins-base \| gstreamer1.0-gl |

**【TIP】** 使用 `gst-inspect-1.0 <video-sink-name>` 来查看对应 video-sink 可用的选项
**【TIP】** 添加 `--gst-debug-level=<lv>` 来获得更多的[输出日志](https://gstreamer.freedesktop.org/documentation/tutorials/basic/debugging-tools.html#the-debug-log)，其中 `<lv>` 代表了从 1 到 6，啰嗦程度从低到高，建议在等级 4 及以下，否则日志会非常长
请尝试不同的 video-sink ，并尝试不同的插件参数，以及给予不同的环境变量，直至找到可以流畅硬解 H264 的那一个。

#### RevyOS 适配记录

- `**waylandsink**`：由于现在（20230720）RevyOS 采用了 Xfce 桌面，不可能支持 Wayland，故 `waylandsink`从原理上无法使用
- `**fbdevsink**`与`**ximagesink**`：无法使用
- `**xvimagesink**`：通过[流水线图](https://gstreamer.freedesktop.org/documentation/tutorials/basic/debugging-tools.html#getting-pipeline-graphs)以及日志可以确定，playbin 或 autovideosink 会自动调用 xvimagesink，使用 perf 分析后可以发现，使用xvimagesink 不可避免地会进行大量的 memcpy 操作，严重降低解码性能；该问题在获得PTG的 dmabuf 补丁后依然存在，故无法使用
- `**gtkglsink**`：[GTK3 不支持 EGL on X11](https://gitlab.gnome.org/GNOME/gtk/-/issues/738)，而 RevyOS 目前基于 x11，且只支持 EGL，故无法使用

剩下的只有`glimagesink`，根据 [Running and debugging GStreamer Applications](https://gstreamer.freedesktop.org/documentation/gstreamer/running.html#environment-variables)，并观察其他使用到 glimagesink 的例子，可以猜测需要明确指定环境变量 `GST_GL_API`与 `GST_GL_PLATFORM`
由于 RevyOS 使用了 gles2+egl 的组合，使用如下的命令，成功硬解。

```shell
GST_GL_API=gles2 GST_GL_PLATFORM=egl gst-launch-1.0 filesrc location=<test.mp4> ! qtdemux !  h264parse ! omxh264dec  ! videoconvert ! fpsdisplaysink video-sink=glimagesink sync=false
```

然而 GStreamer 被播放器调用时是无法通过环境变量来传递参数的，所以构建 gst-plugins-base 时应当传递额外的 meson 编译参数：

```shell
-Dgl_api=[\'gles2\'] -Dgl_platform=[\'egl\']
```

### C. 播放器支持

GStreamer 的 pipeline 没有问题之后，就需要使播放器支持。不同播放器会使用到不同的 video-sink，同样对 gstreamer 有着不同程度的依赖。
适配播放器时，最重要的工作便是①使播放器适配已验证的 video-sink，或者②使 gstreamer pipeline 支持播放器指定的 video-sink，此次 RevyOS 适配过程采用了①方案。

```plain
                +-------------------------------------------+
                |    +------------+       +------------+    |   +--------+
video stream----+--->| omxh264dec +------>| video-sink +----+-->| player |
                |    +------------+       +------------+    |   +--------+
                |                GStreamer                  |
                +-------------------------------------------+
```

#### RevyOS 适配记录

根据 [https://gstreamer.freedesktop.org/apps/](https://gstreamer.freedesktop.org/apps/) 进行简单的排查

| 是否可用 | 是否更新 | 应用名 | 备注 |
| --- | --- | --- | --- |
| ❌ |  | Gnash | Flash 播放器 |
| ❌ |  | GEntrans | Debian 未收录 |
| ❓ | 20230226 | Kaffeine | ❌ 需要大量 KDE 相关组件
||||✔️ 存在于[riscv64 仓库](https://buildd.debian.org/status/package.php?p=kaffeine&suite=sid)中
||||❌ 在 Debian amd64 Gnome 上，播放窗口与控制窗口分离，且默认调用了 VLC 进行播放 |
| ❌ |  | Lcdgrilo | Debian 未收录 |
| ✔️ | 20230218 | Parole | ✔️ For XFCE
||||❓ 不支持 Wayland，仅支持 x11
||||✔️ Debian amd64 Gnome 验证通过
||||✔️ 存在于[riscv64 仓库](https://buildd.debian.org/status/package.php?p=parole&suite=sid) 中 |
| ❌ |  | Songbird | Debian 未收录 |
| ❌ |  | Snappy | Debian 未收录 |
| ❌ |  | Totem | 需要 GTK3，然而 GTK3 不支持 EGL on X11 |

最初选择的播放器是 Totem，但是发现 Totem 无法指定除了 gtkglsink 以外的 video-sink，且 RevyOS 无法支持
随后选择了 Parole ，该软件由 GObject 编写，寻找其构建 parole_gst 对象时的方法 parole_gst_constructed，将 video-sink 设置为前文已验证的 glimagesink，至此，粗略的适配工作完成。

### 总结：RevyOS 适配工作

1. 编译驱动模块至内核，设置启动加载，设置设备权限
2. 将 PTG 提供的 omxil 二进制动态库文件打包为 th1520-vpu
   1. 修改 th1520-vpu 的依赖，使其依赖 gst-omx 、libomxil-bellagio 等包
   2. 设置了一些 postinstall 操作，例如使用  omxregister-bellagio  注册组件等
3. 修改 gst-omx
   1. 增加 config 中对 vpu-omxil 组件的支持
   2. 应用 dmabuf 补丁
   3. 增加对 h265 vp9 的支持
4. 修改 gst-base 编译时的 gl 支持，限制为 gles2+egl
5. 修改 parole 以支持 glimagesink

### 本文所用资源

补丁集合：

https://gist.github.com/Sakura286/26777ea8204c1819885e093806a4f7ca

PTG omxil 库：

https://drive.google.com/file/d/1pYgCVI7WltfpskltJ-RqzVUCEC21FS56