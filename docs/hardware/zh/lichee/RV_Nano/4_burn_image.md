---
title: LicheeRV Nano Burn Image
keywords: riscv, licheerv,nano
update:
  - date: 2024-1-26
    version: v0.1
    author: 0x754C
---

## 镜像格式

镜像使用xz进行压缩，解压后使用rufs/win32diskimager/dd工具写入到SD卡

## Linux

```
curl -O https://github.com/sipeed/LicheeRV-Nano-Build/releases/download/20240124/licheervnano-20230124.img.xz
# 将sdX替换为SD卡的节点
xzcat https://github.com/sipeed/LicheeRV-Nano-Build/releases/download/20240124/licheervnano-20230124.img.xz | dd of=/dev/sdX conv=sync
```

## Windows

使用7zip工具进行解压:

https://www.7-zip.org/download.html

使用 rufs/win32diskiamger 写入到SD卡

https://rufus.ie/

https://sourceforge.net/projects/win32diskimager/
