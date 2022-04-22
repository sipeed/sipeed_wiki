---
title: licheeRV debian镜像相关问题
keywords: debian, Rv, Problam, apt, img, sipeed
---

## apt 相关

- 在使用默认debian镜像时，如果进行apt操作，发现以下报错：
  
> GPG error: http://ftp.ports.debian.org/debian-ports sid InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY E852514F5DF312F6

说明内置的密钥到期了，需要手工更新下密钥；下面是两种下载密钥的方式：
 - 网页下载：https://packages.debian.org/sid/all/debian-ports-archive-keyring/download
 - wget方式 `wget http://ftp.cn.debian.org/debian/pool/main/d/debian-ports-archive-keyring/debian-ports-archive-keyring_2022.02.15_all.deb`
  
将密钥拷贝（使用scp或者lrzsz工具）到LicheeRV板上，执行：
> sudo dpkg -i debian-ports-archive-keyring_2022.02.15_all.deb
> 
即可更新密钥，然后可以正常进行apt更新：`sudo apt-get update`