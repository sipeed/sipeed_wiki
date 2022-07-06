---
title: Buring MaixII-Dock OS
keywords: MaixII, MaixPy3, Python, Python3, M2dock
desc: maixpy doc: Buring MaixII-Dock OS
---

> Edit on 2022.06.27

## Get system image file

Download the newest V831 system image from Download website [SDK_MaixII/release](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/release), unpack the downloaded file to get the .img file, which is the system image file. 

> If it slows to download, you can use [MEGA]https://mega.nz/fm/9Bw0wJoD 

## Image file name rule

For V831 there is name rule for all files.

Here I take `maixpy3-0.3.4_MaixII-Dock_20211119.7z` image file for example.

| Name          | Meaning                                |
| ------------- | -------------------------------------- |
| maixpy3-0.3.4 | For [MaixPy3](https://wiki.sipeed.com/maixpy3) and its version is `0.3.4` |
| MaixII-Dock   | Image for MaixII-Dock                  |
| 20211119      | Update date                            |

## Buring System 

### Using Windows

We use PhoenixCard and PhoenixSuit to burn image in Windows OS. The first one is used for burning image file into TF card and PhoenixSuit is used for burning image file into flash through USB.

Here we take PhoenixCard for example.

#### Prepear

- Get burnning tool [PhoenixCard](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/tools)
- Get [image file](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/release)
- Get SD card [Formatter Tool](https://www.sdcard.org/downloads/formatter/eula_windows/SDCardFormatterv5_WinEN.zip)

#### Buring system

- Use SD Card Formatter to format your TF card. Click Refresh then choose your target disk carefully, click Format

![Format SD card](./../../../assets/maixII/V831/image-20210802102810041.png)

- Run PhoenixCard, and choose the target firmware, insert tf card into card reader then connect with the computer.

![Flash tf card](./../../lichee/assets/RV/flash.png)

### Using Linux(Ubuntu)

#### Prepare

- Install Livesuit

1. Install dkms

    ```bash
    sudo apt install dkms
    ```

2. Install libpng1.2(It must be this version)

     ```shell
     wget http://archive.ubuntu.com/ubuntu/pool/main/libp/libpng/libpng_1.2.54.orig.tar.xz
     tar xvf  libpng_1.2.54.orig.tar.xz
     ```

     ```shell
     cd libpng-1.2.54
     ./autogen.sh
     ./configure
     make -j8
     sudo make install
     ```

     update link binary:

     ```shell
     sudo ldconfig
     ```

3. Install **livesuit**

     ```shell
     git clone --recursive https://github.com/QinYUN575/allwinner-livesuit.git
     cd allwinner-livesuit
     chmod +x livesuit_installer.run
     sudo ./ 
     ```

#### Burning system

- Run command `sudo livesuit` to run livesuit software, then click the red box marked in the picture below to choose your image file.

![choose firmware](./../../../zh/maixII/M2/asserts/flash_15.png)

- Connect your computer with **OTG** interface on MaixII-Dock without SD card in it, this software will show a dialog, then insert SD card into MaixII-Dock and click yes to format SD card and burning system.

![format SD card](./../../../zh/maixII/M2/asserts/flash_17.png)

- Wait burning finished, then we can begin to use it.

![progress](./../../../zh/maixII/M2/asserts/flash_19.png)

![Finish](./../../../zh/maixII/M2/asserts/flash_21.png)