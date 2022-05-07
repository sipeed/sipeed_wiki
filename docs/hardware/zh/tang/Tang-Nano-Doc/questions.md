---
title: Note
---

> 编辑于2022.05.07

这里汇总一些常见问题，持续更新

## Programmer 相关

首先确定设备管理器里面有两个converter，在进行下面的操作

![](./../assets/questions/converter.png)

### 下载失败

对于Programmer(下载程序)建议使用 
https://dl.sipeed.com/shareURL/TANG/programmer 里面的文件。
下载后解压替换掉Gowin对应安装目录的Programmer文件夹即可。
不会替换的话可以在下载解压后的Programmer程序中手动添加对应下载文件来进行烧录。

### ID code mismatch

这种情况是工程芯片与下载芯片不一致。

重新检查工程中的芯片型号（比如工程设置、引脚约束、各个IP中的型号），与板子上的芯片丝印对应上。

### No Gowin devices found

这种情况可以和上面的 下载失败 里面的内容一样先替换 Programmer 文件夹。

## IDE 使用相关

### 使用GAO

目前测试过IDE v1.9.8.1和之前的版本可使用。其他新版的不行