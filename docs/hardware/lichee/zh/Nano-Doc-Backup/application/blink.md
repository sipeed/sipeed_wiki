一起来点灯
==========

本文描述点灯的一种简易方法；

查询原理图可知，底板上的RGB LED灯，分别连接到：

> -   红 --\> PE6
> -   蓝 --\> PE5
> -   绿 --\> PE4

查询 User manual 并计算可知：

> -   端口 PE 的数据寄存器为 0x01C208a0
> -   端口 PE 的控制寄存器为 0x01C20890

依此，借助devmem工具 可编写点灯脚本：

``` {.sourceCode .bash}
#! /bin/bash

# ------------------ Some declare ----------------------------
# 0x01C20890 ---> Pin control regesistor for Port E
# 0x01C208a0 ---> Data regesister for Port E

# devmem 0x01C20890 32 0x71117655 ---> 0x7???7655    红  蓝  绿 ---> PE6 PE5 PE4
# 本处操作的是 控制寄存器来控制开关，可改为 操作数据寄存器 控制LED开关
# ----------------- End of declare ---------------------------

devmem 0x01C208a0 32 0x00000004

trap 'onCtrlC' INT                              # 退出时的控制台输出
function onCtrlC () {
    devmem 0x01C208a0 32 0x00000074
    echo ' '
    echo 'Blink will at the end'
    exit 
}

sleep 0.5

devmem 0x01C20890 32 0x77777655                # 关闭各端口

while true                                     # 跑马灯开启
do
    devmem 0x01C20890 32 0x71177655
    sleep 0.5
    devmem 0x01C20890 32 0x77117655
    sleep 0.5
    devmem 0x01C20890 32 0x71717655
    sleep 0.5
    devmem 0x01C20890 32 0x71177655
    sleep 0.5
    devmem 0x01C20890 32 0x71717655
    sleep 0.5
    devmem 0x01C20890 32 0x77117655
    sleep 0.5
done 
```

> **交流与答疑**
>
> 欢迎到 [模组使用交流帖](http://bbs.lichee.pro/d/24--) 提问或分享经验。
