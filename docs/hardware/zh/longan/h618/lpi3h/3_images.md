---
title: 镜像集合
keywords: Linux, Longan, H618, SBC, ARM, image
update:
  - date: 2023-04-07
    version: v1.1
    author: ztd
    content:
      - Add Debian CLI image
  - date: 2023-12-08
    version: v1.0
    author: ztd
    content:
      - Release docs
---

## Sipeed官方镜像

### Debian

Sipeed 官方镜像基于 Debian 系统修改适配。 

默认镜像的帐号密码配置如下：
账户：`root`，密码： `root`；
账户： `sipeed`，密码：`licheepi`；

**注意，不建议用root用户登陆桌面。**

![debian](./assets/images/debian.png)  
![debian_neofetch](./assets/images/debian_neofetch.png)  

#### Changelog

20231220：
- 发布初版镜像
20240106：
- 更新EMMC启动支持
20240110：
- 添加 SD、EMMC 启动可烧录镜像文件
- 修复 DNS 问题
20240226：
- 添加 GPIO sysfs
- 允许使用 root 用户登陆 SSH
- 添加 USB gadget 功能
20240407：
- 添加 Debian CLI 版本镜像

下载地址：
百度网盘：[点我](https://pan.baidu.com/s/1VGaARAq6dbicFy4VOytRuw) 提取码: cd68
Mega 云盘：[点我](https://mega.nz/folder/gt50zDoC#LgRvHVCzWTUgGohKoMtlqA)


### Android 12

20240226：
- 发布初版镜像（无wifi/bt支持）

下载地址：
百度网盘：[点我](https://pan.baidu.com/s/1t-cNlIIU0P8VDmkC518W6Q) 提取码: rb4d
Mega 云盘：[点我](https://mega.nz/folder/Z14klTRI#l4aMYdxgFzUf-SirkvdOhg)