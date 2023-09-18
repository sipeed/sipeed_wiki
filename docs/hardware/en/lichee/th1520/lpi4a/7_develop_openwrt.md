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

[Project address](https://github.com/ruyisdk/openwrt)

## Build

There are some issues with building on Ubuntu currently, using Debian can build smoothly. The repository provides the corresponding Dockerfile for Debian.

First you need to clone the project source code:
```shell
git clone https://github.com/ruyisdk/openwrt.git
```

If your machine has not been configured with Docker environment before, refer to the steps in [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/):

Uninstall possible versions of Docker:
```shell
sudo apt-get remove docker docker-engine docker.io containerd runc
```

Install basic software that Docker depends on:
```shell
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
```

Add official sources:
```shell
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

Install Docker:
```shell
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

Then enter the docker-build directory to configure the corresponding environment and start compiling.

```shell
cd openwrt/docker-build
# Build docker image
sudo docker build -t ruyisdk-openwrt-builder .
# Build openwrt using docker
sudo docker run --rm -v "$(cd .. && pwd)":/workspace ruyisdk-openwrt-builder
```

After the build is complete, flash the built image to the development board.

Then you can refer to [Openwrt Docs](https://openwrt.org/docs/start) to develop.

## Reference

[Openwrt](https://github.com/ruyisdk/openwrt)
[Docker-Build](https://github.com/ruyisdk/openwrt/tree/lpi4a-new/docker-build)
[Openwrt Docs](https://openwrt.org/docs/start)