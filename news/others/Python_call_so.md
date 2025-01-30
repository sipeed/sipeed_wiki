---
title: Python3调用c/cpp的方法
keywords: python, c, cpp,
desc: python调用so
date: 2022-03-31
tags: python, c, cpp
---

<!-- more -->

原文链接：https://blog.csdn.net/springlustre/article/details/101177282
作者：[springlustre](https://blog.csdn.net/springlustre?type=blog)
有改动，仅供参考

python中使用 ctypes 模块可以在python中直接调用C/C++。
首先要将C/C++编译成动态库（.so)，然后python中调用即可。

特别注意在调用C++函数需要在函数声明时，加入前缀 extern "C" ，这是因为C++支持函数重载功能，在编译时会改变函数名。在函数声明时，前缀extern "C"可以确保按C的方式进行编译。

值得注意的是，一定要有函数输入输出类型的声明，int型不用转换，float和double类型需要进行转换；
ctypes中的变量类型与C中对应如下：

| ctypes数据类型 | C数据类型     |
| -------------- | ------------- |
| c_char         | char          |
| c_short        | short         |
| c_int          | int           |
| c_long         | long          |
| c_float        | float         |
| c_double       | double        |
| c_void_p       | void          |
| c_uint8        | unsigned char |

使用方法：
- 编写c++代码

```cpp
#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>
#include <stdio.h>


class Test{
    private:
        double _calculate(int a, double b);
    public:
        double calculate(int a, double b, char c[], int * d, double * e, char ** f);
};

double Test::_calculate(int a, double b){
    double res = a+b;
    std::cout<<"res: "<<res<<std::endl;
    return res;
}

double Test::calculate(int a, double b, char c[], int * d, double * e, char ** f){
    std::cout<<"a: "<<a<<std::endl;
    std::cout<<"b: "<<b<<std::endl;
    std::cout<<"c: "<<c<<std::endl;
    std::cout<<"d: "<<d[0]<<d[1]<<std::endl;
    std::cout<<"e: "<<e[0]<<e[1]<<std::endl;
    std::cout<<"f: "<<f[0]<<f[1]<<std::endl;
    return this->_calculate(a, b);
}


// 封装C接口
extern "C"{
// 创建对象
    Test* test_new(){
        return new Test;
    }
    double my_calculate(Test* t, int a, double b, char c[], int * d, double * e, char ** f){
        return t->calculate(a, b,c,d,e,f);
    }
}

```
- 将上面的代码编译成so文件

> g++ -shared -Wl,-soname,test -o test.so -fPIC test.cpp

- 使用python调用so文件

```python
# -*- coding: utf-8 -*-
import ctypes
# 指定动态链接库
lib = ctypes.cdll.LoadLibrary('./test.so')
#需要指定返回值的类型，默认是int
lib.my_calculate.restype = ctypes.c_double

class Test(object):
    def __init__(self):
        # 动态链接对象
        self.obj = lib.test_new()

    def calculate(self, a, b,c,d,e,f):
        res = lib.my_calculate(self.obj, a, b,c,d,e,f)
        return res

#将python类型转换成c类型，支持int, float,string的变量和数组的转换
def convert_type(input):
    ctypes_map = {int:ctypes.c_int,
              float:ctypes.c_double,
              str:ctypes.c_char_p
              }
    input_type = type(input)
    if input_type is list:
        length = len(input)
        if length==0:
            print("convert type failed...input is "+input)
            return null
        else:
            arr = (ctypes_map[type(input[0])] * length)()
            for i in range(length):
                arr[i] = bytes(input[i],encoding="utf-8") if (type(input[0]) is str) else input[i]
            return arr
    else:
        if input_type in ctypes_map:
            return ctypes_map[input_type](bytes(input,encoding="utf-8") if type(input) is str else input)
        else:
            print("convert type failed...input is "+input)
            return null

if __name__ == '__main__':
    t = Test()
    A1	= 123;
    A2	= 0.789;
    A3	= "C789";
    A4	= [456,789];
    A5	= [0.123,0.456];
    A6	= ["A123", "B456"];
    print(t.calculate(convert_type(A1), convert_type(A2), convert_type(A3),convert_type(A4),convert_type(A5),convert_type(A6)))
```