<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

# Raspberry Pi 5 PCIe Acceleration Guide

## Final Demo

After completing the following prerequisites for Raspberry Pi 5, running [the large language model DeepSeek-R1:1.5B](https://huggingface.co/AXERA-TECH/DeepSeek-R1-Distill-Qwen-1.5B-GPTQ-Int4)(Int4 Quantization for Model Parameters) achieves 13.69 tokens/s (performance for smaller models is limited by PCIe link bandwidth, showing a gap compared to the standalone board's 19 tokens/s),but RPI5 can only achieve 6.12 tokens/s. Watch the demo video:

<video controls autoplay src="../../../zh/maixIV/assets/m4nhat/PCIe/axcl-run-llm-on-raspi5-2025-08-19-3xspeedup.mp4" type="video/mp4"> Your browser does not support video playback. </video>

## Preparation

- Maix4-HAT
- sdcard-20250818.img.zst or newer

### Installation
<div style="display: flex; justify-content: space-between;">
  <img src="../../../zh/maixIV/assets/m4nhat/DSC07559.JPG" style="width: 48%;">
  <img src="../../../zh/maixIV/assets/m4nhat/DSC07561.JPG" style="width: 48%;">
</div>

![](../../../zh/maixIV/assets/m4nhat/DSC07569.JPG)

### Flashing the Maix4-HAT Slave System

1.Connect the Maix4-HAT to the Raspberry Pi 5's PCIe slot using an FPC cable and secure it.

2.Powering the Raspberry Pi 5 and Maix4-HAT.

3.Refer to the [System Flashing Guide](../m4n/system-update.html#Booting-into-the-Live-System-(Manual-Intervention-Required)) and boot into the TFCard Live System。

4.Execute `dd if=/boot/spl_AX650_card_signed.bin of=/dev/mmcblk0 conv=fsync` to flash the slave system for supporting PCIe boot:
  ```bash
  root@m4chat-08080a:~# dd if=/boot/spl_AX650_card_signed.bin of=/dev/mmcblk0 conv=fsync
  512+0 records in
  512+0 records out
  262144 bytes (262 kB, 256 KiB) copied, 0.0165514 s, 15.8 MB/s
  ```

5.Enable Raspberry Pi 5's PCIe x1 Interface.
  Run `sudo raspi-config → 6 Advanced Options → A8 PCIe Speed → Select Yes` for PCIe x1 Gen3.
5.1.or Manually add contents below to `/boot/firmware/config.txt`:
  ```bash
  [all]
  dtparam=pciex1_gen=3
  ```

  Actually the `config.txt` file is located in the FAT32 type partition, so you can modify it after mount it on your PC directly.

  > Note: Newly flashed Raspberry Pi SD cards lack the /boot/firmware directory. Boot once to generate it.

6. Reboot Raspberry Pi. Verify the accelerator card is detected with `lspci`:
  ```bash
  sipeed@rpi-sipeed:~$ lspci
  0001:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 21)
  0001:01:00.0 Multimedia video controller: Axera Semiconductor Co., Ltd Device 0650 (rev01)
  0002:00:00.0 PCI bridge: Broadcom Inc. and subsidiaries BCM2712 PCIe Bridge (rev 21)
  0002:01:00.0 Ethernet controller: Raspberry Pi Ltd RP1 PCIe 2.0 South Bridge
  ```

The first two lines confirm PCIe initialization and detection of the Axera AX650 controller. ANd the `Multimedia video controller: Axera Semiconductor Co., Ltd Device 0650 (rev01)` has been mounted correctly.

### Installing AXCL Software on Raspberry Pi 5

You can download it separately to the Raspberry Pi development board from the download site, or directly use the provided AIDemos.tar.zst below.

After PCIe detection, install the AXCL package for model acceleration:

```bash
$ sudo apt install axcl_host_aarch64_V3.6.2_20250603154858_NO4873.deb
# If your PCIe device is detected (visible in lspci), but axcl-smi fails to display it, follow these steps to reinstall the driver:
sudo apt install --reinstall axcl_host_aarch64_V3.6.2_20250603154858_NO4873.deb
```

Reboot the Pi. Verify installation with `axcl-smi`:

```bash
sipeed@rpi-sipeed:~$ axcl-smi
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
```

## Model Demonstration Guide

Download [AIDemos.tar.zst](https://mega.nz/folder/NxxEzRAB#e-sA_IK0K5JqQM6FnCH6_Q) from the cloud storage and extract it to reproduce and experience the following deployed models.

### Preparation:
Prepare the Python environment and install the `axengine` package.
```bash
cd /path/to/AIDemos/extra
python -m venv venv-llm
source venv-llm/bin/activate
pip install -r requirements.txt
pip install axengine-0.1.3-py3-none-any.whl
```

Result:
```bash
sipeed@rpi-sipeed:~/Downloads/AIDemos/extra $ ls -lh
total 44M
-rw-r--r-- 1 sipeed sipeed  44M Aug 14 09:04 axcl_host_aarch64_V3.6.2_20250603154858_NO4873.deb
-rw-r--r-- 1 sipeed sipeed  19K Aug 14 09:46 axengine-0.1.3-py3-none-any.whl
-rw-r--r-- 1 sipeed sipeed 1.3K Aug 18 08:50 requirements.txt
drwxr-xr-x 6 sipeed sipeed 4.0K Aug 18 03:24 venv-llm
```

### YOLO11
Link: https://huggingface.co/AXERA-TECH/YOLO11

Preparation:
```bash
source ../extra/venv-llm/bin/activate
```

Example:
```bash
sipeed@rpi-sipeed:~/Downloads/AIDemos/YOLO11 $ ls
axcl_yolo11  ax_yolo11	football.jpg  ssd_horse.jpg  yolo11s.axmodel  yolo11x.axmodel
sipeed@rpi-sipeed:~/Downloads/AIDemos/YOLO11 $ ./axcl_yolo11 -m yolo11s.axmodel -i football.jpg
--------------------------------------
model file : yolo11s.axmodel
image file : football.jpg
img_h, img_w : 640 640
--------------------------------------
axclrtEngineCreateContextt is done.
axclrtEngineGetIOInfo is done.

grpid: 0

input size: 1
    name:   images
        1 x 640 x 640 x 3


output size: 3
    name: /model.23/Concat_output_0
        1 x 80 x 80 x 144

    name: /model.23/Concat_1_output_0
        1 x 40 x 40 x 144

    name: /model.23/Concat_2_output_0
        1 x 20 x 20 x 144

==================================================

Engine push input is done.
--------------------------------------
post process cost time:0.90 ms
--------------------------------------
Repeat 1 times, avg time 3.34 ms, max_time 3.34 ms, min_time 3.34 ms
--------------------------------------
detection num: 7
 0:  95%, [ 759,  213, 1126, 1152], person
 0:  94%, [   0,  359,  315, 1107], person
 0:  94%, [1350,  344, 1629, 1036], person
 0:  89%, [ 490,  480,  658,  996], person
32:  73%, [ 771,  888,  830,  939], sports ball
32:  67%, [1231,  876, 1280,  924], sports ball
 0:  62%, [   0,  565,   86,  995], person
--------------------------------------
```
<div style="display: flex; justify-content: space-between;">
  <img src="../assets/m4nhat/PCIe/football.jpg" style="width: 48%;">
  <img src="../assets/m4nhat/PCIe/yolo11_out.jpg" style="width: 48%;">
</div>

<div style="width: 80%; margin: 0 auto;">
    <canvas id="YOLOv11BarChart"></canvas>
<script>
    var ctx = document.getElementById('YOLOv11BarChart').getContext('2d');
    var YOLOv11BarChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['YOLOv11s', 'YOLOv11x'],  // Now the models are the labels
            datasets: [
                {
                    label: 'Maix4 HAT 24T(PCIe mode)',
                    data: [298, 40.48],
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Jetson Orin Nano Super 67T',
                    data: [196.85, 50.25],
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Hailo8 26T',
                    data: [147, 0],
                    backgroundColor: 'rgba(255, 206, 86, 0.2)',  // Gold
                    borderColor: 'rgba(255, 206, 86, 1)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'YOLOv11 Performance Benchmark(fps)',  // Chart title added here
                    font: {
                        size: 20
                    }
                },
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            return tooltipItem.dataset.label + ': ' + tooltipItem.raw + ' fps';
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
</script>
</div>

Data Source Attribution: [Ultralytics](https://docs.ultralytics.com/zh/guides/nvidia-jetson/#nvidia-jetson-orin-nano-super-developer-kit_1), [RK3588](https://github.com/yuunnn-w/rknn-cpp-yolo?tab=readme-ov-file#report-inference-results-and-speed)

### DeepSeek-R1-Distill-Qwen-1.5B-GPTQ-Int4
Link: https://huggingface.co/AXERA-TECH/DeepSeek-R1-Distill-Qwen-1.5B-GPTQ-Int4

Usage:
```bash
./run_from_pi.sh
```

Example:
```bash
sipeed@rpi-sipeed:~/Downloads/AIDemos/DeepSeek-R1-Distill-Qwen-1.5B-GPTQ-Int4 $ ./run_from_pi.sh
Main script running (PID: 9852), subprocess PID: 9856
build time: Feb 13 2025 15:44:57
[I][                            Init][ 111]: LLM init start
bos_id: 151646, eos_id: 151643
100% | ████████████████████████████████ |  31 /  31 [17.22s<17.22s, 1.80 count/s] init post axmodel okremain_cmm(-1 MB)
[I][                            Init][ 226]: max_token_len : 1023
[I][                            Init][ 231]: kv_cache_size : 256, kv_cache_num: 1023
[I][                     load_config][ 282]: load config:
{
    "enable_repetition_penalty": false,
    "enable_temperature": true,
    "enable_top_k_sampling": true,
    "enable_top_p_sampling": false,
    "penalty_window": 20,
    "repetition_penalty": 1.2,
    "temperature": 0.9,
    "top_k": 10,
    "top_p": 0.8
}

[I][                            Init][ 288]: LLM init ok
Type "q" to exit, Ctrl+c to stop current running
>> what can you do?
<think>

</think>

I'm DeepSeek-R1, an AI assistant created exclusively by DeepSeek. My purpose is to help you generate helpful responses. I don't have personal experiences or emotions, so I don't have feelings, but I'm focused on providing accurate and useful information. For more information, please visit DeepSeek's official website.

[N][                             Run][ 610]: hit eos,avg 13.69 token/s

>>
```

<div style="width: 80%; margin: 0 auto;">
    <canvas id="DeepSeekR1BarChart"></canvas>
<script>
    var ctx = document.getElementById('DeepSeekR1BarChart').getContext('2d');
    var DeepSeekR1BarChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['DSR1:1.5B', 'DSR1:7B'],  // Models as labels
            datasets: [
                {
                    label: 'Maix4 HAT 24T(PCIe mode)',
                    data: [13.69, 4.64],
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                },
                {
                    label: 'RPI5',
                    data: [6.12, 1.43],
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'DeepSeek-R1 Performance Benchmark(higher is better)',  // Chart title added here
                    font: {
                        size: 20
                    }
                },
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            return tooltipItem.dataset.label + ': ' + tooltipItem.raw + ' token/s';
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
</script>
</div>

Data Source Attribution: [deepseek-r1-on-RPI5](https://dev.to/jeremycmorgan/running-deepseek-r1-locally-on-a-raspberry-pi-1gh8)


### InternVL2_5-1B
Link: https://huggingface.co/AXERA-TECH/InternVL2_5-1B

Usage:
```bash
./run_from_pi.sh
```

Example:
```bash
sipeed@rpi-sipeed:~/Downloads/AIDemos/InternVL2_5-1B $ ./run_from_pi.sh
Main script running (PID: 10379), subprocess PID: 10383
[I][                            Init][ 128]: LLM init start
[I][                            Init][ 321]: connect http://127.0.0.1:49152 ok
bos_id: -1, eos_id: 151645
  7% | ███                               |   2 /  27 [0.70s<9.41s, 2.87 count/s] embed_selector init ok
[I][                             run][  30]: AXCLWorker start with devid 0
100% | ████████████████████████████████ |  27 /  27 [18.42s<18.42s, 1.47 count/s] init post axmodel ok,remain_cmm(6433 MB)6574 MB)
[I][                            Init][ 225]: image_encoder_height : 448, image_encoder_width: 448
[I][                            Init][ 227]: max_token_len : 1023
[I][                            Init][ 230]: kv_cache_size : 128, kv_cache_num: 1023
[I][                            Init][ 238]: prefill_token_num : 320
[I][                            Init][ 240]: prefill_max_token_num : 320
________________________
|    ID| remain cmm(MB)|
========================
|     0|           6066|
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
[I][                     load_config][ 282]: load config:
{
    "enable_repetition_penalty": false,
    "enable_temperature": true,
    "enable_top_k_sampling": true,
    "enable_top_p_sampling": false,
    "penalty_window": 20,
    "repetition_penalty": 1.2,
    "temperature": 0.9,
    "top_k": 10,
    "top_p": 0.8
}

[I][                            Init][ 337]: LLM init ok
Type "q" to exit, Ctrl+c to stop current running
prompt >> describe the picture in English
image >> ssd_car.jpg
[I][                          Encode][ 393]: image encode time : 362.10 ms, size : 229376
[I][                          Encode][ 453]: offset : 42 out_embed.size() : 276864
[I][                             Run][ 481]: input token num : 309, prefill_split_num : 1
[I][                             Run][ 604]: ttft: 510.61 ms
The image shows a classic red double-decker bus parked on the side of a city street. The bus is adorned with advertisements, one of which reads, "THINGS GET MORE EXCITING WHEN YOU SAY YES," along with a website, "VMGIVING.COM." The bus number on it is 16.

In the foreground, a woman is standing with a cheerful expression. She is wearing a black coat, a scarf, and jeans and appears to be smiling at the camera. In front of her, there is a streetcar, also red, passing by. The street is marked with a bicycle lane, indicated by a dashed white line on the road. In the background, several multi-story buildings, likely commercial establishments, are visible.

The setting appears to be a bustling urban area, with a mix of historical and modern architecture, suggesting a city center.

[N][                             Run][ 756]: hit eos,avg 18.73 token/s

prompt >>
```
![ssd_car.jpg](../assets/m4nhat/PCIe/ssd_car.jpg)


### lcm-lora-sdv1-5
Link: https://huggingface.co/AXERA-TECH/lcm-lora-sdv1-5

Preparation:
```bash
source ../extra/venv-llm/bin/activate
```

Usage:
```bash
python run_txt2img_axe_infer_once.py --prompt 'two beautiful girl'
# or
python run_txt2img_axe_infer_loop.py # wait it be ready and then type prompt and press Enter
# or
python run_img2img_axe_infer.py --prompt "8k, cute" --init_image txt2img_output_axe.png
```

Example:
```bash
(venv-llm) sipeed@rpi-sipeed:~/Downloads/AIDemos/lcm-lora-sdv1-5 $ python run_txt2img_axe_infer_once.py --prompt 'two beautiful girl'
[INFO] Available providers:  ['AXCLRTExecutionProvider']
prompt: two beautiful girl
text_tokenizer: ./models/tokenizer
text_encoder: ./models/text_encoder
unet_model: ./models/unet.axmodel
vae_decoder_model: ./models/vae_decoder.axmodel
time_input: ./models/time_input_txt2img.npy
save_dir: ./txt2img_output_axe.png
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.4 9215b7e5
text encoder take 4936.9ms
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 972f38ca
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 972f38ca
load models take 25627.9ms
unet once take 433.6ms
unet once take 433.4ms
unet once take 433.5ms
unet once take 433.5ms
unet loop take 1736.7ms
vae inference take 914.8ms
save image take 206.9ms

(venv-llm) sipeed@rpi-sipeed:~/Downloads/AIDemos/lcm-lora-sdv1-5 $ python run_img2img_axe_infer.py --prompt "8k, cute" --init_image txt2img_output_axe.png
[INFO] Available providers:  ['AXCLRTExecutionProvider']
prompt: 8k, cute
text_tokenizer: ./models/tokenizer
text_encoder: ./models/text_encoder
unet_model: ./models/unet.axmodel
vae_encoder_model: ./models/vae_encoder.axmodel
vae_decoder_model: ./models/vae_decoder.axmodel
init image: txt2img_output_axe.png
time_input: ./models/time_input_img2img.npy
save_dir: ./img2img_output_axe.png
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.4 9215b7e5
text encoder take 2954.0ms
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3-dirty 2ecead35-dirty
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 972f38ca
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 972f38ca
load models take 15804.3ms
vae encoder inference take 459.1ms
unet once take 433.6ms
unet once take 433.3ms
unet loop take 868.3ms
vae decoder inference take 913.7ms
grid image saved in ./lcm_lora_sdv1-5_imgGrid_output.png
save image take 445.9ms
```
![img2img_output_axe](../assets/m4nhat/PCIe/img2img_output_axe.png)

<div style="width: 80%; margin: 0 auto;">
    <canvas id="SDV1_5BarChart"></canvas>
<script>
    var ctx = document.getElementById('SDV1_5BarChart').getContext('2d');
    var SDV1_5BarChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['U-Net (s/it)', 'VAE Decoder (s)'],  // Models as labels
            datasets: [
                {
                    label: 'Maix4 HAT 24T(PCIe mode)',
                    data: [0.43, 0.91],
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                },
                {
                    label: 'RK3588',
                    data: [5.65, 11.13],
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Stable-Diffusion-1.5 (512x512) Performance Benchmark (lower is better)',  // Chart title added here
                    font: {
                        size: 20
                    }
                },
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            return tooltipItem.dataset.label + ': ' + tooltipItem.raw + ' s';
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
</script>
</div>

Data Source Attribution: [RK3588](https://huggingface.co/happyme531/Stable-Diffusion-1.5-LCM-ONNX-RKNN2)


### Depth-Anything-V2
Link: https://huggingface.co/AXERA-TECH/Depth-Anything-V2

Preparation:
```bash
source ../extra/venv-llm/bin/activate
```

Usage:
```bash
python infer.py --model depth_anything_v2_vits.axmodel --img examples/demo01.jpg
# or
python infer_onnx.py --model depth_anything_v2_vits.onnx --img examples/demo02.jpg
```
![depth_ouput_ax1](../assets/m4nhat/PCIe/depth_ouput_ax1.png)
![depth_ouput_ax2](../assets/m4nhat/PCIe/depth_ouput_ax2.png)

<div style="width: 80%; margin: 0 auto;">
    <canvas id="Depth_Anything_V2BarChart"></canvas>
<script>
    var ctx = document.getElementById('Depth_Anything_V2BarChart').getContext('2d');
    var Depth_Anything_V2BarChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Depth-Anything-V2 (fps)'],  // Models as labels
            datasets: [
                {
                    label: 'Maix4 HAT 24T(PCIe mode)',
                    data: [24.39],
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Jetson Orin',
                    data: [10.2],
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: 'Depth-Anything-V2 (518x518) Performance Benchmark (fps)',  // Chart title added here
                    font: {
                        size: 20
                    }
                },
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            return tooltipItem.dataset.label + ': ' + tooltipItem.raw + ' fps';
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
</script>
</div>

Data Source Attribution: [Jetson Orin](https://github.com/IRCVLab/Depth-Anything-for-Jetson-Orin)


### clip
Link:
- https://huggingface.co/AXERA-TECH/clip
- https://github.com/AXERA-TECH/clip.axera

Preparation:
```bash
source ../extra/venv-llm/bin/activate
```

Example:
```bash
(venv-llm) sipeed@rpi-sipeed:~/Downloads/AIDemos/clip $ ls
clip_vit_l14_336px_image_encoder_all_u16_fc_u8.axmodel	clip_vit_l14_336px_text_encoder_u16.axmodel  images  infer.py  Tokenizer.py  vocab.txt
(venv-llm) sipeed@rpi-sipeed:~/Downloads/AIDemos/clip $ python infer.py
[INFO] Available providers:  ['AXCLRTExecutionProvider']
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 4.0 685bfee4
input.1 [1, 3, 336, 336] float32
4002 [1, 768] float32
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 4.0 685bfee4
texts [1, 77] int32
text_features [1, 768] float32
(14, 768)
(11, 768)
=== logits_per_image ===
                   cat   dog  husky  airplane   car  cityscape  fire  person  eagle  bike  pineapple
bike2.jpg         0.00  0.02   0.01      0.00  0.46       0.00  0.01    0.29    0.0  0.21       0.00
eagle.jpg         0.00  0.00   0.00      0.00  0.00       0.00  0.00    0.00    1.0  0.00       0.00
mv2seg.png        0.00  0.00   0.00      0.00  0.98       0.00  0.00    0.01    0.0  0.00       0.00
husky.jpeg        0.00  0.00   1.00      0.00  0.00       0.00  0.00    0.00    0.0  0.00       0.00
fire.png          0.00  0.00   0.00      0.00  0.00       0.00  1.00    0.00    0.0  0.00       0.00
dog.jpg           0.00  0.12   0.04      0.00  0.04       0.00  0.00    0.00    0.0  0.80       0.00
cat.jpg           0.91  0.03   0.01      0.00  0.01       0.00  0.01    0.00    0.0  0.01       0.03
big-dog.jpg       0.00  0.15   0.07      0.00  0.56       0.00  0.03    0.09    0.0  0.01       0.08
pineapple.jpg     0.00  0.00   0.00      0.00  0.00       0.00  0.00    0.00    0.0  0.00       1.00
bike.jpg          0.00  0.00   0.01      0.00  0.01       0.00  0.00    0.05    0.0  0.92       0.00
cityscape.png     0.00  0.00   0.00      0.00  0.19       0.24  0.50    0.00    0.0  0.00       0.05
air.jpg           0.00  0.00   0.00      0.94  0.04       0.00  0.01    0.00    0.0  0.01       0.00
dog-chai.jpeg     0.00  0.23   0.04      0.00  0.57       0.00  0.06    0.07    0.0  0.01       0.02
grace_hopper.jpg  0.02  0.07   0.00      0.00  0.55       0.00  0.28    0.07    0.0  0.00       0.00

=== logits_per_text ===
           bike2.jpg  eagle.jpg  mv2seg.png  husky.jpeg  fire.png  dog.jpg  cat.jpg  big-dog.jpg  pineapple.jpg  bike.jpg  cityscape.png  air.jpg  dog-chai.jpeg  grace_hopper.jpg
cat             0.00       0.01        0.00        0.00      0.00     0.00     0.92         0.01            0.0      0.00           0.00     0.00           0.04              0.02
dog             0.00       0.02        0.00        0.01      0.00     0.40     0.01         0.14            0.0      0.00           0.00     0.00           0.41              0.01
husky           0.00       0.00        0.00        1.00      0.00     0.00     0.00         0.00            0.0      0.00           0.00     0.00           0.00              0.00
airplane        0.00       0.07        0.00        0.00      0.00     0.00     0.00         0.01            0.0      0.00           0.00     0.91           0.01              0.00
car             0.03       0.01        0.29        0.00      0.00     0.05     0.00         0.19            0.0      0.00           0.01     0.01           0.38              0.03
cityscape       0.00       0.01        0.05        0.00      0.00     0.00     0.00         0.05            0.0      0.09           0.64     0.00           0.16              0.00
fire            0.00       0.01        0.00        0.00      0.94     0.00     0.00         0.01            0.0      0.00           0.01     0.00           0.02              0.01
person          0.15       0.04        0.01        0.00      0.00     0.03     0.00         0.22            0.0      0.17           0.00     0.00           0.33              0.03
eagle           0.00       1.00        0.00        0.00      0.00     0.00     0.00         0.00            0.0      0.00           0.00     0.00           0.00              0.00
bike            0.01       0.00        0.00        0.00      0.00     0.69     0.00         0.00            0.0      0.29           0.00     0.00           0.00              0.00
pineapple       0.00       0.00        0.00        0.00      0.00     0.00     0.00         0.00            1.0      0.00           0.00     0.00           0.00              0.00
```


### Whisper
Link: https://huggingface.co/AXERA-TECH/Whisper

Preparation:
```bash
source ../extra/venv-llm/bin/activate
```

Usage:
```bash
python whisper_onnx.py --model_path ./models-onnx/base/ -t base --wav ./demo.wav

python whisper.py --model_path ./models/small/ -t small --wav ./demo.wav
# or
./whisper_axcl_aarch64 -e ./models/small/small-encoder.axmodel -m ./models/small/small-decoder-main.axmodel -l ./models/small/small-decoder-loop.axmodel -p ./models/small/small-positional_embedding.bin -t ./models/small/small-tokens.txt -w ./demo.wav
```

Example:
```bash
(venv-llm) sipeed@rpi-sipeed:~/Downloads/AIDemos/Whisper $ ./whisper_axcl_aarch64 -e ./models/small/small-encoder.axmodel -m ./models/small/small-decoder-main.axmodel -l ./models/small/small-decoder-loop.axmodel -p ./models/small/small-positional_embedding.bin -t ./models/small/small-tokens.txt -w ./RP1intro.wav --language en
encoder: ./models/small/small-encoder.axmodel
decoder_main: ./models/small/small-decoder-main.axmodel
decoder_loop: ./models/small/small-decoder-loop.axmodel
wav_file: ./RP1intro.wav
language: en
Load encoder take 2442.17 ms
Load decoder_main take 4068.22 ms
Load decoder_loop take 3837.32 ms
Read positional_embedding
Encoder run take 190.63 ms
First token: 41154 	 take 51.20ms
Next Token: 17741 	 take 30.39 ms
Next Token: 1025 	 take 30.33 ms
Next Token: 307 	 take 30.36 ms
Next Token: 3094 	 take 30.25 ms
Next Token: 1228 	 take 30.30 ms
Next Token: 264 	 take 30.26 ms
Next Token: 497 	 take 30.30 ms
Next Token: 48 	 take 30.30 ms
Next Token: 16 	 take 30.36 ms
Next Token: 39839 	 take 30.21 ms
Next Token: 1969 	 take 30.29 ms
Next Token: 11 	 take 30.34 ms
Next Token: 257 	 take 30.30 ms
Next Token: 7372 	 take 30.22 ms
Next Token: 19273 	 take 30.29 ms
Next Token: 22848 	 take 30.20 ms
Next Token: 4761 	 take 30.13 ms
Next Token: 294 	 take 30.31 ms
Next Token: 1782 	 take 30.33 ms
Next Token: 295 	 take 30.32 ms
Next Token: 41154 	 take 30.29 ms
Next Token: 17741 	 take 30.33 ms
Next Token: 13 	 take 30.28 ms
Next Token: 50257 	 take 30.31 ms
All Token: take 778.48ms, 32.11 token/s
All take 1010.35ms
Result:  Raspberry Pi 5 is built using the RQ1 IO control, a package containing silicon designed in house of Raspberry Pi.
```


### MeloTTS
Link: https://huggingface.co/AXERA-TECH/MeloTTS

Preaparation:
```bash
source ../extra/venv-llm/bin/activate
cp -R nltk_data ~/
```

Usage:
```bash
(venv-llm) sipeed@rpi-sipeed:~/Downloads/AIDemos/MeloTTS/python $ cd python
(venv-llm) sipeed@rpi-sipeed:~/Downloads/AIDemos/MeloTTS/python $ python melotts.py -h
[INFO] Available providers:  ['AXCLRTExecutionProvider']
usage: melotts [-h] [--sentence SENTENCE] [--wav WAV] [--encoder ENCODER] [--decoder DECODER] [--dec_len DEC_LEN] [--sample_rate SAMPLE_RATE] [--speed SPEED]
               [--language {ZH,ZH_MIX_EN,JP,EN,KR,ES,SP,FR}]

Run TTS on input sentence

options:
  -h, --help            show this help message and exit
  --sentence SENTENCE, -s SENTENCE
  --wav WAV, -w WAV
  --encoder ENCODER, -e ENCODER
  --decoder DECODER, -d DECODER
  --dec_len DEC_LEN
  --sample_rate SAMPLE_RATE, -sr SAMPLE_RATE
  --speed SPEED
  --language {ZH,ZH_MIX_EN,JP,EN,KR,ES,SP,FR}, -l {ZH,ZH_MIX_EN,JP,EN,KR,ES,SP,FR}
```

Example:
```bash
(venv-llm) sipeed@rpi-sipeed:~/Downloads/AIDemos/MeloTTS/python $ python melotts.py -s "Dig the well before you are thirsty." -l EN
[INFO] Available providers:  ['AXCLRTExecutionProvider']
sentence: Dig the well before you are thirsty.
sample_rate: 44100
encoder: ../encoder-onnx/encoder-en.onnx
decoder: ../decoder-ax650/decoder-en.axmodel
language: EN
 > Text split to sentences.
Dig the well before you are thirsty.
 > ===========================
split_sentences_into_pieces take 0.7653236389160156ms
[INFO] Using provider: AXCLRTExecutionProvider
[INFO] SOC Name: AX650N
[INFO] VNPU type: VNPUType.DISABLED
[INFO] Compiler version: 3.3 3251425d
load models take 1990.5009269714355ms

Sentence[0]: Dig the well before you are thirsty.
Load language module take 11539.379358291626ms
encoder run take 30.54ms
Decode slice[0]: decoder run take 99.54ms
Decode slice[1]: decoder run take 92.79ms
Decode slice[2]: decoder run take 92.74ms
Save to output.wav
```


## AXCL Inference Performance 

Run `axcl_run_model` (usage mirrors native ax_run_model). Example with YOLOv5s (single-core model; full-core performance scales ~3x):


```bash
sipeed@rpi-sipeed:~/Downloads/AIDemos/models $ axcl_run_model -m yolov5s.axmodel
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


## Known Issues

### Maix4-HAT Fails to Mount After Soft Reboot RPI5

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

Debian GNU/Linux 12 rpi-sipeed ttyAMA10

My IP address is 192.168.10.176 fdae:b0ae:ebf1:0:b270:135e:b646:70c3

rpi-sipeed login:
```
**Workaround:**

Before rebooting, reset the Maix4-HAT via GPIO:

```bash
gpioset gpiochip0 28=0  # Force Maix4-HAT reset  
reboot
```

## Additional Resources for AXCL

- [AXCL Documentation](https://axcl-docs.readthedocs.io)

- [RPi 5 AXCL Guide](https://axcl-pi5-examples-cn.readthedocs.io)

- Refer to [here](../m4n/axmodel-deploy.html) for detailed model development.