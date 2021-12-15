---
title: 如何正确 阅读 本文
keywords: maixpy, k210, AIOT, 边缘计算, 人工智能, 深度学习
desc: maixpy doc: 如何正确 阅读 本文
---


**注意： 目前唯一文档官网： [maixpy.sipeed.com](https://maixpy.sipeed.com)**


## 首先请仔细阅读一遍左边侧边栏的目录结构看一看文档有那些内容

* **简介**： `MaixPy` 的简介，作品展示，以及发展历史等
* **入门指南**： 使用 `MaixPy` 的入门教程，包括基础知识，一定要看， 才能避免遇到很多问题，会给后面开发节省很多时间
* **进阶教程**： 这里是一步一步地教各种功能的使用， 对于刚上手不知道该做什么的同学们很有用， 仔细读哦
* **API 手册**： 各个功能模块的 API 手册， 方便编程时查阅
  * **标准库**： `micropython` 的标准库， 很多 API 兼容 `python3` 的 API
  * **machine**： 机器相关， 重启控制，机器 UID， 以及各种外设控制
  * **Maix**: 一些特殊的模块， 比如 FPIOA， KPU， FFT等
  * **内置类**：内置的用 `mpy` （micropython 的缩写）编写的类， 可以在源码项目中找到
  * **机器视觉**: 一些机器视觉相关的模块， image sensor lcd 大致上兼容 OpenMV 的 API， 但是后期不会实时跟着 OpenMV 更新
  * **附加外设模块**： 一些外设模块的使用， 比如触摸屏， 超声波， LED 灯等
  * **内置应用**： 内置的应用， 比如 NES 游戏机（FC 红白机，也就是小时候的小霸王游戏机），pye（内置的文档编辑器）
* **常见问题 FAQ**： 大家经常问的问题汇总
* **进阶**： 一些进阶的玩法， 以及如何参与 [`文档的修改`](./contribute/doc_convention.md) 和 [`源码的修改`](./contribute/code_convention.md)，或者 `例程` 的贡献
* **社区 & 分享**： 收集一些来自社区的好的教程、作品、开源项目等， 大家也可以按照贡献说明来共享自己的作品或者教程

## 重要必读部分

<code><strong><font size=4>简介</font></strong></code> 和 <code><strong><font size=4>入门指南</font></strong></code>，一定要完整看完， 遇到问题也一定要先看 <code><strong><font size=4>常见问题</font></strong></code>


## 开始学习

* 刚接触，可以根据左边侧边栏的目录从上到下一页一页仔细看，跟着做即可， 入门一定不要跳过！！！
* 学会如何更新固件，如何写代码，其中学会使用串口终端也十分重要，不建议过分依赖 IDE， 特别是在程序死掉的时候， 用终端可能会获得更多报错信息，更有利于解决问题，在遇到问题在社区提问时，也尽量给出终端运行的完整信息
* 每个模块/库文档里面的结尾都附有简单例程， 或者到这里: [MaixPy_script](https://github.com/sipeed/MaixPy_scripts) 查找需要的示例， 可以尝试运行看效果

## 学会搜索

* 关于模块的接口及参数，在使用时根据自己的需求进行查阅，<code><strong><font size=4>页面顶部右上角有搜索框</font></strong></code>，可以好好利用，同时也可以使用浏览器的页面搜索功能，即按键盘<kbd> Ctrl+F </kbd>，然后输入要搜索的内容后按确认键
* 如果有找不到的内容也请不要着急， 可以上 github 的 [issue](https://github.com/sipeed/MaixPy/issues) 页面找一找（搜一搜）是不是有人提过了，没有的话可以新建 issue， 或者到 [论坛](https://bbs.sipeed.com) 搜索问题，没有再向大家求助， 或者联系技术支持。

## 本文档常见问题

* 文档加了 PDF 生成， 但是尽量不要传播 PDF 版本， 因为内容更新后 PDF 得不到及时更新， 尽量访问此网站([`https://maixpy.sipeed.com`](https://maixpy.sipeed.com))查看文档

* 如果网页加载比较慢， 请尝试刷新或者等待， 或者换个线路（使用代理或者换手机流量试试）

* 本文档有两个域名： [`https://maixpy.sipeed.com`](https://maixpy.sipeed.com) 和 [`https://cn.maixpy.sipeed.com`](https://cn.maixpy.sipeed.com)， 一个访问不了时可以访问另一个

* 文档使用 gitbook 从 markdown 自动生成为静态页面， 如果遇到有些页面无法访问， 请检查一下网址（路径）是否正确， 可以回到首页 ([`maixpy.sipeed.com`](https://maixpy.sipeed.com)) 重新进入即可。

比如这个网址就是由于网络情况不佳点击过快导致的：
```
http://localhost:4000/zh/zh/how_to_read.html
```
正确的网址应该是：
```
http://localhost:4000/zh/how_to_read.html
```



## MaixPy 常见问题

* 常见问题请见[常见问题](./others/maixpy_faq.md)


## 其它教程

* 除了文档，还可以浏览[博客](http://blog.sipeed.com)，[BBS](https://bbs.sipeed.com)用户写的教程， 或者百度搜索， 以及各个开发者的博客，都会有很多开发教程开发日记等， 都可以参考

## 提问技巧

在各种地方提问， 不管是  github 还是 QQ 群，还是论坛， 还是邮件， 提问要尽量提供完整的问题复现步骤，把你所经过的使用过程， 问题是怎么产生的， 现象是什么样的， 一定要完整地说明， 不要怕文字多，要站在解决问题的人的角度想问题，提的问题开发者能解决吗？ 方便开发者百忙之中测试问题并解决！

更加具体的请看下一节 [如何优雅提问](./how_to_ask.md)




