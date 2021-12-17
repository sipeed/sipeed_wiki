# Lichee RV 系统烧录

系统镜像分为 Tina与Debian两种，Tina为专用小linux镜像，Debian为桌面级镜像

## 准备

1. Lichee RV 核心板
2. TF 内存卡（建议使用官方店上的内存卡，别的卡可能存在烧录失败和烧录之后不能启动的问题）
3. 烧录工具 [PhoenixCard](https://dl.sipeed.com/shareURL/LICHEE/D1/Lichee_RV/tool)
4. 系统镜像
    [Tina](https://dl.sipeed.com/shareURL/LICHEE/D1/Lichee_RV/SDK/image) 系统镜像或者 Debian 系统镜像(链接：https://pan.baidu.com/s/1QJTaDw6kkTM4c_GAlmG0hg 提取码：wbef)

| 镜像名 | 含义 | 备注 |
| --- | --- | --- |
| LicheeRV_Tina_86_waft.img | 在 LicheeRV 上运行 Tina 系统，支持 LicheeRV 86 底板，内置 waft 软件 | --- |
| LicheeRV_Tina_86_480p.img | 在 LicheeRV 上运行 Tina 系统，支持 86 底板，支持480p分辨率的屏幕 | --- |
| LicheeRV_Tina_86_800480.img |  在 LicheeRV 上运行 Tina 系统，支持 LicheeRV Dock 底板，分辨率为 800 * 480 | --- |
| LicheeRV_Debian_hdmi.img | 在 LicheeRV 上运行 Debian 系统，支持 LicheeRV Dock 底板，支持 HDMI 接口 | --- |
| LicheeRV_Debian_86_480p.img | 在 LicheeRV 上运行 Debian 系统，支持 LicheeRV 86 底板，支持 480p 分辨率 | --- |



## 烧录镜像

打开烧录软件 PhoenixCard，选择烧录的固件，将内存卡通过读卡器插入电脑中

![](./../assets/RV/flash.png)

> 并不能保证每台电脑和每个人的内存卡都是可以烧录的，推荐烧录失败的时候直接购买官方的镜像卡。（全志的）

等待烧录结束，烧录 Tina 系统镜像会比较快，但是烧录 Debian 系统镜像是将会长一些，可能需要10多分钟。

## 启动
插卡启动，可以在串口工具中查看到启动信息

```shell
BusyBox v1.27.2 () built-in shell (ash)

    __  ___     _        __   _   
   /  |/  /__ _(_)_ __  / /  (_)__  __ ____ __
  / /|_/ / _ `/ /\ \ / / /__/ / _ \/ // /\ \ /
 /_/  /_/\_,_/_//_\_\ /____/_/_//_/\_,_//_\_\ 
 ----------------------------------------------
 Maix Linux (Neptune, 5C1C9C53)
 ----------------------------------------------
```

TIPS：
如果在烧录时提示格式化失败，或者烧过卡之后电脑上没有了盘符，可以按以下操作恢复执行：

1. 在此下载磁盘处理软件： https://www.diskgenius.cn/
2. 电脑上显示不出的盘符，会在该软件里显示出来，使用该软件进行快速分区：
    ![attachmentId-2788](https://bbs.sipeed.com/storage/attachments/2021/12/17/K9SdDOalmpgIwFopjoUU7sV2zgp26E1d85EMwgXf.png)
3. 分区完成后，电脑上就能够看到盘符，PhoenixCard 里也能看到，在 PhoenixCard 里点击恢复卡即可恢复卡到正常状态
4. 按之前步骤继续烧录即可

> Tina 系统登录用户名：root  密码：tina
> Debian 系统登录用户名：sipeed 密码：licheepi