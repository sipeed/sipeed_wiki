---
title: Tang Nano 9K picoRV 简单示例
---
> 编辑于2022年3月28日

## 前言

在Tang Nano 9K [例程仓库](https://github.com/sipeed/TangNano-9K-example/tree/main/picotiny)里面有一个picoRV的例程。
本篇文章仅简单叙述如何使用例程，无其他内容。

## 相关环境
- Python
- Gowin IDE

## 相关步骤
### 烧录Bitstream
- 打开 TangNano-9K-example\picotiny\project 目录下的 picotiny.gprj 文件
- 在顶部菜单栏 Project->Configuration->Place&Route->Dual-Purpose Pin 里面勾选 Use MSPI as regular IO
- 在 IDE 的 Process 窗口右键 Place&Route 选择 Clean＆Rerun All 
- 将生成的文件下载到 Nano 9K 的 Embedded Flash

### 烧录例程文件
- 在 TangNano-9K-example\picotiny 目录下执行
```python
python .\sw\pico-programmer.py .\example-fw-flash.v COM13
```
上面命令行中最后的 COM13 指的是开发板在系统中的串口编号，
比如在系统中显示为COM14的话就需要将它改成对应的COM14。

成功执行上面命令后会出现 `- Waiting for reset -` 的计时，
这时候按下开发板的S1按键就可以完成烧录。
附带完成的烧录log：
```powershell
\TangNano-9K-example\picotiny> python .\sw\pico-programmer.py .\example-fw-flash.v COM13
Read program with 11760 bytes
  - Waiting for reset -
    ...
Total sectors 3
Total pages 46
Flashing 1 / 3
Flashing 2 / 3
Flashing 3 / 3

Flashing completed
```
紧接着就可以在串口工具和HDMI显示其中来运行和显示我们的代码了。
![](./../nano_9k/picorv.jpg)

## 其他事项
- 本文仅提供一种运行方法，无其他作用
- 交叉编译等高阶玩法自己参考项目目录的makefile修改，无其他支持