# NeoRV32 on nano 9K

## Preface

NeoRV32 is a powerful RISCV5 core

![](https://github.com/stnolting/neorv32/raw/main/docs/figures/neorv32_processor.png)

There is an example neorv32 project using the built in 72kb of user flash as instruction memory and with GPIO and JTAG enabled for debugging: [Tang Nano 9K github repository](https://github.com/jimmyw/tang_nano_9k_neorv32).

## Environment

- [Gowin IDE](./../../common-doc/install-the-ide.md)
- [GCC Toolchain](https://stnolting.github.io/neorv32/ug/#_software_toolchain_setup)

## Steps

### Program FPGA

- Clone example repo `git clone git@github.com/jimmyw/tang_nano_9k_neorv32`
- Open tang_nano_9k project by `tang_nano_9k.gprj` file in `src` directory
- Right-click Place&Route which is in Process interface and choose Clean&Rerun All
- Compile the userspace code in `hello_world` using `make all`
- Download the generated .fs file to the Embedded Flash of Nano 9K using `openFPGALoader -f impl/pnr/tang_nano_9k.fs  --user-flash hello_world/neorv32_raw_exe.bin`

You can at a later state update the user space flash directly from the bootloader using `python uart_upload.py /dev/ttyUSB0 neorv32_exe.bin`

