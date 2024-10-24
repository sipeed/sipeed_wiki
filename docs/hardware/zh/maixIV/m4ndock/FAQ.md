---
title: Maix-IV 系列 常见问题（FAQ）
---

## Q：更新到1.45版本号，根文件系统大小仅剩8G，如何扩容？

A：首次烧录会出现该现象，实际EMMC该分区大小已预先设置最大可用，请运行一次`resize2fs /dev/mmcblk0p10`更新文件系统元数据。之后应为28G：执行完记得`sync`再断电或重启设备否则会造成不开机**（切记！！！切记！！！）**。
```bash
root@maixbox:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        28G  6.0G   21G  23% /
```

## Q：MAC物理地址重复，导致同一局域网下无法正常连接网络，如何解决？

A：可通过进入`uboot`命令行模式设置环境变量`ethaddr`和`eth1addr`并保存，可永久修改对应网卡的mac地址：
```bash
# 例如
setenv ethaddr d0:00:00:00:00:01
setenv eth1addr d0:00:00:00:00:02
saveenv
```