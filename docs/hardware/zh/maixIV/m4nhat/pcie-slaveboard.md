# 树莓派 5 安装 M4N-Hat

## 最终结果演示
树莓派 5 安装后，演示运行大模型 QWen3，性能达 13.2 tokens/s。见以下视频：
<video controls autoplay src="../assets/m4nhat/axcl-run-llm-on-raspi5-2025-07-03-4xspeedup.mp4" type="video/mp4"> Your browser does not support video playback. </video>
视频中完整演示了：
1. 下载已支持的大语言模型 QWen3-0.6B
2. 准备 python-venv 环境，安装所需 python 库
3. 运行 QWen3 并完成两次问答

## 安装
<div style="display: flex; justify-content: space-between;">
  <img src="../assets/m4nhat/DSC07559.JPG" style="width: 48%;">
  <img src="../assets/m4nhat/DSC07561.JPG" style="width: 48%;">
</div>

![](../assets/m4nhat/DSC07569.JPG)

## M4N 烧录从机系统
1.参考 [System Flashing Guide](../m4n/system-update.html) 使用 AXDL 烧录 [AX650_card_V3.6.2_20250603154858_20250626183000.axp](https://dl.sipeed.com/MaixIV/M4N-Dock/09_Image/)。

2.然后 fpc 排线连接 M4N-Hat 和 树莓派 5 的 pcie 座子，并确认固定完毕。

3.上电进入树莓派的系统。使用 lspci 命令检查加速卡是否正确被识别：
```bash
# 应能看到以下输出
sipeed@raspberrypi:~$ lspci
0001:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 21)
0001:01:00.0 Multimedia video controller: Axera Semiconductor Co., Ltd Device 0650 (rev01)
0002:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 21)
0002:01:00.0 Ethernet controller: Raspberry Pi Ltd RP1 PCIe 2.0 South Bridge
```

其中前两行信息则表示树莓派的 pcie 初始化成功，并识别挂载了 `Multimedia video controller: Axera Semiconductor Co., Ltd Device 0650 (rev01)`。

3.1. 若不显示如上前两行信息，很有可能是树莓派的该 pciex1 端口并未启用（默认行为），因此需要额外以下操作：

执行 `sudo raspi-config` 并进入 `6 Advanced Options -> A8 PCIe Speed`，选择 `Yes` 以使能 pciex1 gen3。
或检查 `/boot/firmware/config.txt` 中的内容（文件末尾）是否包含以下字段：
```bash
[all]
dtparam=pciex1_gen=3
```
实际上这个 `config.txt` 文件所在 SD 卡的 boot 分区为 FAT32 格式，因此可被广大操作系统识别和读写。可在树莓派关机后取出，并通过读卡器插在 PC 上直接修改。
> 注意：刚烧录树莓派镜像的新卡不存在这个 /boot/firmware 目录，此时需要插入树莓派完整启动一次才会生成上文所描述的结构。


## Raspi 5 安装 AXCL 软件包
pcie 可以正常识别到 M4N-Hat 后，还需要继续安装 AXCL 软件包以提供支持，才能通过 M4N-Hat 加速运行模型。
该软件包 `axcl_host_aarch64_V3.6.2_20250603154858_NO4873.deb` 与先前的 M4N 系统镜像 xx.axp 位于下载站同一目录。
下载到树莓派开发板上，然后运行安装命令：
```bash
$ sudo apt install axcl_host_aarch64_V3.6.2_20250603154858_NO4873.deb
```

安装成功后，断电重启树莓派。
此时运行 `axcl-smi` 显示内容如下，即代表安装成功：
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


## 测试 AXCL 模型推理能力
测试一下 `axcl_run_model` （与原生系统内 ax_run_model 同样使用方法），推理 yolov5s 的性能与 M4N 原生系统上的数据极度接近。


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

其余常用模型的性能实测数据如下表：

| Model         | Input Size | Batch 1 (IPS) | Batch 8 (IPS) |
|---------------|------------|---------------|---------------|
| Inceptionv1   | 224        | 1073          | 2494          |
| Inceptionv3   | 224        | 478           | 702           |
| MobileNetv1   | 224        | 1508          | 4854          |
| MobileNetv2   | 224        | 1366          | 5073          |
| ResNet18      | 224        | 1066          | 2254          |
| ResNet50      | 224        | 576           | 1045          |
| SqueezeNet11  | 224        | 1560          | 5961          |
| Swin-T        | 224        | 342           | 507           |
| ViT-B/16      | 224        | 162           | 207           |
| YOLOv5s       | 640        | 326           | 394           |
| YOLOv6s       | 640        | 282           | 322           |
| YOLOv8s       | 640        | 248           | 279           |
| YOLOv9s       | 640        | 237           | -             |
| YOLOv10s      | 640        | 298           | -             |
| YOLOv11n      | 640        | 860           | -             |
| YOLOv11s      | 640        | 305           | -             |
| YOLOv11m      | 640        | 114           | -             |
| YOLOv11l      | 640        | 87            | -             |
| YOLOv11x      | 640        | 41            | -             |


## AXCL 更详细使用说明
**其余详细信息可查看 [axcl官方文档](https://axcl-docs.readthedocs.io)。**

**另有 [树莓派5 AXCL专项页面](https://axcl-pi5-examples-cn.readthedocs.io)。**

可于 [文中](../m4n/axmodel-deploy.html) 介绍到的大模型仓库下载各种已被支持的大模型，并在树莓派上部署运行。

## 已知问题

### 不断电重启树莓派会导致 M4N-Hat 无法再次挂载
> 注意：
> 目前有一已知问题，因为当前板卡不能满足树莓派的启动过程中关于 pciex1 的复位时序，所以只有断电后再冷启动才能成功挂载 M4N-Hat。而在挂载成功后若是保持不断电来重启树莓派，会导致下一次树莓派无法挂载 M4N-Hat。因此每次都需要断电后再冷启动树莓派。

若是直接重启了树莓派，树莓派串口应会打印如下启动日志。其中第 18 行显示 `1000110000.pcie: link down`，表示 pcie 建立链接失败，显然此时未能成功挂载 M4N-Hat。
```bash
  7.11 fs_open: 'armstub8-2712.bin'
  7.15 Loading 'kernel_2712.img' to 0x00000000 offset 0x200000
  7.33 Read kernel_2712.img bytes  9727677 hnd 0x3c43
  9.93 PCI1 reset
  9.03 PCI2 reset
  9.13 set_reboot_order 0
  9.13 set_reboot_arg1 0
  9.14 USB-OTG disconnect
  9.56 MESS:00:00:09.256590:0: Starting OS 9256 ms
  9.62 MESS:00:00:09.262115:0: 00000040: -> 00000480
  9.63 MESS:00:00:09.263966:0: 00000030: -> 00100080
  9.68 MESS:00:00:09.268679:0: 00000034: -> 00100080
  9.73 MESS:00:00:09.273392:0: 00000038: -> 00100080
  9.78 MESS:00:00:09.278105:0: 0000003c: -> 00100080

NOTICE:  BL31: v2.6(release):v2.6-240-gfc45bc492
NOTICE:  BL31: Built : 12:55:13, Dec  4 2024
[    0.695249] brcm-pcie 1000110000.pcie: link down

Debian GNU/Linux 12 raspberrypi ttyAMA10

My IP address is 192.168.10.176 fdae:b0ae:ebf1:0:b270:135e:b646:70c3

raspberrypi login:
```

> 当然现有一更简便方法。我们把树莓派的一个 GPIO 连到了 M4N-Hat 的复位引脚上，因此若需要保持不断电也能重启树莓派并能成功挂载。需要在每次重启前先执行命令 `gpioset gpiochip0 28=0` 让 M4N-Hat 进入复位状态，再正常执行树莓派重启命令即可再次正常挂载。