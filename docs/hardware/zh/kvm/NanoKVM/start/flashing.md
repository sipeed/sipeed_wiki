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
