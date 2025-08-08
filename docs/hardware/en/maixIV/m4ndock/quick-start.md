## System Boot and Login

**Note:** The system must be powered via 12V DC input. USB power alone may cause insufficient power supply leading to system instability.

### Pre-Boot Preparation

Required:

1. 12V DC power supply

2. HDMI cable and display

3. Type-C cable (optional: for serial debugging/login)

4. RJ45 Ethernet cable (optional: for network connection and SSH login)

For first-time use, verify the following status matches your hardware version:

- Power switch on enclosure is ON (for enclosed versions)

- Jumper cap remains shorted at Button marking (for bare board versions)

![top](../../../zh/maixIV/assets/top.png)

### Normal Boot

Connect display via HDMI1 and provide 12V DC power. After approximately 20 seconds, the LightDM login interface will appear, indicating successful system boot.

![desktop](../../../zh/maixIV/assets/desktop.jpg)

Connect mouse/keyboard to the onboard USB-A port for operation. Use default credentials (username: `root`, password: `root`) to access the Debian desktop system.

### Advanced: Serial & SSH Login

The onboard Type-C USB port serves as the default debug UART (**115200 8n1**).

Use a serial tool to view kernel logs or log in directly via terminal.

For SSH access, expand network connectivity via USB Ethernet/WiFi dongles.

Note: The system only has the root superuser, and SSH password login is disabled by default for security. For temporary access, refer to [here](../m4n/FAQ.md)。


## Interactive Image Segmentation & Inpainting

A QT-based GUI for real-time segmentation (point/box selection) and inpainting.

![samqt](../../../zh/maixIV/assets/samqt.jpg)

Open Source Official GitHub Repo: [SAM-ONNX-AX650-CPP](https://github.com/AXERA-TECH/SAM-ONNX-AX650-CPP)
Download prebuilt binaries or compile from source.

Example: Removing a player from a photo:

<div><table><tr>
<td><img src="../../../zh/maixIV/assets/sam_example_before.png" alt=sam_example_before border=0></td>
<td><img src="../../../zh/maixIV/assets/sam_example_after.png" alt=sam_example_after border=0></td>
</tr></table></div>

Live Demo (Screenshots):

<div><table><tr>
<td><img src="../../../zh/maixIV/assets/sam_raw.jpg" alt=sam_raw border=0></td>
<td><img src="../../../zh/maixIV/assets/sam_sam.jpg" alt=sam_sam border=0></td>
<td><img src="../../../zh/maixIV/assets/sam_inpaint.jpg" alt=sam_inpaint border=0></td>
</tr><tr>
<td>RAW</td>
<td>SAM</td>
<td>Inpaint</td>
</tr></table></div>


## Interactive Text-to-Image Search (CLIP)
A QT-based GUI using OpenAI’s CLIP (Contrastive Language–Image Pre-training) for zero-shot image retrieval via text input (supports Chinese/English).

Open Source Official GitHub Repo: [CLIP-ONNX-AX650-CPP](https://github.com/AXERA-TECH/CLIP-ONNX-AX650-CPP)

[DEMO VIDEO](https://github.com/sipeed/sipeed_wiki/assets/13964381/df4cec7f-29af-465f-bfad-e54312274437)

1. Install QT:
    ```bash
    apt update
    apt install cmake qt6-base-dev
    ```

2. Download prebuilt files (executable, models, test images/text):
    - [Baidu Pan](https://pan.baidu.com/s/17M5ugUyuf9mbi1cHLGJHXg)

3. Extract *CLIP.zip* to `/root/Desktop/`:
    ```bash
    root@m4nhat-7190c7:~/Desktop/CLIP# tree -L 1
    .
    ├── CLIPQT
    ├── cn_vocab.txt
    ├── coco_1000
    ├── libonnxruntime.so
    ├── libonnxruntime.so.1.16.0
    ├── onnx_models
    ├── run_en.sh
    ├── run_zh.sh
    └── vocab.txt
    ```

4. Run in Desktop's terminal:
    ```bash
    ./run_zh.sh  # For Chinese  
    ./run_en.sh  # For English  
    ```

Screenshots:

![b38722991915fa54f17df18ca1f1447](https://github.com/AXERA-TECH/CLIP-ONNX-AX650-CPP/assets/13964381/8fa2c4b8-b061-413e-b72d-298bb4a445aa)

![34c8b68b1a8721d4ebff3b4b7184733](https://github.com/AXERA-TECH/CLIP-ONNX-AX650-CPP/assets/13964381/7d0b9740-3598-492c-ad42-2de23e7764e2)


## **Important Demo Pre-requisites**

HDMI0 (demo output) and HDMI1 (desktop) cannot operate simultaneously due to display driver limitations.

**To run demos:**

1. Terminate fb_vo process:
        ```bash
        kill -9 $(pgrep fb_vo)
        ```

2. Connect display to HDMI0

3. Execute demo scripts via SSH/serial terminal

4. After demo, you can restore desktop:
        ```bash
        /root/runVoHook.sh
        ```

## 32-Channel AI BOX (Person/Vehicle Detection)

BoxDemo showcases the complete pipeline from **H.264/H.265** decoding → AI analysis → HDMI display.

**Features:**

- Default: 32-channel display (6×6 layout)

- Dual HDMI support (mirror/extended)

- System power consumption <7W

- 3.6T NPU utilization (1/3 capacity)

- 15-20 FPS (CPU-bound)

**Configuration:**

- Edit /opt/bin/BoxDemo/box.conf:

    - streamxx: RTSP source URLs

    - DISP1=1: Enable HDMI1 output

**Run:**

```bash
bash /opt/bin/BoxDemo/run.sh
```

![aibox_pipeline](../../../zh/maixIV/assets/aibox_pipeline.png)

![aibox_example32ch](../../../zh/maixIV/assets/aibox_example32ch.png)


## DINO v2 Monocular Depth Estimation

Leveraging Facebook's DINO v2 model for relative depth estimation using single RGB camera.


![pipeline_bin](../../../zh/maixIV/assets/pipeline_bin.png)

**Execution:**

```bash
cd ~/ax-pipeline/bin

./sample_multi_demux_ivps_npu_multi_rtsp_hdmi_vo \
        -p ./config/dinov2_depth.json \
        -f ~/boxvideos/13.mp4
```
*Supports H.264 video files or RTSP streams*

**Results:**

<div><table><tr>
<td><img src="../../../zh/maixIV/assets/dinov2-1.png" alt=dinov2-1></td>
<td><img src="../../../zh/maixIV/assets/dinov2-2.png" alt=dinov2-2></td>
</tr></table></div>

![dinov2-3](../../../zh/maixIV/assets/dinov2-3.png)



## YOLOv5 Pedestrian Detection & Tracking

```bash
cd ~/ax-pipeline/bin

./sample_multi_demux_ivps_npu_multi_rtsp_hdmi_vo \
        -p ./config/yolov5_seg.json \
        -f ~/boxvideos/25.mp4
```

![yolov5_seg](../../../zh/maixIV/assets/yolov5_seg.png)
