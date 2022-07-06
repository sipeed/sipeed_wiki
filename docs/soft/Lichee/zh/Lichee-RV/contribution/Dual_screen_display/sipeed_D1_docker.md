---
title: 使用sipeed提供的docker
---

> 编辑于2022年4月2日 

- 本文讲解如何使用sipeed提供的docker镜像来编译D1

## 获取镜像

- 国内用户：[百度网盘](https://pan.baidu.com/s/1QJTaDw6kkTM4c_GAlmG0hg)  提取码：wbef
- 国外用户：[Mega](https://mega.nz/folder/lx4CyZBA#PiFhY7oSVQ3gp2ZZ_AnwYA)

提供上述两种镜像的获取方式

## 导入镜像

成功下载完镜像之后需要解压成tar格式，然后再docker中导入

```bash
gzip -d licheerv_d1_compile.tar.gz #解压成tar文件
sudo docker import licheerv_d1_compile.tar licheerv_d1_compile:latest #docker导入镜像
```

## 启动docker镜像

```bash
sudo docker run -it licheerv_d1_compile:latest /bin/bash # 交互模式启动D1镜像编译环境
login #切换用户，为了下面能够正常进行 make 指令
```

接着会让输入用户名和密码。
用户名为`nihao`，密码是`sipeed123`。

## 结语

完成上面的操作之后就可以开始编译D1镜像了。
其中编译环境位于 ~/sdk/tina-d1-open_new/ 目录下。
其他编译操作可以参考官方网页 [编译和烧写](https://d1.docs.aw-ol.com/study/study_4compile/)

