---
title: MaixPy programming specification
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: MaixPy programming specification
---


This is a development guide for **MaixPy** developers. **MaixPy** as an open source software, it needs to be completed by different people in a cooperative way. This document is a guide for developers.

**MaixPy** developers please follow this programming style. At the same time, users who use MaixPy can also use this document to understand some conventions in the MaixPy code so that they can easily grasp the implementation of MaixPy.

## Normative principles

- [x] Simple, avoid obscure syntax
- [x] Strict and logical thinking
- [x] Simple, concise naming and refined code
- [x] Performance, optimized by algorithm, compiler and hardware

## Directory structure && file name

- Directory Structure

The entire project is divided into subdirectories according to functional modules, and each subdirectory is divided into header files and source file directories to make the structure clear and easy to understand.
If the catalog name has no special requirements, please use all lowercase; the catalog name should reflect part of the meaning, and the components directory can reflect the meaning of components.

- File structure

If there is no special requirement for the file name (if you quote other places, you can keep the corresponding name), please use all lowercase. In addition, in order to avoid the problem of duplicate file names, please try not to use generalized and frequently used names in some places.

## Header file definition

C language header files need to define a symbol in order to avoid repeated inclusion. Please use the following definition of this symbol
style of:

```c
#ifndef __FILE_H__
#define __FILE_H__
/* header file content */
#endif
```

That is, "__" is used on both sides of the defined symbol to avoid duplication. In addition, it can also be changed according to whether the file name contains multiple words.
Use "_" to connect.

## File header comment

The header of each source file should include the corresponding copyright information, Change Log record:

```c
/**
 * File: maixpy_main.h
 * This file is part of MaixPy
 * Copyright 2019 Sipeed Co.,Ltd. MaixPy Development Team
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
```

For example, the above form is adopted.

## Structure definition

Please use lowercase English names for structure names, and use "_" to connect words to words, for example:

```c
struct lcd_config
{
    int width;
    int height;
};
```

Among them, "{", "}" occupies a line independently, and the following member definitions are defined by indentation.

For the type definition of structure, please use the structure name plus "_t" as the name, for example:

```c
    typedef struct lcd_config lcd_config_t;
```

## Macro definition

In MaixPy, please use uppercase English names as macro definitions, and use "_" between words to connect, for example:

```c
    #define MAIXPY_TRUE 1
```

## Function name, declaration

Please use lowercase English for the function name, and use "_" to connect between words. Provide APIs for upper-level applications
Interface must be declared in the corresponding header file; if the function entry parameter is empty, void must be used as the entry parameter
Number, for example:

```c
    maixpy_err_t lcd_init(void);
```

## Comment writing

Please use English as comments. Using Chinese comments will mean that you need to switch back and forth between Chinese and English input methods when writing code to interrupt the idea of ​​writing code. And the use of English annotations can better communicate with technicians outside of China.

There should not be too many comments on the source code. More explanation should be what the code does. Only when individual key points need some corresponding suggestive comments to explain how a complex algorithm works. Comments on the statement can only be written above or on the right, other positions are illegal.

## Indentation and branching

Please use 4 spaces for indentation. If there is no special meaning, please branch after "{" and use indentation on the next line, for example:

```c
if (condition)
{
    /* others */
}
```

The only exception is the switch statement. The switch-case statement uses the alignment of the case statement with the switch.
E.g:

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

The case statement is aligned with the previous switch statement, and the subsequent statements are indented.

On the branch, if there is no special consideration, please **do not use more than two blank lines in a row** in the code.

## Braces and spaces

From the perspective of code reading, it is recommended that each curly brace occupy a separate line instead of following the statement, for example:

```c
if (condition)
{
    /* others */
}
```

The matching braces occupies a single line, and the code will have a corresponding level when reading it without confusion.

Space It is recommended to leave a space before the non-function bracket call to distinguish it from the previous one, for example:

```c
if (x <= y)
{
    /* others */
}

for (index = 0; index <MAX_NUMBER; index ++)
{
    /* others */
}
```

It is recommended to leave a space before the brackets (including if, for, while, switch statements involved), and a space between the operator and the string in the operation expression. In addition, do not leave spaces on both sides of the expression in parentheses, for example:

```c
if (x <= y)
{
    /* other */
}
```

The spaces on both sides of the brackets are not allowed.

## log information

In MaixPy, the commonly used log method is printk, and the py terminal is mp_print, and after we increase or decrease the MaixPy function, it is recommended to delete or comment out the unnecessary printk

But **note**, the final submitted code cannot contain `printk` and `printf` functions, they can only be used during debugging! ! ! Otherwise it will cause disconnection when using the IDE

The log output should be designed to be turned off under normal circumstances (for example, it can be turned on by a variable or macro), and
When the log is actually output, the log is an easy way to understand and locate the problem. The "heavenly book" log system is bad and unreasonable.

## Function

In kernel programming, functions should be as concise as possible and only complete relatively independent simple functions. The implementation of the function should not be too long, and the implementation of the function should be too long. You should reflect on how you can modify (or split) the function to make the function more concise and understandable.

## Use astyle to format code automatically

parameter:

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


## Specification Reference

- AliOS-Things - [《AliOS Things Coding Style Guide》](https://github.com/alibaba/AliOS-Things/wiki/AliOS-Things-Coding-Style-Guide)

- RT-Thread - [《RT-Thread Programming Style》](https://github.com/RT-Thread/rt-thread/blob/master/documentation/coding_style_cn.md)
