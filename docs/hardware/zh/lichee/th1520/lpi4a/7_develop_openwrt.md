---
title: OpenWrt
keywords: Linux, Lichee, TH1520, SBC, RISCV, Kernel, SDK, Develop
update:
  - date: 2023-09-17
    version: v1.1
    author: ztd
    content:
      - Update docs
  - date: 2023-05-12
    version: v1.0
    author: wonder
    content:
      - Release docs
---

## OpenWrt

[项目地址](https://github.com/ruyisdk/openwrt)

## 构建

Ubuntu 上构建目前会存在一些问题，使用 Debian 能够顺利构建。仓库中提供 Debian 相应的 Dockerfile。

首先需要 clone 该项目源码：
```shell
git clone https://github.com/ruyisdk/openwrt.git
```

若你的机器之前没有配置过Docker环境，参考 [Docker 官方文档](https://www.yuque.com/za4k4z/uzn618/fvxfnefpbdsg15hk)的步骤：

卸载可能存在的 docker 版本：
```shell
sudo apt-get remove docker docker-engine docker.io containerd runc
```

安装 docker 依赖的基础软件：
```shell
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
```

添加官方源：
```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

安装 docker：
```shell
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

然后进入到 docker-build 目录中配置好相应环境并开始编译。

```shell
cd openwrt/docker-build
# 构建 Docker 镜像
sudo docker build -t ruyisdk-openwrt-builder .
# 使用 Docker 构建 Openwrt
sudo docker run --rm -v "$(cd .. && pwd)":/workspace ruyisdk-openwrt-builder
```

构建完成后，将构建好的镜像烧录至开发板中。


接下来可以参考 [Openwrt 官方文档](https://openwrt.org/docs/start)进行开发。

## 参考

[Openwrt](https://github.com/ruyisdk/openwrt)
[Docker-Build](https://github.com/ruyisdk/openwrt/tree/lpi4a-new/docker-build)
[Openwrt 官方文档](https://openwrt.org/docs/start)