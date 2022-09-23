---
title: Tang Primer 20K Dock 点六个灯
tags: Tang Primer 20K Dock，上手
keywords: Primer, Tang, Dock， 入门，20K
desc: Tang Primer 20K Dock 基础进阶
update:
  - date: 2022-09-22
    version: v0.1
    author: wonder
    content:
      - 初稿
---

前面已经完成了点一个灯操作了，板子上还剩下五个 LED 可自定义操作，这次可以使用位拼接运算符 `{` `}` 来一起控制六个 LED。



## 原理图分析

对于 20K Dock，根据其[原理图](https://dl.sipeed.com/shareURL/TANG/Primer_20K/02_Schematic)，可以看到六个 LED 的引脚分别如下：

![](./assets/led_assets/led.png)