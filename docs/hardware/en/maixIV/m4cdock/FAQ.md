---
title: Maix-IV Series Frequently Asked Questions (FAQ)
---

## Q: How to check the SDK version of the current system?

A: Run the command `cat /proc/ax_proc/version`. Example output:
```bash
root@ax650:~# cat /proc/ax_proc/version
Ax_Version V1.45.0_P39_20240830020829
```

## Q: After updating to v1.45.0_P39, the root filesystem is smaller than 5GB. How to expand it?

A: Before expansion:
```bash
root@ax650:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root       4.9G  4.3G  336M  93% /
```

After expansion:
```bash
root@ax650:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        15G  4.3G  9.6G  31% /
```

Steps:
1. Identify whether the system boots from TFCard or eMMC:
    ```bash
    root@ax650:~# grep -oP 'root=\K\S+' /proc/cmdline
    /dev/mmcblk1p2 # TFCard 启动
    # /dev/mmcblk0p2 # 或 eMMC 启动
    ```
2. Replace `/dev/mmcblkX` in the following commands with the detected device (e.g., `/dev/mmcblk0` or `/dev/mmcblk1`), then execute:
    ```bash
    parted /dev/mmcblkX resizepart 2 100%
    resize2fs /dev/mmcblkXp2
    fsck -y /dev/mmcblkXp2
    sync
    ```

Q: After updating to v1.45, the root filesystem only shows 8GB. How to fix this?

A: This occurs when booting after the first flash. The eMMC partition is pre-configured for maximum capacity. Run the following to update filesystem metadata (post-expansion size should be 28GB):

```bash
resize2fs /dev/mmcblk0p10  
fsck -y /dev/mmcblkXp10
sync  # Critical! Prevents boot failure after power cycle.  
```

Expected result:
```bash
root@maixbox:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        28G  6.0G   21G  23% /
```
Warning: Always run `sync` before rebooting/power-off to avoid system corruption.

## Q: How to resolve network conflicts caused by duplicate MAC addresses?

A: Permanently modify MAC addresses via U-Boot environment variables:
```bash
# 例如
setenv ethaddr d0:00:00:00:00:01
setenv eth1addr d0:00:00:00:00:02
saveenv
```

## Key Notes:

- For eMMC operations, ensure sync is executed to prevent data loss.

- MAC address changes require saveenv to persist across reboots.

- Refer to official docs for advanced partitioning scenarios.