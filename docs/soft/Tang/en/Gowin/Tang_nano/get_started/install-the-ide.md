# Download

Go to the official website http://www.gowinsemi.com.cn/faq.aspx, you can see the software list below, select the version of the system suitable for the computer to download.

![1-1](./../assets/gowin_down.png)

## Installation

**Windows** User:

Double-click the downloaded exe installation file, select the installation language, installation location, click the next step to complete the installation.

Be sure to install the driver that prompts you to install when you complete the installation.

![2-1](./../assets/gowin_install.png)

Check the installation driver and click Finish, the driver will be installed.

**Linux** User:

TODO

## license

There are currently two ways to license.

**The first type: use the stand-alone version of the licence (need to apply for license)**

Send an application email to `Support@sipeed.com` under the heading `[Apply Tang Lic] MAC: XXXXXX`. The content template is as follows

```
Company Name:
Company Website:
Department:
Contact Person:
Contact No.:
Email:
Media Access Control Address(MAC):
Type of License: Shared Type, Local Only
Operating System: Windows, Linux
```

When you open the High Cloud IDE, in the license management that pops up, select your local license path.

![3-5](./../assets/lic_file_5.png)

Then you need to add the path of the license of synplifypro to the system variable. The following is a brief introduction to an add method. In ` `The second: use the sipeed license server networking activation`, there is a more detailed introduction.

**Windows** User press win+r on the keyboard, enter `cmd` in the pop-up window, click OK to pop up the black command line window, enter the following command, `path_to_the_file` is your `gowin_Synplifypro.lic Path of `.

```
setx LM_LICENSE_FILE path_to_the_file
```

**Second: Network activation with license server using sipeed**

This method is simple to configure, but you can't use the software without a network.

After downloading the software, the software will prompt you for a licence. Fill in the server address `45.33.107.56` in the pop-up box, IDE port: 10559.

![3-6](./../assets/lic_remote_1.png)

The activation of the synopsys advanced function requires adding the environment variable `LM_LICENSE_FILE=27020@45.33.107.56` to the system.

**Windows** User presses win+r on the keyboard, enter `cmd` in the pop-up window, click OK to pop up the black command line window, enter the following command.

```
setx LM_LICENSE_FILE 27020@45.33.107.56
```

Windows can be added in addition to the command line. You can also add it by right-clicking Computer->Properties->Environment Variables and then adding it as shown below.

![3-7](./../assets/lic_remote_2.png)

**Linux** users need to add in `~/.bashrc`

```
Export LM_LICENSE_FILE 27020@45.33.107.56
```

After entering the IDE, click on `Synplify Pro` in Tools.

![3-8](./../assets/lic_remote_3.png)

Then the interface will pop up as shown below. At this time, you need to wait for a short time. After the license is initialized, you can use it.

![3-9](./../assets/lic_remote_4.png)

## Instructions

Refer to the official documentation [Gowin Source Software User Guide] (http://cdn.gowinsemi.com.cn/SUG100-1.8_Gowin%E4%BA%91%E6%BA%90%E8%BD%AF%E4%BB%B6%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf), Chapter 5 Cloud Source Software Usage.

## Reference document

+ [Gowin Software Introduction and Installation](http://cdn.gowinsemi.com.cn/%E9%AB%98%E4%BA%91%E8%BD%AF%E4%BB%B6%E7%AE%80%E4%BB%8B%E5%92%8C%E5%AE%89%E8%A3%85.pdf)

## How to Flash Tang FPGA in Linux

We suggest use **openFPGALoader** flash Tang boards in Ubuntu, here is the steps:

### install openFPGALoader
refer to：https://trabucayre.github.io/openFPGALoader/guide/install.html
```
# preprocess
sudo apt-get install libftdi1-2 libftdi1-dev libhidapi-hidraw0 \
  libhidapi-dev libudev-dev zlib1g-dev cmake pkg-config make g++
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

### Flash method
detect board
```
$ ./openFPGALoader --detect
Jtag frequency : requested 6.00MHz   -> real 6.00MHz  
index 0:
	idcode 0x100481b
	manufacturer Gowin
	family GW1N
	model  GW1N(R)-9C
	irlength 8
detach error -5

```
download bitstreams
```
$ ./openFPGALoader -b tangnano9k -f ../../nano9k_lcd/impl/pnr/Tang_nano_9K_LCD.fs
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
detach error -5

```

the -b indicate target board, it can be the value of:

|Board name|FPGA|Memory|Flash|
|--|--|--|--|
|tangnano|GW1N-1 QFN48|OK|Internal Flash|
|tangnano1k|GW1NZ-1 QFN48|OK|Internal Flash|
|tangnano4k|GW1NSR-4C QFN48|OK|Internal Flash/External Flash|
|tangnano9k|GW1NR-9C QFN88|OK|Internal Flash/External Flash|


