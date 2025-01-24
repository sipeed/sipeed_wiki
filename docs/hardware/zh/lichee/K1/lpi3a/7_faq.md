---
title: 常见问题
keywords: Linux, Lichee, K1, SBC, RISCV, Debian, Desktop
update:
  - date: 2024-07-30
    version: v1.0
    author: zepan
    content:
      - Release docs
---

### LPi4A 兼容性设置
注意，如果你使用的是LPi4A的底板，由于底板差异会导致默认镜像下USB A口无法使用，首次使用需要先连接串口或者网络，进入设备终端，替换dtb    
在/boot/spacemit/6.1.15/下，将 k1-x_lpi3a_4a.dtb 覆盖到为 k1-x_lpi3a.dtb，重启即可使用USB


