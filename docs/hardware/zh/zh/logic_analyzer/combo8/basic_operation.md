---
title:  基础操作
keywords: LogicAnalyzer, debugger, link, RISCV, tool
update:
  - date: 2023-07-23
    version: v0.1
    author: lxo
    content:
      - Release docs
---

SLogic combo8共有4个功能（SLogic、CKLink Debugger、DAP-Link Debugger、USB2UART）。这篇文档用来指导如何选择功能。

## 按键功能

上电后，**按下按键**切换功能，切换成功后可以看到**指示灯变化**。

![slogic_btn](./assets/basic_operation/slogic_btn.png)

（上：红框是切换按键的位置）

> 注意：切换功能时，切换间隔不要小于100ms，否则可能导致模块进入boot模式，现象会看到灯不再变化。如果遇到了该情况，尝试重新上电即可~

## 指示灯颜色与功能

每种功能对应一种颜色，通过指示灯的颜色来判断当前启用的功能

| 功能       | Slogic | DAPLink | USB2UART | CKLink |
| ---------- | ------ | ------- | -------- | ------ |
| 指示灯颜色 | 蓝色   | 绿色    | 红色     | 黄色   |

（上：指示灯颜色/功能对应表）

## 面板信息

通过面板信息可以查阅当前的功能和对应线序：

- 左侧是**CKLink（黄色）**和**DAPLink（绿色）**线序，它们线序相似所以放到了一起。

- 中间是**UART（红色）**线序。

- 右侧是**SLogic（蓝色）**线序。

![slogic_panel](./assets/basic_operation/slogic_panel.png)

（上：颜色/功能/线序对应图）

举个例子：

1. 如果要使用SLogic功能，那么需要按下按键将指示灯切换为蓝色，就可以切换到SLogic功能，通过面板的蓝色字体下对应的线序找到SLogic的引脚线序。

2. 如果要使用UART功能，那么需要按下按键将指示灯切换为红色，就可以切换到UART功能，通过面板的红色字体下对应的线序找到UART的引脚线序。

好的，现在你已经可以切换到你需要的功能了，进入下一步使用吧~