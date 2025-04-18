---
title: Deploy models to AX-Pi (Maix-III(M3) series) board
date: 2022-09-21
update:
  - date: 2025-04-17
    author: Aristore
    content:
      - Translated the documentation
---

> This article is translated from Chinese, so may have some misexpressions, Pull request is welcome!

<div id="title_card">
    <div class="card" style="background-color: #fafbfe">
        <img src="../../assets/maix-iii-small.png" alt="AXera-Pi Model Conversion and Deployment">
        <div class="card_info card_purple">
            <div class="title">Maix-III Series AXera-Pi</div>
            <div class="brief">
                <div>High computing power, unique AI-ISP imaging system</div>
                <div>Up to 3.6Tops@INT8, rich operator support</div>
            </div>
        </div>
    </div>
</div>
<style>
#title_card {
    width:100%;
    text-align:center;
    background-color: #fafbfe;
    margin-bottom: 1em;
}
#title_card img {
  max-height: 20em;
}
.card_purple {
    background-color: #d1c4e9;
    color: #673ab7;
}
.dark .card_purple {
    background-color: #370040;
    color: #ffffffba;
}
.title {
    font-size: 1.5em;
    font-weight: 800;
    padding: 0.8em;
}
</style>

> Any thoughts or modification suggestions? Feel free to leave comments or directly click the "Edit this page" button in the top-right corner to submit a PR.

> [MaixHub](https://maixhub.com/model/zoo) model zoo has models that can run directly on AXera-Pi. You can download and use them, and also share your models~

[Click to view Maix-III(M3) series AXera-Pi development board details and basic usage documentation](/hardware/en/maixIII/index.html)

To deploy models to `AXera-Pi`, you need to quantize the model to INT8 to reduce model size and improve runtime speed. Generally, `PTQ` (Post-Training Quantization) is used. Steps:
**1.** Prepare the floating-point model.
**2.** Use the model quantization and format conversion tool to convert it into a format supported by AXera-Pi. The tool here is [pulsar](https://pulsar-docs.readthedocs.io) provided by AXERA.

> This document provides a quick start guide and process overview. It is strongly recommended to read through this document first, then check the pulsar documentation for more details.

**3.** Run the model on AXera-Pi.

## Prepare Floating-Point Model

Train the model using `Pytorch` or `TensorFlow`, then save it in `onnx` format.

Note that only operators supported by `AXera-Pi` can be used. See [Operator Support List](https://pulsar-docs.readthedocs.io/zh_CN/latest/appendix/op_support_list.html).

For some networks, post-processing may need to be separated and handled by the `CPU`.

### Example

Using [mobilenetv2](https://pytorch.org/hub/pytorch_vision_mobilenet_v2/) from PyTorch Hub:
```python
import torch
model = torch.hub.load('pytorch/vision:v0.10.0', 'mobilenet_v2', pretrained=True)
model.eval()
```

Export to `onnx` format:

```python
x = torch.randn(1, 3, 224, 224)
torch.onnx.export(model, x, "mobilenetv2.onnx", export_params=True, verbose=True, opset_version=11)
```

Some models can be simplified with `onnxsim` (not needed for this model):

```
pip install onnx-simplifier
python -m onnxsim mobilenetv2.onnx mobilenetv2-sim.onnx
```

## Model Quantization and Format Conversion

### Install `docker`

[Installation Guide](https://docs.docker.com/engine/install/)

Verify installation with:

```
docker --version
```

On Linux, add the current user to the `docker` group to avoid needing `sudo`:

```shell
sudo gpasswd -a $USER docker
newgrp docker
```

### Download Conversion Tool

The conversion tool is provided as a Docker image. Pull the image using:

| Source                                                       | Description          | Command                                                      |
| :----------------------------------------------------------- | :------------------- | :----------------------------------------------------------- |
| [dockerhub](https://hub.docker.com/r/sipeed/pulsar/tags)     | Pull directly        | `docker pull sipeed/pulsar`                                  |
| Domestic Mirror (China)                                      | China domestic mirror for accelerated downloads | 1. Edit `/etc/docker/daemon.json` to add `"registry-mirrors": ["https://docker.mirrors.ustc.edu.cn"]`<br>2. `docker pull sipeed/pulsar` |

After pulling, verify with `docker images` to see `sipeed/pulsar:latest`.
> Note: The image name `sipeed/pulsar` is equivalent to `axera/neuwizard` mentioned in some documents.

Create a container:
```shell
docker run -it --net host --rm --shm-size 32g -v $PWD:/data sipeed/pulsar
```
> * Adjust `--shm-size` based on your system's memory.
> * Omit `--rm` to keep the container, and use `-name xxx` to name it for later reuse.
> * `-v host_path:/data` mounts the host directory to `/data` in the container.

Inside the container, use `pulsar -h` to view commands.

### Perform Model Quantization and Conversion

Refer to [pulsar](https://pulsar-docs.readthedocs.io) documentation for conversion commands and configuration file setup.
> Note: AXera-Pi uses virtual NPU concepts to allocate computing resources between NPU and AI-ISP.

#### Example

Using `mobilenetv2`:
* Prepare configuration file `config_mobilenetv2.prototxt` (details in [Configuration Documentation](https://pulsar-docs.readthedocs.io/zh_CN/latest/test_configs/config.html)):
  .. details:: config_mobilenetv2.prototxt
    ```protobuf
    # Basic configuration parameters: input/output
    input_type: INPUT_TYPE_ONNX
    output_type: OUTPUT_TYPE_JOINT
    
    # Hardware platform selection
    target_hardware: TARGET_HARDWARE_AX620
    
    # CPU backend selection, default using AXE
    cpu_backend_settings {
        onnx_setting {
            mode: DISABLED
        }
        axe_setting {
            mode: ENABLED
            axe_param {
                optimize_slim_model: true
            }
        }
    }
    
    # ONNX model input data type description
    src_input_tensors {
        color_space: TENSOR_COLOR_SPACE_RGB
    }
    
    # Joint model input data type configuration
    dst_input_tensors {
        color_space: TENSOR_COLOR_SPACE_RGB
    }
    
    # NeuWizard tool configuration parameters
    neuwizard_conf {
        operator_conf {
            input_conf_items {
                attributes {
                    input_modifications {
                        # y = x * (slope / slope_divisor) + (bias / bias_divisor)
                        # Normalize data to [0, 1] range first
                        affine_preprocess {
                            slope: 1
                            slope_divisor: 255
                            bias: 0
                        }
                    }
                    input_modifications {
                        # y = (x - mean) / std
                        # Standardize using training parameters
                        input_normalization {
                            mean: [0.485,0.456,0.406]  ## Mean values (order depends on src_input_tensors.color_space, here [R G B])
                            std: [0.229,0.224,0.255]   ## Standard deviation values
                        }
                    }
                }
            }
        }
        dataset_conf_calibration {
            path: "imagenet-1k-images-rgb.tar" # PTQ calibration dataset path
            type: DATASET_TYPE_TAR         # Dataset type: TAR package
            size: 256                      # Number of images used for calibration
            batch_size: 1
    }
    }
    
    # Pulsar compiler batch size configuration
    pulsar_conf {
        ax620_virtual_npu: AX620_VIRTUAL_NPU_MODE_111 # Use virtual NPU, split resources between NPU and AI-ISP (111 represents NPU)
                        #  AX620_VIRTUAL_NPU_MODE_0   # Disable virtual NPU, full resources to NPU
                        #  AX620_VIRTUAL_NPU_MODE_112 # Use virtual NPU, split resources (112 represents AI-ISP exclusive use, do not modify casually)
        batch_size: 1
    }
    ```
    > Preprocessing must match the training pipeline (normalize to [0,1] then apply mean/std).
    > The `imagenet-1k-images-rgb.tar` dataset can be downloaded from [Baidu Cloud](https://pan.baidu.com/s/1TiZSIm0fpqbLn-2qLBX58g?pwd=1rpb) or [GitHub](https://github.com/sipeed/sipeed_wiki/releases/download/v0.0.0/imagenet-1k-images-rgb.tar).
    > The `ax620_virtual_npu` setting is critical for AI-ISP compatibility.


Then execute the following inside the `docker` container (note that the files are mounted from the host machine to the `docker` container using the `-v` parameter of the previous `docker run` command, so just copy them directly into the host's directory):
```
pulsar build --input mobilenetv2.onnx --output mobilenetv2.joint --config config_mobilenetv2.prototxt --output_config out_config_mobilenet_v2.prototxt
```
Be patient, as it may take a little while, and you will eventually get the converted model result `mobilenetv2.joint`.

### Using GPU for Model Quantization and Format Conversion in Docker

By default, docker cannot use the graphics card driver, but if needed, it’s not difficult:
* Install the graphics card driver on the host machine as usual. For example, on `ubuntu`, it can be installed directly via the package manager.
* Follow the instructions at [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) to install, then test whether it is usable:
```
docker run --rm --gpus all nvidia/cuda:11.0.3-base-ubuntu20.04 nvidia-smi
```
This will execute the `nvidia-smi` command, allowing you to see the GPU information mapped into docker.
* When creating containers that require the use of the GPU, add the `--gpus all` parameter to map all GPU drivers into the container, or specify particular GPU numbers with `--gpus '"device=2,3"'`, for example:
```
docker run -it --net host --rm --gpus all --shm-size 32g -v $PWD:/data sipeed/pulsar
```
Note that the current version (0.6.1.20) of `pulsar build` only supports sm_37 sm_50 sm_60 sm_70 sm_75 architecture GPUs; 30/40 series GPUs are not yet supported.

## Testing Model Execution on AXera-Pi

After converting the model according to the documentation, transfer the model to `AXera-Pi` via `scp` or `adb` and run the model using the model testing commands provided in the documentation.

### Example

Still using `mobilenetv2` as an example:
Save the test image as `cat.jpg`:
<img src="../../assets/cat.jpg" style="max-height: 20em;">

* First, compare the results with the `onnx` model on your computer:
```
pulsar run mobilenetv2.onnx mobilenetv2.joint --input cat.jpg --config out_config_mobilenet_v2.prototxt --output_gt gt
```
You’ll obtain the cosine distance, which here is `0.9862`, indicating that the output similarity between the `joint` model and the `onnx` model is `98.62%`, within an acceptable range. If the value is too small, it indicates errors during quantization, suggesting potential issues with settings, input data, or model design.
```log
Layer: 536  2-norm RE: 17.03%  cosine-sim: 0.9862
```

* Copy the model to `AXera-Pi` and run it directly (use the `scp` command to copy the `joint` format model file to the development board):
Run the model on the board:
```
time run_joint mobilenetv2.joint --repeat 100 --warmup 10
```
You’ll see the model execution time is `2.1ms`. Here we haven’t enabled the virtual NPU; if enabled, the time doubles to `4ms`. Additionally, `overhead 250.42 ms` represents other timing costs (e.g., model loading, memory allocation).
```
Run task took 2143 us (99 rounds for average)
        Run NEU took an average of 2108 us (overhead 9 us)

```
If you want to test inputs, first convert the image to binary content arranged in `HWC + RGB` order, and specify the binary file with `--data`.

.. details:: Script to convert to binary file
    ```python
    from PIL import Image
    import sys
    out_path = sys.argv[2]
    img = Image.open(sys.argv[1])
    img = img.convert('RGB')
    img = img.resize((224, 224))
    rgb888 = img.tobytes()
    with open(out_path, "wb") as f:
        f.write(rgb888)
    ```
    Execute `python convert.py cat.jpg cat.bin` to obtain the `cat.bin` file.
```
run_joint mobilenetv2.joint --data cat.bin --bin-out-dir ./
```
A `bin` file sized `4000` bytes, i.e., `1000` `float32` values, will be generated in the directory. You can load it with `python` to find the maximum value.
```python
out = np.fromfile("536.bin", dtype=np.float32)
print(out.argmax(), out.max())
```
The result is `282 8.638927`. In the [labels](https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt), index `282`, or line `283`, corresponds to `tiger cat`. This matches the result of running the floating-point model directly on the computer (`282 9.110947`), although there are slight differences, they are within an acceptable range.
> Note that no `softmax` calculation was performed here, so `out.max()` is not a probability.

## Writing Code to Run the Model

To formally run the model, you might need to modify the code, change input preprocessing, or add post-processing. Currently, a `C/C++` SDK is provided, and reference code is available at [ax-samples](https://github.com/AXERA-TECH/ax-samples). Cross-compilation is possible, or you can compile directly on `AXera-Pi`.

Code for running classification models is located in [ax_classification_steps.cc](https://github.com/AXERA-TECH/ax-samples/blob/main/examples/ax_classification_steps.cc). After compiling according to the repository’s instructions, you'll get the executable `build/bin/install/ax_classification`, which you can copy to the development board to execute:
```
./ax_classification -m mobilenetv2.joint -i cat.jpg
```
> The code uses `opencv` to read images in `BGR` format. When running the model, it automatically determines based on the conversion model configuration whether to convert to `RGB`. So, `mw::prepare_io` is used to copy the `BGR` image to the input buffer, and further processing is handed off to the underlying library.

If your model isn't a simple classification model, you may need to add post-processing code after model inference to parse the results.

## Using Cameras and Screens

At this point, the model runs independently. To build an application, since it’s `Linux`, many general development methods and libraries are available. If you wish to use cameras and screens together, you can use [libmaix](https://github.com/sipeed/libmaix) or develop directly using [axpi_bsp_sdk](https://github.com/sipeed/axpi_bsp_sdk) (which is somewhat more challenging).
* Refer to the [SDK Development Instructions](/hardware/en/maixIII/ax-pi/sdk.html) to compile and execute the [camera screen display routine](https://github.com/sipeed/libmaix/tree/release/examples/axpi). Since the repositories are on `github`, having a good proxy server is recommended.
* When merging the model execution code into the routine, one important issue to note: if you plan to use the camera, the default `AI-ISP` will be activated (no way to turn it off for now, TODO for future updates). **Therefore, when converting the model, specify it to run on the virtual NPU by setting `ax620_virtual_npu: AX620_VIRTUAL_NPU_MODE_111` in the configuration file, otherwise initialization will fail**.
> You can directly use the [1000-classification routine](https://github.com/sipeed/libmaix/tree/release/examples/axpi_classification_cam).
> After compilation on the board, execute `./dist/axpi_classification_cam -m mobilenetv2.joint` to start recognition. Models can also be downloaded from the [MaixHub Model Zoo](https://maixhub.com/model/zoo/89).


## QAT Quantization and Other Optimization Methods

`QAT` (Quantization Aware Training) involves simulating quantized inference during training to reduce quantization errors. Unlike `PTQ` (Post-training Quantization), which quantizes already trained models, `QAT` offers higher accuracy but is more complex. It is not recommended to start with `QAT`.

For more details, see [superpulsar](https://pulsar-docs.readthedocs.io). The documentation will continue to be updated, and if you're proficient in this area, feel free to click `Edit this page` in the upper right corner to contribute.


## Other References and Shared Summaries

> Feel free to share your work! Click `Edit this page` in the upper right corner to add your contributions.

* [爱芯元智AX620A部署yolov5 6.0模型实录](https://zhuanlan.zhihu.com/p/569083585)
* [AX620A运行yolov5s自训练模型全过程记录（windows）](http://t.csdn.cn/oNeYG)
* [MOT：如何在爱芯派上实现多目标跟踪的神奇效果！](https://www.yuque.com/prophetmu/chenmumu/ax_tracker)
* [MMPose：在爱芯派上玩转你的关键点检测！](https://www.yuque.com/prophetmu/chenmumu/m3axpi_keypoint)
* [2023年最新 使用 YOLOv8 训练自己的数据集，并在 爱芯派硬件 上实现 目标检测 和 钢筋检测 ！！](https://www.yuque.com/prophetmu/chenmumu/m3axpi)
