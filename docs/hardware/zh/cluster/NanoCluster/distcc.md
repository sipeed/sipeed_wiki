---
title: distcc 部署
---

## 简介
[distcc](https://github.com/distcc/distcc) 是一个分布式 C/C++ 编译系统，它通过将编译任务分发到多台机器上来加速编译过程。它允许你利用多台计算机的计算能力，更快速地编译代码，特别适用于大型代码库或资源受限的设备环境。

## 部署教程

### 服务端
对于 Debian 系统,可以直接使用包管理器安装 distcc
```bash
sudo apt install distcc
```

开启 distcc 服务
```bash
distccd --daemon --allow 192.168.0.0/24  # 允许特定 IP 范围的机器访问
```

### 客户端
```bash
sudo apt install distcc distcc-pump
```

配置 DISTCC_HOSTS 环境变量，指定可用的工作节点。可以在 .bashrc 中添加以下内容：
```bash
export DISTCC_POTENTIAL_HOSTS='localhost 192.168.0.240 192.168.0.243 192.168.0.245 192.168.0.246'
```

然后，可以尝试编译一个简单的程序，检查 distcc 是否正常分发编译任务：

```bash
distcc-pump distcc -o test test.c
```

```bash
sipeed@lpi3h-a2d1:~/distcc$ distcc-pump distcc -o test test.c
__________Using distcc-pump from /usr/bin
__________Found 4 available distcc servers
__________Shutting down distcc-pump include server
```
## 编译测试

为了测试 distcc 是否能够有效地加速编译过程，我们使用 OpenSSL 来进行编译测试。OpenSSL 是一个广泛使用的 C 库，包含大量源代码，适合用来测试分布式编译的效果。

```bash
git clone https://github.com/openssl/openssl.git
cd openssl
./config
distcc-pump make -j20 CC=distcc
```

可以使用 distccmon-text 查看当前编译任务的分发情况

```bash
sipeed@lpi3h-2193:~$ distccmon-text 
 67535  Compile     cmp_ctx.c                                 192.168.0.240[0]
 67528  Compile     cmp_asn.c                                 192.168.0.240[1]
 67635  Compile     cms_dh.c                                  192.168.0.240[2]
 67569  Compile     cmp_http.c                                192.168.0.243[0]
 67696  Compile     cms_io.c                                  192.168.0.245[0]
 67583  Compile     cmp_server.c                              192.168.0.245[1]
 67561  Compile     cmp_hdr.c                                 192.168.0.245[2]
 67606  Compile     cmp_vfy.c                                 192.168.0.245[3]
 67657  Compile     cms_enc.c                                 192.168.0.246[1]
 67672  Compile     cms_env.c                                 192.168.0.246[2]
```

### 编译性能对比
在测试过程中，我们对 OpenSSL 项目分别使用了单机编译和分布式编译（5台机器），下面是两种方式的编译结果：

##### 单机编译（不使用 distcc）
```bash
real    18m11.760s
user    64m37.024s
sys     5m56.326s
```
##### 分布式编译（使用 distcc）
```bash
real    6m32.262s
user    18m39.468s
sys     4m30.008s
```

可以看到，使用 distcc 进行分布式编译后，编译时间显著缩短，从 18 分钟降至约 6 分钟。可见分布式编译的加速效果明显，同时也可以有效地减轻单个机器的负载。