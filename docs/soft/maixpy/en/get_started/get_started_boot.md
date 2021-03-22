---
title: boot script
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: boot script
---


The system will create the `boot.py` file and `main.py` in the `/flash` or `/sd` (priority) directory, and automatically execute `boot.py` first, and then execute `main.py` (if If the SD card is detected, execute the SD card), edit the contents of these two scripts to achieve self-startup. If you write an infinite loop (While True) program in `boot.py`, it will cause `main.py `Can't run (call `boot.py` first and then `main.py`), and re-send `boot.py` without infinite loop to solve it.

- boot.py is mainly used to configure the hardware and only needs to be configured once.
- main.py can be used for the main running program.

The corresponding specific implementation [code here](https://github.com/sipeed/MaixPy/blob/972059491227ece63fbfc2cd0e78fe13ee78427d/components/micropython/port/src/maixpy_main.c#L586-L595), if you have any questions, just look at the source .

note:
    * The Micro SD card should be formatted as FAT (FAT32) file system
    * FAT formatted memory card will be mounted to `/sd`, and SPIFFS in internal Flash will be mounted to `/flash`
