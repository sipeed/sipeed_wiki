---
title: CPU 跑分测试
keywords: Linux, Lichee, TH1520, SBC, RISCV, benchmark
update:
  - date: 2023-05-08
    version: v1.0
    author: wonder
    content:
      - Release docs
---

## Dhrystone

平头哥官方数据，C910 为 5.6 分左右。

![dmips](./assets/benchmark/dmips.png)  

## CoreMarks 

测试参数配置：  

`-funroll-all-loops -finline-limit=500 -fgcse-sm -fno-schedule-insns  -msignedness-cmpiv -fno-code-hoisting -mno-thread-jumps1 -mno-iv-adjust-addr-cost -mno-expand-split-imm`

使用公版工具链，GCC 版本为`13.1.0`的测试结果（1.85GHz）：
```txt
2K performance run parameters for coremark.
CoreMark Size    : 666
Total ticks      : 11989
Total time (secs): 11.989000
Iterations/Sec   : 9175.077154
Iterations       : 110000
Compiler version : GCC13.1.0
Compiler flags   : -O2 -DPERFORMANCE_RUN=1  -lrt -funroll-all-loops -finline-limit=500 -fgcse-sm -fno-schedule-insns -msignedness-cmpiv -fno-code-hoisting -mno-thread-jumps1 -mno-iv-adjust-addr-cost -mno-expand-split-im
Memory location  : Please put data memory location here
                        (e.g. code in flash, data on heap etc)
seedcrc          : 0xe9f5
[0]crclist       : 0xe714
[0]crcmatrix     : 0x1fd7
[0]crcstate      : 0x8e3a
[0]crcfinal      : 0x33ff
Correct operation validated. See README.md for run and reporting rules.
CoreMark 1.0 : 9175.077154 / GCC13.1.0 -O2 -DPERFORMANCE_RUN=1 -lrt -funroll-all-loops -finline-limit=500 -fgcse-sm -fno-schedule-insns -msignedness-cmpiv -fno-code-hoisting -mno-thread-jumps1 -mno-iv-adjust-addr-cost -mno-expand-split-im / Heap
```

使用平头哥专用工具链，GCC 版本为`10.4.0`的测试结果（1.85GHz）：

```txt
2K performance run parameters for coremark.
CoreMark Size    : 666
Total ticks      : 15129
Total time (secs): 15.129000
Iterations/Sec   : 13219.644392
Iterations       : 200000
Compiler version : GCC10.4.0
Compiler flags   : -O2 -march=rv64gv0p7_zfh_xtheadc -O3 -funroll-all-loops -finline-limit=500 -fgcse-sm -fno-schedule-insns  -msignedness-cmpiv -fno-code-hoisting -mno-thread-jumps1 -mno-iv-adjust-addr-cost -mno-expand-split-imm -DPERFORMANCE_RUN=1  -lrt
Memory location  : Please put data memory location here
                        (e.g. code in flash, data on heap etc)
seedcrc          : 0xe9f5
[0]crclist       : 0xe714
[0]crcmatrix     : 0x1fd7
[0]crcstate      : 0x8e3a
[0]crcfinal      : 0x4983
Correct operation validated. See README.md for run and reporting rules.
CoreMark 1.0 : 13219.644392 / GCC10.4.0 -O2 -march=rv64gv0p7_zfh_xtheadc -O3 -funroll-all-loops -finline-limit=500 -fgcse-sm -fno-schedule-insns  -msignedness-cmpiv -fno-code-hoisting -mno-thread-jumps1 -mno-iv-adjust-addr-cost -mno-expand-split-imm -DPERFORMANCE_RUN=1  -lrt / Heap  -lrt / Heap
```

![coremarks](./assets/benchmark/coremarks.png) 

## Geekbench5

> 注：这里的测试使用公版工具链，若使用thead专用工具链，性能预计可提升50%以上

![geekbench5](./assets/benchmark/geekbench5.png) 

https://browser.geekbench.com/v5/cpu/compare/21100603?baseline=21092115

## 7-Zip LZMA 

[7-Zip LZMA Benchmark](https://7-cpu.com/)
![7z](./assets/benchmark/7z.png) 

## OpenSSL

```bash
openssl speed -evp aes-256-cbc
openssl speed -evp aes-256-gcm
openssl speed -evp sha1
openssl speed -evp sha256
```

| type                                          | 16bytes   | 64bytes   | 256bytes  | 1024bytes  | 8192bytes  | 16384bytes |
| --------------------------------------------- | --------- | --------- | --------- | ---------- | ---------- | ---------- |
| <p style="white-space:nowrap">AES-256-CBC</p> | 29206.05k | 36957.73k | 39648.85k | 40407.72k  | 40624.13k  | 40768.21k  |
| <p style="white-space:nowrap">AES-256-GCM</p> | 24610.57k | 28191.29k | 29459.29k | 29727.06k  | 29911.72k  | 29949.95k  |
| <p style="white-space:nowrap">sha1</p>        | 9428.03k  | 30591.02k | 72920.06k | 113164.63k | 135271.77k | 137052.16k |
| <p style="white-space:nowrap">sha256</p>      | 6206.94k  | 17151.38k | 34806.19k | 47151.10k  | 52559.87k  | 53163.07k  |

## LLVM 

编译脚本使用[scriptlets](https://github.com/AOSC-Dev/scriptlets/tree/master/buildbot-benchmark)仓库下的 `buildbot-benchmark.bash`，CPU频率为1.843Ghz，内存为16G。

编译用时：
```text
real    265m50.172s
user    980m15.164s
sys     60m51.329s
```

## 其它

欢迎投稿～ 投稿接受后可得￥5～150（$1~20）优惠券！