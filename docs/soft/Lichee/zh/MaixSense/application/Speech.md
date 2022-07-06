---
title: Maix-Speech 在R329上的应用
keywords: R329, Speech, 语音
---
- Maix-Speech 是专为嵌入式环境设计的离线语音库，设计目标包括：ASR/TTS/CHAT
- 不建议新手使用

## 准备环境
- Ubuntu 18.04 以上
- gcc 7.5 以上，
- CMake 3.20以上，
- anaconda虚拟环境
- 在x86 (Linux)或其他架构的系统里编译，需要额外安装工具链和库(`Ubuntu` 为例)
    ```
    sudo apt install build-essential libasound2-dev
    ```

* 下载交叉编译工具链，并解压到合适的文件夹。例如 `R329`, 从[release](https://github.com/sipeed/Maix-Speech/releases)下载 `r329_toolchain.tar.gz`, 并解压到一个合适的路径，比如 `/opt/r329_toolchain`。又比如 `v83x`, 在[这里](https://github.com/sipeed/libmaix)找到工具链下载链接并下载工具链，解压到一个文件夹，比如`/opt/toolchain-sunxi-musl`。

| 架构 | 前缀名 | 工具链 |
|:---: |----- | ------|
| r329 | aarch64-openwrt-linux-         | [release](https://github.com/sipeed/Maix-Speech/releases) 下寻找 r329 toolchain |
| v83x | arm-openwrt-linux-muslgnueabi- | [sipeed/libmaix](https://github.com/sipeed/libmaix) README 中寻找 |
| armv7| arm-linux-gnueabihf-           | [linaro(v3s)](https://wiki.sipeed.com/soft/Lichee/zh/Zero-Doc/System_Development/uboot_build.html) 或者其它 arm-linux-gnueabihf toolchain  |
| armv7musl | arm-openwrt-linux-muslgnueabi- | [sipeed/libmaix (v83x)](https://github.com/sipeed/libmaix) README 中寻找 |
| aarch64   | aarch64-openwrt-linux-         | [release](https://github.com/sipeed/Maix-Speech/releases) 下寻找 r329 toolchain |
| riscv64   | riscv64-unknown-linux-gnu-     | |

## 代码仓库:

```
git clone https://github.com/sipeed/Maix-Speech
```


对应的项目结构

```
.
├── assets
│   └── test_files                 # 提供的测试文件，方便上手测试
├── components                     # 组件
│   ├── asr_lib                    # 组件 asr_lib
│   │   ├── CMakeLists.txt         # 组件配置文件
│   │   ├── include                # 头文件
│   │   ├── Kconfig                # 组件 menuconfig 配置文件
│   │   ├── lib                    # 各个平台的库文件
│   │   └── src                    # 源文件
│   └── utils                      # 工具类组件，包括了跑分、字体等
├── Kconfig                        # 最顶级的 menuconfig 配置文件
├── LICENSE                        # 开源协议（证书）
├── projects                       # 项目
│   └── maix_asr                   # ASR 项目
│       ├── CMakeLists.txt         # 项目配置文件
│       ├── main                   # 项目里面的主组件
│       └── project.py             # 构建脚本，方便输入命令
├── README.md                      # 项目首页英文文档
├── README_ZH.md                   # 项目首页中文文档
├── tools                          # 项目构建相关代码，一般不用看
└── usage_zh.md                    # 使用方法
```


## 编译

* 在x86 (Linux) 或在其它架构的系统里编译时，例如`R329`或 `树莓派`应使用对应的`GCC`

> conda 环境下工具链可能有问题，如果出现错误可以先尝试退出conda环境使用转用原生环境编译   

```bash{.line-numbers}
cd projects/maix_asr               # 打开对应的文件夹

python project.py clean_conf       # 清除工具链配置
python project.py menuconfig       # 配置选择芯片架构（ARCH），默认是 x86

python project.py build
#python project.py rebuild         # 如果有新建文件需要使用 rebuild
#python project.py build --verbose # 打印详细构建过程

./build/maix_asr                   # 测试下运行可执行文件，可以执行即可

python project.py clean            # 清除构建内容
python project.py distclean        # 彻底清除构建内容, 包括 menuconfig 内容

```

* 其它架构（交叉编译）

[前面](#准备环境)已经说明不同架构相应的编译工具链，在编译时需要配置一下相应的工具链信息。

需要配置：
* 工具链可执行文件所在文件夹路径，比如`/opt/r329_toolchain/bin` `/opt/toolchain-sunxi-musl/bin`
* 工具链前缀，可在前面的表格中找到， 比如`aarch64-openwrt-linux-`

```bash{.line-numbers}
cd projects/maix_asr
# 配置工具链位置和前缀， distclean 不会清除工具链配置, 这会在目录下生成一个 .config.mk 文件
python project.py --toolchain 工具链可执行文件路径路径 --toolchain-prefix 前缀名 config
# python project.py --toolchain /opt/r329_toolchain/bin --toolchain-prefix aarch64-openwrt-linux- config

python project.py menuconfig       # 选择目标架构
python project.py build

# python project.py clean_conf     # 清除工具链配置
```

关于更详细地如何使用编译框架请看 [github.com/Neutree/c_cpp_project_framework](https://github.com/Neutree/c_cpp_project_framework)


## 运行语音识别例程

以 `x86(Linux)` 平台为例的快速验证 demo， 其它需要交叉编译的平台自行复制可执行文件到开发板的系统再运行:

* 先保证编译通过， 可执行文件 `projects/maix_asr/build/maix_asr` 存在并且可以运行
* 在 [release 页面](https://github.com/sipeed/Maix-Speech/releases) 找到 `am_7332.zip` 和 `lmM.zip` 文件并下载， 解压到`assets/test_files` 目录, 解压后的`assets`目录结构如下
```
assets
├── image
└── test_files
    ├── 1.2.wav
    ├── am_7332
    ├── asr_wav.cfg
    └── lmM
```

上面主要包含了两种模型 —— 声学模型`AM` 和 语言模型`LM`。每种模型又有几种模型大小选择，精度越大资源消耗越大。另外还有字体文件。

下面不同平台实时运行的典型配置：
```{.line-numbers}
Cortex-A7  1.0GHz, <=128M 系统内存：am_3316 + lmS, is_mmap=1, beam<5
Cortex-A7  1.0GHz, >=256M 系统内存：am_3316 + lmM, is_mmap=0, beam=5~10
Cortex-A53 1.2GHz, >=256M 系统内存：am_3324 + lmM, is_mmap=0, beam=5~10
Cortex-A72 1.5GHz, >=1G   系统内存：am_3332 + lmL, is_mmap=0, beam=5~10
```

带[NPU](https://baike.baidu.com/item/NPU/17905535)的硬件平台，选用对应转换好的 `NPU` 硬件加速的声学模型，比如`R329`需要下载对应的`r329_7332_192.bin`， 然后根据系统内存大小选择对应的语言模型。语言模型目前没有硬件加速，均使用 CPU 运算。

```bash{.line-numbers}
cd assets/test_files                                #进入到 test_files 目录
../../projects/maix_asr/build/maix_asr asr_wav.cfg  #执行测试
#可以看到语音识别的结果
HANS: 一点 二三 四五 六七 八九 
PNYS: yi4 dian3 er4 san1 si4 wu3 liu4 qi1 ba1 jiu3 
```

如果是 `Windows` 需要 `GBK`编码则需要修改`asr_wav.cfg`中的 `words_txt:lmM/words_utf.bin` 为 `words_txt:lmM/words.bin` 。

测试其他 `wav` 文件只需要修改 `asr_wav.cfg` 中的 `device_name` 到对应测试 `wav` 路径即可。
测试其它模型，修改`model_name`指定文件路径即可。

**注意** wav 需要 **16KHz** 采样，**S16_LE** 的存储格式。另外还支持 `PCM` 或者 `MIC` 实时识别，详见 [usage_zh.md](./Speech_usage_zh.md) 中对 cfg 文件的介绍。

> 可以使用工具转换，比如 `arecord -d 5 -r 16000 -c 1 -f S16_LE audio.wav`


## 详细使用文档

请看[使用文档](./Speech_usage_zh.md)


## Maix ASR 模型选择

MAIX ASR **声学模型**按尺寸分为：7332,3332,3324,3316。  
大小如下表：

|model|7332|3332|3324|3316|
|--|--|--|--|--|
|float(MB)|44|28|18|10|
|int8(MB)|11|7|4.5|2.5|

MAIX ASR **语言模型**可以自由选择，默认开放三种尺寸的模型：lm_s,lm_m,lm_l  
每种模型分成 sfst, sym, phones, words 四部分，其中 sym,phones,words 仅用于输出字符串使用，无需加载入内存，仅放在磁盘。sfst为解码图文件（LG.fst的压缩版），可选载入内存或者mmap实时读取。  
表中的wer表示 aishell 测试集的汉字转拼音作为输入，通过LM转汉字后的错误率

|model|lmS|lmM|lmL|lmXL|
|:--:|:--:|:--:|:--:|:--:|
|sfst|12MB|104MB|750MB|3700MB|
|sym|6.5MB|59MB|404MB|1940MB|
|phones|12KB|13KB|13KB|13KB|
|words|8.0MB|72MB|72MB|107MB|
|WER|2.78%|1.94%|1.61%|1.24%|

以下是各个模型的benchmark  
pny wer表示带声调的拼音错误率，lmX表示加上对应语言模型后的汉字错误率  

|model/len|pny wer |lmS 12M |lmM 104M|lmL 750M| 
|:--:     |:--:    |:--:    |:--:    |:--:    |
|7332 11MB|||||
|192      |17.7    |13.1   |11.1   |10.0   |
|ali192   |9.94    |9.02   |7.56   |6.53   |
|non-flow |8.63    |7.81   |6.60   |5.38   |
|3332 7MB |||||
|128      |16.4    |13.3   |11.9   |11.0   |
|192      |11.6    |8.73   |7.22   |6.48   |
|non-flow |10.6    |8.46   |6.71   |5.94   |
|3324 4.5MB|||||
|128      |23.4    |20.4   |19.4   |18.5   |
|192      |11.3    |13.7   |9.66   |8.55   |
|non-flow |12.2    |10.2   |8.65   |7.56   |
|3316 2.5M|||||
|128      |25.5    |19.2   |17.4   |16.0   |
|192      |16.9    |12.9   |11.4   |10.1   |
|non-flow |16.1    |11.2   |11.0   |9.68   |

模型说明：  
- 下划线后的数字表示选取的帧长度，如192表示一帧为192x8=768ms，asr库每采集完一帧后进行一次处理  
- 帧长度关系到识别延迟，如192就会最大有768ms延迟，128则为512ms，可见帧长的模型错误率更优，但是延迟稍长  
- 表中默认为流式识别，使用有限的上下文（一帧长度），noflow表示非流式识别（整体识别），可见非流式识别错误率大幅下降  
- ali表示对齐优化后的结果，即类sMBR处理后的结果，可见对齐训练后错误率大幅下降。  
附件默认上传了192长度的流式识别模型，需要其他识别模型的可以联系矽速。


## Maix-Speech TTS 

* TODO


## Maix-Speech CHAT

* TODO

## TODO List

- [ ] Support English
- [ ] Test Conformer
- [ ] Support TTS
- [ ] Support CHAT

## License

项目使用 [Apache 2.0](./LICENSE) 开源协议，以及其引用和使用的开源项目的开源协议见 [LICENSE](./LICENSE)

## 致谢

MaixSpeech 借鉴和使用了一些优秀的开源项目，并咨询了一些业内大佬，包括：

1. WFST 解码 [Kaldi](http://kaldi-asr.org/)
2. 前端推理框架 [MNN](https://github.com/alibaba/MNN)
3. ARM中国 周易团队,尤其是toby
4. wenet 彬彬大佬；原cvte大佬 pfluo；


## 其他
Maix-Speech 目前以静态库形式提供给用户评估使用，有商业定制需求的用户可以发邮件到 <support@sipeed.com> 咨询
