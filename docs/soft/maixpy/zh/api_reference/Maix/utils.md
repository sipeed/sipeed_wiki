---
title: Maix.utils
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: Maix.utils
---


## gc_heap_size([size])

获取或者设置 GC 堆大小，如果报内存不够时可以考虑设置大一点

### 参数

无 或者 传入新的 GC 堆大小.
* 如果没有参数就只是获取堆大小；
* 如果有参数则设置堆大小，然后会自动重启

### 返回值

GC 堆大小

- 使用实例

```python
import Maix
# Maix.utils.gc_heap_size(0x80000) # 固件默认配置为 500KB
Maix.utils.gc_heap_size(0x96000) # 600KB
```

## flash_read(flash_offset, size)

从内部 flash 读取 size 指定大小(字节数) 数据

### 参数

flash_offset: flash 地址偏移

flash_offset: flash 地址偏移

## heap_free()

```shell
>>> Maix.utils.gc_heap_size()
524288
>>> Maix.utils.heap_free()
4374528
```


-----

文章中脚本测试条件为:

- MaixDock
- MaixPy v0.5.0_246(标准版固件)
