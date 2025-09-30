---
title: MaixCAM2 ISP Tuning
---

## Can I tune the ISP myself if I want a specific image style?

In theory, yes, but it’s quite complicated.
This article will not go into detail for now, but just provides you with the possibility. If you’re not prepared to hit some roadblocks, you can assume it’s not supported.
That said, you’re welcome to try, share your experiences, and contribute to this document.

## Brief overview of ISP tuning

Simply put, the ISP loads configuration files and reads parameters at runtime (you can see many configuration files under `/opt/etc/` in the system, such as `sc850sl_hdr_4lane_sipeed_0716.bin`).
We can use the chip vendor’s ISP tuning tool to connect to the development board for tuning. Once finished, you’ll get a configuration file that can replace the original one.

The official chip documentation and tools are available on the [download site](https://dl.sipeed.com/shareURL/MaixCAM/MaixCAM2/Software/Tools). Just download, read, and use them.
