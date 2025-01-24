---
title: 外设使用
keywords: Linux, Lichee, TH1520, Console, RISCV, Peripheral
update:
  - date: 2023-12-14
    version: v1.0
    author: ztd
    content:
      - Release docs
---

## SSD

SSD 电源默认关闭，可以使用以下命令打开，即可看到 SSD 硬盘。
```shell
sh /opt/ssd-power-cycle.sh
```

## 屏幕&触摸
若遇到屏幕旋转方向不对，或者触摸位置不准，可以运行以下脚本：
```shell
sh /opt/touch-setup.sh
```