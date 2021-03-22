---
title: uheapq-heap queue algorithm
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy doc: uheapq-heap queue algorithm
---



This module implements a subset of the corresponding CPython module, as described below.For more information, please refer to the original CPython documentation: [heapq](https://docs.python.org/3.5/library/heapq.html#module-heapq).

This module implements the heap queue algorithm.

A heap queue is just a list that stores its elements in some way.


## Function

### heappush

```python
uheapq.heappush(heap, item)
```

Put elements into the heap.

### heappop

```python
uheapq.heappop(heap)
```

Pop the first element in the heap and return it.If the heap is empty, an `IndexError` is raised.

### heapify

```python
uheapq.heapify(x)
```

Convert the list x to a heap.This is an in-place (division exchange sort) operation.
