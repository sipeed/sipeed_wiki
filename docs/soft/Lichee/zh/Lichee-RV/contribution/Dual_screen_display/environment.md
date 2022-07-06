---
title: 使用 WSL2 编译 LicheeRV Tina BSP
---
> 编辑于2022年3月28日

[原文链接](http://www.gloomyghost.com/live/20220130.aspx) [原文作者空间](http://www.gloomyghost.com/) 
原创时间: 2022年1月30日

- 下载WSL镜像：链接：https://pan.baidu.com/s/1geVQFcTpkoVgc-HNcHuENw 提取码：di1l

WIndows上准备好WSL环境以及WSL2相关补丁。导入WSL镜像。
```bash
wsl --import <Distro> <InstallLocation> <FileName>
```
例如将Tina开发环境导入到 D:\VirtVM\Tina_build 并命名为 TinaBuild
```bash
wsl --import TinaBuild D:\VirtVM\Tina_build Tina_WSL2.tar.gz
```
将镜像转换为WSL2版本。
```bash
wsl --set-version TinaBuild 2
```
进入 Tina 开发环境
```bash
cd tina-d1-open
source build/envsetup.sh
lunch
```
镜像相关：
```
用户名: tina
密码: tina
```
![](./assets/enviroument.png)