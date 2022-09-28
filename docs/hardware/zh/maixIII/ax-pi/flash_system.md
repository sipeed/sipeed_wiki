---
title: 烧录系统  

---

## 系统简介

## 获取镜像

## 烧录镜像

### 准备工作

官方底板作为测试的原型样机，除了板子自带的内容外，还需要准备材料如下：
- 一张大于 4g 的 SD 卡，一个能出 1A 的 USB3.0 口，也可以是带供电的 usb hub 拓展。 
- 一对支持输出 3.5MM 左右声道的喇叭，测试音频相关。
- 一台 WIFI 路由器 AP 热点账号及密码以供连接 WIFI 或以太网。
供电要求：需要两条线来自不同源头的输入供电达 1A 左右即可。

### 镜像系统烧录方法

- 使用软件为 balenaEtcher [点击跳转](https://www.balena.io/etcher/)
- 使用镜像为 `sipeed_ax620a_debian11_20220819.zip` []()

烧录方法如下图示意
![etcher](../../../assets/maixIII/ax-pi/etcher.jpg)
点击“flash!”开始烧录，可看到进度条的跳动。
![etcher_two](../../../assets/maixIII/ax-pi/etcher_t.jpg)
最终下载结束后的效果会和下图一样，显示 `Flash Complete!`：
![etcher_three](../../../assets/maixIII/ax-pi/etcher_h.jpg)
如果烧录失败的话 方法：
