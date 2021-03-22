---
title: MaixPy Development History
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: MaixPy development history
---


Write down the development history of this article, hoping to let future developers know what MaixPy has gone through, what are the reasons for some major changes, and when major progress has been made.


The code submission history can be seen in the [historic](https://github.com/sipeed/MaixPy/commits/historic) and [master](https://github.com/sipeed/MaixPy/commits/master) branches


## September 2018

The MaixPy project was launched, and the opportunity was the completion of the K210 chip tapeout.

So everyone wanted to make a set of easy-to-use software kits that allow more people to use AI development in embedded applications. Because of the ease of use of Micropython, and the k210 has 6+2MiB memory, the main frequency is 400MHz, and it is fully capable of controlling Micropython. Micropython is selected as the programming syntax

Based on the development board Maix dock, the name is now called Lichee Pill, and the QQ group name is also called Lichee Pill Alchemy Group

[xiaohui](https://github.com/xiaoxiaohuixxh) and [wipping](https://github.com/wipping) started to try to port Micropython

## December 2018

K210 SDK was replaced from freertos to standalone SDK, and the on-chip peripheral driver adaptation was started

[neucrack](https://github.com/neutree), [xel](https://github.com/xelll) and [zepan](https://github.com/Zepan) join the project team


## February 2019

Release the first version of the firmware [v0.1.1 beta](https://github.com/sipeed/MaixPy/releases/tag/v0.1.1), support basic peripherals, inherit the image sensor lcd API of openmv, Equipped with some open source tools such as upyloader, armpy, etc., write documents and publish them on maixpy.sipeed.com

In addition, there are also two new development boards, Maix bit and Maix Go.

Xiaohui left the project team

## March 2019

Release the second version of the firmware [v0.2.4](https://github.com/sipeed/MaixPy/releases/tag/v0.2.4), adding support for jpeg, wav, kpu, nes, avi, lvgl, etc.


## April 2019

Adapted to OpenMV IDE, which is MaixPy IDE, based on the original software, only USB communication is changed to serial communication supported by k210, and other functions remain unchanged

The pre-compiled firmware began to differentiate the function into multiple firmware, mainly considering the problem of insufficient memory in the running model

wipping left the project team, zepan and xel focused on other project teams


## June 2019


The project structure was refactored. Previously, the code was directly added to the directory structure of micropython and the code was added to the port directory. However, there would be a problem, that is, updating the micropython program becomes more troublesome, and you need to separate the code added by micropython and MaixPy , And the old code structure is too messy, the Makefile is not very well written, and the build is slow.
So with the current directory structure, cmake + kconfig is used to build the project, and each component is modularized, and you can choose whether to compile into the firmware. The compilation framework is [here](https://github.com/Neutree/ c_cpp_project_framework). But there are still some remaining problems. There are some legacy codes under the directory that are not fully coupled.


## July 2019

Added support for M5Stick-V development board, maintained by [Martin Han](https://github.com/MarsTechHAN)


## December 2019

[Maixhub](https://www.maixhub.com) is online, used for online model training, only need to upload data set without writing code

Hardware update: online M1N module, golden finger module

## April 2020

[Sugar Lao Duck](https://github.com/QinYUN575) Join the project team


## May 2020

[Big Rats](https://github.com/junhuanchen) Join the project team

## June 2020

Hardware update: Maix Cube development board is online

## July 2020

Add board-level configuration files for different boards, put them in the file system, and read them after booting. This is mainly because Cube and Amigo add power chips. In order to use them normally, you must first set the power chip when booting.

Hardware update: Maix Amigo development board is online, with a shell added

## November 2020

Reorganize the documents, more perfect documents and communities
