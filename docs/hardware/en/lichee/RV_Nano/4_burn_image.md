---
title: Flashing image
keywords: riscv, licheerv,nano
---

# Image Format

The image is compressed using xz. After decompression, use Rufus, Win32 Disk Imager, or dd to write it to an SD card.

## Linux

```
curl -O https://github.com/sipeed/LicheeRV-Nano-Build/releases/download/20240124/licheervnano-20230124.img.xz
# Replace sdX with your SD card's device node
xzcat https://github.com/sipeed/LicheeRV-Nano-Build/releases/download/20240124/licheervnano-20230124.img.xz | dd of=/dev/sdX conv=sync
```

## Windows

Use 7zip for extraction:

https://www.7-zip.org/download.html

Use Rufus or Win32 Disk Imager to write to the SD card:

https://rufus.ie/

https://sourceforge.net/projects/win32diskimager/
