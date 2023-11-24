---
title: Maix-IV 系列 常见问题（FAQ）
---

## Q：更新到1.45版本号，根文件系统大小仅剩8G，如何扩容？

A：首次烧录会出现该现象，实际EMMC该分区大小已预先设置最大可用，请运行一次`resize2fs /dev/mmcblk0p10`更新文件系统元数据。之后应为28G：
```bash
root@maixbox:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        28G  6.0G   21G  23% /
```