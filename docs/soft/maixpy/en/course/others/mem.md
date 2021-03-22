---
title: Memory management
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: memory management
---



In MaixPy, two types of memory management are currently used, one is GC (garbage collection) and the other is system heap memory, both of which exist at the same time.

For example: the chip has 6MiB of memory, adding the firmware uses the previous 2MiB, and the remaining 4MiB, the default `GC` uses 512KiB, and the rest is used for system heap memory management.


* In the code written at the level of `mpy`, variables are stored in the memory block managed by `GC`, such as defining a variable `a = [1,2,3,4]`, if the memory of `GC'` is insufficient, It will automatically trigger the execution of the `gc.collect()` function, and the `GC` will automatically destroy the unused variables, leaving space for new variables.
> `GC` uses the method of `mark-clear` to reclaim memory. If you are interested, please see [here](https://neucrack.com/p/46)
* Because `GC` needs to scan the memory, if the rest is given to `GC` except for the memory occupied by the program, each scan will take a lot of time, so it is divided into two memory. Heap memory is controlled by code at the `C` level, mainly used for image memory, AI memory, LCD memory, and loading models into memory, etc.


The total size of `GC` memory can be set. Therefore, the size of `GC` memory can be modified appropriately according to the specific usage, for example:
* In order to load a larger model, you can set the `GC` memory setting smaller
* If the allocation of new variables indicates insufficient memory, you can appropriately set the `GC` memory to be larger
* If it is not enough, consider reducing the firmware size or optimizing the code

Example of setting `GC` memory size:

```python
from Maix import utils
import machine

print(utils.gc_heap_size())

utils.gc_heap_size(1024*1024) # 1MiB
machine.reset()
```

Note that the modification needs to be restarted to take effect

View memory allocation:

```python
import gc

print(gc.mem_free() / 1024) # stack mem

import Maix

print(Maix.utils.heap_free() / 1024) # heap mem

'''
>>>
raw REPL; CTRL-B to exit
>OK
352.0937
4,640.0
>
MicroPython v0.5.1-136-g039f72b6c-dirty on 2020-11-18; Sipeed_M1 with kendryte-k210
Type "help()" for more information.
>>>
'''
```
