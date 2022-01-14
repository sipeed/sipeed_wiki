# Lichee RV 系统烧录

系统镜像分为 Tina与Debian两种，Tina为专用小linux镜像，Debian为桌面级镜像

## 准备

1. Lichee RV 核心板
2. TF 内存卡（建议使用官方店上的内存卡，别的卡可能存在烧录失败和烧录之后不能启动的问题）
3. 烧录工具 [PhoenixCard](https://dl.sipeed.com/shareURL/LICHEE/D1/Lichee_RV/tool)
4. 系统镜像
    [Tina](https://dl.sipeed.com/shareURL/LICHEE/D1/Lichee_RV/SDK/image) 系统镜像或者 Debian 系统镜像(链接：https://pan.baidu.com/s/1QJTaDw6kkTM4c_GAlmG0hg 提取码：wbef)
    国外用户：<https://mega.nz/folder/lx4CyZBA#PiFhY7oSVQ3gp2ZZ_AnwYA>

| 镜像词缀说明 | 含义 | 备注 |
| --- | --- | --- |
| LicheeRV | Sipeed 专用的 RISCV D1 Linux 系列系统。 | --- |
| Tina | 标记为 tina openwrt 系统。 | --- |
| debian | 标记为 riscv debian 系统。 | --- |
| 86panel | [taobao 86panel](https://item.taobao.com/item.htm?spm=a230r.1.14.18.30b534187YMsRx&id=663345415205&ns=1&abbucket=7#detail) | --- |
| dock | [taobao dock](https://item.taobao.com/item.htm?spm=a1z10.3-c-s.w4002-21410578028.20.35765d54K9XCOt&id=666274331852) | --- |
| hdmi | 表示屏幕默认输出到 HDMI 屏幕上。 |  |
| 800480 / 480P | 表示屏幕默认输出到 LCD 屏幕上，分辨率可以是 800*480 或 480P (640X480)。 |  |
| 8723ds | 表示该镜像支持 8723ds WIFI / BLE 驱动。 |  |
| xr829 | 表示该镜像支持 xr829 WIFI / BLE 驱动。 |  |
| waft | 是否内置 waft 软件。 |  |


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
