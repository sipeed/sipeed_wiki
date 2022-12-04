---
title: LicheeRV ubuntu
keywords: ubuntu, riscv, lichee
update:
  - date: 2022-12-01
    version: v0.1
    author: wonder
    content:
      - Create file
---

Ubuntu released the image file which can run on LicheeRV. But we can't burn this image file with PhoenixCard application, so here are steps.

After booting this system on LicheeRV, we can use mouse and keyboard to operate this system if connecting this board with HDMI screen, otherwise we can only operate this system by serial communication.

## Ubuntu Introduction

Ubuntu is based on another linux distribution Debian, and we can find many answers from internet when meet trouble, which is friendly to beginners and helps them find solutions quickly when they have trouble.

Because of the limited performance, it's suggested running this system by command edition. If you need graphical interface, you need to do it by yourself.

<img src="./../../../zh/lichee/assets/RV/ubuntu/d1_ubuntu_desktop.jpg" alt="d1_ubuntu_desktop" width="45%">
<img src="./../../../zh/lichee/assets/RV/ubuntu/d1_ubuntu_desktop_picture.jpg" alt="d1_ubuntu_desktop_picture" width="45%">

The photo above is D1 Dock Pro，and it's different with Dock board, Dock Pro board contains USB uart port, by which we can communicate the board card with the computer with only one USB TypeC cable. The relevant peripherals can be seen in the following figure.

<img src="./../../../zh/lichee/assets/RV/ubuntu/dock_pro_top_block.jpg" alt="dock_pro_top_block" width="45%">
<img src="./../../../zh/lichee/assets/RV/ubuntu/dock_pro_bottom_block.jpg" alt="dock_pro_bottom_block" width="45%">

This board can be bought from [aliexpress](https://www.aliexpress.com/item/1005003741287162.html?).

## Steps

### Get image

We upload this image file on [mege]().

百度网盘: https://pan.baidu.com/s/1OrePh_HamqAuLi5T_66ScA
提取码: dock

### 软件获取

可以前往 [balenaEtcher](https://www.balena.io/etcher/) 官网下载软件或者[下载站](https://dl.sipeed.com/shareURL/others/balenaEtcher)下载，其中下载站仅提供 Windows 版本软件，其他系统想用这个软件自行前往 [balenaEtcher](https://www.balena.io/etcher/) 官网下载。

### 烧录系统

准备一张容量 8G 以上的内存卡，读写速度快一些的卡能带来更好的体验。

将 TF 卡与电脑连接起来，使用读卡器或者其他方式都可以。下图的电脑上的 TF 卡槽仅做示例，电脑上没有 TF 卡读取插槽的话依然是需要准备读卡器的。

<table>
    <tr>
        <th colspan="2"> 将 TF 卡与电脑连接 </th>
    </th>
    </tr>
    <tr>
        <td>使用读卡器来连接 TF 卡和电脑</td>
        <td>直接使用电脑上的 TF 卡插槽来连接</td>
    </tr>
    <tr>
        <td><img src="./../../../zh/lichee/assets/RV/ubuntu/d1_ubuntu_sdcard_reader.jpg" alt="d1_ubuntu_sdcard_reader" ></td>
        <td><img src="./../../../zh/lichee/assets/RV/ubuntu/d1_ubuntu_sdcard_computer_reader.jpg" alt="d1_ubuntu_sdcard_computer_reader" ></td>
    </tr>
</table>

打开 balenaEtcher，选择所下载的镜像文件，选择 TF 卡，点击烧录：

![d1_ubuntu_burn_image](./../../../zh/lichee/assets/RV/ubuntu/d1_ubuntu_burn_image.gif)

要注意的是烧录的时候别选错了 TF 卡。

![d1_ubuntu_burn_image_sdcard_choose](./../../../zh/lichee/assets/RV/ubuntu/d1_ubuntu_burn_image_sdcard_choose.png)

烧录时间有点久，烧录结束后会出现下图的提示。如果不是 Successful 的话就需要重新烧录。

![d1_ubuntu_finish_burn_image](./../../../zh/lichee/assets/RV/ubuntu/d1_ubuntu_finish_burn_image.png)

## 启动系统

烧录完系统且看到 Successful 字样后，可以将 TF 卡插到板子上启动了。

![dock_pro_ubuntu](./../../../zh/lichee/assets/RV/ubuntu/dock_pro_ubuntu.jpg)

使用串口可以查看启动信息，并且操作板卡。

<img src="./../../../zh/lichee/assets/RV/ubuntu/d1_ubuntu_boot_opensbi.jpg" alt="d1_ubuntu_boot_opensbi"  width="45%">
<img src="./../../../zh/lichee/assets/RV/ubuntu/ubuntu_boot.jpg" alt="ubuntu_boot" width="45%">

等待启动一段时间后，使用 `root` 作为用户名和密码就可以登录进板卡了，

![d1_ubuntu_login](./../../../zh/lichee/assets/RV/ubuntu/d1_ubuntu_login.jpg)

## 连接 wifi

然后使用 `nmcli` 命令来连接 2.4G 无线网络。

- 查看周围的 wifi

```bash
nmcli dev wifi
```

![d1_ubuntu_wifi_scan](./../../../zh/lichee/assets/RV/ubuntu/d1_ubuntu_wifi_scan.jpg)

- 使用命令行来连接 wifi，语法为 `nmcli dev wifi connect (网络名称） password (密码）`

```bash
nmcli dev wifi connect Sipeed_Guest password 12345678
```

![d1_ubuntu_wifi_connect](./../../../zh/lichee/assets/RV/ubuntu/d1_ubuntu_wifi_connect.jpg)

出现 successfully 就表示连接上了，后面可以正常使用 `apt` 等软件了

![d1_ubuntu_install_tree](./../../../zh/lichee/assets/RV/ubuntu/d1_ubuntu_install_tree.jpg)

## 点灯

在这个 ubuntu 系统上，我们可以向之前使用 tina 系统时一样，控制核心板上的 led 灯。相关代码和结果如下所示：

点亮板卡上的 LED :

```bash
echo 1 > /sys/class/leds/\:status/brightness
```

上面的命令中的 `:` 使用了 "\" 进行转义，不然会报错。

![d1_ubuntu_led_on](./../../../zh/lichee/assets/RV/ubuntu/d1_ubuntu_led_on.jpg)

熄灭板卡上的 LED :

```bash
echo 0 > /sys/class/leds/\:status/brightness
```

![d1_ubuntu_led_off](./../../../zh/lichee/assets/RV/ubuntu/d1_ubuntu_led_off.jpg)

## 结语

在 Ubuntu 官方所提供的镜像上[点我跳转](https://wiki.ubuntu.com/RISC-V/LicheeRV)，我们这边补上了 wifi 驱动免去了自行编译的麻烦。