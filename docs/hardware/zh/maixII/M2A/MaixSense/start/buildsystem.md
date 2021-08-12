# 配置系统

## Tina系统配置

Lichee MaixSense的Tina系统配置和M2dock基本相同，这里不另作赘述。

## armbian系统配置

R329可以通过otg外接HID设备直接在屏幕上启动控制台进行操作，也可以通过常用的串口启动控制台。为了方便演示，这里以控制台为例；

通过typec数据线连接Lichee MaixSense和电脑，使用Xshell新建会话框，选中新弹出COM，波特率设置115200，连接。
第一次启动大概需要10min时间初始化系统，请耐心等待；

![image-20210805140544186](./../assets/image-20210805140544186.png)

初始化结束后，需要输入登录密码，密码复杂度要求较高，请多次尝试

```
New to Armbian? Documentation: https://docs.armbian.com Support: https://forum.armbian.com

New root password: **********
Repeat password: **********
```

然后设置默认shell,一般选择bash

```
Choose default system command shell:

1) bash
2) zsh

Shell: BASH
```

然后可以设置一个非root用户日常操作用

```
Creating a new user account. Press <Ctrl-C> to abort

Please provide a username (eg. your forename): ll
Create password: *********
Repeat password: *********
```

![2021080511-46-52](./../assets/2021080511-46-52.gif)

