---
title: What is MaixPy3?
keywords: Maixpy3 官方文档
desc: maixpy  MaixPy3 是什么？能做什么？
---

<div style="font-size: 1.2em;border: 2px solid green; border-color:#c33d45;padding:1em; text-align:center; background: #c33d45; color: white">
    <div>
    <span>新版 MaixPy (v4) 已经上线， 更完善的API和文档，功能更强大， 请看:</span>
    <a target="_blank" style="color: #ffe0e0" href="https://wiki.sipeed.com/maixpy">
        wiki.sipeed.com/maixpy
    </a>
    <br>
    <div style="height:0.4em"></div>
    <span>全新硬件产品 MaixCAM，性能大升级，请看:</span>
    <a target="_blank" style="color: #ffe0e0" href="https://wiki.sipeed.com/maixcam">
        https://wiki.sipeed.com/maixcam
    </a>
    </div>
    <div style="padding: 1em 0 0 0">
      <a style="color: white; font-size: 0.9em; border-radius: 0.3em; padding: 0.5em; background-color: #a80202" href="https://item.taobao.com/item.htm?id=784724795837">淘宝</a>
      <a style="color: white; font-size: 0.9em; border-radius: 0.3em; padding: 0.5em; background-color: #a80202" href="https://www.aliexpress.com/store/911876460">速卖通</a>
    </div>
</div>

**Maix-II V831 系列会被逐渐淘汰，如果你正准备购买 v831, 请立刻选择 MaixCAM;**
**也欢迎 v831 用户升级到 MaixCAM**

<br>
<br>
<br>
<br>
<br>

中国的 [Sipeed 开源组织](https://github.com/sipeed) 在 2020 年底推出了 [MaixPy3](https://github.com/sipeed/MaixPy3) 开源软件，这是一款基于 Python3 语言的软件开发工具包（SDK），借助开源 Python 编程语言实现跨平台统一和简化 Linux 嵌入式设备上开发 AIoT （人工智能物联网） = AI（人工智能） + IoT（物联网）应用，意在打造可落地的视觉 AI 应用生态，帮助更多人了解、使用 AI 技术来解决实际问题，推进全球边缘 AI 的落地化进程。

## MaixPy3 能做什么？

> 以下内容均是社区用户基于 MaixPy3 开发的成果分享，本文档不提供他人的二次开发成果。

### M2DOCK 产品功能速览

- M2DOCK：国产全志 V831 开源 人工智能 神经网络 视觉 AI Python开发板

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=298543445&bvid=BV1sF411u7xb&cid=586467021&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:640px; max-height:480px;"> </iframe>
</p>

### M2DOCK 电赛数字送药小车

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=258696230&bvid=BV1Wa411D7DL&cid=779040049&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:640px; max-height:480px;"> </iframe>
</p>

### M2DOCK V831 车牌识别

- 社区是检测后联网识别，官方是检测后本地识别。

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=854443414&bvid=BV1M54y1o7YH&cid=730413361&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:640px; max-height:480px;"> </iframe>
</p>

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=941105171&bvid=BV1zW4y117U4&cid=775859102&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:640px; max-height:480px;"> </iframe>
</p>

### M2DOCK 冰箱水果识别系统

- 简易水果识别系统。基于pytorch的yolo训练模型，移植到v831，app和开发板实时显示。

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=853065689&bvid=BV1sL4y157us&cid=572354654&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:640px; max-height:480px;"> </iframe>
</p>

### yolov2_20classes by Maix ⅡDock(V831)

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=594688527&bvid=BV16q4y1i7rS&cid=546750387&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:640px; max-height:480px;"> </iframe>
</p>

### M2DOCK 人脸和口罩检测

- ［maixpy3] 831 脸子姐姐的毕设人脸口罩识别

<p align="center">
    <iframe src="//player.bilibili.com/player.html?aid=467818856&bvid=BV1X5411S7F6&cid=713976242&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="max-width:640px; max-height:480px;"> </iframe>
</p>

## 本开源项目适用于以下人群：

1. 想要了解与学习应用视觉 AI 开发的学生、爱好者、创客等。
2. 想要应用视觉 AI 功能解决问题，但不想浪费生命在底层原理实现的同学们。
3. 需要对 Python AI 教学、电赛毕设、视觉应用等功能评估与验证的同行们。
4. 有过 opencv 、openmv 、 maixpy 使用基础的老朋友们！！！

## 本开源项目建议具备的背景知识

- 有过 [Python 语言](./origin/python.md)编程基础，了解基本语法，如面向对象、交互解释等概念。

- 有过嵌入式、单片机的基本概念，了解 IO 口、电压、串口、外设等概念。

- 有使用过 maixpy K210 AI 开发板的基础（与上代[MaixPy](https://github.com/sipeed/MaixPy)开源产品联动）。

当你有这些基础概念后，你可以减少很多犯错的次数，避免踩到一些不必要的坑。

## [MaixPy3](https://github.com/sipeed/MaixPy3) star-history

![GitHub forks](https://img.shields.io/github/forks/sipeed/maixpy3.svg?style=social) ![GitHub stars](https://img.shields.io/github/stars/sipeed/maixpy3.svg?style=social) ![GitHub watchers](https://img.shields.io/github/watchers/sipeed/maixpy3.svg?style=social)

<iframe style="width:100%;height:auto;min-width:600px;min-height:400px;" src="https://star-history.com/embed?secret=#sipeed/MaixPy3&Date" frameBorder="0"></iframe>

> 快来与我们一起同行吧！ “Life is short. You need Sipeed.”

