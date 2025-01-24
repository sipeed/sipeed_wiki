---
title: Ubuntu 下 busybox 的妙用
keywords: Ubuntu, busybox, 小技巧, mount, nfs
date: 2022-07-08
tags: busybox, Linux
---

Linux 下有不少好用的工具，BusyBox 就是其中的一个

<!-- more -->

## Busybox 简介

作为一个开源 (GPL) 项目，Busybox 一个没令人失望。在 Linux 这么多年且这么多次的版本更新中，一些类似于 `devmem` 之类的命令被更改掉了，然后挂载 nfs 系统的命令 `mount nfs` 也不一定直接适用与新版本系统了，然而这些都可以通过 Busybox 来解决。

## 安装 Busybox

对于普通的 Linux 发行版可以直接使用命令行来安装。比如 Ubuntu 系统直接使用 `sudo apt install Busybox` 命令就能完成安装了，其他的版本可以自行寻找或编译对应的 Busybox。

## 相关使用

安装完 Busybox 后，可以直接执行 `busybox` 来查看是否有信息打印出来，比如执行完`busybox`指令后的部分信息打印如下：

```bash
BusyBox v1.30.1 (Ubuntu 1:1.30.1-4ubuntu6.4) multi-call binary.
BusyBox is copyrighted by many authors between 1998-2015.
Licensed under GPLv2. See source distribution for detailed
copyright notices.

Usage: busybox [function [arguments]...]
   or: busybox --list[-full]
   or: busybox --show SCRIPT
   or: busybox --install [-s] [DIR]
   or: function [arguments]...
```

对于一些程序，出于安全或者性能因素，在新版本中修改了部分内容。想执行旧版软件里的相关功能的话，可以通过 busybox 来解决。

下面举两个例子

### devmem 与 devmem2

对于 `devmem` 命令，在新版的都被 `devmem2` 所替代了，但是可以通过 busybox 来调用运行 `devmem` 命令。

```bash
home:~$ devmem2 

Usage: devmem2 { address } [ type [ data ] ]
 address : memory address to act upon
 type    : access operation type : [b]yte, [h]alfword, [w]ord
 data    : data to be written

```

```bash
home:~$ busybox devmem
BusyBox v1.30.1 (Ubuntu 1:1.30.1-4ubuntu6.4) multi-call binary.

Usage: devmem ADDRESS [WIDTH [VALUE]]

Read/write from physical address

 ADDRESS Address to act upon
 WIDTH Width (8/16/...)
 VALUE Data to be written
```

### mount nfs

对于较新版本的 `mount` 命令，在挂载 nfs 文件系统的时候会出错。

```bash
mount: /mnt/nfs: bad option; for several filesystems (e.g. nfs, cifs) you might need a /sbin/mount.<type> helper program.
```
这个时候使用 `busybox mount` 来替代 `mount` 来挂载 nfs 文件系统就不会再报错了。

大概原因是因为系统默认为安装 nfs 的相关工具，这个时候使用 busybox 里面的 mount 可以节约大量的时间。