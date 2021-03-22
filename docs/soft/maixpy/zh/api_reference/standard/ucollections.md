---
title: ucollections – 集合和容器类型
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: ucollections – 集合和容器类型
---




该模块实现了相应CPython模块的子集，如下所述。有关更多信息，请参阅原始CPython文档 [collections](https://docs.python.org/3.5/library/collections.html#module-collections).

此模块实现高级集合和容器类型以保存/累积各种对象。

## 类

### ucollections.deque(iterable, maxlen[, flags])

Deques（双端队列）是一个类似列表的容器，支持O（1）追加并从双端队列的任一侧弹出。使用以下参数创建新的deques：

* iterable必须是空元组，并且新的deque被创建为空。
* 必须指定maxlen，并且双端队列将限制为此最大长度。一旦双端队列已满，添加的任何新项目将丢弃对方的项目。
* 添加项目时，可选标志可以为1以检查溢出。

除了支持bool和len之外，deque对象还有以下方法：

#### `deque.append(x)`

将`x`添加到双端队列的右侧。如果启用了溢出检查并且没有剩余空间，则引发 IndexError。

#### `deque.popleft()`

从双端队列的左侧移除并返回一个项目。如果没有项目，则引发 IndexError。

### ucollections.namedtuple(name, fields)

这是工厂函数，用于创建具有特定名称和字段集的新的namedtuple类型。 namedtuple是元组的子类，它不仅可以通过数字索引访问其字段，还可以使用符号字段名称访问属性访问语法。 Fields是指定字段名称的字符串序列。为了与CPython兼容，它也可以是一个以空格分隔的字段命名的字符串（但效率较低）。使用示例：

```python
from ucollections import namedtuple

MyTuple = namedtuple("MyTuple", ("id", "name"))
t1 = MyTuple(1, "foo")
t2 = MyTuple(2, "bar")
print(t1.name)
assert t2.name == t2[1]
```

### ucollections.OrderedDict(...)

`dict`类型子类，它记住并保留添加的键的顺序。当迭代命令dict时，按照添加的顺序返回键/项：

```python
from ucollections import OrderedDict

# To make benefit of ordered keys, OrderedDict should be initialized
# from sequence of (key, value) pairs.
d = OrderedDict([("z", 1), ("a", 2)])
# More items can be added as usual
d["w"] = 5
d["b"] = 3
for k, v in d.items():
    print(k, v)
```

Output:

```python
z 1
a 2
w 5
b 3
```




