---
title: Maix-IV 系列 常见问题（FAQ）
---

## Q：如何确认自己系统使用的 SDK 的版本号？

A：使用命令 `cat /proc/ax_proc/version`，参考结果如下：
```bash
root@ax650:~# cat /proc/ax_proc/version
Ax_Version V1.45.0_P39_20240830020829
```

## Q：更新到 1.45.0_P39 版本，根文件系统大小不到 5G，如何扩容？

A：扩容前：
```bash
root@ax650:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       4.9G  4.3G  336M  93% /
```

扩容后：
```bash
root@ax650:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        15G  4.3G  9.6G  31% /
```

操作步骤：首先明确当前是 TFCard 启动还是 eMMC 启动，可通过命令 `grep -oP 'root=\K\S+' /proc/cmdline` 获取得到结果如下：
```bash
root@ax650:~# grep -oP 'root=\K\S+' /proc/cmdline
/dev/mmcblk1p2 # TFCard 启动
# /dev/mmcblk0p2 # 或 eMMC 启动
```
可得知当前文件系统位于 `/dev/mmcblk0` 或 `/dev/mmcblk1`，用于替换下面的 `/dev/mmcblkX` 后执行命令：
```bash
parted /dev/mmcblkX resizepart 2 100%
resize2fs /dev/mmcblkXp2
sync
```

## Q：更新到 1.45 版本，根文件系统大小仅剩 8G，如何扩容？

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