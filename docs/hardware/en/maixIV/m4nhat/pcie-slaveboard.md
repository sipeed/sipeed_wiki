# Installing M4N-Hat on Raspberry Pi 5

## Final Demo

After installation on Raspberry Pi 5, running the large language model QWen3 achieves 13.2 tokens/s (performance for smaller models is limited by PCIe link bandwidth, showing a gap compared to the standalone board's 19 tokens/s). Watch the demo video:

<video controls autoplay src="../../../zh/maixIV/assets/m4nhat/axcl-run-llm-on-raspi5-2025-07-03-4xspeedup.mp4" type="video/mp4"> Your browser does not support video playback. </video>

The video demonstrates:

1. Downloading the pre-supported QWen3-0.6B model

2. Setting up a Python virtual environment and installing required libraries

3. Running QWen3 and completing two Q&A sessions

## Installation

<div style="display: flex; justify-content: space-between;">
  <img src="../../../zh/maixIV/assets/m4nhat/DSC07559.JPG" style="width: 48%;">
  <img src="../../../zh/maixIV/assets/m4nhat/DSC07561.JPG" style="width: 48%;">
</div>

![](../../../zh/maixIV/assets/m4nhat/DSC07569.JPG)

## Flashing the M4N Slave System

1. Refer to the [System Flashing Guide](../m4n/system-update.html) and use AXDL to flash [AX650_card_V3.6.2_20250603154858_xxx.axp](https://dl.sipeed.com/MaixIV/M4N-Dock/09_Image/)。

2. Connect the M4N-Hat to the Raspberry Pi 5's PCIe slot using an FPC cable and secure it.

3. Power on the Raspberry Pi. Verify the accelerator card is detected with `lspci`:
  ```bash
  # 应能看到以下输出
  sipeed@raspberrypi:~$ lspci
  0001:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 21)
  0001:01:00.0 Multimedia video controller: Axera Semiconductor Co., Ltd Device 0650 (rev01)
  0002:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 21)
  0002:01:00.0 Ethernet controller: Raspberry Pi Ltd RP1 PCIe 2.0 South Bridge
  ```

The first two lines confirm PCIe initialization and detection of the Axera AX650 controller. ANd the `Multimedia video controller: Axera Semiconductor Co., Ltd Device 0650 (rev01)` has been mounted correctly.

**Troubleshooting PCIe Detection**
If the above output is missing, the PCIe x1 port may be disabled (default). Enable it via:
- Run `sudo raspi-config → 6 Advanced Options → A8 PCIe Speed → Select Yes` for PCIe x1 Gen3.

- or Manually add contents below to `/boot/firmware/config.txt`:
  ```bash
  [all]
  dtparam=pciex1_gen=3
  ```

  Actually the `config.txt` file is located in the FAT32 type partition, so you can modify it after mount it on your PC directly.

  > Note: Newly flashed Raspberry Pi SD cards lack the /boot/firmware directory. Boot once to generate it.

## Installing AXCL Software on Raspberry Pi 5

After PCIe detection, install the AXCL package for model acceleration:

```bash
$ sudo apt install axcl_host_aarch64_V3.6.2_20250603154858_NO4873.deb
```

Reboot the Pi. Verify installation with `axcl-smi`:

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


## Testing AXCL Model Inference

Run `axcl_run_model` (usage mirrors native ax_run_model). Example with YOLOv5s (single-core model; full-core performance scales ~3x):


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

Performance Benchmarks Table：

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


## AXCL Advanced Usage

- [AXCL Documentation](https://axcl-docs.readthedocs.io)

- [RPi 5 AXCL Guide](https://axcl-pi5-examples-cn.readthedocs.io)

- Refer to [here](../m4n/axmodel-deploy.html) for detailed model development.

## Known Issues

### M4N-Hat Fails to Mount After Soft Reboot RPI5

Due to PCIe reset timing limitations, cold boot (power cycle) is required for successful mounting. A soft reboot leaves PCIe link down (line 18):

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
**Workaround:**

Before rebooting, reset the M4N-Hat via GPIO:

```bash
gpioset gpiochip0 28=0  # Force M4N-Hat reset  
reboot
```
