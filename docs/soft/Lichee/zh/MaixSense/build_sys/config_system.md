# 配置系统

## Tina系统配置

Lichee MaixSense 的 Tina 系统配置和 M2dock 基本相同，这里不另作赘述。

## armbian系统配置

R329 可以通过 otg 外接 HID 设备直接在屏幕上启动控制台进行操作，也可以通过常用的串口启动控制台。为了方便演示，这里以控制台为例；

通过 typec 数据线连接 Lichee MaixSense 和电脑，使用 Xshell 新建会话框，选中新弹出 COM，波特率设置115200，连接。


初始化结束后，需要输入登录密码，密码复杂度要求较高，请多次尝试（配置完后直接 `passwd -d root` 就可以删除密码了。）

> 目前公开带有 MaixPy3 名称 armbian 镜像输入 root 即可登录，不需要进行密码设置！

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

![2021080511-46-52](./../assets/2021080511-46-52.gif)
