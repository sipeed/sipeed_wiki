---
title: Maix.utils
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy doc: Maix.utils
---


## gc_heap_size([size])

Get or set the GC heap size, if the memory is not enough, you can consider setting it larger

### Parameters

None or pass in the new GC heap size.
* If there is no parameter, just get the heap size;
* If there are parameters, set the heap size, and then automatically restart

### return value

GC heap size

-Use case

```python
import Maix
# Maix.utils.gc_heap_size(0x80000) # The firmware default configuration is 500KB
Maix.utils.gc_heap_size(0x96000) # 600KB
```

## flash_read(flash_offset, size)

Read data of size specified size (number of bytes) from internal flash

### Parameters

flash_offset: flash address offset

flash_offset: flash address offset

## heap_free()

```shell
>>> Maix.utils.gc_heap_size()
524288
>>> Maix.utils.heap_free()
4374528
```


-----

The script test conditions in the article are:

-MaixDock
-MaixPy v0.5.0_246 (standard firmware)
