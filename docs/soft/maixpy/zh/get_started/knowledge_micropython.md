---
title: MicroPython 背景知识
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: MicroPython 背景知识
---


由于 **MaixPy** 是基于 **MicroPython** 之上进行开发构建的,
提供给用户最终的接口是 **Micropython** ，所以在使用 MaixPy 开发之初我们需要熟悉下 `MicroPython` 的基础知识与语法


## 关于 MicroPython:

MicroPython 是编程语言 Python3 的精简高效实现，语法和 Python3 保持一致，但只实现了 Python 标准库的一小部分，并且经过优化，可以在 MCU ， WIFI SOC 上等资源受限的环境中使用，所以我们在使用 MicroPython 需要了解其语法。

如果之前有 **C/C++/Java** (或任何其他语言)的编程经验，推荐
[《廖雪峰的 Python 教程》](https://www.liaoxuefeng.com/wiki/1016959663602400)

如果之前没有任何编程经验，推荐
[《笨方法学 Python》](https://wizardforcel.gitbooks.io/lpthw/content/)

## REPL 和 串口

首先，断开开发板与 MaixPy IDE 的连接，否则串口会冲突！

打开 MaixPy IDE 中的终端窗口

print('The quick brown fox', 'jumps over', 'the lazy dog')

输出:

```
The quick brown fox jumps over the lazy dog
```

print() 会依次打印每个字符串，遇到逗号“,”会输出一个空格，因此，输出的字符串是这样拼起来的：

> The quick brown fox jumps over the lazy dog

print() 也可以打印整数，或者计算结果：

```python
print(300)
300
print(100 + 200)
300
```

因此, 我们可以把计算100 + 200的结果打印得更漂亮一点:

```python
print('100 + 200 =', 100 + 200)
100 + 200 = 300
```

注意, 对于 100 + 200, Python 解释器自动计算出结果 300，但是 '100 + 200 =' 是字符串而非数学公式，Python 把它视为字符串。

## MicroPython 基本语法
### 变量

在 Python 中，等号 `=` 是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，例如：

```python
a = 123 # a是整数
print(a)
a = 'ABC' # a变为字符串
print(a)
```

这种变量本身类型不固定的语言称之为**动态语言**，与之对应的是 **静态语言**。
静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如 Java 是静态语言，赋值语句如下(// 表示注释)：

```java
int a = 123; // a是整数类型变量
a = "ABC";// 错误:不能把字符串赋给整型变量
```

和静态语言相比，动态语言更灵活，就是这个原因。

### list 列表

Python 内置的一种数据类型是**列表**：**list**.<br/>
**list** 是一种有序的集合, 可以随时添加和删除其中的元素.
比如, 列出班里所有同学的名字, 就可以用一个 **list** 表示:

```python
classmates = ['Michael', 'Bob', 'Tracy']
classmates
['Michael', 'Bob', 'Tracy']
```

变量 classmates 就是一个 `list`.<br/>
用 `len()` 函数可以获得 list 元素的个数:

```python
len(classmates)
3
```

用索引来访问 list 中每一个位置的元素, 索引是从 0 开始的:

```python
classmates[0]
'Michael'
classmates[1]
'Bob'
classmates[2]
'Tracy'
classmates[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

当索引超出了范围时，Python 会报一个 IndexError 错误，所以，要确保索引不要越界，记得最后一个元素的索引是 len(classmates) - 1。

如果要取最后一个元素，除了计算索引位置外，还可以用 -1 做索引，直接获取最后一个元素：

```python
classmates[-1]
'Tracy'
```

以此类推，可以获取倒数第2个、倒数第3个：

```python
classmates[-2]
'Bob'
classmates[-3]
'Michael'
classmates[-4]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  IndexError: list index out of range
```

当然，倒数第 4 个就越界了。

list 是一个**可变**的**有序表**，所以可以往 list 中追加元素到末尾：

```python
classmates.append('Adam')
classmates
['Michael', 'Bob', 'Tracy', 'Adam']
```

也可以把元素插入到指定的位置，比如索引号为1的位置：

```python
classmates.insert(1, 'Jack')
classmates
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
```

要删除 list 末尾的元素, 用 pop() 方法：

```python
classmates.pop()
'Adam'
classmates
['Michael', 'Jack', 'Bob', 'Tracy']
```

要把某个元素替换成别的元素, 可以直接赋值给对应的索引位置:

```python
classmates[1] = 'Sarah'
classmates
['Michael', 'Sarah', 'Tracy']
```

list 里面的元素的数据类型也可以不同, 比如:

```python
L = ['Apple', 123, True]
```

如果一个 list 中一个元素也没有，就是一个空的 list，它的长度为 0：

```python
L = []
len(L)
0
```

### tuple 元组

另一种有序列表叫元组: **tuple**.<br/>
tuple 和 list 非常类似，但是 `tuple` 一旦初始化就不能修改，比如同样是列出同学的名字：

```python
classmates = ('Michael', 'Bob', 'Tracy')
```

现在，classmates 这个 **tuple** 不能变了，它也没有 append(), insert() 这样的方法.其他获取元素的方法和 list 是一样的, 你可以正常地使用 classmates[0], classmates[-1], 但不能赋值成另外的元素.

不可变的 tuple 有什么意义？因为 tuple 不可变, 所以代码更安全。
如果可能，能用 tuple 代替 list 就尽量用 tuple。

tuple 的陷阱:当你定义一个 tuple 时, 在定义的时候, tuple 的元素就必须被确定下来, 比如:

```python
t = (1, 2)
t
(1, 2)
```

但是, 要定义一个
只有1个元素的 tuple, 如果你这么定义:

```python
t = (1)
t
1
```

但此时,定义的不是 tuple, t 是整型变量, 变量 t 的值为1! <br/>
这是因为括号()既可以表示tuple, 又可以表示数学公式中的小括号, 这就产生了歧义, 因此, Python规定, 这种情况下, 按小括号进行计算, 计算结果自然是1.

所以, 只有 1 个元素的 **tuple** 定义时必须加一个逗号`,`, 来消除歧义:

```python
t = (1,)
t
(1,)
```

Python在显示只有 1 个元素的 tuple 时, 也会加一个逗号`,`, 以免你误解成数学计算意义上的括号.

### 条件判断

if 语句的完整形式是:

```
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
```

比如:

```python
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')
```

### 循环

Python 的循环有两种, 一种是 `for...in` 循环, 依次把 list 或 tuple 中的每个元素迭代出来, 看例子:

```python
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
```

执行这段代码, 会依次打印 names 的每一个元素:

```python
Michael
Bob
Tracy
```

所以 `for x in ...` 循环就是把每个元素代入变量x, 然后执行缩进块的语句.

如果要计算 1-100 的整数之和, 从 1 写到 100 有点困难, 幸好 Python提供一个 range() 函数, 可以生成一个整数序列, 再通过 list() 函数可以转换为 list.<br/>
比如 range(5) 生成的序列是从 0 开始小于 5 的整数:

```python
list(range(5))
[0, 1, 2, 3, 4]
```

range(101) 就可以生成 0-100 的整数序列, 计算如下:

```python
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
```

第二种循环是 `while 循环`, 比如我们要计算 100 以内所有奇数之和, 可以用 while 循环实现:

```python
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
```

-----

### 数据类型转换

Python 内置的常用函数还包括数据类型转换函数, 比如 int() 函数可以把其他数据类型转换为整数:

```python
>>> int('123')
123
>>> int(12.34)
12
>>> float('12.34')
12.34
>>> str(1.23)
'1.23'
>>> str(100)
'100'
>>> bool(1)
True
from machine import GPIO
```
### 函数

在 Python 中, 定义一个函数要使用 `def` 语句, 依次写出函数名、括号、括号中的参数和冒号`:`, 然后在缩进块中编写函数体, 函数的返回值用 `return` 语句返回.

我们先写一个计算 x2 的函数:

```python
def power(x):
    return x * x
```

对于 power(x) 函数, 参数 x 就是一个位置参数.

当我们调用 power 函数时, 必须传入有且仅有的一个参数x:

```python
power(5)
25
power(15)
225
```

现在, 如果我们要计算 x3 怎么办?可以再定义一个 power3 函数, 但是如果要计算x4、x5……怎么办?我们不可能定义无限多个函数.

你也许想到了, 可以把 power(x) 修改为 power(x, n), 用来计算 xn , 说干就干:

```python
def power(x, n):
    s = 1
    while n > 0:
        n = n
         - 1
        s = s
         * x
    return s
```

对于这个修改后的power(x, n)函数, 可以计算任意n次方:

```python
power(5, 2)
25
power(5, 3)
125
```

修改后的 power(x, n) 函数有两个参数: x 和 n, 这两个参数都是位置参数, 调用函数时, 传入的两个值按照位置顺序依次赋给参数x和n.

### 切片

取一个 `list` 或 `tuple` 的部分元素是非常常见的操作.比如, 一个list 如下:

```python
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
```

取前3个元素, 用一行代码就可以完成切片:

```python
L[0:3]
['Michael', 'Sarah', 'Tracy']
```

L[0:3] 表示, 从索引 0 开始取, 直到索引 3 为止, 但不包括索引3.即索引0, 1, 2, 正好是3个元素.

如果第一个索引是0, 还可以省略:

```python
L[:3]
['Michael', 'Sarah', 'Tracy']
```

也可以从索引1开始, 取出2个元素出来:

```python
L[1:3]
['Sarah', 'Tracy']
```

`tuple` 也是一种 list, 唯一区别是 `tuple` 不可变.因此, `tuple` 也可以用切片操作, 只是操作的结果仍是 `tuple`:

```python
(0, 1, 2, 3, 4, 5)[:3]
(0, 1, 2)
```

`字符串` 'xxx' 也可以看成是一种 `list`, 每个元素就是一个字符.因此, 字符串也可以用切片操作, 只是操作结果仍是字符串:

```python
'ABCDEFG'[:3]
'ABC'
```

### 对象

Python 是**面向对象**编程的, 比如一个 LED 灯

```python
from pyb import LED

red_led = LED(1)
red_led.on()
```

LED 是一个**类**, red_led 就是一个**对象**, 可以对这个对象进行操作, 比如点亮 on, 关掉 off, 查看 value.

### 模块

### 什么是模块?

随着代码的增多，在一个文件里的代码会越来越长，越来越难看懂。

为了编写可维护的代码，我们把很多函数分组，放到不同的文件里。在Python 中，一个 `.py` 文件就称之为一个**模块(Module)**.

模块有什么好处?

复用代码方便！如果我写了一个模块，你也写了一个模块，我们就有了两个模块。我们把这些模块都组织起来，大家就可以少写很多代码了！

#### 如何使用模块?

```python
import time

time.sleep_ms(500)
```

`import time` 就是引入 `time` 这个模块。通过 `import` 语句，就可以引入模块。

### 更多

更多 MicroPython 基础语法教程请自行搜索。