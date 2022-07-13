---
title: Python 变量作用域
keywords: Python, 作用域,
desc: Python作用域说明
date: 2022-07-13
tags: Python
---

这里说明一下 Python 变量作用域，帮助大家更好地使用 Python； [原文链接](https://www.cnblogs.com/Jolly-hu/p/12228320.html)

<!-- more -->

## 作用域简介

**作用域指的是变量的有效范围**。变量并不是在任何位置都可以访问的，访问权限取决于这个变量是在哪里赋值的，也就是在哪个作用域内的。

通常而言，在编程语言中，变量的作用域从代码结构形式来看，有块级、函数、类、模块、包等由小到大的级别。但是在 Python 中，没有块级作用域，也就是类似 if语句块、for语句块、with上下文管理器 等等是不存在作用域概念的，他们等同于普通的语句

```python
if True:            # if语句块没有作用域
    x = 1
print(x)
# 1
def func():         # 函数有作用域
    a = 8
print(a)
# Traceback (most recent call last):
#   File "<pyshell#3>", line 1, in <module>
#     a
# NameError: name 'a' is not defined
```

上面的代码可以试着运行一下，然后发现在 if 语句内定义的变量 x，可以被外部访问，而在函数 func() 中定义的变量 a，则无法在外部访问。

通常，函数内部的变量无法被函数外部访问，但内部可以访问；类内部的变量无法被外部访问，但类的内部可以。通俗来讲，就是内部代码可以访问外部变量，而外部代码通常无法访问内部变量。

变量的作用域决定了程序的哪一部分可以访问哪个特定的变量名称。
Python 的作用域一共有4层，分别是：
- L （Local） 局部作用域
- E （Enclosing） 闭包函数外的函数中
- G （Global） 全局作用域
- B （Built-in） 内建作用域

```python
global_var = 0  # 全局作用域
def outer():
    out_var = 1  # 闭包函数外的函数中
    def inner():
        inner_var = 2  # 局部作用域
```

前面说的都是变量可以找得到的情况，那如果出现本身作用域没有定义的变量，那该如何寻找呢？

Python 以 L –> E –> G –>B 的规则查找变量，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，最后去内建中找。

如果这样还找不到，那就提示变量不存在的错误。例如下面的代码，函数 func 内部并没有定义变量 a，可是 print 函数需要打印 a，那怎么办？

向外部寻找！按照 L –> E –> G –>B 的规则，层层查询，这个例子很快就从外层查找到了 a，并且知道它被赋值为 1，于是就打印了 1。

```python
a = 1

def func():
    print(a)
```

## 全局变量和局部变量

定义在函数内部的变量拥有一个局部作用域，被叫做局部变量，定义在函数外的拥有全局作用域的变量，被称为全局变量。（类、模块等同理）

所谓的局部变量是相对的。局部变量也有可能是更小范围内的变量的外部变量。

局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。

```python
a = 1               # 全局变量

def func():
    b = 2           # 局部变量
    print(a)        # 可访问全局变量a,无法访问它内部的c

    def inner():
        c = 3       # 更局部的变量
        print(a)    # 可以访问全局变量a
        print(b)    # b对于inner函数来说，就是外部变量
        print(c)
```

## global 和 nonlocal 关键字

我们先看下面的例子：

```python
total = 0                        # total是一个全局变量

def plus( arg1, arg2 ):
    total = arg1 + arg2          # total在这里是局部变量.
    print("函数内局部变量total=  ", total)
    print("函数内的total的内存地址是: ", id(total))
    return total

plus(10, 20)
print("函数外部全局变量total= ", total)
print("函数外的total的内存地址是: ", id(total))
```
很明显，函数 plus 内部通过 total = arg1 + arg2 语句，新建了一个局部变量 total，它和外面的全局变量 total 是两码事。而如果我们想要在函数内部修改外面的全局变量 total 呢？使用  global 关键字！ 

> global：指定当前变量使用外部的全局变量

```python
global：指定当前变量使用外部的全局变量

total = 0                        # total是一个全局变量

def plus( arg1, arg2 ):
    global total    # 使用global关键字申明此处的total引用外部的total
    total = arg1 + arg2
    print("函数内局部变量total=  ", total)
    print("函数内的total的内存地址是: ", id(total))
    return total

plus(10, 20)
print("函数外部全局变量total= ", total)
print("函数外的total的内存地址是:
```
所运行结果：
```python
函数内局部变量total=   30
函数内的total的内存地址是:  503494624
函数外部全局变量total=  30
函数外的total的内存地址是:  503494624
```
我们再来看下面的例子：
```python
a = 1
print("函数outer调用之前全局变量a的内存地址： ", id(a))

def outer():
    a = 2
    print("函数outer调用之时闭包外部的变量a的内存地址： ", id(a))
    def inner():
        a = 3
        print("函数inner调用之后闭包内部变量a的内存地址： ", id(a))
    inner()
    print("函数inner调用之后，闭包外部的变量a的内存地址： ", id(a))
outer()
print("函数outer执行完毕，全局变量a的内存地址： ", id(a))
```
如果你将前面的知识点都理解通透了，那么这里应该没什么问题，三个 a 各是各的 a，各自有不同的内存地址，是三个不同的变量。

打印结果也很好的证明了这点：
```python
函数outer调用之前全局变量a的内存地址：  493204544
函数outer调用之时闭包外部的变量a的内存地址：  493204576
函数inner调用之后闭包内部变量a的内存地址：  493204608
函数inner调用之后，闭包外部的变量a的内存地址：  493204576
函数outer执行完毕，全局变量a的内存地址：  493204544
```
那么，如果，inner 内部想使用 outer 里面的那个 a，而不是全局变量的那个 a，怎么办？用 global 关键字？先试试看吧：
```python
a = 1
print("函数outer调用之前全局变量a的内存地址： ", id(a))
def outer():
    a = 2
    print("函数outer调用之时闭包外部的变量a的内存地址： ", id(a))
    def inner():
        global a   # 注意这行
        a = 3
        print("函数inner调用之后闭包内部变量a的内存地址： ", id(a))
    inner()
    print("函数inner调用之后，闭包外部的变量a的内存地址： ", id(a))
outer()
print("函数outer执行完毕，全局变量a的内存地址： ", id(a))
```
运行结果如下，很明显，global使用的是全局变量a。
```python
函数outer调用之前全局变量a的内存地址：  494384192
函数outer调用之时闭包外部的变量a的内存地址：  494384224
函数inner调用之后闭包内部变量a的内存地址：  494384256
函数inner调用之后，闭包外部的变量a的内存地址：  494384224
函数outer执行完毕，全局变量a的内存地址：  494384256
```
那怎么办呢？使用 nonlocal 关键字！它可以修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量。将 global a 改成 nonlocal a 后运行，代码这里我就不重复贴了，

运行后查看结果，可以看到我们真的引用了 outer 函数的 a 变量。
```python
函数outer调用之前全局变量a的内存地址：  497726528
函数outer调用之时闭包外部的变量a的内存地址：  497726560
函数inner调用之后闭包内部变量a的内存地址：  497726592
函数inner调用之后，闭包外部的变量a的内存地址：  497726592
函数outer执行完毕，全局变量a的内存地址：  497726528
```

## 面试真题
不要上机测试，请说出下面代码的运行结果：

```python
a = 10
def test():
    a += 1
    print(a)
test()
```

很多同学会说，这太简单了！函数内部没有定义 a，那么就去外部找，找到 a=10，于是加 1，打印 11！

我会告诉你，这段代码有语法错误吗？a += 1 相当于 a = a + 1，按照赋值运算符的规则是先计算右边的 a+1。但是，Python 的规则是，如果在函数内部要修改一个变量，那么这个变量需要是内部变量，除非你用 global 声明了它是外部变量。很明显，我们没有在函数内部定义变量 a，所以会弹出局部变量在未定义之前就引用的错误。

## 更多的例子

再来看一些例子（要注意其中的闭包，也就是函数内部封装了函数）：

```python
name = 'jack'

def outer():
    name='tom'

    def inner():
        name ='mary'
        print(name)

    inner()

outer()
```
上面的题目很简单，因为inner函数本身有name变量，所以打印结果是mary。那么下面这个呢？
```python
name ='jack'

def f1():
    print(name)

def f2():
    name = 'eric'
    f1()

f2()
```

这题有点迷惑性，想了半天，应该是‘eric’吧，因为 f2 函数调用的时候，在内部又调用了 f1 函数，f1 自己没有 name 变量，那么就往外找，发现 f2 定义了个 name，于是就打印这个 name。错了！！！结果是‘jack’！

**Python函数的作用域取决于其函数代码块在整体代码中的位置，而不是调用时机的位置**。调用 f1 的时候，会去 f1 函数的定义体查找，对于 f1 函数，它的外部是 name ='jack'，而不是 name = 'eric'。

再看下面的例子，f2 函数返回了 f1 函数：

```python
name = 'jack'

def f2():
    name = 'eric'
    return f1

def f1():
    print(name)

ret = f2()
ret()
```

仔细回想前面的例子，其实这里有异曲同工之妙，所以结果还是‘jack’。