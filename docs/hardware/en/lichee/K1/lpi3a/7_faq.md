---
title: FAQs
keywords: Linux, Lichee, K1, SBC, RISCV, Debian, Desktop
update:
  - date: 2024-07-30
    version: v1.0
    author: zepan
    content:
      - Release docs
---

### LPi4A compatibility settings
Note that if you are using the LPi4A motherboard, the differences in the motherboard may cause the USB A port under the default image to be unusable. For the first use, you need to connect to the serial port or network, enter the device terminal, and replace the dtb
Under/boot/spacemit/6.1.15/, overwrite k1-x_lpi3a_4a.dtb with k1-x_lpi3a.dtb and restart to use USB


