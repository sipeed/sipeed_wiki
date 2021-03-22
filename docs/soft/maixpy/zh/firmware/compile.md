---
title: 源码编译
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 源码编译
---


预编译的固件可能不满足特定的使用场景， 如果需要修改配置，请配置并编译需要的固件

## 本机环境编译

编译方法请参考 源码下的编译说明 [build.md](https://github.com/sipeed/MaixPy/blob/master/build.md)

## 使用 docker 环境编译

docker 可以简化开发环境安装
> 如果你没用过 docker， 关于 docker 的知识请自行学习，
> 在没学习过的情况下你可以认为它和虚拟机类似，即已经为你准备好了带编译环境的虚拟机，直接下载运行就可以用来编译源码了

docker 镜像已经打包好了环境，直接拉取镜像并且运行即可开始编译， 参考 [使用 Docker 编译源码](https://github.com/sipeed/MaixPy/tree/master/tools/docker)



