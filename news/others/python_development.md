---
title: 学习开源项目和 Python 编程入门建议
keywords: Python,入门,开源
date: 2022-06-11
tags: Python, 入门, 开源
---

本文是给有一点 Python 基础但还想进一步深入的同学，有经验的开发者建议跳过。

<!-- more -->

原文链接: https://www.cnblogs.com/juwan/p/14485001.html 有改动
作者：[Juwan](https://www.cnblogs.com/juwan/) 

## 前言

在写这篇文章的时候的时候 [junhuanchen](https://github.com/junhuanchen) 希望引导用户成为专业的开发者，而不是只会调用代码就好，所以在 MaixPy3 开源项目上会为你带来值得学习和容易上手的开源项目，因此开篇会引导用户学习一些长期有利于编程工作上好的做法和观念，就先从最简单的认知项目开始吧。

第一次接触需要编程的开源硬件项目，要做的第一件事就是先有一个好的开始——例如运行 Hello World 程序，意味着你必须能够先将这个代码运行起来才能够继续后续的内容，它可以是硬件、软件、工具等可编程的载体。

要先找到它所提供的开发文档（例如本文），先速览全文，从专业的角度来看，你需要先关注它提供了哪些资源，可以在哪里反馈你的疑问，这样就有利于你后续开发过程中碰到问题后能够迅速得到解决，避免在之后在学习和开发过程中耽误时间。

有哪些资源是值得关注的？
- 学会搜索！！！！！(Google，Bing，stackoverflow等)
- 找到它的开源项目（如：github.com/sipeed），获取它所提供的一系列源码。
- 找到它提供的用户手册、应用案例、数据手册等等一系列开发所需要的文档。
- 找到它的开发、编译、烧录、量产等一系列配套工具链，为后续软件开发活动中做准备。
- 找到它的公开交流的环境，如 bbs、github、twitter、facebook、qq、wechat 等交流平台。

现在你可以开始编程了，但是要遵守一些在开源软件上的规则，认知到**开源协议**的存在，不要随意地做出侵犯他人软件的行为，哪怕没有法律责任的问题。

在开源软件的世界里，**鼓励人们自由参与和贡献代码，而不是鼓励如何免费白嫖，自由不等于免费，免费不等于服务，将软件源码公开是为了让用户更好更具有针对性的提交和反馈项目中存在的问题，不是为了更好服务你，请不要以服务自己的产品为中心**。

请尊重所有在开源环境里工作的朋友们，尊重他们（或是未来的你）的劳动成果。

最后在开源的世界里，学会技术，学会成长，学会参与项目，学会分享成果

## Hello World

说了这么多，不如先来运行一段 Python3 代码吧。当然这里不教语法，语言语法请自行学习

```python
print("hello world")
```

直接点击右上角的执行即可

<iframe src="https://tool.lu/coderunner/embed/aEj.html" style="height: 320px" frameborder="0" mozallowfullscreen="" webkitallowfullscreen="" allowfullscreen=""></iframe>

> 在线 Python 编程 [runoob-python](https://www.runoob.com/try/runcode.php?filename=HelloWorld&type=python3) 备用地址。

但是实际项目中那种代码是不行的，认真写一个：

```python
# encoding: utf-8

def unit_test():
    '''
    this is unit_test
    '''
    print("hello world")
    raise Exception('unit_test')

if __name__ == "__main__":
    try:
        unit_test()
    except Exception as e:
        import sys, traceback
        exc_type, exc_value, exc_obj = sys.exc_info()
        traceback.print_tb(exc_obj)
        print('have a error:', e)
```

运行上面的代码后会出现下面的 log (运行在不同地方可能会出现不同的 log，但是不影响分析)：

```python
hello world
have a error: unit_test

  File "script.py", line 12, in 
    unit_test()
  File "script.py", line 8, in unit_test
    raise Exception('unit_test')
```

代码瞬间就变得复杂了起来？其实不然，这么写必然有它的用意，那这么写都考虑到了哪些情况呢？

### 注意字符编码和代码缩进格式

初学者经常会出现缩进不对齐的语法问题，代码的语法出现问题过于基础就不详谈，检查代码的小技巧就是 `CTAL + A` 全选代码，按 `TAB` 键右缩进，再配合 `SHIFT + TAB` 左缩进来发现哪段代码存在问题。

首行的 `# encoding: utf-8` 是为了避免在代码中存在中文或其他语言的字符编码导致的运行出错的问题。

在 python3 的字符串类型中 str 与 bytes 是一对欢喜冤家，例如 print(b'123') 打印出来的是 b'123' ，而实际上就是 '123' 的 bytes 字符串，前缀 b 只是为了和 str 区分，因为用途不同，在不同的接口对数据类型的需求不对，例如传递 str 字符串时候是不允许输入 '\xFF' (0xFF) 字符的（会在转换过程中丢失），但 bytes 可以存储和表达。

### 给代码加入单元测试和异常捕获

想要写出一套稳定可用的代码，需要围绕接口可重入可测试的设计来编写封装。每个人写的代码都可能存在缺陷，在不能确定是哪里产生的问题之前，要能够恢复现场也要能够定位具体位置，使问题能够最快得到反馈。

所以在代码功能还没写之前，先把测试和异常的模板写好，再开始写功能，边写边测，确保最终交付的软件代码就算出问题也可以随时被测试（定位）出来。

```python
def unit_test():
    '''
    this is unit_test
    '''
    print("hello world")

if __name__ == "__main__":
    unit_test()
```

这样的代码可以保证任何人在任何时候运行该代码的时候都可以复现当时写下的场合所做的内容，然后 `if __name__ == "__main__":` 意味着该代码被其他模块包含的时候，不会在 import 该 Python 模块（可取名成 hello ）模块时调用，而是根据自己的代码需要执行相应的单元测试进行测试。

相关链接：[Python中“if \_\_name\_\_ == "\_\_main\_\_":”详细解析](https://zhuanlan.zhihu.com/p/340997807)

```python
import hello
hello.unit_test() # print("hello world")
```

接着加入异常机制（try: except Exception as e:）保护代码段，表示该段代码出错的时候，能够不停下代码继续运行，像硬件资源访问的代码常常会发生超时、找不到、无响应的错误状态，这种情况下，一个跑起来的系统程序通常不需要停下来，出错了也可以继续运行下一件事，然后把当时的错误记录下来，通过 print 或 logging 日志模块记录下来，拿着错误结果（日志）反馈给开发者，这样开发者就可以分析、定位和解决问题，这其中也包括你自己。

```python
try:
    raise Exception('unit_test')
except Exception as e:
    import sys, traceback
    exc_type, exc_value, exc_obj = sys.exc_info()
    traceback.print_tb(exc_obj)
    print('have a error:', e)
```

单元测试是每个程序都尽可能保持的基本原则，虽然人会偷懒，但最起码的代码格式还是要有的。

- 注：traceback 可以抓取最后一次运行出现的错误而不停止运行，但该模块不存在 MicroPython(MaixPy) 中，它有类似的替代方法。

## 封装代码接口成通用模块的方法

在 Python 上有很多封装参考，主要是为了形成抽象的函数模块。

所以出现了一些经典的编程思想，如面向过程、面向对象、面向切面、面向函数等编程方法，哪一种更好就不比较和讨论了。

这里就简单叙述一下这些编程方法的逐渐发展与变化的过程，可以如何做出选择。

### 面向过程

用面向过程的思维写代码，强调的是这份代码做的这件事需要分几步完成，例如最开始写代码都是这样的。

```python
one = 1
two = 2
three = one + two
print(three)
```

这是用最初直觉来写代码，后来意识到可以这样写成通用功能，这是最初的代码封装成某个函数。

```python
def sum(num1, num2):
    return num1 + num2
one, two = 1, 2
print(sum(one, two)) # 1 + 2 = 3
```

于是你多写了个类似的乘法操作。

```python
def mul(num1, num2):
    return num1 * num2
one, two = 1, 2
print(mul(one, two)) # 1 * 2 = 2
```

这时的代码是按照每一个代码操作流程来描述功能的。

### 面向对象

面向对象是相对于面向过程来讲的，把相关的数据和方法组织为一个整体来看待，从更高的层次来进行系统建模，更贴近事物的自然运行模式，一切事物皆对象，通过面向对象的方式，将现实世界的事物抽象成对象，现实世界中的关系抽象成类、继承，帮助人们实现对现实世界的抽象与数字建模。

在看了一些面向对象的描述后，你会意识到上节面向过程的函数操作可能很通用，应该不只适用于一种变量类型，所以可以通过面向对象（class）的方法来封装它，于是可以试着这样写。

```python
class object:
    def sum(self, a, b):
        return a + b
    def mul(self, a, b):
        return a * b
obj = object()
print(obj.sum(1, 2)) # 1 + 2 = 3
print(obj.mul(1, 2)) # 1 * 2 = 2
```

这样会意识到似乎还不只是数字能用，感觉字符串也能用。

```python
class object:
    def sum(self, a, b):
        return a + b
    def mul(self, a, b):
        return a * b
obj = object()
print(obj.sum('1', '2')) # 1 + 2 = 3
print(obj.mul('1', '2')) # 1 * 2 = 2
```

但这么写会出问题的，字符串相加的时候可以，但相乘的时候会报错误，因为是字符串这个类型的变量是不能相乘的。

```python
12
Traceback (most recent call last):
  File "script.py", line 8, in <module>
    print(obj.mul('1', '2')) # 1 * 2 = 2
  File "script.py", line 5, in mul
    return a * b
TypeError: can't multiply sequence by non-int of type 'str'
```

显然这样写代码就不合理了，但这时运用的面向对象的思想是可行的，只是实现的方式不够好而已，所以这时候应该重新设计对象类结构，例如可以写成下面的类结构。

```python
class obj:
    def __init__(self, value):
        self.value = value
    def __add__(self, obj):
        return self.value + obj
    def __mul__(self, obj):
        return self.value * obj

print(obj(1) + 2) # 3
print(obj(1) * 2) # 2
```

其中 `__add__` 和 `__mul__` 是可重载运算符函数，意味着这个类实例化的对象在做 + 和 * 运算操作的时候，会调用类（class）重载函数，接着可以提升可以运算的对象类型，进一步继承对象拓展功能（`class number(obj):`）和访问超类的函数（`super().__add__(obj)`），其中 `if type(obj) is __class__:` 用于判断传入的参数对象是否可以进一步处理。

```python
class number(obj):
    def __add__(self, obj):
        if type(obj) is __class__:
            return self.value + obj.value
        return super().__add__(obj)
    def __mul__(self, obj):
        if type(obj) is __class__:
            return self.value * obj.value
        return super().__mul__(obj)

print(number(1) + 2)
print(number(1) * 2)
print(number(1) + number(2))
print(number(1) * number(2))
```

这时候会发现可以进一步改写成字符串数值运算。

```python
class str_number(obj):
    def __init__(self, value):
        self.value = int(value)
    def __add__(self, obj):
        if type(obj) is __class__:
            return str(self.value + int(obj.value))
        return str(super().__add__(int(obj)))
    def __mul__(self, obj):
        if type(obj) is __class__:
            return str(self.value * int(obj.value))
        return str(super().__mul__(int(obj)))

print(str_number('1') + '2')
print(str_number('1') * '2')
print(str_number('1') + str_number('2'))
print(str_number('1') * str_number('2'))
```

现在就可以解决了最初的同类操作适用不同的数据类型，把最初的一段操作通用到数值和字符串了，可以受此启发，它不仅仅只是加法或乘法，还有可能是其他操作，关于面向对象的内容就说到这里，感兴趣的可以查阅相关资料深入学习，本节只讲述可以怎样使用面向对象的思维写代码，而不是单纯把 Class 当 Struct 来使用。

- 像最初写的代码，如果不通过对象继承分解函数，最终将会形成一个巨大的 Struct 结构。

### 面向切面

现在到了选择更多编程思维方式了，关于面向切面编程方法的场景是这样提出的：有一些函数，它在产品调试的时候会需要，但在产品上线的时候是不需要的，那这样的函数应该如何实现比较好？接下来不妨直接看代码，以日志输出的代码为例来说说面向切面，介绍一下如何使用装饰器进行编程的方法。

```python
def log(param):
    # simple
    if callable(param):
        def wrapper(*args, **kw):
            print('%s function()' % (param.__name__,))
            param(*args, **kw)
        return wrapper
    # complex
    def decorator(func):
        import functools
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (param, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

def now():
    print("2019")

@log
def now1():
    print("2020")

@log("Is this year?")
def now2():
    print("2021")

now()
now1()
now2()
```

运行结果:

```python
2019
now1 function()
2020
Is this year? now2():
2021
```

对于产品上线时不需要的函数，注释掉就可以了，更进一步还可以重新设计某些函数满足于某些条件后再运行。

- 在执行某段操作前，先打印当前的系统状态记录下来，确保出错时可以追溯到出错的地方。
- 在发送网络数据前，要先检查网络通路是否存在，网卡是否还在工作。
- 在运行操作前，先检查内存够不够，是否需要释放内存再继续操作。

可以看到，当想要不改变某些现成库代码的条件下拓展系统的功能，就不免需要面向切面的设计方法。

**注意！面向切面提出的是编程思想，实现的方法不一定是装饰函数，可以是回调函数，也可以是重载函数。**

### 面向函数

关于面向函数的场景是由于有些问题是被数学公式提出的，所以对于一些数学问题，并不一定要按过程化的思维来写，如实现阶乘函数（factorial），它的功能就是返回一个数的阶乘，即 1*2*3*...*该数。

```python
def fact(n):
    if n == 3:
        return 3*2*1
    if n == 2:
        return 2*1
    if n == 1:
        return 1
print(fact(3))
print(fact(2))
print(fact(1))
```

不难看出用最初的面向过程来写是写不下去的，不可能去定义所有的可能性，所以要找出规律，可以通过递归的方式实现。

```python
def fact(n):
    return 1 if n == 1 else n * fact(n - 1)
print(fact(1))
print(fact(5))
print(fact(100))
```

这样功能就完整了，简单来说函数式编程是让编程思维追求程序中存在的公式。

## 试试快速迭代的敏捷开发？

现代开源软件在经历了产测、内测、公测等环节后，直到更新到用户的手里，从前到后的过程通常在一周内就可以完成，所以在设计程序接口的时候，可以接受当下接口设计的不完美，等到未来有一个更好的替代功能接口的时候，就可以将其迭代替换下来，这意味着可以不用设计好整体的软件系统再开始工作，而是边做边改进，这套理论适用于初期需要频繁更新业务逻辑的开源软件。

这里简单引用一段小故事来说明这个现象。

快速迭代，不是说一定要产品做好了，才能上线，半成品也能上线。

在没有上线之前，你怎么知道哪好那不好。所以半成品也是可以出门的，一定不要吝惜在家，丑媳妇才需要尽早见公婆。尽早的让用户去评判你的想法，你的设计是否可以赢得用户的喜爱。快速发出，紧盯用户反馈。百度完成了第一版的搜索引擎，也是让用户去做的选择。用百度 CEO 李彦宏（Robin）的话来说“你怎么知道如何把这个产品设计成最好的呢？只有让用户尽快去用它。既然大家对这版产品有信心，在基本的产品功能上我们有竞争优势，就应该抓住时机尽快将产品推向市场，真正完善它的人将是用户。他们会告诉你喜欢哪里不喜欢哪里，知道了他们的想法，我们就迅速改，改了一百次之后，肯定就是一个非常好的产品了。”

## 准备一个好的开始

看到这里的你，可能会困惑，可能会看不懂，会觉得很复杂，这是认知上的偏差，实际上本文所讲述的都是编程思想上的基础，如果想专业起来，不认真是不行的。

不妨自己动手试试看吧。

