# 开箱使用

> 编辑于2022.06.15

## 准备系统存储介质

前面有一个章节已经介绍烧录镜像了，这里就不重复了。

## 焊接排针

使用的话就要焊接排针与电脑通信，然后进行相关操作会方便得多。

默认使用串口0来进行通信的，对应在板子上的 U0T R 引脚。

## 启动系统

把 TF 卡插进板子，然后连接好串口（gnd也连一下），打开串口工具。给板子上电。

我们就可以在串口终端里看到板子的打印信息了。

```bash
U-Boot SPL 2017.01-rc2-00073-gdd6e874-dirty (Nov 09 2021 - 06:26:31)
DRAM: 64 MiB
Trying to boot from MMC1

U-Boot 2017.01-rc2-00073-gdd6e874-dirty (Nov 09 2021 - 06:26:31 +0000) Allwinner Technology

CPU:   Allwinner V3s (SUN8I 1681)
Model: Lichee Pi Zero
DRAM:  64 MiB
```

接着就会到登陆选项

```bash
Welcome to licheepi
licheepi login: 
Password:
```

对于在前面使用的名为  Zero_pub_V0.3.gz 的镜像，用户名和密码分别是 `root` 和 `licheepi` 。
对于使用 debian 镜像的，用户名为 `root`，密码为 `toortoor` 。

要知道输密码的时候是没有输入回显的，所以不要问为什么输密码没有反应了

### 使用

对于 Zero_pub_V0.3.gz 镜像登陆进去后有如下文件:

```bash
licheepi# ls -l
total 18356
-rw-r--r--    1 root     root      13727311 Nov  9  2021 badapple.mp4
-rwxr--r--    1 root     root       2837888 Nov  9  2021 demo
-rwxr--r--    1 root     root         25318 Nov  9  2021 gpiod-1.5.0.tar.gz
-rwxr-xr-x    1 root     root       2187328 Nov  9  2021 maix_asr
-rw-r--r--    1 root     root            60 Nov  9  2021 readme
drwxr-xr-x    5 root     root          4096 Nov  9  2021 test_files
```

我们可以直接运行 demo 程序，然后在配套的 rgb 屏幕上看到图案。

```bash
licheepi# ./demo
The framebuffer device was opened successfully.
800x480, 32bpp
The framebuffer device was mapped to memory successfully.
```

从上面的信息可以看到之分辨率为 480\*800 的图形。因此要是在480\*272的屏幕中会显示不全

![](./../static/start/800_400_zero_lvgl_demo.png)

关于其他的使用会在后序章节中提到。