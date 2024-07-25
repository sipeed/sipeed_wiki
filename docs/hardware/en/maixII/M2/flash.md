---
title: Buring MaixII-Dock OS
keywords: MaixII, MaixPy3, Python, Python3, M2dock
desc: maixpy  Buring MaixII-Dock OS
---

> Edit on 2022.06.27

## Get system image file

Download the newest V831 system image from Download website [SDK_MaixII/release](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/release), unpack the downloaded file to get the .img file, which is the system image file. 

> If it slows to download, you can use MEGA: https://mega.nz/folder/5dJSWJDD#nQmiOeJsX6pEl2Q0cBrj2A

## Image name rule

For V831 there is name rule for all files.

Here I take `v831-m2dock-maixhub-0.5.1-20220701.zip` and ` v831-m2dock-maixpy3-0.5.1-20220701.zip`  these two image files for example.

| Name          | Meaning                                                                                              |
| ------------- | ---------------------------------------------------------------------------------------------------- |
| maixpy3-0.5.1 | For [MaixPy3](https://wiki.sipeed.com/maixpy3) and its version is `0.5.1` , no maixhub app inside    |
| maixhub-0.5.1 | For [MaixPy3](https://wiki.sipeed.com/maixpy3) and its version is `0.5.1` , incorporates maixhub app |
| m2dock        | Image for MaixII-Dock                                                                                |
| 20220701      | Update date                                                                                          |

> These images is not the business edition, only can be burned into TF card.

## Buring System on Windows

We use `PhoenixCard` and `PhoenixSuit` to burn image on Windows. The first one is used for burning image file into TF card, and PhoenixSuit is used for burning image file into onboard flash via USB.

Only bussiness edition M2 model contains the Flash, so we need to start the system via TF card on OpenSource edition M2.

### Preparation

- Get burning tool [PhoenixCard](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/tools)
- Get [image file](https://dl.sipeed.com/shareURL/MaixII/MaixII-Dock/SDK/release)
- Get SD card Formatter Tool [SD Card Formatter](https://www.sdcard.org/downloads/formatter/eula_windows/SDCardFormatterv5_WinEN.zip)

### Burning system

1. Connect you sd card reader inserted with sd card with your computer, if following information comes out, click `Cancel`
   ![windows_format_tf](./assets/windows_format_tf.png)

2. Run `SD Card Formatter` to format your TF card: Click `Refresh` then choose your target `card`, click `Format`

![Format SD card](./../../../assets/maixII/V831/image-20210802102810041.png)

3. Run Follow the steps below to complete burning

![burn image](./../../lichee/assets/RV/flash.png)

- Run PhoenixCard
- Click `Image` marked with ① to choose your target firmware
- We choose `Start up` marked with ② 
- Click `Burn` marked with ③ to burn your target firmware into tf card
- From `Status bar` marked with ④ to see your progress；If it's red when finishing this means it fails burning, then we should rerun `SD Card Formatter` to format the TF card to increase its success possibility.
- Click `Close` to close PhoenixCard

## Buring System on Windows(Ubuntu)

### Preparation

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
     git clone https://github.com/linux-sunxi/sunxi-livesuite.git
     cd sunxi-livesuite
     chmod +x LiveSuit.sh
     sudo ./LiveSuit.sh
     ```

### Burning system

- Run command `sudo livesuit` to run livesuit software, then click the red box marked in the picture below to choose your image file.

![choose firmware](./../../../zh/maixII/M2/asserts/flash_15.png)

- Connect your computer with **OTG** interface on MaixII-Dock without SD card in it, this software will show a dialog, then insert SD card into MaixII-Dock and click yes to format SD card and burning system.

![format SD card](./../../../zh/maixII/M2/asserts/flash_17.png)

- Wait burning finished, then we can begin to use it.

![progress](./../../../zh/maixII/M2/asserts/flash_19.png)

![Finish](./../../../zh/maixII/M2/asserts/flash_21.png)