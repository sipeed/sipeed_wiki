---
title: ucollections-collection and container types
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: ucollections-collections and container types
---




This module implements a subset of the corresponding CPython module, as described below. For more information, please refer to the original CPython documentation [collections](https://docs.python.org/3.5/library/collections.html#module-collections).

This module implements advanced collections and container types to store/accumulate various objects.

## Class

### ucollections.deque(iterable, maxlen[, flags])

Deques (deques) is a list-like container that supports O(1) append and pops from either side of the deque. Create new deques with the following parameters:

* Iterable must be an empty tuple, and the new deque is created as empty.
* Must specify maxlen, and the deque will be limited to this maximum length. Once the deque is full, any new items added will discard each other's items.
* When adding items, the optional flag can be 1 to check overflow.

In addition to supporting bool and len, the deque object has the following methods:

#### `deque.append(x)`

Add `x` to the right side of the deque. If overflow checking is enabled and there is no space left, an IndexError is raised.

#### `deque.popleft()`

Remove and return an item from the left side of the deque. If there are no items, an IndexError is raised.

### ucollections.namedtuple(name, fields)

This is a factory function to create a new namedtuple type with a specific name and field set. namedtuple is a subclass of tuples. It can not only access its fields through numerical indexes, but also use symbolic field names to access attribute access syntax. Fields is a sequence of strings specifying the names of fields. For compatibility with CPython, it can also be a string named after a space separated field (but it is less efficient). Use example:

```python
from ucollections import namedtuple

MyTuple = namedtuple("MyTuple", ("id", "name"))
t1 = MyTuple(1, "foo")
t2 = MyTuple(2, "bar")
print(t1.name)
assert t2.name == t2[1]
```

### ucollections.OrderedDict(...)

The `dict` type subclass, it remembers and preserves the order of the added keys. When the dict is iterated, the keys/items are returned in the order of addition:

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
