# 接入树莓派 5 加速运行大模型

树莓派 5 运行 QWen3-0.6B。
<video controls autoplay src="../assets/m4nhat/axcl-run-llm-on-raspi5-2025-07-03-4xspeedup.mp4" type="video/mp4"> Your browser does not support video playback. </video>

> 1.参考 [System Flashing Guide](https://wiki.sipeed.com/hardware/zh/maixIV/m4n/system-update.html) 使用 AXDL 烧录 [AX650_card_V3.6.2_20250603154858_20250626183000.axp](https://dl.sipeed.com/MaixIV/M4N-Dock/09_Image/)。


> 2.然后排线连接 M4N-Hat 和 树莓派 5，固定安装。上电进入树莓派的系统。
可以使用 lspci 命令检查加速卡是否正确被识别：
```bash
# 应能看到以下输出
sipeed@raspberrypi:~$ lspci
0001:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 21)
0001:01:00.0 Multimedia video controller: Axera Semiconductor Co., Ltd Device 0650 (rev01)
0002:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 21)
0002:01:00.0 Ethernet controller: Raspberry Pi Ltd RP1 PCIe 2.0 South Bridge
```

若不显示前两行信息，很有可能是该 pciex1 并未启用，请如下操作

`sudo raspi-config -> 6 Advanced Options -> A8 PCIe Speed -> Yes`

以使能 pciex1 gen3。或检查 `/boot/firmware/config.txt` 中的内容(末尾)是否包含

```bash
[all]
dtparam=pciex1_gen=3
```

实际上这个 `config.txt` 在 SD 卡的 boot 分区下，因此可在树莓派关机后取出用读卡器插在 PC 上修改。
注意：刚烧录树莓派镜像的卡目录没这个 /boot/firmware 目录，需要插入树莓派完整启动一次。


> 3.再进行驱动的安装，`axcl_host_aarch64_V3.6.2_20250603154858_NO4873.deb` 同样位于先前的下载目录。
将 aarch64 deb 包复制到树莓派开发板上，运行安装命令：
```bash
$ sudo apt install axcl_host_aarch64_V3.6.2_20250603154858_NO4873.deb
```

断电重启树莓派。
在正确安装AXCL驱动包后，AXCL-SMI即安装成功，直接执行 `axcl-smi` 显示内容如下：
```bash
sipeed@raspberrypi:~$ axcl-smi
+------------------------------------------------------------------------------------------------+
| AXCL-SMI  V3.6.2_20250603154858                                  Driver  V3.6.2_20250603154858 |
+-----------------------------------------+--------------+---------------------------------------+
| Card  Name                     Firmware | Bus-Id       |                          Memory-Usage |
| Fan   Temp                Pwr:Usage/Cap | CPU      NPU |                             CMM-Usage |
|=========================================+==============+=======================================|
|    0  AX650N                     V3.6.2 | 0001:01:00.0 |                148 MiB /      945 MiB |
|   --   55C                      -- / -- | 0%        0% |                 18 MiB /     7040 MiB |
+-----------------------------------------+--------------+---------------------------------------+

+------------------------------------------------------------------------------------------------+
| Processes:                                                                                     |
| Card      PID  Process Name                                                   NPU Memory Usage |
|================================================================================================|
sipeed@raspberrypi:~$
```

> 4.测试一下 `axcl_run_model`，推理 yolov5s 的性能与 M4N 原生系统上的数据极度接近。

```bash
sipeed@raspberrypi:~$ axcl_run_model -m yolov5s.axmodel
   Run AxModel:
         model: yolov5s.axmodel
          type: 1 Core
          vnpu: Disable
        warmup: 1
        repeat: 1
         batch: { auto: 1 }
    axclrt ver: 1.0.0
   pulsar2 ver: 1.2-patch2 7e6b2b5f
      tool ver: 0.0.1
      cmm size: 12730188 Bytes
  ------------------------------------------------------
  min =   7.837 ms   max =   7.837 ms   avg =   7.837 ms
  ------------------------------------------------------
```
**其余详细信息可查看[axcl官方文档](https://axcl-docs.readthedocs.io/zh-cn/latest/doc_guide_axcl_smi.html#)。**

> 5.再之后可以参考介绍过的 [大模型仓库](https://wiki.sipeed.com/hardware/zh/maixIV/m4n/axmodel-deploy.html) 在树莓派上部署运行各种已上传的大模型。

---
> 注意：
> 另有一已知 BUG，因为当前板卡不能满足树莓派的启动过程中关于 pciex1 的复位时序，所以在第一次挂载成功后保持不断电重启树莓派，会导致下一次树莓派无法挂载 M4N-Hat。因此只有断电后，再冷启动才能成功挂载 M4N-Hat。
> 当然现有一更简便方法。我们把树莓派的一个 GPIO 连到了 M4N-Hat 的复位引脚上，因此只需要在不断电重启树莓派前，执行命令 `gpioset gpiochip0 28=0` 让 M4N-Hat 先进入复位状态后，再正常重启树莓派即可恢复正常挂载。