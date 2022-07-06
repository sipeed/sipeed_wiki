# 配置系统

## Tina系统配置

Lichee MaixSense 的 Tina 系统配置和 [M2dock](./../M2/usage.md) 基本相同，这里不另作赘述。

## armbian系统配置

R329 通过串口连接电脑启动终端。也可以通过 otg 外接 HID 设备直接在屏幕上启动控制台来进行操作。为了方便演示，这里以终端为例；

通过 typec 数据线连接 Lichee MaixSense 和电脑，这里使用 Xshell 新建会话框，选中新弹出 COM 端口号，波特率设置为115200，连接。

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
