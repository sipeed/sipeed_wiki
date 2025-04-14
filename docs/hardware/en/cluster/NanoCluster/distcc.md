---
title: distcc Deployment
---

## Introduction
[distcc](https://github.com/distcc/distcc) is a distributed C/C++ compilation system that speeds up the compilation process by distributing compilation tasks across multiple machines. It allows you to leverage the computing power of multiple computers to compile code faster, making it especially useful for large codebases or resource-constrained environments.

## Deployment Guide

### Server
For Debian-based systems, you can install distcc directly using the package manager:
```bash
sudo apt install distcc
```

Start the distcc service:
```bash
distccd --daemon --allow 192.168.0.0/24  # Allow specific IP range to access
```

### Client
```bash
sudo apt install distcc distcc-pump
```

Set up the DISTCC_HOSTS environment variable to specify the available worker nodes. You can add the following to your .bashrc
```bash
export DISTCC_POTENTIAL_HOSTS='localhost 192.168.0.240 192.168.0.243 192.168.0.245 192.168.0.246'
```

Then, you can try compiling a simple program to check if distcc is correctly distributing the compilation tasks:

```bash
distcc-pump distcc -o test test.c
```

```bash
sipeed@lpi3h-a2d1:~/distcc$ distcc-pump distcc -o test test.c
__________Using distcc-pump from /usr/bin
__________Found 4 available distcc servers
__________Shutting down distcc-pump include server
```
## Compilation Testing

To test whether distcc effectively accelerates the compilation process, we used OpenSSL for the compilation test. OpenSSL is a widely-used C library with a large codebase, making it a good candidate to test the effectiveness of distributed compilation.

```bash
git clone https://github.com/openssl/openssl.git
cd openssl
./config
distcc-pump make -j20 CC=distcc
```

You can use distccmon-text to check the current distribution of compilation tasks:

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

### Compilation Performance Comparison
In the testing process, we compiled the OpenSSL project using both single-machine compilation and distributed compilation (5 machines). Below are the results for each method:

##### Single-Machine Compilation (without distcc)
```bash
real    18m11.760s
user    64m37.024s
sys     5m56.326s
```
##### Distributed Compilation (using distcc)
```bash
real    6m32.262s
user    18m39.468s
sys     4m30.008s
```

As seen, the compilation time using distcc for distributed compilation is significantly reduced, from 18 minutes to about 6 minutes. The acceleration effect of distributed compilation is evident, and it also helps alleviate the load on individual machines.