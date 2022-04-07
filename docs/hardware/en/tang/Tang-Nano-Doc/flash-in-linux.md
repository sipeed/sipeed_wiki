---
title: Flash in linux
keyeords: Linux, FPGA, Gowin
---

It's suggested to use **openFPGALoader** to flash te development board in Ubuntu.
Other linux distributions have not been verified.

The steps are as shown:

### Install openFPGALoader

Reference：https://trabucayre.github.io/openFPGALoader/guide/install.html

Using the following commands in terminal:

```bash
# preprocess
sudo apt-get install libftdi1-2 libftdi1-dev libhidapi-hidraw0 libhidapi-dev libudev-dev zlib1g-dev cmake pkg-config make g++
# compile
git clone https://github.com/trabucayre/openFPGALoader.git
cd openFPGALoader
mkdir build
cd build
cmake ../ # add -DBUILD_STATIC=ON to build a static version
          # add -DENABLE_UDEV=OFF to disable udev support and -d /dev/xxx
          # add -DENABLE_CMSISDAP=OFF to disable CMSIS DAP support
cmake --build .
# or
# make -j$(nproc)
# install
sudo make install
```

### Flash

Detect board

```bash
$ sudo ./openFPGALoader --detect # This command should be executed in the directory where you previously executed make install  
# The log of succeed running is shown below
Jtag frequency : requested 6.00MHz   -> real 6.00MHz
index 0:
        idcode 0x100481b
        manufacturer Gowin
        family GW1N
        model  GW1N(R)-9C
        irlength 8


```

Download bitstream

```bash
$ sudo ./openFPGALoader -b tangnano9k -f ../../nano9k_lcd/impl/pnr/Tang_nano_9K_LCD.fs
# -b means target model，this can be found in the form below
# -f means download to flash，with it means download to sram
# The last is what need to be downloaded, it should be the related .fs file
# The log of succeed running is shown below
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

-b means target development board, should be decided from the form below：

| Board name | FPGA            | Memory | Flash                         |
| ---------- | --------------- | ------ | ----------------------------- |
| tangnano   | GW1N-1 QFN48    | OK     | Internal Flash                |
| tangnano1k | GW1NZ-1 QFN48   | OK     | Internal Flash                |
| tangnano4k | GW1NSR-4C QFN48 | OK     | Internal Flash/External Flash |
| tangnano9k | GW1NR-9C QFN88  | OK     | Internal Flash/External Flash |