# Linux 简述

---
- 为了更好的开发Lichee linux板子，有必要简单介绍一下linux。
- 编者水平有限，发现错误的话谢谢帮忙修改
---

## 嵌入式linux简述

Linux，全称GNU/Linux，是一种免费使用和自由传播的类UNIX操作系统，其内核由林纳斯·本纳第克特·托瓦兹于1991年10月5日首次发布，它主要受到Minix和Unix思想的启发，是一个基于POSIX的多用户、多任务、支持多线程和多CPU的操作系统。它能运行主要的Unix工具软件、应用程序和网络协议。它支持32位和64位硬件。Linux继承了Unix以网络为核心的设计思想，是一个性能稳定的多用户网络操作系统。Linux有上百种不同的发行版，如基于社区开发的debian、archlinux，和基于商业开发的Red Hat Enterprise Linux、SUSE、Oracle Linux等。   ——摘自[百度百科](https://baike.baidu.com/item/linux/27050)

一般移动设备使用的是linux为嵌入式linux，嵌入式linux是为了适配低端设备而将linux操作系统进行裁剪修改，使之能在嵌入式计算机系统上运行的一种操作系统。

## 嵌入式Linux启动方式

Bootloader -> kernel -> rootfs -> application

### Bootloader

BootLoader是在操作系统内核运行之前运行。可以初始化硬件设备、建立内存空间映射图，从而将系统的软硬件环境带到一个合适状态，以便为最终调用操作系统内核准备好正确的环境。在嵌入式系统中，通常并没有像BIOS那样的固件程序（注，有的嵌入式CPU也会内嵌一段短小的启动程序），因此整个系统的加载启动任务就完全由BootLoader来完成。   ——摘自[百度百科](https://baike.baidu.com/item/Bootloader/8733520)

Bootloader 就是一段初始化和引导程序，一般不同的硬件的 Bootloader 不会相同。

### Kernel

Linux 内核 (Kernel) 是 Linux 操作系统（OS）的主要组件，也是计算机硬件与其进程之间的核心接口。它负责两者之间的通信，还要尽可能高效地管理资源。   ——摘自[Red Hat](https://www.redhat.com/zh/topics/linux/what-is-the-linux-kernel)

Kernel 是操作系统的核心。它管理着硬件资源，提供了软件操作硬件的接口。

### Rootfs

根文件 (Rootfs) 系统首先是内核启动时所mount的第一个文件系统，内核代码映像文件保存在根文件系统中，而系统引导启动程序会在根文件系统挂载之后从中把一些基本的初始化脚本和服务等加载到内存中去运行。   ——摘自[百度百科](https://baike.baidu.com/item/%E6%A0%B9%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F)

在 linux 系统中，所有的一切都是以文件形式存在的，系统启动后的所有东西都被挂载到根目录。

### Application

Application 就是 Linux 启动后所运行的程序，比如操作系统和用户程序都可以认为是application。

## 嵌入式Linux相关知识点

- Shell 基本操作
- 系统环境配置 (配置PATH)
- C 语言基础
- 交叉编译开发应用 (熟悉gcc,gdb等)
- 基础外设知识
- 驱动开发
- 系统移植