---
title: uheapq – 堆队列算法
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: uheapq – 堆队列算法
---



该模块实现了对应 CPython 模块的子集，如下所述。 有关更多信息，请参阅原始CPython文档：[heapq](https://docs.python.org/3.5/library/heapq.html#module-heapq)。

该模块实现堆队列算法。

堆队列只是一个以某种方式存储其元素的列表。


## 函数

### heappush

```python
uheapq.heappush(heap, item)
```

将元素放入堆。

### heappop

```python
uheapq.heappop(heap)
```

弹出堆中的第一个元素，然后将其返回。 如果heap为空，则引发`IndexError`。

### heapify

```python 
uheapq.heapify(x)
```

将列表x转换为堆。 这是一个 in-place（划分交换排序）操作。


