---
title: Linux 下烧录方法
keyeords: Linux, FPGA, Gowin
---

## openFPGAloader

在Ubuntu系统下我们建议使用**openFPGALoader**烧写，其他发行版尚未验证。以下为具体步骤

### 安装openFPGALoader

参考：https://trabucayre.github.io/openFPGALoader/guide/install.html

直接在linux命令行执行下面命令即可

```bash
# preprocess
sudo apt-get install libftdi1-2 libftdi1-dev libhidapi-hidraw0 libhidapi-dev libudev-dev zlib1g-dev cmake pkg-config make g++
# compile
git clone https://github.com/trabucayre/openFPGALoader.git
cd openFPGALoader
mkdir build
cd build
cmake ../ 
#build
cmake --build . -j$(nproc)
# install
sudo make install
```

### 烧录方法

检测板卡
```bash
$ sudo ./openFPGALoader --detect # 对于这行命令应当在你上一步执行make install的目录下执行 
# 下面是正常执行后显示的log
Jtag frequency : requested 6.00MHz   -> real 6.00MHz
index 0:
        idcode 0x100481b
        manufacturer Gowin
        family GW1N
        model  GW1N(R)-9C
        irlength 8
```

下载码流

```bash
$ sudo ./openFPGALoader -b tangnano9k -f ../../nano9k_lcd/impl/pnr/Tang_nano_9K_LCD.fs
# 其中的 -b 表示目标板型号，具体可以参考下面表格
# -f 表示下载到 flash，不加的话会下载到 sram 中
# 最后的是需要烧录的文件，应该找到对应目录下的 .fs 文件
# 下面是成功执行后的log
write to flash
Jtag frequency : requested 6.00MHz   -> real 6.00MHz  
Parse file Parse ../../nano9k_lcd/impl/pnr/Tang_nano_9K_LCD.fs: 
Done
DONE
Jtag frequency : requested 2.50MHz   -> real 2.00MHz  
erase SRAM Done
erase Flash Done
write Flash: [==================================================] 100.00%
Done
CRC check: Success

```

其中-b表示目标板型，可以使用以下取值：

| Board name    | FPGA                | Memory | Flash          |
| ------------- | ------------------- | ------ | -------------- |
| tangnano      | GW1N-1 QN48         | OK     | Internal Flash |
| tangnano1k    | GW1NZ-1 QN48        | OK     | Internal Flash |
| tangnano4k    | GW1NSR-4C QN48      | OK     | Internal Flash |
| tangnano9k    | GW1NR-9C QN88P      | OK     | Internal Flash |
| tangnano20k   | GW2AR-18C QN88      | OK     | External Flash |
| tangprimer20k | GW2A-18C BGA256     | OK     | External Flash |
| tangprimer25k | GW5A-25A BGA121     | OK     | External Flash |
| tangmega60k   | GW5AT-60B BGA484    | OK     | External Flash |
| tangmega138k  | GW5AT-138B/C BGA484 | OK     | External Flash |