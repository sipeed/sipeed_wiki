---
title: MaixPy 编程规范
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: MaixPy 编程规范
---


这是一份 **MaixPy** 开发人员的开发指引。**MaixPy** 做为一份开源软件，它需要由不同的人采用合作的方式完成，这份文档是开发人员的一个指引。

**MaixPy** 的开发人员请遵守这样的编程风格。同时对于使用 MaixPy 的用户，也可通过这份文档了解 MaixPy 代码内部一些约定从而比较容易的把握到 MaixPy 的实现方式。

## 规范原则

- [x] 朴实，避免晦涩语法
- [x] 严谨，逻辑反复思考
- [x] 简约，命名简洁、代码精炼
- [x] 性能，通过算法、编译器、硬件进行优化

## 目录结构 && 文件名称

- 目录结构

整个工程按照功能模块划分子目录，每个子目录再划分头文件和源文件目录，以便架构清晰、易懂。
目录名称如果无特殊的需求，请使用全小写的形式；目录名称应能够反应部分的意思，components 目录下能够反映组件的意义。

- 文件结构

文件名称如果无特殊的需求(如果是引用其他地方，可以保留相应的名称)，请使用全小写的形式。另外为了避免文件名重名的问题，一些地方请尽量不要使用通用化、使用频率高的名称。

## 头文件定义

C语言头文件为了避免多次重复包含，需要定义一个符号。这个符号的定义形式请采用如下
的风格：

```c
#ifndef __FILE_H__
#define __FILE_H__
/* header file content */
#endif
```

即定义的符号两侧采用 "__" 以避免重名，另外也可以根据文件名中是否包含多个词语而
采用 "_" 连接起来。

## 文件头注释

在每个源文件文件头上，应该包括相应的版权信息，Change Log 记录：

```c
/**
 * File      : maixpy_main.h
 * This file is part of MaixPy
 * Copyright 2019 Sipeed Co.,Ltd. MaixPy Development Team
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
```

例如采用如上的形式。

## 结构体定义

结构体名称请使用小写英文名的形式，单词与单词之间采用 "_" 连接，例如：

```c
struct lcd_config
{
    int width;
    int height;
};
```

其中，"{"，"}" 独立占用一行，后面的成员定义使用缩进的方式定义。

结构体等的类型定义请以结构体名称加上 "_t" 的形式作为名称，例如：

```c
    typedef struct lcd_config lcd_config_t;
```

## 宏定义

在 MaixPy 中，请使用大写英文名称作为宏定义，单词之间使用 "_" 连接，例如：

```c
    #define MAIXPY_TRUE                         1
```

## 函数名称、声明

函数名称请使用小写英文的形式，单词之间使用 "_" 连接。提供给上层应用使用的 API
接口，必须在相应的头文件中声明；如果函数入口参数是空，必须使用 void 作为入口参
数，例如：

```c
    maixpy_err_t lcd_init(void);
```

## 注释编写

请使用英文做为注释，使用中文注释将意味着在编写代码时需要来回不停的切换中英文输入法从而打断编写代码的思路。并且使用英文注释也能够比较好的与中国以外的技术者进行交流。

源代码的注释不应该过多，更多的说明应该是代码做了什么，仅当个别关键点才需要一些相应提示性的注释以解释一段复杂的算法它是如何工作的。对语句的注释只能写在它的上方或右方，其他位置都是非法的。

## 缩进及分行

缩进请采用 4 个空格的方式。如果没有什么特殊意义，请在 "{" 后进行分行，并在下一行都采用缩进的方式，例如：

```c
if (condition)
{
    /* others */
}
```

唯一的例外是 switch 语句，switch-case 语句采用 case 语句与 switch 对齐的方式，
例如：

```c
switch (value)
{
case value1:
    break;
case value2:
    break;
defalut:
    break;
}
```

case 语句与前面的 switch 语句对齐，后续的语句则采用缩进的方式。

分行上，如果没有什么特殊考虑，请**不要在代码中连续使用两个以上的空行**。

## 大括号与空格

从代码阅读角度，建议每个大括号单独占用一行，而不是跟在语句的后面，例如：

```c
if (condition)
{
    /* others */
}
```

匹配的大括号单独占用一行，代码阅读起来就会有相应的层次而不会容易出现混淆的情况。

空格建议在非函数方式的括号调用前留一个空格以和前面的进行区分，例如：

```c
if (x <= y)
{
    /* others */
}

for (index = 0; index < MAX_NUMBER; index ++)
{
    /* others */
}
```

建议在括号前留出一个空格(涉及的包括 if、for、while、switch 语句)，而运算表达式中，运算符与字符串间留一个空格。另外，不要在括号的表达式两侧留空格，例如：

```c
if ( x <= y )
{
    /* other */
}
```

这样括号内两侧的空格是不允许的。

## log 信息

在 MaixPy 中，普遍使用的 log 方式是 printk, 而面向 py 终端的是使用 mp_print, 而在我们对 MaixPy 功能增减之后建议将不需要的 printk 删除或者注释掉

但是**注意**，最终提交的代码里面不能有`printk`和`printf`函数， 只能在调试时使用！！！否则会导致 IDE 使用时断开连接

日志输出应该被设计成正常情况下是关闭状态(例如通过一个变量或宏就能够开启)，并且
当真正输出日志时，日志是易懂易定位问题的方式。"天书式"的日志系统是糟糕的，不合理的。

## 函数

在内核编程中，函数应该尽量精简，仅完成相对独立的简单功能。函数的实现不应该太长，函数实现太长，应该反思能够如何修改(或拆分)使得函数更为精简、易懂。

## 用 astyle 自动格式化代码

参数：

    --style=allman
    --indent=spaces=4
    --indent-preproc-block
    --pad-oper
    --pad-header
    --unpad-paren
    --suffix=none
    --align-pointer=name
    --lineend=linux
    --convert-tabs
    --verbose


## 规范参考

- AliOS-Things -- [《AliOS Things Coding Style Guide》](https://github.com/alibaba/AliOS-Things/wiki/AliOS-Things-Coding-Style-Guide)

- RT-Thread -- [《RT-Thread 编程风格》](https://github.com/RT-Thread/rt-thread/blob/master/documentation/coding_style_cn.md)
