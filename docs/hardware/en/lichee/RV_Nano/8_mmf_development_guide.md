---
title: Multimedia Framework (MMF) Development Guide
keywords: riscv, licheerv, nano, mmf
update:
  - date: 2024-02-04
    version: v0.1
    author: lxowalle
---

## Overview
This document is used to introduce the method of using SDK to develop MMF, to provide a development idea for developers who want to start developing MMF but can't get started.
MMF full name is Multimedia Framework, an framework that offers a unified API format for video input/output, audio input/output, image signal processing, and hardware encoding/decoding, allowing users to quickly implement multimedia-related functions by calling these APIs.

## Build MMF development environment
Please refer to the method introduced in `LicheeRV Nano->System Development->cvi_mmf_sdk` to build the MMF development environment.

Or follow the instructions below:

```shell
Copy code
# Download dependencies
sudo apt install pkg-config build-essential ninja-build automake autoconf libtool wget curl git gcc libssl-dev bc slib squashfs-tools android-sdk-libsparse-utils android-sdk-ext4-utils jq cmake python3-distutils tclsh scons parallel ssh-client tree python3-dev python3-pip device-tree-compiler libssl-dev ssh cpio squashfs-tools fakeroot libncurses5 flex bison

# Download SDK and toolchain
git clone https://github.com/sipeed/LicheeRV-Nano-Build.git
wget https://sophon-file.sophon.cn/sophon-prod-s3/drive/23/03/07/16/host-tools.tar.gz
tar xvf host-tools.tar.gz

# Compile all examples with the build_middleware command
cd LicheeRV-Nano-Build
git checkout v4.1.0-licheervnano
ln -s ../host-tools ./
source build/cvisetup.sh
defconfig cv1812cp_licheerv_nano_sd
build_middleware
```

The above instructions describe how to install the MMF-related compilation environment and how to compile the MMF examples provided by the SDK.

- Note: You may fail to compile sample_cvg. If you do not need this example, try again after deleting the `LicheeRV-Nano-Build/middleware/v2/sample/cvg` folder. If you need this demo, try compiling with `build_all`, which requires compiling the entire SDK, so the compilation time will be longer.
## Development Document
Please refer to the `LicheeRV Nano->Board Introduction` to find most of the document.

For MMF applications, pay attention to the following document:

- [Media Processing Software Development Reference](https://doc.sophgo.com/cvitek-develop-docs/master/docs_latest_release/CV180x_CV181x/en/01.software/MPI/Media_Processing_Software_Development_Reference/build/html/index.html)
- [SDK LicheeRV-Nano-Build](https://github.com/sipeed/LicheeRV-Nano-Build)

## Connecting to the Development Board via Network
The purpose of connecting to the development board via network is to upload the firmware we compiled to the board.

Please refer to the methods in `LicheeRV Nano->peripheral` to get the IP address of the development board. Any one of the three methods can be implemented: Ethernet connection, WIFI connection, or USB RNDIS connection.

## Compiling and Running an Example
MMF will use the hardware directly, so incorrect operation can lead to system crash, and you must be careful to pay attention to details when developing MMF. The suggestion is to modify your own program by using the examples.

Compile and run sample_vio example:

```shell
# Ensure that the basic MMF compilation environment has been set up and that build_middleware has been compiled once
# Compile sample_vio
cd middleware/v2/sample/vio
make

# Upload to the development board (account root, password cvitek)
scp sample_vio root@xxx.xxx.xxx.xxx:/root  # xxx.xxx.xxx.xxx is the board's IP address

# Log into the development board
ssh root@xxx.xxx.xxx.xxx

# If you need to use the display, you need to run fb_load.sh to make sure the driver is loaded (it only needs to be executed once)
/opt/fb_load.sh

# Run the example
cd ~
./sample_vio
```
The instructions above explain how to compile a specific MMF example, and how to upload and run the example on the development board. Developers can modify the example based on their applications to eventually develop the functionality they desire.

## Have an unsolvable problem?
1. Please remain patient and carefully review the development document to see if anything was overlooked. For example, check if the input parameters are correct, whether resources have been properly released, etc.
2. Post your problem on [maixhub](https://maixhub.com/discussion) or GitHub. Please organize the functionality you want to achieve, the problems you encountered, the solutions you tried, and the ways to reproduce them, by the way, many times can be solved in the process of organizing your thoughts.