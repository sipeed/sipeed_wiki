---
title: FAQ
keywords: Linux, Lichee, TH1520, SBC, RISCV, Debian, Desktop
update:
  - date: 2023-10-30
    version: v1.2
    author: ztd
    content:
      - Update official development docs.
  - date: 2023-10-23
    version: v1.1
    author: ztd
    content:
      - Update NPU's FAQ
  - date: 2023-09-22
    version: v1.0
    author: ztd
    content:
      - Release docs
---
## Unbox
- Power supply notes:
  1. The USB-C port only supports 5V input. For safety, do not use fast charging power banks or chargers.
  2. The IO pins are 1.8V logic level. Please use the shipped serial adapter board or a serial board that supports 1.8V.
  3. Computer USB ports usually only provide 5V1A, which is not enough for the board. The board needs at least 5V2A, 5V3A adapter is recommended, or use 12V DC power.
  4. If the LED next to the USB silkscreen blinks, it indicates unstable power or a short circuit.
- Differences between formal and beta hardware versions, USB current limit instructions see[Board hardware overview](https://en.wiki.sipeed.com/hardware/en/lichee/th1520/lpi4a/2_unbox.html#Board-hardware-overview)

## Images
- For image versions before 20230721, there is an issue of incorrectly identifying the memory size on the 16+128 core board, the image version needs to be updated. If it is a version after 20230706, you can also refer to[Images summary](https://en.wiki.sipeed.com/hardware/en/lichee/th1520/lpi4a/3_images.html) for repairing.
- Please read the usage instructions for the image collection in the wiki carefully before using the image, to ensure downloading the expected image, for example using the 10.1 inch touch screen requires flashing the image in the MIPI suffixed compressed package.
- The Android 13 image currently does not have peripheral support. After flashing, only basic functions like HDMI display are available.

## Burn image
- When flashing on Windows, please confirm if the driver is installed correctly first. If the driver is installed correctly but there is still no reaction during flashing, try changing the USB cable. Note that the USB cable used must be able to supply power and transmit data, and try not to use the USB ports on the front panel of the PC case when flashing, or the data ports on a laptop, otherwise the device may not be recognized due to power supply issues.
- To switch boot modes, for example to boot from SD card, formal version boards can switch via dip switches (note a dedicated image is needed), beta version boards can also switch by passing boot arguments, see[Board Boot Process](https://en.wiki.sipeed.com/hardware/en/lichee/th1520/lpi4a/4_burn_image.html#Board-Boot-Process).
- After 20231023, large image burning support has been updated. From this version, burning requires using the latest version of fastboot, which can be found in the image collection's [cloud disk link](https://mega.nz/folder/phoQlBTZ#cZeQ3qZ__pDvP94PT3_bGA). The file's name is `burn_tools_support_bigimage.zip`.

## Desktop Usage
- If the icons in the desktop bottom launcher are not working properly, you can manually configure them as desired, or use the following command to restore the default configuration. See [Web Browser](https://en.wiki.sipeed.com/hardware/en/lichee/th1520/lpi4a/5_desktop.html#Web-Browser) for the default configuration.
	```shell
	cp /etc/xdg/xfce4/panel/default.xml /home/sipeed/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml
	chown sipeed:sipeed /home/sipeed/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml
	```
- If you encounter errors when installing software, please update to the latest image or refer to [Software Source](https://en.wiki.sipeed.com/hardware/en/lichee/th1520/lpi4a/5_desktop.html#Software-Installation) for solutions.
- If you find that the Wifi/BT function of the development board cannot be used or if you cannot see the Wifi device after rebooting, unplug the power supply of the development board, completely disconnect it, and then power it back on to restart.

## Peripheral Use
1. To use the NPU, please use image versions 0920 or later.
2. JTAG requires manual wiring and setting pinmux on the board, refer to [JTAG](https://en.wiki.sipeed.com/hardware/en/lichee/th1520/lpi4a/6_peripheral.html#JTAG).
3. When connecting multiple peripherals (e.g. HDMI, USB keyboard/mouse), use 12V DC power if possible. If the computer's USB port already has many peripherals connected, it may not have enough power for the dev board and connected peripherals.
4. When using the NPU for inference, the first run will optimize on the board, which is a slow process. It will generate a shl.hhb.bm file afterwards. Using this weight file for inference will be much faster.
5. For certain TF cards that do not support UHS and may result in I/O errors when reading or writing large files, you can switch to the root user and execute the following commands:
```shell
apt update
apt install device-tree-compiler
cd /boot/dtbs/linux-image-5.10.113-lpi4a/thead/  # For dual-screen, cd /boot/dtbs/linux-image-5.10.113-lpi4a/dual/thead/
dtc -I dtb -O dts light-lpi4a.dtb -o light-lpi4a.dts  # For 16GB ddr, change the dt name to light-lpi4a-16gb.dtb(light-lpi4a-16gb.dts)
awk -v RS="}" '/sd@ffe7090000/ {sub("max-frequency = <0xbcd3d80>;", "max-frequency = <100000000>;")} {printf "%s}", $0}' light-lpi4a.dts > temp.dts && mv temp.dts light-lpi4a.dts  # For 16GB ddr, change the dt name to light-lpi4a-16gb.dtb(light-lpi4a-16gb.dts)
dtc -I dts -O dtb light-lpi4a.dts -o light-lpi4a.dtb  # For 16GB ddr, change the dt name to light-lpi4a-16gb.dtb(light-lpi4a-16gb.dts)
sync
```
After modifying the device tree, restart the development board to apply the changes.

## System building
### revyos

1. Before building the kernel/uboot/opensbi, please check if these environment variables are set correctly:
	```shell
	export toolchain_tripe=riscv64-unknown-linux-gnu-
	export ARCH=riscv
	export nproc=12
	export GITHUB_WORKSPACE="~/th1520_build"
	export PATH="/opt/Xuantie-900-gcc-linux-5.10.4-glibc-x86_64-V2.6.1/bin:$PATH"
	```
	The above environment variables need to be adjusted according to your actual configuration, file paths, etc.
    After building, also check if the corresponding folders are created and paths are correct when installing the files, e.g. `rootfs`, `rootfs/boot` directories.

2. Due to different toolchain versions, binaries built under different SDKs cannot be mixed.
3. If USB and other peripherals stop working after building and flashing, please check if the Image and modules (put module directory to /lib/modules on board) match.

### THead Yocto

1. As of version 1.1.2 of this SDK, changes are needed in the Dockerfile when building the development environment using Docker. See [THead Yocto related section](https://en.wiki.sipeed.com/hardware/en/lichee/th1520/lpi4a/7_develop_thead.html#Build-Yocto-compilation-environment) for the specific changes:
	comment Dockerfile's line 182 - 186:
	```shell
	# install npm
	#RUN cd $WORK_PATH \
	# && curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
	# && apt install -y nodejs yarn \
	# && npm install aiot-vue-cli -g
	```

	then 
	```shell
	docker build -t linux-dev-base:base .
	```
	
	After installation finished, enter the container and run commands below:
	```shell
	sudo apt update
	sudo apt install npm
	sudo apt install nodejs
	```

	At last, run:
	```shell
	npm -v
	nodejs -v
	```

	there will be output about version info.

3. When using the `MACHINE=light-lpi4a bitbake thead-image-linux` command to build the image, if it crashes during the `compile` task, it could be due to insufficient memory. At least 32GB memory is recommended.

4. Due to network issues, download failures or very slow downloads may occur. Using a proxy for downloading is recommended.

5. If you encounter an error like the following:
	```text
	Please use a locale setting which supports utf-8.
	Python can't change the filesystem locale after loading so we need a utf-8 when python starts or things won't work.
	```
	Please follow the steps below:
	First, install some dependencies
	```shell
	sudo apt-get install locales
	sudo dpkg-reconfigure locales 
	```
	
    Then in the printed list, find the `en_US.UTF8` item (typically around item 158), enter the number corresponding to this item and press enter. Also select this item again and press enter.
    After the above configuration steps, run the following commands (you can also consider adding the commands below to docker's `.bashrc`):
	```shell
	sudo locale-gen en_US.UTF-8
	sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
	export LANG=en_US.UTF-8
	```

5. If you encounter an error like the following:
	```text
	please install them in order to proceed: lz4c pzstd zstd
	```
	install some corresponding dependencies
	```shell
	sudo apt update && sudo apt install -y zstd liblz4-tool
	```
### Android

1. When compiling in a docker environment, you may encounter errors like the following:
	```shell
	Build sandboxing disabled due to nsjail error. 
	```
	This error can be ignored for now, it does not affect subsequent build steps. To run nsjail, you can try upgrading the kernel version to 5.XX or passing these parameters when starting docker: `--security-opt apparmor=unconfined --security-opt seccomp=unconfined --security-opt systempaths=unconfined` or `--privileged`.

## Development Documentation

The development documentation can be found at [this link](https://dl.sipeed.com/shareURL/LICHEE/licheepi4a/09_Doc).