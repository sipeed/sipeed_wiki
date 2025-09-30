---
title: MaixCAM2 FAQ (Frequently Asked Questions)
---

**If you can't find your problem below, you can also refer to [MaixPy FAQ](https://wiki.sipeed.com/maixpy/doc/zh/faq.html).**


## The product comes with a case, but I don’t need the case, screen, or camera. Can these be removed for mass production?

Yes.
The included case, screen, and camera are mainly for quick product and idea validation. For actual mass production, you can contact **Sipeed** ([support@sipeed.com](mailto:support@sipeed.com) or through the online store) to customize and remove certain components. Larger orders will receive better support.

In addition, a **core board version** is also available. If you have PCB design capabilities, you can directly purchase the core board and design your own baseboard.


## Why does the 4GB RAM version show only 2GB in the system?

The hardware has **4GB RAM**, but the memory is divided into **user space memory** and **system reserved memory**.
In a **Linux** system, the memory you see with the `free` command is the **user space memory**.
A large portion of the system reserved memory is allocated as **dedicated hardware memory**, for example for **model inference**, **camera**, **display**, etc.

You can adjust the allocation ratio by modifying the value of `maix_memory_cmm=-1` in the `/boot/configs` file.

* `-1` is the default value.
* For example, if you change it to `3072` (no unit needed, the default unit is **MiB**), then **3072 MiB** will be reserved for models and other hardware usage, and the rest will be available for the **Linux system**.

**A reboot is required for changes to take effect.**

For more details, please refer to [MaixPy Memory Usage Guide](https://wiki.sipeed.com/maixpy/doc/en/pro/memory.html).


