# 快速上手

*本章节引导您完成 T256s 的初次上电与基本连接。更详细的功能说明请参考 [使用指南 (UG)](UG.md)。*

## 供电说明

T256s **不内置电池**。您可以采用以下任一方式供电：
- **直插手机**：直接插入手机底部 Type-C 接口（需手机支持 OTG 供电）。
- **外部供电**：通过 Type-C 公、母口连接充电宝、USB 适配器或电脑 USB 接口。

> [!IMPORTANT]
> **电源要求**：建议使用稳定的 5V 电源。若供电能力不足，可能会导致设备反复重启或屏幕闪烁。

## 单机巡检模式

在不连接手机或电脑的情况下，T256s 可作为一台独立的便携式热像仪使用。只需接入电源，即可开始巡检工作。

**启动流程**：
1. **上电开机**：通过 Type-C 母口接入电源，屏幕会立即点亮并显示开机 Logo。
2. **系统加载** (约 3-5 秒)：系统自动进行初始化，加载基础 UI 框架。
3. **传感器预热与校准** (约 5-10 秒)：**红外模组**完成初始化校准，屏幕开始实时显示温度分布图像。

![占位图](../../../zh/ThermalCam/T256s/assets/no-image-signal.jpg)

## UVC 联机模式

T256s 符合标准 UVC (USB Video Class) 协议。在主流操作系统（Windows、Linux、Android）下，设备会被识别为免驱摄像头，无需额外安装额外的驱动程序。

### Windows 连接
将 T256s 通过 USB 数据线连接至 PC。
- **设备识别**：打开“设备管理器”，在“照相机”或“图像设备”分类下，您会看到名为 "USB Camera" 或 "T256s Thermal Camera" 的设备。
- **画面预览**：可以使用 Windows 自带的“相机”应用，或者 OBS Studio、VLC、PotPlayer 等第三方软件。

![占位图](../../../zh/ThermalCam/T256s/assets/no-image-signal.jpg)

### Linux / Raspberry Pi 识别
在 Linux 环境下，T256s 通常映射为 `/dev/videoX` 设备。
- **推荐工具**：使用 `guvcview`、`cheese` 或 `ffmpeg` 进行测试。
- **日志验证**：插入设备后，在终端执行 `dmesg` 命令查看识别日志。

**识别日志示例（来自实际设备）**：
```text
[102310.868452] usb 1-7.4.2: new high-speed USB device number 35 using xhci_hcd
[102310.966974] usb 1-7.4.2: New USB device found, idVendor=359f, idProduct=ffff, bcdDevice= 4.19
[102310.966980] usb 1-7.4.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[102310.966982] usb 1-7.4.2: Product: Thermal Camera (UVC)
[102310.966983] usb 1-7.4.2: Manufacturer: Sipeed Ltd.
[102310.966985] usb 1-7.4.2: SerialNumber: 0123456789
[102310.991815] uvcvideo 1-7.4.2:1.0: Found UVC 1.00 device Thermal Camera (UVC) (359f:ffff)
[102310.998891] usb-storage 1-7.4.2:1.2: USB Mass Storage device detected
[102310.999030] scsi host8: usb-storage 1-7.4.2:1.2
[102312.036627] scsi 8:0:0:0: Direct-Access     Linux    File-Stor Gadget 0419 PQ: 0 ANSI: 2
[102312.036788] sd 8:0:0:0: Attached scsi generic sg1 type 0
[102312.036980] sd 8:0:0:0: Power-on or device reset occurred
[102312.037313] sd 8:0:0:0: [sdb] 65536 512-byte logical blocks: (33.6 MB/32.0 MiB)
[102312.145478] sd 8:0:0:0: [sdb] Write Protect is off
[102312.145485] sd 8:0:0:0: [sdb] Mode Sense: 0f 00 00 00
[102312.255625] sd 8:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[102312.495980]  sdb:
[102312.496065] sd 8:0:0:0: [sdb] Attached SCSI removable disk
[102313.464088] usb 1-7.4.2: USB disconnect, device number 35
[102313.493673] sd 8:0:0:0: [sdb] Synchronizing SCSI cache
[102313.493716] sd 8:0:0:0: [sdb] Synchronize Cache(10) failed: Result: hostbyte=DID_NO_CONNECT driverbyte=DRIVER_OK
[102315.740234] usb 1-7.4.2: new high-speed USB device number 36 using xhci_hcd
[102315.839493] usb 1-7.4.2: New USB device found, idVendor=359f, idProduct=ffff, bcdDevice= 4.19
[102315.839512] usb 1-7.4.2: New USB device strings: Mfr=1, Product=2, SerialNumber=3
[102315.839520] usb 1-7.4.2: Product: Thermal Camera (UVC)
[102315.839526] usb 1-7.4.2: Manufacturer: Sipeed Ltd.
[102315.839530] usb 1-7.4.2: SerialNumber: 0123456789
[102315.864161] uvcvideo 1-7.4.2:1.0: Found UVC 1.00 device Thermal Camera (UVC) (359f:ffff)
[102315.871660] usb-storage 1-7.4.2:1.2: USB Mass Storage device detected
[102315.871856] scsi host8: usb-storage 1-7.4.2:1.2
[102316.899524] scsi 8:0:0:0: Direct-Access     Linux    File-Stor Gadget 0419 PQ: 0 ANSI: 2
[102316.899837] sd 8:0:0:0: Attached scsi generic sg1 type 0
[102316.899962] sd 8:0:0:0: Power-on or device reset occurred
[102316.900374] sd 8:0:0:0: [sdb] 65536 512-byte logical blocks: (33.6 MB/32.0 MiB)
[102317.010049] sd 8:0:0:0: [sdb] Write Protect is off
[102317.010070] sd 8:0:0:0: [sdb] Mode Sense: 0f 00 00 00
[102317.120036] sd 8:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[102317.350047]  sdb:
[102317.350175] sd 8:0:0:0: [sdb] Attached SCSI removable disk
```

### Android 移动端使用
- **连接方式**：支持 OTG 功能的手机可直接插在底部接口。
- **配套软件**：推荐使用“USB摄像头 (USB Camera)”等支持 UVC 协议的应用程序。
- **操作步骤**：插入设备后，手机通常会弹出权限申请，点击“确定”即可预览热像画面。

![占位图](../../../zh/ThermalCam/T256s/assets/no-image-signal.jpg)

## 微距镜头安装

若需观察 PCB 元器件，请将随货附带的微距镜头片轻轻贴合在热像模组前端。
- **工作距离**：约 5cm。
- **效果**：可看清 0402 贴片电阻的发热情况。
