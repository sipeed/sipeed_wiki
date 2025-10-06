---
title: Flashing on linux
keyeords: Linux, FPGA, Gowin
---

It's recommended to use **openFPGALoader** to flash the development board from linux environments. This page covers installation instructions and has been verified on Ubuntu but may work on other linux distributions.

The currently available package on Ubuntu is older ('openfpgaloader') and does not support the latest boards (i.e. tangnano20k), because of this compiling the latest git source is recommended and covered below (adapted from the official projects documentation: https://trabucayre.github.io/openFPGALoader/guide/install.html).

### Compiling openFPGALoader from git

1. Install build dependences
2. Clone the source code
3. Configure and compile the code
4. Install

```bash
# Install build dependencies
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

### Optionally install Udev rules

Using the board may require root permissions if Uden rules are not used. If this is not done you will likely need to run `openFPGAloader` as root or with `sudo` each time.

```bash
# Working in the openFPGAloader/ directory
# Copy the Udev rules to the correct directory
sudo cp 99-openfpgaloader.rules /etc/udev/rules.d/
# Reload the udev rules and activate them
sudo udevadm control --reload-rules && sudo udevadm trigger # force udev to take new rule
# Add the current user to the plugdev group
sudo usermod -a $USER -G plugdev # add user to plugdev group
```

### Flashing the board

First ensure openFPGAloader detects the cable and device.

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

Flash the bitstream to the device as shown below. The board name must be specified after the `-b` option, `-f` options means the file is programmed to the non-volatile flash, without it it will be stored in SRAM but lost if the device loses power.

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
#### Board names

You can find the list of supported tang boards using the command `openFPGAloader --list-boards | grep tang`.

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
