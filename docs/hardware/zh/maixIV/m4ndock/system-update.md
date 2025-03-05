**该页面介绍的烧录方法所使用的镜像包因体积过大，且下载站带宽有限故仅存储在百度企业网盘同级目录下，入口链接可见于下载站页面顶端区域。**

## 通过 TFCard 启动和烧录 eMMC

文件名格式为 `sdcard.img`。

下载地址为：[MaixIV/M4N-Dock/09_Image/TFCard&eMMC Images](https://pan.baidu.com/e/1-r6V352TIN8eqiFEIsUQoA)。

下载的文件如果尾缀是 `.xz`，请先进行解压操作。Linux 用户可使用 xz 工具，Windows 用户可使用 7-zip 等工具。

具体操作方法如下：

### 启动 Live 系统

#### 准备 TFCard 并烧录镜像

准备一张至少 8GB 的 TFCard，使用任意读卡器工具或电脑自带的卡槽进行读写。

注意：按以下操作，TFCard 内容将会全部丢失，如有重要数据请提前备份。

##### Linux 系统

使用 `dd` 将镜像文件写卡：

```sh
sudo dd if=sdcard.img of=/path/to/tfcard bs=4G conv=sparse,fsync status=progress
```

##### 或 Windows 系统

使用 `win32diskimager` 或 `balenaEtcher` 等写卡工具选择镜像文件 `sdcard.img` 进行烧写。

#### 使用烧录有镜像的 TFCard 启动 Live 系统

1. 将 TFCard 插入 M4N-Dock 尾部左下方的 TF 卡槽内。

2. 保持板卡正常上电，请使用 DC 进行供电。

3. 按住前端 Type-C 座子附近的 `BOOT` 按键不放，点按（按下再松开） `RST` 按键。

    3.1. （选做）如有外壳需要移除前面板，拧下 3 颗螺丝即可旋转打开。

-----------

执行完以上操作， Live 系统应已启动，可在 Type-C 串口里面看到系统启动的打印信息。

该 Live 系统具备功能完全，可直接体验使用。如有固化到 eMMC 来解放 TFCard 以作他用的需求，可续看下节。


### 在 Live 系统内烧录 eMMC

eMMC 的设备文件保持为 `/dev/mmcblk0`。

先提供两个方法烧录到板载的 eMMC 中，请根据条件进行二择：

#### 方法一：直接安装 Live 系统

1. 按上节说明成功启动 Live 系统，接着通过 Type-C 串口执行下列操作。

2. 使用 `dd` 将 TFCard 内的 Live 系统直接还原到 eMMC中，命令如下：

    ```sh
    dd if=/dev/mmcblk1 of=/dev/mmcblk0 bs=3M count=1 conv=fsync
    sync
    dd if=/dev/mmcblk1p1 of=/dev/mmcblk0p1 bs=64M conv=fsync
    dd if=/dev/mmcblk1p2 of=/dev/mmcblk0p2 bs=1G conv=sparse,fsync status=progress
    ```

3. 等待上述指令执行完后，即可取出 TFCard，后续可直接上电或点按 `RST` 正常启动 eMMC 内系统。

#### 方法二：Live 系统内烧录镜像

要求：能够访问和读写已烧录 Live 系统的 TFCard 格式为 `ext4` 的第二分区，如不清楚相关知识点，那么该方法暂时不适用，请采用更通用的方法一。

1. 拷贝镜像文件 `sdcard.img` 到第二分区（Live系统根目录）任意地方。

2. 参考 TFCard 烧录 Live 系统，执行以下命令：

    ```sh
    sudo dd if=/path/to/sdcard.img of=/dev/mmcblk0 bs=1G conv=sparse,fsync status=progress
    ```

3. 等待上述指令执行完后，即可取出 TFCard，后续可直接上电或点按 `RST` 正常启动 eMMC 内系统。


## 通过 AXDL 烧录

烧录文件名格式为 `xxx.axp`。

具体操作方法见首页资源汇总软件开发文档压缩包内`AXDL 工具使用指南.pdf`。

**提示：官方 EVB 板上 Download 按键对应 M4NDOCK 的 BOOT 按键**

AXDL软件（仅 Windows 可用）位于下载站`PC_Software`目录下。

**注意：USB 烧录口是位于靠近 `HDMI` 接口的以太网座子最下面贴近板子的那一个 `USB-A` 口。请准备`A-to-A`的数据线，或者电脑有 `Type-C` 口也可以直接使用 `A-to-C` 的数据线**

**注意：烧写时不要连接 `12V` 电源，仅使用 USB 烧写线供电即可，否则有烧毁 `PC` 的 `USB接口` 的风险**
