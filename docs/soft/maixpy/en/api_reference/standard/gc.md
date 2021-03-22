---
title: gc-memory recovery
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: gc-memory recovery
---



This module implements a subset of the corresponding CPython module, as described below. For more information, please refer to the original CPython documentation: [gc](https://docs.python.org/3.5/library/gc.html#module-gc).

## Function

### gc.enable()

Enable automatic garbage collection.

### gc.disable()

Disable automatic garbage collection. Heap memory can still be allocated, and garbage collection can still be started manually using `gc.collect()`.

### gc.collect()

Run garbage collection.

### gc.mem_alloc()

Returns the number of bytes of heap RAM allocated.

#### Difference to CPython

This feature is a MicroPython extension.

### gc.mem_free()

Returns the number of bytes of available heap RAM, or -1 if the remaining amount of heap is unknown.

#### Difference with CPython

This feature is a MicroPython extension.

### gc.threshold([amount])

Set or query other GC allocation thresholds. Generally, the collection is triggered only when the new allocation cannot be met, that is, under out of memory (OOM) conditions. If you call this function, in addition to OOM, a set will be triggered every time a large number of bytes are allocated (in total, because so many bytes were allocated last time). The amount is usually specified as less than the full heap size, with the intention to trigger the collection before the heap is exhausted, and hope that the early collection can prevent excessive memory fragmentation. This is a heuristic measurement whose effect varies from application to application, as well as the optimal value of the measurement parameter.

Calling the function without parameters will return the current value of the threshold. A value of -1 indicates a disabled allocation threshold.

#### Difference with CPython

This function is a MicroPython extension. CPython has a similar function-`set_threshold()`, but due to different GC implementations, its signature and semantics are different.
