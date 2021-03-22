---
title: 什么是 Python ？
keywords: MaixPy, Python, AIOT, 边缘计算
desc: maixpy doc: Python
---

## 说起 Python 语言

> 只提及一些重点，更详细的就请到一些 Python 教程网站学习吧。

为了让从程序员从~~秃头~~事业中解脱，在开源世界里诞生了名为大蟒蛇（Python）的编程语言。

它带来了什么？

- 提供了完整的软件开发标准库。
- 适应多种编程方式。
- 用尽量少的代码完成更多工作。
- 适应时间短、变化快的需求。
- 让编程工作看起来更像是在“搭积木”。
- 开源社区长期贡献了大量的第三方库。
- 可拓展 C 、 C++ 等其他语言编写的模块。
- 满足了想偷懒的愿望。

它是一门易用的动态编程语言，可以看作现代入门编程语言的起点，程序员平时或多或少都需要使用 Python 代码帮助完成一些日常、简单、重复的脚本操作。

相比其他编程语言，它看起来会很容易理解和使用，对于非专业人士也可以轻松使用起来，以 “Hello, World” 为例。

- C 

```c
#include <stdio.h>

int main(void) {
  printf("Hello, World!\n");
  return 0;
}
```

- C++

```c++
#include <iostream>
using namespace std;

int main() {
  cout << "Hello, World!" << endl;
  return 0;
}
```

- Java

```java
class HelloWorld {
  public static void main(String[] args) {
    System.out.println("Hello, World!");
  }
}
```

- JavaScript

```javascript
alert("Hello World")
```

```javascript
document.write("Hello World")
```

```javascript
console.log("Hello World")
```

- Python

```python
print("Hello, World!")
```

不难看出，从人类自然语言的角度来看 Python 语法简单直接，减少了不必要的讯息。

## 它是怎样工作的呢？

在编辑框上编写的 Python 代码，实际上是依次输入到实时运行的解释器程序当中的。

例如下述代码：

```python
tmp = 1 + 1
print(tmp)
```

运行它后就会输出 2 ，其中 tmp （变量）等于 2 ，如果这时候再运行下述代码。

```python
tmp = tmp + 1
print(tmp)
```

这时候就会输出 3 ，表示 tmp （变量）等于 3 了。

这是因为每一次运行的 Python 程序都并非是一个全新的开始，它是一直存在于一段程序当中的，只有当解释器程序退出后，才是真的结束程序，所以上一次运行的结果并没有清除，这也是程序不需要编译的原因。

这是与 C / C++ / JAVA 一类编程语言相冲突的地方，我们基于这个差异将 Python 称为动态语言，与此关联的还有 JavaScript 和 Lua 等编程语言。

实时上还有各种各样支持 Python 语言的解释器，虽然写的都是 Python 代码，但并非同一个事物。

我们常用的 Python 编程环境通常指 C 语言实现的 Python 解释器，涵盖 Python2.7 ~ Python3.10 的语法。

而在其他领域来说，有各式各样的 Python 语言的实现，如下：

- MicroPython 使用 Python3.5 语法

- Jython 使用 Java 实现的 Python 语言

- PyPy 通过 JIT 优化的 Python 语言

- IPython 基于 Python 语言的交互接口

也就是说 Python 这个名词，不一定是说 Python 编程语言，还可能是解释器，也可能是程序，这可能会有利于你理解 Python 这个事物背后可能存在的事物。

> 2020 年后不再提及 Python2.7 的任何内容，今后描述的 Python 以 Python3 的语法为准。

## 这一切都这么美好？

并不是。

在这么多编程语言中，Python 对于初学者来说是很上手且简单的，对于一些调用各种库的代码、不在意运行效率，甚至是代码的可维护性也可以忽略的场合，随手一写就可以完成任务。

但代价就是想提升你瞎写程序的性能，你要付出更多的时间去做优化。

> 写出文章不难，写好文章才难。

因为最初不了解 Python 所写出的代码，就像小孩子的涂鸦，到处复制粘贴，以至于写出来的代码东拼西凑整合起来的。

到了这时候，你会发现，一旦你想要改进它是很难做到的，从一开始就不了解它，又谈何改进。

所以这里提及一下，传统的编程语言入门要经历的过程：

- 学习计算机历史
- 学习计算机语法
- 学习编程范式
- 学习使用开发工具
- 学习使用调试代码
- 学习程序设计

而使用 Python 语言速成入门培养兴趣和获得成就感的代价就是以后从事这份职业会花费额外的时间补计算机的基础。

> 至少 Python 能让你点火先把火箭飞起来，而不用把火箭制造原理研究透彻了再起飞。

## 学哪个语言更好？

至于哪个更好，这里无法做出评价，建议顺应时代潮流，先解决问题，其他的再说。

- 黑猫白猫抓住老鼠就是好猫。
- 实践是检验事实的唯一标准。

最终怎么选择，就取决于你自己了。

