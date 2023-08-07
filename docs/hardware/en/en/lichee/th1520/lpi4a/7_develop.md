---
title: System Development
keywords: Linux, Lichee, TH1520, SBC, RISCV, Kernel, SDK, Develop
update:
  - date: 2023-05-08
    version: v1.0
    author: wonder
    content:
      - Release docs
---

## Yocto Linux  

The official development environment is based on yocto and customized by T-head, which could be obtained here: https://gitee.com/thead-yocto/

This section gives a brief introduction of setuping uilding Linux Yocto environment and use it to build the full image able to run on the development board.

### Setup Yocto Compilation Environment

Linux SDK uses Yocto to build images, which runs under Ubuntu 18.04. It is recommended to deploy Yocto under Linux with Docker. Yocto could also be deployed under Ubuntu18.04 directly. (Refer to [T-Head曳影1520Yocto用户指南.pdf](https://gitee.com/thead-yocto/documents/blob/master/zh/user_guide/T-Head%E6%9B%B3%E5%BD%B11520Yocto%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)2.2)

This section includes the guide to deploy with Docker only. **It is recommended to reserve 200G disk space and more than 4G memory on the machine. The time cosumed varies because of network situation. Building with a typical Linux configuration (mininal system plus essential basic components) takes about 1.5 hours. (with i5-11400, as only a reference)

- Install docker with official script
	```bash
	curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
	```
- Download dockerfile and modify username and ID
	Click here to download [linux-dev-master.7z](https://gitee.com/thead-yocto/documents/blob/master/linux-dev-master.7z) ，enter `linux-dev-master` after decompressing，open `Dockerfile` and find following instructions
	```bash
	ENV DOCKER_USER2 "your the same user name asyour host"`
	ENV USER2_ID "your user id"
	```
	Change "your the same user name as your host" to the name of user on host OS, "your user id" to the corresponding password
- Setup Docker image environment
	```bash
	docker build -t linux-dev-base:base .
	```
	Some errors may occur during downloading packages in this step. You could modify Dockerfile and put off downloading to successfully logining. This Docker image is able to build Linux SDKs released by T-Head, such as buildroot, yocto and so on. The default password is `123`.
- Startup Docker
	```bash
	docker run -u thead -dt --name linux-dev-{your_name} -v {your_lock_home}:{your_home} linux-dev-base:base /bin/bash
	```
	{your\_name} is the name of your container. Remember not to reuse an existing name.
	It is possible mount a directory in host with option `-v`, which could serve as a way to share files. {your\_lock\_home} is the local path under host, {your\_home} is the path mounted in Docker.
- Check started Docker containers.
	```bash
	docker ps | grep linux-dev-base
	```
then started Docker containers are shown,
- Login Docker
	```bash
	docker exec -it linux-dev-{your_name} /bin/bash
	```
- Download open-source packages (only needed at the first time of building SDK)
	Packages will be downloaded during building the firmware, which could take a long time with a poor network connection. To speed up the process, you could download the packages from Gitee ahead of time.
	```bash
	cd ~
	git clone https://gitee.com/thead-yocto/yocto-downloads.git
	```
- Download Yocto building packages
	```bash
	git clone https://gitee.com/thead-yocto/xuantie-yocto.git -b Linux_SDK_V1.1.2
	```
- Load configuration of targeted device and environment variables (remember to check before building)
	```bash
	cd xuantie-yocto
	source openembedded-core/oe-init-build-env thead-build/light-fm
	```
- Create a softlink to downloaded packages in directory downloads in SDK directory.
	```bash
	ln -s ~/yocto-downloads ../downloads
	```

Now the building environment is ready.

### Supported List of Machine/Target

In the step above (load environment variables), following message is shown after successfully setuping.

```bash
### Shell environment set up for builds. ###
You can now run 'bitbake <target>'
Common targets are:
    thead-image-linux
    thead-image-multimedia
    thead-image-gui
machines:
    light-beagle
    light-b-product
    light-a-val
    light-lpi4a
```

Here is the description:
target (List of images supported by the SDK):

|Name|Description|
|---|---|
|thead-image-linux|Typical configuration of Linux, mininal system with essential basic components|
|thead-image-multimedia|Typical configuration of Linux with video & CV support, mininal system with components of video subsystem (GStreamer etc.)|
|thead-image-gui|All of above with GUI-related components, full image, including applications like Gnome desktop, weston, QT and so on.|

machines (Board-level configuration supported by the SDK):

|Name|Description|
|---|---|
|light-a-val|TH1520-A EVB Board|
|light-b-product|TH1520-B EVB Board|
|light-beagle|beagleV-Ahead Development Board|
|light-lpi4a|Lichee Pi 4A Development Board|

### Building images

Building commands are like following:

```bash
MACHINE={machine} bitbake {target}
```

Replace {machine} and {target} with corresponding names in tables above. For example, the command to build a typical Linux image running on LicheePi 4A development board is:

```bash
MACHINE=light-lpi4a bitbake thead-image-linux
```
#### Problems while building images

- Caused by poor network, downloading may be slow and even fails at this step. Recommend proxies if possible.
- Error message:
	```bash
	Please use a locale setting which supports utf-8.
	Python can't change the filesystem locale after loading so we need a utf-8 when python starts or things won't work.
	```
	Run following commands first
	```bash
	sudo apt-get install locales
	sudo dpkg-reconfigure locales 
	```
	Then find `en\_US.UTF8` in the printed list (approximately the 158th). Type its ID and then press enter. Select this option also in the next step.
	Then run following commands (it is worth adding to `.bashrc` in Docker)
	```bash
	sudo locale-gen en_US.UTF-8
	sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
	export LANG=en_US.UTF-8
	```
	After finishing, there will not be errors during building.
- Error message:
	```bash
	please install them in order to proceed: lz4c pzstd zstd
	```
	Simply install corrsponding dependencies.
	```bash
	sudo apt update && sudo apt install -y zstd liblz4-tool
	```
### Packaging images

This repository [light\_deploy\_images](https://gitee.com/thead-yocto/light_deploy_images/tree/master/tarball) contains serveral pre-released images. `sdk.sh` in the repository is suitable to package new-built images.
Enter `light-fm` directory in the built image and move `sdk.sh` here. Run it with `./sdk.sh` and the corresponding image is generated after packaging. For file paths and directory structure of the image, refer to repository [light\_deploy\_images](https://gitee.com/thead-yocto/light_deploy_images/tree/master/tarball).
Finally, copy the built image and related files to the shared directory mounted with option `-v` and the file could be used for burning.
Now we have finished building and packaging, resulting with an image able to burn into and run in the development board.

### Build Separately
How to build official components released by T-head separately
- OpenSBI

- Uboot
	```bash
	git clone https://gitee.com/thead-yocto/u-boot
	cd u-boot
	make CROSS_COMPILE=riscv64-unknown-linux-gnu- ARCH=riscv light_lpi4a_defconfig
	make CROSS_COMPILE=riscv64-unknown-linux-gnu- ARCH=riscv
	```
	The generated firmware is u-boot-with-spl.bin, which could be burnt with fastboot.

- Kernel


### Device Tree Analysis

TODO  

### Other References

**light_deploy_images Repository：**

- Includes pre-built and burnable Linux images, packaging scripts and other reletive tools. Refer to the repository for more information.
- Repository Address: [https://gitee.com/thead-yocto/light_deploy_images](https://gitee.com/thead-yocto/light_deploy_images)

**documents Repository: **

- Includes all released documentation related to SDK
- Repository Address: [https://gitee.com/thead-yocto/documents](https://gitee.com/thead-yocto/documents)

## Mainline

How to build mainline version (under developing)

### OpenSBI
- Download and build
    ```bash
	git clone https://github.com/riscv-software-src/opensbi
	cd opensbi
	make CROSS_COMPILE=riscv64-unknown-linux-gnu- PLATFORM=generic
	```
	Generated firmware is build/platform/generic/firmware/fw\_dynamic.bin. Copy it to /boot

### U-boot
- Download and build
	```bash
	git clone -b th1520 https://github.com/dlan17/u-boot.git
	cd u-boot
	make CROSS_COMPILE=riscv64-unknown-linux-gnu- ARCH=riscv light_lpi4a_defconfig
	make CROSS_COMPILE=riscv64-unknown-linux-gnu- ARCH=riscv
	```
	Generated firmware is u-boot-dtb.bin. Copy it to /boot
- Boot mainline U-boot (under developing) with on-board U-boot
	Pre-burnt U-boot has supported Ethernet already, which makes it possible to obtain new U-boot image through tftp protocol.

	Startup a tftp instance on the developing machine. Taking Alpine for example, install package `tftp-hpa` and enable corresponding service.

	```bash
	apk add tftp-hpa
	rc-update add in.tftp
	rc-service in.tftp start
	```

	By default tftp uses `/var/tftpboot` as the root directory, so copy the new-built U-boot `u-boot-dbt.bin` to `/var/tftpboot`.

	Connect UART and Ethernet on LicheePi 4A development board, power it and press any key when following message is shown in serial
	```
	Press any key to stop autoboot
	```
	to enter U-boot shell.

	Type `dhcp` to configure Ethernet card with DHCP protocol. Mainline U-boot is expected to be loaded at 0x1c00000, so type
	```
	tftp 0x1c00000 TFTP_SERVER_IP:u-boot-dtb.bin
	go 0x1c00000
	```
	in U-boot shell to load the new-built U-boot into 0x1c00000 and jump to it.

### Linux

## OpenWRT

TODO

## Andriod 
TODO  

## OpenHarmony  
TODO

## Others

欢迎投稿～ 投稿接受后可得￥5～150（$1~20）优惠券！
