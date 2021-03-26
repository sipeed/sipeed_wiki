---
title: bsp内核中的保留内存
---

> **问？**
>
> bsp内核启动时，打印的内存信息发现有35M内存是保留的，这些内存是被谁使用了呢？

> **答！**
>
> 原来，其中的大头，28MB是被 ion 使用了，在menuconfig里的
> **CONFIG\_ION\_SUNXI** 中，有
> **CONFIG\_ION\_SUNXI\_RESERVE\_LIST**，默认保留了28M 内存给 *vfe, ve*
> 等。
