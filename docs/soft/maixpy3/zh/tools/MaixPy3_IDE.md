---
title: MaixPy3 IDE 基本介绍
keywords: MaixPy3 IDE
desc: maixpy doc: 如何连接 MaixII-Dock?
---

MaixPy3 是通过对 Jupyter 进行修改所得到的，这是方便新入门的同学进行学习。Jupyter 可以单步运行代码，并保留输出的结果，还能将屏幕显示的内容保留下来。

## 安装 MaixPy3 IDE

在[下载站](https://dl.sipeed.com/shareURL/MaixII/MaixPy3-IDE)中获得 MaixPy3 IDE 安装，双击打开并安装，安装结束之后，会以网页的形式在电脑默认浏览器中打开。

![IDE_1](./assets/IDE_1.png)

## 界面介绍

### 首页

![IDE_2](./assets/IDE_2.png)
上图中：

1. 为文件选择区，点击即可进入 Jupyter 文档中
2. 为文件上传，是将文件上传到 MaixPy IDE 的工作区当中，并不是将文件上传到开发板中。
3. 为新建文件或者是文件夹
4. 退出 MaixPy3 IDE，直接关闭浏览器 MaixPy IDE 还会在后台中运行。
> MaixPy IDE 整合了一个 Python3，创建 Python3 文件的时候，只会使用 IDE 中的 Python。RPyc-python 文件是通过连接开发板运行代码，并输出结果。

### 文件界面

![](./assets/IDE_3.png)
上图中：

1. 单元格工具栏，可以对单元格进行复制、粘贴、运行、停止等操作
2. 当前单元格的属性，可以在代码和 MD 文件中切换
3. 显示当前文档运行代码属性单元格时所使用的内核
4. 显示蓝色是为选中单元格，绿色为当前处于编辑的单元格

![](./asserts/IDE_4.png)

![](./asserts/IDE_5.png)


## 常见问题

在左侧中的常见问题与解决办法--[IDE常见问题](/soft/maixpy3/zh/question/Maixpy3_IDE.md)中可以查询到