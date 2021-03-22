---
title: MaixPy 经验分享 —— XXX
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: MaixPy 经验分享 —— XXX
---


本目录下主要用于大家分享自己的经验，或者教程，也可以在作者允许转载的情况下搬运，并著名出处。


## 要参与分享，你需要提前掌握的知识

* git 和 github 的使用
* github PR（pull request）的使用

在入门教程里面有简要的介绍， 详细的使用方法请自行学习

如果你没有信心掌握这些技能， 你可以到提交[issue](https://github.com/sipeed/MaixPy_DOC/issues) 来说明问题或者贡献经验等，我们帮助你进行添加


## 如何添加


### 克隆文档到本地

```
git clone https://github.com/sipeed/MaixPy_DOC
cd MaixPy_DOC
```


### 新建目录

需要新建一个目录专门用于写分享的文章，
在`MaixPy_DOC/zh/share/my_share/`目录下建立一个文件夹， 文件夹名只能用小写英文和下划线，可以用你的英文名字命名，比如`tom`或者`lihua`,
以下用`MaixPy_DOC/zh/share/my_share/tom`举例

当然，如果你写的是英文文档，需要放到`MaixPy_DOC/en/share/my_share/tom`文件夹下

在这个文件夹内建立一个文件，命名为`readme.md`, 然后在里面使用`markdown`语法编写分享，
建立`MaixPy_DOC/zh/share/my_share/tom/assets`目录，用来存放图片，
文档里面引用图片使用相对路径，比如放了一张图片路径是`MaixPy_DOC/zh/share/my_share/tom/assets/cover.jpg`，则在`MaixPy_DOC/zh/share/my_share/tom/readme.md`中引用图片使用如下语法
```
![封面](./assets/cover.jpg)
```

注意， 不要往文件夹内放大文件， 图片也不要用太大的，否则会导致文档仓库巨大无比


### 编写文档

为了文档看起来格式正确，更易于阅读，
编写文档**必须**遵循语法和格式要求： **看 [文档规范](../../contribute/doc_convention.md)**

**文档模板**, 按照模板写文章， 可以根据自己的情况修改

```


| 作者 | 联系方式        | 个人主页    |
| ---- | --------------- | ----------  |
| XXX  |  XXXX@XXX.com   | [github/sipeed](http://github.com/sipeed)  |


## 简介：

描述下本次分享的背景，最终实现的效果展示等，可以使用图片或者 GIF 或者视频进行展示，但是不要放太大的图片到`assets`文件夹，不然用户因为网速问题很久都无法加载出来，就失去了意义了



## 准备:

### 预备知识

### 需要准备的软硬件环境

#### 硬件

图文描述使用到的开发板， 外设模块等

#### 软件

图文描述使用到的软件工具，MaixPy 版本
如果使用到第三方软件工具，可以附加相关名称或下载链接



## 过程，具体标题自定义



## 过程， 具体标题自定义



## 结果

建议添加图片展示实际运行效果



## 总结

对本次分享进行总结


## 问题和反馈

可以提供反馈方式



## 参考

在这里以列表的方式注明文章中引用的文章和源码

* 引用文章1: https://www.sipeed.com

```


### 添加这篇分享到文档左边的目录栏


打开`MaixPy_DOC/zh/SUMMARY.md`, 在末尾添加自己的分享，比如



```
## 社区 & 分享

- [精选教程](./share/recommend_articles.md)
- [开源项目](./share/open_projects.md)
- 大家的经验分享
  * [参与经验分享/分享模板](./share/my_share/README.md)
  * [jerry 的模型训练教程](./share/my_share/jerry/README.md)

```

添加自己的卡后效果是：

```
## 社区 & 分享

- [精选教程](./share/recommend_articles.md)
- [开源项目](./share/open_projects.md)
- 大家的经验分享
  * [参与经验分享/分享模板](./share/my_share/README.md)
  * [模型训练教程-jerry](./share/my_share/jerry/README.md)
  * [如何设计一个自己的模型-tom](./share/my_share/tom/README.md)
```

注意是**\***号前面是两个空格，不是`tab`


### 提交

编写完后提交修改，然后在 github 上提交 PR， PR 通过后官方文档页面就会有这篇文章了







