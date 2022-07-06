---
title: K210 kmodel 模型储存数据结构
keywords: K210, kmodel
date: 2022-06-09
tags: K210, kmodel
---

K210 kmodel 模型储存结构

<!-- more -->

版权声明：本文为 neucrack 的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://neucrack.com/p/307 有改动

## K210 kmodel 简介

V3 由 nncase v0.1.0 RC5 转换而来
V4 由 nncase v0.2.0 从 tflite 转换而来

V4相比于V3, 支持了更多算子, 但是运算速度更慢, 部分算子使用了CPU运算, K210侧也使用了C++编写, 部分库会拉低速度, 如果你需要移植或者优化可以注意这一点

## kmodel V3 数据结构
| 头                  | 输出层信息                        | 各层的头                                 | 各个层数据内容 |
| ------------------- | --------------------------------- | ---------------------------------------- | -------------- |
| kpu_kmodel_header_t | kpu_model_output_t * output_count | kpu_model_layer_header_t * layers_length | layers_body    |

这里有个注意点, kpu_kmodel_header_t 没有8字节对齐, 所以在第一层的数据实际是保存在8字节对齐处, 比如前面所有header 长度为 228 字节, 那么 第一层数据中, 头 kpu_model_conv_layer_argument_t 占用24个字节, 228+24 不是8的整数倍, 所以层数据保存在 228+24+4 处, 所以在 kpu_model_conv_layer_argument_t 中用了 layer_offset 这个来表示层数据相对于模型起始地址的偏移

```c
typedef struct
{
    uint32_t version;     // 固定  0x00000003, 0x03在低地址
    uint32_t flags;       // 最低位 为1, 表示8bit模式
    uint32_t arch;
    uint32_t layers_length;
    uint32_t max_start_address;
    uint32_t main_mem_usage;
    uint32_t output_count;
} kpu_kmodel_header_t;
typedef struct
{
    uint32_t address;
    uint32_t size;
} kpu_model_output_t;
typedef struct
{
    uint32_t type;
    uint32_t body_size;
} kpu_model_layer_header_t;
```

## kmodel V4 数据结构
| 头                    | 输入                     | 输入形状                    | 输出                      | 常量          | 各层的头                        | 各个层数据内容 |
| --------------------- | ------------------------ | --------------------------- | ------------------------- | ------------- | ------------------------------- | -------------- |
| struct modelv4_header | memory_range\*hdr.inputs | runtime_shape_t\*hdr.inputs | memory_range\*hdr.outputs | hdr.constants | hdr.nodes \* struct node_header | nodes content  |

```c
struct modelv4_header
{
    uint32_t identifier; // 固定为 KMDL, L在低地址
    uint32_t version;    // 固定为 0x00000004, 0x04 在低位
    uint32_t flags;
    uint32_t target;     // CPU: 0, K210: 1
    uint32_t constants;  // 多少个 uint_t 类型的常量
    uint32_t main_mem;   // 主内存, 用于AI, 运行时会先把输入的数据拷贝到这里
    uint32_t nodes;
    uint32_t inputs;     // input size
    uint32_t outputs;    // output size
    uint32_t reserved0;
};
struct node_header
{
    uint32_t opcode;
    uint32_t size;
};
struct memory_range
{
    memory_type_t memory_type;
    datatype_t datatype;
    uint32_t start;
    uint32_t size;
};  // 16 Bytes
typedef enum _datatype
{
    dt_float32,
    dt_uint8
} datatype_t;
typedef enum _memory_type
{
    mem_const,
    mem_main,
    mem_k210_kpu
} memory_type_t;
using runtime_shape_t = std::array<int, 4>;
```