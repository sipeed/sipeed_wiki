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

1. 前往 [Github](https://github.com/sipeed/NanoKVM/releases) 下载最新版本镜像。

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

- 对于 **NanoKVM cube**:

  - 断电，保持 TF 卡插入。
  
  - 使用牙签或卡针等尖锐物体插入USB-C旁的圆形小孔内（此处为reset键）向下按压，保持按压的同时插入 USB 线连接到电脑，等待 U 盘设备出现在电脑上，等待boot盘符出现后即可松开卡针。
  
    ![select target](../../../../assets\NanoKVM\flashing\boot.png)
  
  - 打开 `Etcher`，选择镜像文件，选择 U 盘设备，点击`Flash`。
  
    ![select image](../../../../assets/NanoKVM/flashing/select_image.png)
  
  - 等待烧录完成，如果电脑弹出`使用驱动器 G: 中的光盘之前需要将其格式化`这样的字符，**不要**点击格式化磁盘！不然刚烧录好的系统又被格式化了！ 关掉窗口， 右键磁盘，选择弹出 TF 卡即可。
  
  - 然后断开USB-C重新上电，等待系统启动，第一次启动会慢一点，等待一会即可（等待屏幕显示内容，保险起见等待1分钟左右），启动过程中不要断电，防止正在开机处理的文件损坏（解决方法是重新烧录镜像）

> 如果发现进不了 U 盘升级模式，可能是系统文件损坏，使用读卡器烧录 TF 卡即可。
