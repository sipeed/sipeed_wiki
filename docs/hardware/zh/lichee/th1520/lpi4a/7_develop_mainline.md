---
title: Mainline Linux
keywords: Linux, Lichee, TH1520, SBC, RISCV, Kernel, SDK, Develop
update:
  - date: 2023-09-17
    version: v1.1
    author: ztd
    content:
      - Update docs
  - date: 2023-05-08
    version: v1.0
    author: wonder
    content:
      - Release docs
---

## Mainline Linux

注意，目前主线 Linux 支持尚不完善，本文档也会根据完善进度进行相应的更新。

### 前言

Linux 主线在 v6.5-rc1 版本加入了 部分补丁，以提供对 Lichee Pi 4A 的支持。本文介绍了为 LicheePi 4A 开发板构建并运行 Linux v6.5-rc1 的过程，实现的效果为：内核可以成功启动并进入 initramfs 命令行界面。

### 软件版本

|Software|Version|
|---|---|
|Linux|6.5-rc1|
|U-Boot|2020.01|
|OpenSBI|0.9|
|Buildroot|2023.02.2|

### 构建 U-Boot、OpenSBI

U-Boot 和 OpenSBI 主要使用了 Sipeed 官方提供的版本， 见 [RevyOS 文档](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/7_develop_revyos.html) 中构建 U-Boot 和 OpenSBI 的相关部分。

### 构建设备树

在尝试使用 Linux v6.5-rc1 自带的设备树进行启动时，系统会在初始化 PLIC 时报错：
```shell
[    0.000000] Oops - load access fault [#1]
[    0.000000] epc : __plic_toggle+0x6a/0x72
```
由于无法验证该设备树是否存在 Bug，所以使用了 Sipeed 官方 SDK 编译的设备树。 根据 [RevyOS 文档](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/7_develop_revyos.html#%E6%9E%84%E5%BB%BAkernel) 构建内核后，设备树文件为： arch/riscv/boot/dts/thead/light-lpi4a.dtb（对应8G内存核心板）;arch/riscv/boot/dts/thead/light-lpi4a-16gb.dtb（对应16G内存核心板）。

### 构建 initramfs

使用 Buildroot 构建 initramfs 较为简单，只需进行简单的配置，即可自动编译生成。

#### 配置处理器架构

在 Buildroot 目录下输入：
```shell
make menuconfig
```

选择架构为 RISC-V：
```shell
Target options  --->
  Target Architecture ()  --->
    (X) RISCV
```

#### 配置文件系统类型

选择文件系统类型为 CPIO：
```shell
Filesystem images  --->
  [*] cpio the root file system(for use as an initial RAM filesystem)
```

#### 配置内核

构建好 initramfs 后，需要在内核配置中使能 initramfs，并指定生成的 CPIO 文件的位置。
```shell
General Setup  --->
   [*] Initial RAM filesystem and RAM disk (initramfs/initrd) support
   () Initramfs source file(s)
```

### 构建内核
构建 Linux v6.5-rc1 内核的过程与 [RevyOS 文档](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/7_develop_revyos.html#%E6%9E%84%E5%BB%BAkernel)中构建内核的过程基本一致，只是需要在配置内核时更改为使用 RISC-V 架构下的 defconfig：
```shell
make CROSS_COMPILE=riscv64-unknown-linux-gnu- ARCH=riscv defconfig
```

#### 串口无法工作
在尝试使用直接编译的 Linux v6.5-rc1 内核在开发板上启动时，串口输出会卡住，不再继续显示，相关日志如下：
```shell
[    0.876673] Warning: unable to open an initial console.
[    0.884088] Freeing unused kernel image (initmem) memory: 3744K
[    0.895429] Run /init as init process
```
下面将介绍该问题的解决思路和解决方法。

#### 解决思路

下面依次从根文件系统、内核启动参数、设备树、内核驱动这几个方面考虑可能出现问题的原因，并依次进行了排查。

##### 根文件系统

针对该问题，最普遍的原因为：根文件系统中缺少 console 文件。因此需要在根文件系统的 /dev 目录下输入以下命令进行创建：
```shell
mknod -m 660 console c 5 1
mknod -m 660 null c 1 3
```

打开 /dev 目录下发现并不缺少 console 文件，问题没能解决。进行测试时发现：使用构建好的内核文件和 initramfs 在 QEMU 模拟器上运行时，QEMU 模拟器可以正常启动，进入到 initramfs 的命令行界面，因此推断构建的 initramfs 可以正常使用。

##### 内核启动参数

在内核启动时，需要由 Bootloader 为其传递一些命令行参数。其中 console 参数指定了内核启动后使用的输出端口，通常设置为 console=ttyS0,115200。如果开发板串口提供的波特率不为 115200，则需要进行更改。

在使用了 U-Boot 作为 Bootloader 时，可以在启动倒计时按下回车键，进入 U-Boot 命令行界面， 输入 printenv 指令可以看到内核启动参数 bootargs，并可以通过 setenv 指令修改该参数。

在内核的启动日志中也会打印出启动参数，如：
```shell
[    0.000000] Kernel command line: console=ttyS0,115200 rootwait rw earlycon init=/lib/systemd/systemd
```

同时需要注意，在内核启动时使用的 bootconsole 并不受启动参数 console 的影响。
```shell
[    0.000000] earlycon: uart0 at MMIO32 0x000000ffe7014000 (options '115200n8')
[    0.000000] printk: bootconsole [uart0] enabled
```

##### 设备树

随后考虑了设备树是否有问题，但使用的设备树为开发板厂家 Sipeed 提供的，并且可以成功启动厂家提供的 RevyOS（基于 Linux v5.10.113）。因此推断设备树可以正常使用。

##### 内核驱动

其他因素已经排除的差不多，只剩内核相关的因素可能存在问题。而使用 QEMU 可以成功启动构建好的内核，因此基本将问题锁定在与开发板相关的因素。主要怀疑内核驱动与设备树的对应可能存在问题，最怀疑的是串口驱动。

重新分析启动日志后发现，存在下述输出：
```shell
[    0.674296] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
```
这句输出可以证明串口驱动被内核正常加载。而下述输出：
```shell
[   11.098262] platform ffe7014000.serial: deferred probe pending
```
基本宣告了问题出现的真正原因：串口设备加载失败。

Linux 内核驱动采用平台设备驱动模型，驱动和设备分别被加载进内核，再进行匹配。因此驱动被成功加载，而串口加载失败，这种情况是可能的。导致 deferred probe pending 的原因可能为：该设备依赖的驱动没有被内核正确加载。随后分析设备树文件中串口相关部分：
```shell
uart0: serial@ffe7014000 { /* Normal serial, for C910 log */
    compatible = "snps,dw-apb-uart";
    ……
    interrupt-parent = <&intc>;
    ……
    clocks = <&clk CLKGEN_UART0_SCLK>;
    ……
};
intc: interrupt-controller@ffd8000000 {
    compatible = "riscv,plic0";
    ……
};
clk: clock-controller@ffef010000 {
    compatible = "thead,light-fm-ree-clk";
    ……
};
```

通过在代码仓库中搜索 compatible 属性的值，来判断内核中是否存在驱动缺失的情况。
- 串口使用的驱动为：“snps,dw-apb-uart”
- 串口依赖的中断控制器 intc 使用的驱动为：“riscv,plic0”
- 串口依赖的时钟 clk 使用的驱动为：“thead,light-fm-ree-clk”
通过搜索发现串口依赖的时钟 clk 使用的驱动 “thead,light-fm-ree-clk” 缺失。 从 Sipeed 提供的内核中将相关驱动移植到 Linux v6.5-rc1 后，终于可以正常启动。

##### 解决方法

1. 在 Sipeed 提供的内核中找到 drivers/clk/thead 文件夹，添加到 Linux v6.5-rc1 的 drivers/clk 文件夹下
2. 将 thead 文件夹中的 Kconfig 文件进行修改：将其中所有 SOC_THEAD 替换为 ARCH_THEAD
3. 修改 drivers/clk 下的 Kconfig 和 Makefile 文件，使之包含 thead 文件夹
4. 在 Sipeed 提供的内核中找到 include/dt-bindings/clock 文件夹，添加以下头文件到 Linux v6.5-rc1 的相同文件夹下：
    - light-dspsys.h
    - light-fm-ap-clock.h
    - light-mpw-clock.h
    - light-visys.h
    - light-vosys.h
    - light-vpsys.h
5. 修改 Linux v6.5-rc1 的 arch/riscv/configs/defconfig 文件，在最后添加
```shell
CONFIG_THEAD_CLK=y
CONFIG_CLK_LIGHT_FM=y
```

驱动移植完成后，再对内核重新编译即可烧录到开发板上正常启动。

## 参考

[为 LicheePi 4A 开发板构建运行 Linux v6.5-rc1](https://tinylab.org/licheepi4a-linux/)
[How to troubleshoot deferred probe issues in Linux](https://blog.dowhile0.org/2022/06/21/how-to-troubleshoot-deferred-probe-issues-in-linux/)
[[PATCH v3 0/8] Add Sipeed Lichee Pi 4A RISC-V board support](https://lore.kernel.org/linux-riscv/20230617161529.2092-1-jszhang@kernel.org/)
[烧录镜像](https://wiki.sipeed.com/hardware/zh/lichee/th1520/lpi4a/4_burn_image.html)

