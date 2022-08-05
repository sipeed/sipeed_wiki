# 配置系统

配置系统我们需要将电脑与板子先连接上，然后使用[串口](https://baike.baidu.com/item/%E4%B8%B2%E8%A1%8C%E7%AB%AF%E5%8F%A3/7353286)来通信，接着可以正常操作板子了。

Lichee MaixSense 的引脚图如下:

![](./assets/R329-pin.jpg)

直接将电脑与上图中所示的板子上的 TTYS0 的口(默认在板子上DEBUG标识附近的口)相连就行，这样就已经完成了电脑与板子的连接。

为了能够正常通信，我们还需要安装 [CH340 驱动](https://dl.sipeed.com/fileList/MAIX/tools/ch340_ch341_driver/CH341SER.EXE)

## Tina系统配置

一般建议使用 armbian 系统，对于 Tina 系统还是经验丰富的用户来使用比较好。

Lichee MaixSense 的 Tina 系统配置和 [M2dock](./../M2/usage.md) 基本相同，这里不另作赘述。

- 可以使用串口连接上板子后再使用串口工具软件比如 [Mobaxterm](./../M2/tools/mobaxterm.md) 来操作板子
- 可以将板子上的摄像头拆下来后再将电脑与该接口相连然后使用 [adb](https://developer.android.google.cn/studio/releases/platform-tools?hl=zh-cn) 。工具来操作板子因为不推荐小白使用 Tina 系统所以不再深说

## armbian系统配置

根据本文开头描述来将电脑与板子连接且安装 [CH340 驱动](https://dl.sipeed.com/fileList/MAIX/tools/ch340_ch341_driver/CH341SER.EXE) 后，可以在串口软件比如 Xshell 或者 [Mobaxterm](./../M2/tools/mobaxterm.md)中，设置波特率 (baudrate) 为115200，选择板子的串口，连接上板子。

**如果自己的板子启动和下面的动图不一样那么直接进入基础使用就好了 [点我](./Usages.md)**





板子初始化结束后，可能需要输入登录密码，请多次尝试（配置完后直接 `passwd -d root` 就可以删除密码了）

> 烧录带有 MaixPy3 的镜像只需要输入账号密码登录即可，不需要进行系统配置
> 如果需要用户名和密码的话建议尝试 用户名：root 密码：root

```bash
New to Armbian? Documentation: https://docs.armbian.com Support: https://forum.armbian.com

New root password: **********
Repeat password: **********
```

然后设置默认 shell,一般选择 bash

```bash
Choose default system command shell:

1) bash
2) zsh

Shell: BASH
```

然后可以设置一个非 root 用户日常操作用

```bash
Creating a new user account. Press <Ctrl-C> to abort

Please provide a username (eg. your forename): ll
Create password: *********
Repeat password: *********
```

![2021080511-46-52](./assets/2021080511-46-52.gif)
