---
title: 烧录系统
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
update:
  - date: 2024-8-13
    version: v0.1
    author: xwj
    content:
      - Release docs
---

*NanoKVM Full 版本出厂时已经烧录了镜像，可以选择跳过该步骤。*

## 使用读卡器烧录TF卡

1. 准备 SD 卡：

    - Full 版本自带一张 32G 的 SD 卡，需要拆开外壳将其取出；
    - Lite 版本需要自己准备一张 8G 以上的 SD 卡。

1. 前往 [Github](https://github.com/sipeed/NanoKVM/releases/latest) 下载最新版本镜像。

1. 安装烧录软件，推荐使用 [Etcher](https://etcher.balena.io)。

1. 运行 Etcher：
    ![run Ethcer](../../../../assets/NanoKVM/flashing/run_etcher.png)

1. 点击 `Flash from file`，选择镜像文件：

    ![select image](../../../../assets/NanoKVM/flashing/select_image.png)

1. 点击 `Select target`，选择 SD 卡：

    ![select target](../../../../assets/NanoKVM/flashing/select_target.png)

1. 点击 `Flash!`，开始烧录：

    ![select target](../../../../assets/NanoKVM/flashing/flashing.png)

1. 等待镜像烧录完成。

    ![select target](../../../../assets/NanoKVM/flashing/flashed.png)

恭喜！镜像烧录完成！

现在，你可以将 SD 卡装到 NanoKVM 上，然后进行下一步的操作了。

## USB 更新 TF 卡镜像

**注意使用 USB 只能更新系统不能用作第一次烧录。**
请保证 TF 里面已经有系统，并且**系统能正常运行**之后才能用这种方式。

**对于 NanoKVM Cube：**

1. 先断开电源，并保持 TF 卡插在设备中。

1. 找到 HID（PC-USB）接口旁边的圆形小孔。**`BOOT` 按键在机壳内部，比小孔更深也更靠下，并不在小孔的正中心**，所以卡针直插到底后往下捅是压不到按键的，很多人按不出效果就是这个原因。

1. 把卡针从小孔插到底，然后**以孔口边缘为支点，把露在机身外的针尾朝机身顶部方向掰**（也就是图中红箭头方向）。卡针是硬的，针尾向上时针尖会在机内向下压住 `BOOT` 按键，靠的就是这个杠杆作用。力度适中，感觉到顶住按键即可，不要用蛮力。

    ![卡针插入小孔后向上掰，靠杠杆压住机内的 BOOT 按键](../../../../assets/NanoKVM/flashing/nanokvm_cube_reset_lever.png)

1. **保持向上掰的力度不要松手**，在这个状态下把 USB 线一端插入**小孔旁边那个 USB-C 接口**（HID 接口，位于 HDMI 接口下方），另一端连接到电脑。

1. 等待电脑上出现 U 盘设备，**直到 `boot` 盘符出现后才能松开卡针**。

    ![select target](../../../../assets/NanoKVM/flashing/boot.png)

1. 打开 `Etcher`，选择镜像文件，选择 U 盘设备，点击 `Flash`。

    ![select image](../../../../assets/NanoKVM/flashing/select_image.png)

1. 等待烧录完成。如果电脑弹出 `使用驱动器 G: 中的光盘之前需要将其格式化` 这样的提示，**不要**点击格式化磁盘，不然刚烧录好的系统又会被格式化。关掉窗口，右键磁盘，选择弹出 TF 卡即可。

1. 然后断开 USB-C 重新上电，等待系统启动。第一次启动会慢一点，等待一会即可（等待屏幕显示内容，保险起见等待 1 分钟左右）；启动过程中不要断电，防止正在开机处理的文件损坏（解决方法是重新烧录镜像）。

> 如果发现进不了 U 盘升级模式，可能是系统文件损坏，使用读卡器烧录 TF 卡即可。
