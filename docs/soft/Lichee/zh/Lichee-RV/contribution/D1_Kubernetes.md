---
title: RISCV64架构下 Kubernetes相关软件编译
keywords: Sipeed, Kubernetes, RISCV, D1, docker
---

转载自知乎用户 [在路上](https://www.zhihu.com/people/zai-lu-shang-8-7)
原文链接 ： <https://zhuanlan.zhihu.com/p/443777923>
## 编译环境

* OS ：openEuler Linux 5.4.61 （openEuler镜像[下载地址](https://mirror.iscas.ac.cn/plct/openEuler-D1-wifi-hdmi-docker-20210826.img.bz2))
* ARCH： riscv64
* 平台： 全志D1开发板
* go版本: go version go1.17 linux/riscv64

## go和docker安装

详见教程：[在D1/openEuler上安装docker，并运行docker/Debian](https://zhuanlan.zhihu.com/p/406132856)
docker安装前请先确认一下内核配置是否满足：`check-config.sh`
安装完成docker后还是无法正常使用docker的话(报错与`libseccomp`相关)，建议重新安装一下`libseccomp`。

## conntrack安装
```
## 安装支持包
yum install -y bison
yum install -y flex

## 手动编译安装conntrack-tools, 因为openEuler-riscv64的软件源中还没有
git clone git://git.netfilter.org/conntrack-tools
./configure --prefix=/usr/local/conntrack && make && make install
```

编译conntrack-tools会出现依赖包文件找不到的问题，根据提示进行安装即可。目前openEuler软件源有大部分的包，可直接下载软件以及对应的devel软件。依赖包源码下载地址：<https://git.netfilter.org/>

```
# 依赖包如果需要手动安装，一般默认安装路径为/usr/local/lib，需要把对应文件拷贝到以下位置中
/usr/include/libnetfilter_conntrack/
/usr/include/libnfnetlink/
/usr/lib64/libnetfilter_conntrack.la
/usr/lib64/libnetfilter_conntrack.so
/usr/lib64/libnetfilter_conntrack.so.3
/usr/lib64/libnetfilter_conntrack.so.3.1.3
/usr/lib64/pkgconfig/libnetfilter_conntrack.pc
/usr/lib64/pkgconfig/libnfnetlink.pc
```

## 编译Kubernetes

由于目前还没有基于riscv架构的kubernetes release包，因此需要从源码入手。

RISCV移植过的源码地址：<https://github.com/carlosedp/kubernetes/tree/riscv64_build>

对应的PR地址：<https://github.com/kubernetes/kubernetes/pull/86011>
```
# 全部编译
KUBE_BUILD_PLATFORMS=linux/riscv64 make
# 编译指定组件
KUBE_BUILD_PLATFORMS=linux/riscv64 make all WHAT=cmd/kubelet GOFLAGS=-v GOGCFLAGS="-N -l"
```

编译完成后，可以在 `_output/local/bin/linux/riscv64/` 中找到需要的二进制文件
```
[root@openEuler-RISCV-rare kubernetes]# ls -l _output/local/bin/linux/riscv64/
total 1166679
-rwxr-xr-x 1 root root  41711688 Nov 30 06:43 apiextensions-apiserver
-rwxr-xr-x 1 root root   6227408 Nov 27 08:57 conversion-gen
-rwxr-xr-x 1 root root   5961136 Nov 27 08:51 deepcopy-gen
-rwxr-xr-x 1 root root   5944720 Nov 27 08:54 defaulter-gen
-rwxr-xr-x 1 root root 107038704 Nov 30 06:44 e2e.test
-rwxr-xr-x 1 root root 116796584 Nov 30 06:42 e2e_node.test
-rwxr-xr-x 1 root root  38709064 Nov 30 06:44 gendocs
-rwxr-xr-x 1 root root 129439752 Nov 30 06:44 genkubedocs
-rwxr-xr-x 1 root root 135353224 Nov 30 06:42 genman
-rwxr-xr-x 1 root root   3285672 Nov 30 06:42 genswaggertypedocs
-rwxr-xr-x 1 root root  38704744 Nov 30 06:45 genyaml
-rwxr-xr-x 1 root root   7187536 Nov 30 06:42 ginkgo
-rwxr-xr-x 1 root root   1900544 Nov 27 09:09 go-bindata
-rwxr-xr-x 1 root root   1801424 Nov 30 06:43 go-runner
-rwxr-xr-x 1 root root   3366768 Nov 27 08:51 go2make
-rwxr-xr-x 1 root root 102367232 Nov 30 06:44 kube-apiserver
-rwxr-xr-x 1 root root  95092736 Nov 30 06:43 kube-controller-manager
-rwxr-xr-x 1 root root  33816576 Nov 30 06:42 kube-proxy
-rwxr-xr-x 1 root root  37289984 Nov 30 06:45 kube-scheduler
-rwxr-xr-x 1 root root  35192832 Nov 30 06:44 kubeadm
-rwxr-xr-x 1 root root  39321600 Nov 30 06:44 kubectl
-rwxr-xr-x 1 root root  96825128 Nov 30 06:43 kubelet
-rwxr-xr-x 1 root root  95325544 Nov 30 06:43 kubemark
-rwxr-xr-x 1 root root   4674000 Nov 30 06:43 linkcheck
-rwxr-xr-x 1 root root   1572864 Nov 30 06:43 mounter
-rwxr-xr-x 1 root root   9751176 Nov 27 09:04 openapi-gen
```

本实验在全志D1的开发板上进行，系统采用的openEuler，由于CPU核数和存储的限制，以下是编译过程中可能遇到的错误：
### 相关错误及对应的解决办法
+  **network: /usr/local/go/pkg/tool/linux_riscv64/compile: signal: killed**

问题重现： 
```
go build k8s.io/kubernetes/vendor/github.com/Azure/azure-sdk-for-go/services/network/mgmt/2019-06-01/network: /usr/local/go/pkg/tool/linux_riscv64/compile: signal: killed
```

解决方法：

属于OOM错误，需要扩大swap分区


1.创建作为swap分区的文件:增加1GB大小的交换分区
>dd if=/dev/zero of=/root/swapfile bs=1M count=1024

2.格式化为交换分区文件
>mkswap /root/swapfile

3.启用交换分区文件
>swapon /root/swapfile

+  **_output/bin/deepcopy-gen: Permission denied**
  
问题重现：编译kubernetes时遇到报错
>./hack/run-in-gopath.sh: line 33: _output/bin/deepcopy-gen: Permission denied

解决方法：
```
yum install -y  rsync
chmod +x _output/bin/deepcopy-gen
make clean
make clean_generated
```
然后重新 make 编译操作。

+  **vendor/https://github.com/onsi/ginkgo/internal/remote/syscall_dup_unix.go:10:9: undefined: syscall.Dup2**

问题重现：编译kubernetes时遇到报错信息

```
k8s.io/kubernetes/vendor/github.com/onsi/ginkgo/internal/remote/vendor/github.com/onsi/ginkgo/internal/remote/syscall_dup_unix.go:10:9: undefined: syscall.Dup2
```

解决方法：
这是由于kubernetes库 `go.mod` 中依赖 `ginkgo` ，但是 `go.mod` 中为 `ginkgo v1.10.1` 版本，而支持riscv的`ginkgo`版本从v1.11.0开始，因此在编译前需要将`go.mod`中的`ginkgo`版本修改为1.11.0
>github.com/onsi/ginkgo => github.com/onsi/ginkgo v1.11.0

+  **tmp存储Out of Memory**

解决方法参考，如何增加 Linux 下临时文件夹 /tmp 的大小
http://xiehongfeng100.github.io/2016/01/18/ops-how-to-increase-tmp-partition-size/

## 编译etcd
etcd的RISCV移植已经并入主线可直接下载主线代码：
https://link.zhihu.com/?target=https%3A//github.com/etcd-io/etcd
对应的PR地址：https://github.com/etcd-io/etcd/pull/10834
```
# 编译命令
GOOS=linux GOARCH=riscv64 ARCH=riscv64 GO_BUILD_FLAGS='-v -mod=readonly' ./build.sh
# 编译结果
[root@k8s-01 etcd]# ls -l bin/
total 70377
-rwxr-xr-x 1 root root 30298920 Nov 28 05:46 etcd
-rwxr-xr-x 1 root root 22962560 Nov 28 05:48 etcdctl
-rwxr-xr-x 1 root root 18803030 Nov 28 05:46 etcdutl
```
### etcd编译过程中出现的问题
+  **etcd on unsupported platform without ETCD_UNSUPPORTED_ARCH=riscv64 set**

问题重现

安装etcd时出现`etcd on unsupported platform without ETCD_UNSUPPORTED_ARCH=riscv64 set`，致使etcd启动失败。

解决方法：
```
vim etcd/server/etcdmain/etcd.go
# 在最后checkSupportArch()函数中添加
if runtime.GOARCH == "amd64" ||
                runtime.GOARCH == "arm64" ||
                runtime.GOARCH == "riscv64" ||
                runtime.GOARCH == "ppc64le" ||
                runtime.GOARCH == "s390x" {
                return
        }
# 重新编译
GOOS=linux GOARCH=riscv64 ARCH=riscv64 GO_BUILD_FLAGS='-v -mod=readonly' ./build.sh
```
重启一下etcd即成功。
## 编译flannel
尚未进行RISCV移植，目前只支持二进制编译。

