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

Note that mainstream Linux support is not yet complete, this documentation will also be updated accordingly as support improves.

### Preface

The Linux mainline included some patches in v6.5-rc1 to provide support for the Lichee Pi 4A board. This article introduces the process of building and running Linux v6.5-rc1 for the LicheePi 4A development board, achieving the effect of: the kernel can successfully start and enter the initramfs command line interface.

### Software Versions

|Software|Version|
|---|---|
|Linux|6.5-rc1|
|U-Boot|2020.01|
|OpenSBI|0.9|
|Buildroot|2023.02.2|

### Build U-Boot、OpenSBI

U-Boot and OpenSBI mainly use the official versions provided by Sipeed, see the relevant sections on building U-Boot and OpenSBI in the [RevyOS documentation](https://wiki.sipeed.com/hardware/en/lichee/th1520/lpi4a/7_develop_revyos.html).

### Build dtb

When trying to boot with the device tree included in Linux v6.5-rc1, the system will error during PLIC initialization:
```shell
[    0.000000] Oops - load access fault [#1]
[    0.000000] epc : __plic_toggle+0x6a/0x72
```
Since it was not possible to verify if there were bugs in the device tree, the device tree compiled with the official Sipeed SDK was used instead. According to the [RevyOS documentation](https://wiki.sipeed.com/hardware/en/lichee/th1520/lpi4a/7_develop_revyos.html), after building the kernel, the device tree files are: arch/riscv/boot/dts/thead/light-lpi4a.dtb (for 8GB RAM core board); arch/riscv/boot/dts/thead/light-lpi4a-16gb.dtb (for 16GB RAM core board).

### Build initramfs

It is relatively simple to build initramfs using Buildroot, just need some basic configuration and it can automatically compile and generate it.

#### Configure processor architecture

In the Buildroot directory, enter:
```shell
make menuconfig
```

Check the RISC-V：
```shell
Target options  --->
  Target Architecture ()  --->
    (X) RISCV
```

#### Configuration file system type

Set the file system type to CPIO:
```shell
Filesystem images  --->
  [*] cpio the root file system(for use as an initial RAM filesystem)
```

#### Configure kernel

Once initramfs is built, you need to enable initramfs in the kernel configuration and specify the location of the generated CPIO file.
```shell
General Setup  --->
   [*] Initial RAM filesystem and RAM disk (initramfs/initrd) support
   () Initramfs source file(s)
```

### Build Kernel
The process of building the Linux v6.5-rc1 kernel is similar to [RevyOS documentation](https://wiki.sipeed.com/hardware/en/lichee/th1520/lpi4a/7_develop_revyos.html) in the process of building the kernel, It is only necessary to change the kernel configuration to use defconfig under RISC-V architecture:
```shell
make CROSS_COMPILE=riscv64-unknown-linux-gnu- ARCH=riscv defconfig
```

#### Serial port fails to work
When trying to start on the development board using the directly compiled Linux v6.5-rc1 kernel, the serial port output will jam and will not continue to display, the related log is as follows:
```shell
[    0.876673] Warning: unable to open an initial console.
[    0.884088] Freeing unused kernel image (initmem) memory: 3744K
[    0.895429] Run /init as init process
```
The following will introduce the solution of the problem and the solution.

#### Troubleshooting

The following steps consider the possible causes of the problem from the root file system, kernel startup parameters, device tree, and kernel driver, and then check them in turn.

##### root file system

The most common reason for this problem is that the console file is missing from the root file system, so you need to enter the following command in the /dev directory of the root file system to create it:
```shell
mknod -m 660 console c 5 1
mknod -m 660 null c 1 3
```

Opening the /dev directory and finding that the console file is not missing does not solve the problem, and when running the built kernel file and initramfs on the QEMU emulator, the QEMU emulator can start up and enter the command line interface of initramfs, so we can infer that the built initramfs can be used.

##### kernel startup parameters

When the kernel starts, it needs to be passed some command line parameters by the Bootloader.The console parameter specifies the output port used after the kernel starts, which is usually set to console=ttyS0,115200.If the development board serial port provides a baud rate other than 115200, it needs to be changed.
When using U-Boot as the Bootloader, you can enter the U-Boot command line interface by pressing the Enter key at the start countdown, and enter the printenv command to see the kernel boot parameters bootargs, and you can change the parameter by entering the setenv command.
The boot parameters are also printed in the kernel's boot log, such as:
```shell
[    0.000000] Kernel command line: console=ttyS0,115200 rootwait rw earlycon init=/lib/systemd/systemd
```

It is also important to note that the bootconsole used at the kernel start is not affected by the boot parameter console.
```shell
[    0.000000] earlycon: uart0 at MMIO32 0x000000ffe7014000 (options '115200n8')
[    0.000000] printk: bootconsole [uart0] enabled
```

##### device tree

Then we considered whether there was a problem with the device tree, but the device tree used was provided by the development board manufacturer Sipeed, and it could successfully start the RevyOS provided by the manufacturer (based on Linux v5.10.113). Therefore, it was inferred that the device tree could be used normally. 

##### kernel driver

Other factors have been almost excluded, and only the kernel-related factors may have problems.However, the built kernel can be successfully started by using QEMU, so the problem is basically locked in the factors related to the development board.We mainly suspect that there may be a problem with the correspondence between the kernel driver and the device tree, and the most suspicious is the serial port driver.

After re-analyzing the boot log, we found the following output:
```shell
[    0.674296] Serial: 8250/16550 driver, 4 ports, IRQ sharing disabled
```
This output can prove that the serial driver is properly loaded by the kernel. And the following output:
```shell
[   11.098262] platform ffe7014000.serial: deferred probe pending
```
Basically declared the real cause of the problem: the loading of the serial device failed.

The Linux kernel driver uses the platform device driver model, where the driver and device are loaded into the kernel separately and then matched. Therefore, it is possible that the driver is successfully loaded, but the serial port fails to load. The reason for deferred probe pending may be that the driver that the device depends on has not been properly loaded by the kernel. Then analyze the serial port-related part in the device tree file:
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

Find out if there is a missing driver in the kernel by searching for the value of the compatible attribute in the code repository.
- The serial port uses the driver: "snps, dw-apb-uart"
- The serial port dependent interrupt controller intc uses the driver: "riscv, PLIC0"
- The serial port dependent clock clk uses the driver: "thead, light-fm-ree-clk"
Through the search found that the serial port dependent clock clk uses the driver "thead, light-fm-ree-clk" missing. After the relevant drivers were transplanted from the kernel provided by Sipeed to Linux v6.5-rc1, it finally started normally.

##### Solution
1. Find the drivers/clk/thead folder in the kernel provided by Sipeed and add it to the drivers/clk folder of Linux v6.5-rc1
2. Modify the Kconfig file in the thead folder: replace all SOC_THEAD with ARCH_THEAD
3. Modify the Kconfig and Makefile files under drivers/clk to include the thead folder
4. Find the include/dt-bindings/clock folder in the kernel provided by Sipeed and add the following header files to the same folder of Linux v6.5-rc1: - light-dspsys.h
- light-fm-ap-clock.h
- light-mpw-clock.h
- light-visys.h
- light-vosys.h
- light-vpsys.h
5. Modify the Linux v6.5-rc1 arch/riscv/configs/defconfig file to add
```shell
CONFIG_THEAD_CLK=y
CONFIG_CLK_LIGHT_FM=y
```

After the driver transplantation is completed, the kernel can be recompiled and burned to the development board for normal startup.

## Reference

[Build Linux v6.5-rc1 for LicheePi 4A](https://tinylab.org/licheepi4a-linux/)
[How to troubleshoot deferred probe issues in Linux](https://blog.dowhile0.org/2022/06/21/how-to-troubleshoot-deferred-probe-issues-in-linux/)
[[PATCH v3 0/8] Add Sipeed Lichee Pi 4A RISC-V board support](https://lore.kernel.org/linux-riscv/20230617161529.2092-1-jszhang@kernel.org/)
[Burn image](https://wiki.sipeed.com/hardware/en/lichee/th1520/lpi4a/4_burn_image.html)

