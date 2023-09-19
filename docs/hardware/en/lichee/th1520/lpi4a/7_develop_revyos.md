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

## Build kernel

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
#sudo make CROSS_COMPILE=${toolchain_tripe}  ARCH=${ARCH} INSTALL_PATH=${GITHUB_WORKSPACE}/rootfs/boot zinstall -j$(nproc)
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
sudo cp -v arch/riscv/boot/dts/thead/{light-lpi4a.dtb,light-lpi4a-16gb.dtb} ${GITHUB_WORKSPACE}/rootfs/boot/
popd
```

After that, you only need to copy or overwrite the contents of the rootfs to the corresponding directory. Note that the kernel image and kernel module directories must correspond to each other, or else the peripheral functions will be disabled due to the missing kernel module.

Starting from commit `c56347a43e850de287a2249d3d9118910718527b`, the kernel defaults to include a 16GB memory device tree, so 8G/16G share one kernel, with only uboot being different.

## Building uboot

Note that at this point, you are still in the th1520_build directory and have already configured the environment variables and toolchain, refer to building the kernel for the steps.

```shell
git clone https://github.com/revyos/thead-u-boot.git uboot
```

Note that at this point, you are still in the th1520_build directory and have already configured the environment variables and toolchain, refer to building the kernel for the steps.

```shell
pushd uboot
# Build uboot for 16G memory version
make light_lpi4a_16g_defconfig
make -j$(nproc)
find . -name "u-boot-with-spl.bin" | xargs -I{} cp -av {} ${GITHUB_WORKSPACE}/rootfs/u-boot-with-spl-lpi4a-16g.bin
make clean
# Build uboot for 8G memory version
make light_lpi4a_defconfig
make -j$(nproc)
find . -name "u-boot-with-spl.bin" | xargs -I{} cp -av {} ${GITHUB_WORKSPACE}/rootfs/u-boot-with-spl-lpi4a.bin
make clean
popd
```

When flashing, pay attention to flash the uboot corresponding to the development board you are using. When flashing, please pay attention to the command you use. If the image version you are using is `0912` or above, you only need to run the following command to upgrade uboot:
```shell
sudo ./fastboot flash uboot u-boot-with-spl-lpi4a-16g.bin
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

## GStreamer Player Adaptation Documentation with PTG omxil Library Support

### Overview
PTG's OpenMAX IL library (hereinafter referred to as vpu-omxil) enables the LicheePi 4A to smoothly hard-decode 4k 60fps video, so how to use this library? This article will mainly introduce the integration and use of the Parole player on the LicheePi 4A development board, users can follow this article to understand the process of adapting to the LicheePi 4A Take the hard decoding of h264 as an example, the workflow of the hard decoding of the video is shown in the following figure
```text
                +-------------------------------------------+ +-------------------------------------------+ +-------------------------------------------+
                | +------------+ +------------+ | +--------+
video stream----+--->| omxh264dec +------>| video-sink +----+--->| player |
                | +------+-----+ +------------+ | +--------+
                | | GStreamer |
                +-----------+-------------------------------+
                            GStreamer | +++ ++ | ++
                      +-----v-----+ |
                      | vpu-omxil |
                      +-----+-----+
                            | vpu-omxil | +++
                            vpu-omxil | +++ | vpu-omxil
                    +-------v-------+
                    | kernel module |
                    | (driver) |
                    +-------+-------+
                            kernel module || (driver) | +++
                            v
                        hardware
```
1. the video stream is read in by the GStreamer and then goes through a series of pre-processing before being sent to the GStreamer's decoder `omxh264dec`.
2. omxh264dec calls a dynamic library, the vpu-omxil library provided by PTG, which accesses the hardware (kernel module) through the driver to perform hard decoding.
3. the decoded stream is transferred to the video-sink of GStreamer and rendered by the player

### GStreamer omxh264dec decoding test
The omxh264 decoding section is separated out and has the following general structure

```text
  +---+------------+----+ |+------------+----+
  | +------------+ |
  | | omxh264dec | |
  | +------------+ |
  | GStreamer |
  +----------+----------+
             || omxh264dec
  | +----+-----v-----+----+ |
  | +-----------+ |
  | | vpu-omxil | | | | vpu-omxil
  | +-----------+ |
  | libomxil-bellagio |
  +----------+----------+
             || libomxil-bellagio
+------------v------------+
| - memalloc - vc8000 |
| - hantrodec - vidmem |
| kernel modules |
+------------+------------+
             | - kernel modules | +++
             v
          kernel modules | +++ | v
```
We build the chain shown in bottom-up order. The main purpose of this section is to get the omxh264dec decoder up and running, and does not deal with outputting screens, etc. The main purpose of this section is to get the omxh264dec decoder running.

#### 1. Driver Compilation, Installation, and Hardware Access Setup
Hard decoding requires access to the hardware, and access to the hardware requires a driver, so you need to compile and install the driver.

##### 1.1 Compile driver
PTG provides the driver source:

https://gitee.com/thead-yocto/vpu-vc8000e-kernel

https://gitee.com/thead-yocto/vpu-vc8000d-kernel

https://gitee.com/thead-yocto/video_memory

##### 1.2 Install the driver
```shell
# depmod analyzes the dependencies of loadable modules and adds a modules.dep file to /lib/modules/<kernel-version> for subsequent modprobe use
sudo depmod -a
sudo modprobe vidmem vc8000 hantrodec memalloc

## If you are having trouble installing modprobe, try using insmod to install it.
#cd /usr/lib/modules/$(uname -r)
#sudo insmod $(find . -name *vidmem.ko*)
#sudo insmod $(find . -name *vc8000.ko*)
#sudo insmod $(find . -name *hantrodec.ko*)
#sudo insmod $(find . -name *memalloc.ko*)

# Optional: set bootloader module
echo -e "\nvidmem\nhantrodec\nmemalloc\nvc8000\n" | sudo tee -a /etc/modules > /dev/null
```

##### 1.3 Setting Hardware Access Privileges

After installing the kernel module, three device files, hantrodec vidmem vc8000, appear in the /dev directory. By default, users do not have access rights to these files. If you do not change the permissions, non-root users will get an error when opening the omxil library.
```shell
# Execute the shell once.
cd /dev
sudo chmod 666 hantrodec vidmem vc8000

# Long term
cat << EOF | sudo tee /lib/udev/rules.d/70-hantro.rules > /dev/null
KERNEL=="vidmem", MODE="0666"
KERNEL=="hantrodec", MODE="0666"
KERNEL=="vc8000", MODE="0666"
EOF
```

##### RevyOS Adaptation Records

To get the kernel module for a specific version of RevyOS, go to [revyos/thead-kernel](https://github.com/revyos/revyos/wiki/%E6%94%AF%E6%8C%81-PTG-omxil-%E5%BA%93%E7%9A% 84-GStreamer-%E6%92%AD%E6%94%BE%E5%99%A8%E9%80%82%E9%85%8D%E6%96%87%E6%A1%A3), and download the artifacts from the GitHub CI

#### 2. Install vpu-omxil and adjust the configuration

First, download and extract vpu-omxil into /usr/lib/omxil/: [vpu-omxil_1.2.1.tar.gz](https://drive.google.com/file/d/1pYgCVI7WltfpskltJ-RqzVUCEC21FS56/ edit?pli=1). As shown below, it is required:

1. register the OpenMax component from vpu-omxil to libomxil-bellagio
2. gst-omx (this package provides the omxh264dec decoder) You also need to know the name of the component you are calling when you call libomxil-bellagio.

```text
+---------+ +-------------------+ +-----------+
| gst-omx +-->| libomxil-bellagio +-->| vpu-omxil |
+---------+ +-------------------+ +-----------+
```

##### 2.1 Registering components from vpu-omxil to libomxil-bellagio

```shell
sudo apt install libomxil-bellagio-bin libomxil-bellagio0
# Register the component
omxregister-bellagio -v /usr/lib/omxil/
```

##### 2.2 Adjusting gstomx.conf settings

Adjust the settings of gstomx.conf so that the decoder omxh264dec calls the correct components, see the patch for gst-omx:

[gst-omx-01-add-libomxil-config.patch](https://gist.github.com/Sakura286/26777ea8204c1819885e093806a4f7ca#file-gst-omx-01-add- libomxil-config-patch)

#### 3. Add dmabuf patch

Please check the dmabuf patch for gst-omx provided by PTG:

[gst-omx-02-set-dec-out-port-dmabuf.patch](https://gist.github.com/Sakura286/26777ea8204c1819885e093806a4f7ca#file-gst-omx-02-set- dec-out-port-dmabuf-patch)

#### 4. GStreamer decoding preliminary test

```shell
sudo apt install gstreamer1.0-omx-generic gstreamer1.0-omx-bellagio-config gstreamer1.0-plugins-bad gstreamer1.0-plugins-base gstreamer1.0-gl gstreamer1.0-plugins-good gstreamer1.0-tools

# 1 Basic decoding
gst-launch-1.0 filesrc location=<test.mp4> ! qtdemux !  h264parse ! omxh264dec ! videoconvert ! fakesink sync=false
# 2 Display fps in terminal
# Reference: https://stackoverflow.com/questions/73948308
gst-launch-1.0 filesrc location=<test.mp4> ! qtdemux !  h264parse ! omxh264dec ! videoconvert ! fpsdisplaysink video-sink=fakesink text-overlay=false sync=false -v 2>&1
```

`fakesink` swallows the previous video stream in its entirety and doesn't output the picture (thus not losing performance in the video-sink part), but in combination with fpsdisplaysink you can read the decoding speed. The normal log is as follows:
```shell
Setting pipeline to PAUSED ... [DBGT]
vc8kdec compiled without trace support (ENABLE_DBGT_TRACE switch not enabled)
Pipeline is PREROLLING ...
Redistribute latency...
OMX ! decoder_get_parameter OMX_ErrorNoMore (2)
Pipeline is PREROLLED ...
Setting pipeline to PLAYING ...
New clock: GstSystemClockRedistribute latency...
0:01:39.5 / 0:01:49.4 (90.9 %)
```

**[TIP]**
If there is [omxh264dec-omxh264dec0: Could not initialize supporting library.](https://gist.github.com/Sakura286/ 015fae6792e160268db7ad8a697dd2df), you can install `gst-omx`, `libomxil-bellagio` and `debug-symbol` package related to `libc6`, and start the above commands with `gdb` for debugging. When debugging, break `DWLInit` and then break `open`, depending on which part of `open` is wrong.

##### RevyOS adaptation log

During the adaptation of RevyOS, the following three reasons were found for the failure of initializing dynamic libraries:

1. the toolchain used to compile vpu-omxil is not compatible with the current system
2. vpu-omxil was not registered with `omxregister-bellagio`.
3. not adjusting permissions on devices like `hantrodec`, `vc8000`, `vidmem` in `/dev` directory.

### B. Selecting a suitable GStreamer video-sink

The `video-sink` is the last step of the video stream in the whole [GStreamer pipeline](https://gstreamer.freedesktop.org/documentation/tutorials/basic/concepts.html), and its role is generally to output the video stream to the screen.
The `fakesink` in the previous section is just a special `video-sink` to test that the decoder is working correctly, [optional video-sink](https://gstreamer.freedesktop.org/documentation/tutorials/basic/platform) -specific-elements.html?gi-language=c) are very numerous, common ones are `autovideosink`, `ximagesink`, `xvimagesink`, `fbdevsink`, `waylandsink`, `glimagesink`, `gtkglsink` and so on. gtkglsink`, etc. They are each in different plugin packages and need to be installed as appropriate:

| **video-sink** | **Package name** |
| --- | --- |
| waylandsink | gtkglsink | waylandsink | gtkglsink
| waylandsink | gstreamer1.0-plugins-bad |
| fbdevsink | gstreamer1.0-plugins-bad |
| autovideosink | gstreamer1.0-plugins-good | gtkglsink | fbdevsink | gstreamer1.0-plugins-bad
| gtkglsink | gstreamer1.0-plugins-good | gstreamer1.0-plugins-good | gstreamer1.0-plugins-good
| ximagesink \| xvimagesink | gstreamer1.0-plugins-base |
| glimagesink | gstreamer1.0-plugins-base \| gstreamer1.0-gl |

**[TIP]** Use `gst-inspect-1.0 <video-sink-name>` to see what options are available for the corresponding video-sink.
**[TIP]** Add `--gst-debug-level=<lv>` to get more [output logs] (https://gstreamer.freedesktop.org/documentation/tutorials/basic/debugging-tools. html#the-debug-log), where `<lv>` stands for 1 to 6, and the verbosity level is from low to high, it is recommended to be at level 4 and below, otherwise the log will be very long.
Please try different video-sinks, and try different plugin parameters, and different environment variables, until you find one that can smoothly harden H264.

#### RevyOS adaptation log

- `**waylandsink**`: Since RevyOS now (20230720) uses the Xfce desktop, it is not possible to support Wayland, so `waylandsink` does not work in principle.
- `**fbdevsink**` and `**ximagesink**`: not working
- `**xvimagesink**`: via [pipeline graphs](https://gstreamer.freedesktop.org/documentation/tutorials/basic/debugging-tools.html#getting-pipeline-graphs) and logs, we can determine that playbin or autovideosink will automatically call xvimagesink, and after analyzing with perf, we can find that using xvimagesink will inevitably perform a large number of memcpy operations, which will seriously degrade the decoding performance; this problem still exists after obtaining PTG's dmabuf patch. This problem still exists after obtaining PTG's dmabuf patch, so it is not possible to use
- `**gtkglsink**`: [GTK3 does not support EGL on X11](https://gitlab.gnome.org/GNOME/gtk/-/issues/738), and RevyOS is currently based on x11 and only supports EGL, so it cannot be used.

The only thing left is `glimagesink`, according to [Running and debugging GStreamer Applications](https://gstreamer.freedesktop.org/documentation/gstreamer/running), and looking at other examples that use glimagesink, we can guess that we need to explicitly specify the environment variables `GST_GL_API` and `GST_GL_PLATFORM`.
Since RevyOS uses a combination of gles2+egl, it was successfully hardened using the following command.

```shell
GST_GL_API=gles2 GST_GL_PLATFORM=egl gst-launch-1.0 filesrc location=<test.mp4> ! qtdemux !  h264parse ! omxh264dec ! videoconvert ! fpsdisplaysink video-sink=glimagesink sync=false
```

However, GStreamer cannot be passed parameters via environment variables when called by the player, so additional meson compilation parameters should be passed when building gst-plugins-base:

```shell
-Dgl_api=[\'gles2\'] -Dgl_platform=[\'egl\']
```

### C. Player support

After the pipeline of GStreamer is OK, we need to make the player support. Different players use different video-sinks, and also have different levels of dependency on gstreamer.
When adapting a player, the most important thing to do is to either (i) adapt the player to a validated video-sink, or (ii) make the gstreamer pipeline support the video-sink specified by the player, which is what we have done in this RevyOS adaptation.

```plain
                +-------------------------------------------+ | +-------------------------------------------+ +-------------------------------------------+
                | +------------+ +------------+ | +--------+
video stream----+--->| omxh264dec +------>| video-sink +----+--->| player |
                | +------------+ +------------+ | +--------+
                | GStreamer |
                +-------------------------------------------+
```

#### RevyOS adaptation log

Simple troubleshooting based on [https://gstreamer.freedesktop.org/apps/](https://gstreamer.freedesktop.org/apps/)

| Available | Updated | App Name | Remarks |
| --- | --- | --- | --- |
| ❌ | Gnash | Flash Player |
| ❌ | | GEntrans | Debian Uncovered |
| ❓ | 20230226 | Kaffeine | ❌ Requires a lot of KDE-related components
||||✔️ exists in [riscv64 repository](https://buildd.debian.org/status/package.php?p=kaffeine&suite=sid)
||||❌ On Debian amd64 Gnome, the playback window is separate from the control window, and VLC is called by default for playback |
| ❌ | | Lcdgrilo | Debian not included |
| ✔️ | 20230218 | Parole | ✔️ For XFCE
||||❓ No Wayland support, only x11 support
||||✔️ Debian amd64 Gnome Verified by
||||✔️ exists in [riscv64 repository](https://buildd.debian.org/status/package.php?p=parole&suite=sid) |
| ❌ | |Songbird | Debian not included |
| ❌ | |Snappy | Debian not included |
| ❌ | | Totem | requires GTK3, which does not support EGL on X11 |

The first player of choice was Totem, but it turns out that Totem can't specify video-sinks other than gtkglsink, and RevyOS doesn't support it.
I then chose Parole, which is written by GObject, and looked for the method parole_gst_constructed when constructing the parole_gst object, and set the video-sink to the glimagesink as verified in the previous section, and the rough adaptation was completed.

### Summary: Adapting to RevyOS

1. Compile the driver module into the kernel, set bootloading, and set device permissions.
2. Package the omxil binary library provided by PTG into th1520-vpu.
   1. modified the dependencies of th1520-vpu to depend on packages like gst-omx, libomxil-bellagio, etc. 2. set some postinstalls.
   2. set up some postinstall operations, such as registering components with omxregister-bellagio, etc.
3. Modify gst-omx
   1. added support for vpu-omxil component in config
   2. apply dmabuf patch
   3. add support for h265 vp9. 4.
4. modify gst-base compile-time gl support to gles2+egl. 5. modify parole to support gl.
5. modify parole to support glimagesink

### Resources used in this article

Patch collection:

https://gist.github.com/Sakura286/26777ea8204c1819885e093806a4f7ca

PTG omxil library:

https://drive.google.com/file/d/1pYgCVI7WltfpskltJ-RqzVUCEC21FS56