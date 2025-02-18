---
title: Primer 20K Lite blink led
keywords: Primer 20K, Lite, FPGA
desc: Primer 20K start
tags: FPGA, Primer 20K
update:
  - date: 2022-10-18
    version: v0.1
    author: wonder
    content:
      - First time edit
---

Let's blink a led after getting the Tang Primer 20K Lite suits.

## Preread

This document is writen for guiding user start preparing GOWIN development environment and use the Tang Primer 20K.

The default firmware function in the Core board is as followings:
- All IO port routed to pin 2.54mm pad toggles regularly, including spi_lcd connector ports and sd_card connector ports on Core Board
- DDR test; Test result print_out by serial port connector on Core Board and we can use serial tool in computer to see

Because of the DDR test function, Core Board will be very hot. you can erase the firmware in the Core Board if you mind this. And default firmware project can be found here: [github](https://github.com/sipeed/TangPrimer-20K-example/tree/main/Lite-bottom%20test%20project/test_board)

## Install IDE

Visit [Install IDE](./../../../common-doc/install-the-ide.md) to prepare the environment for this FPGA.

For Linux users, if it's difficult to run Programmer application to burn firmware into fpga, please visit [OpenFpgaloader](https://wiki.sipeed.com/hardware/en/tang/common-doc/flash-in-linux.html) to see how to use it.

## New Project

New Project：File-->NEW-->FPGA Design Project-->OK

<img src="./../../../Tang-Nano-1K/assets/LED-1.png" width=35% alt="new_project">

Set Project Name and path, Project Name and project path should be English.

![project_path](./../../../../../../../news/others/20k_lite_start/assets/project_path.png)

Select Device we choose GW2A-LV18PG256C8/I7, use filter like below to help us choose device more easily. Note that the Device is GW2A-18C.

![device_choose](./../../../../../../../news/others/20k_lite_start/assets/device_choose.png)

Then click OK to preview the project. After confirming no error, the project is created.

## New file

Gowin IDE contains 3 ways to create file. Here we use shortcut keys `Ctrl + N` to new a file. The other 2 ways to new file are not mentioned here,

In the pop-up windows, we choose `Verilog File`, you can also choose `VHDL File` if you are good at it. Here we just use Verilog as an example.

<img src="./../../../../../../../news/others/20k_lite_start/assets/new_verilog_file.png" width=50% alt="new_verilog_file">

Then click OK to set the file name, here we take `led` as the verilog file name as example.

<img src="./../../../../../../../news/others/20k_lite_start/assets/file_name.png" width=75% alt="file_name">

Up to now we have finished creating file, then we need to prepare our code.

![created_file](./../../../../../../../news/others/20k_lite_start/assets/created_file.png)

### Verilog introduction

Verilog is a kind of Hardware Description Language(HDL), it's used to describe digital circuits.

The basic unit in Verilog is module.

A module is composed of two parts: one describes the interface, and the other describes the internal logic function, that is, defines how the input affects the output.

A module is like this:

```v
module module_name
#(parameter)
(port) ;
    function   
endmodule
```

The module starts from module and ends by endmodule. The module is followed by the module name (module_name), transitable variable parameters (parameter), port and direction declaration (port), followed by internal logic function description (function), and finally, endmodule is used to represent this module.

The internal logic function is usually composed by the assign and always blocks; The assign statement describes logical circuit, and the always block is used to describe timing circuit.

### Think storm

Before coding, we need to think our purpose: The led flashes every 0.5S.

Then we draw a demand block diagram as follows:

![block_method](./assets/block_method.png)

Then we need a counter to time of every 0.5S, LED flashes means IO flip.

![count_block](./assets/time_count.png)

Put the thought diagram into practical use, then it will look like this:

![clock_time_count](./assets/clock_time_count.png)

The Clock is the clock source, providing the accurate time for the time counter.

### Code description

From the verilog introduction and think storm diagram above, we can see the module we will create contains 2 ports:

```v
module led(
    input  Clock,
    output IO_voltage
);

endmodule
```

For time counter inside module, crystal oscillator on the Primer 20K core board is 27MHZ, so we have 27 million times rising edges per second, and we just need to count 13500000 times rising edges to get 0.5 seconds. The counter starts from `0`, and to count 13500000 times rising edges, we count to 13499999. When counted to 0.5S, we set a flag to inform LED IO to flip its voltage. The overall count code is as follows:

```v
//parameter Clock_frequency = 27_000_000; // Crystal oscillator frequency is 27Mhz
parameter count_value       = 13_499_999; // The number of times needed to time 0.5S

reg [23:0]  count_value_reg ; // counter_value
reg         count_value_flag; // IO change flag

always @(posedge Clock) begin
    if ( count_value_reg <= count_value ) begin //not count to 0.5S
        count_value_reg  <= count_value_reg + 1'b1; // Continue counting
        count_value_flag <= 1'b0 ; // No flip flag
    end
    else begin //Count to 0.5S
        count_value_reg  <= 23'b0; // Clear counter,prepare for next time counting.
        count_value_flag <= 1'b1 ; // Flip flag
    end
end
```

The code to change IO voltage are as follows:

```v
reg IO_voltage_reg = 1'b0; // Initial state

always @(posedge Clock) begin
    if ( count_value_flag )  //  Flip flag 
        IO_voltage_reg <= ~IO_voltage_reg; // IO voltage flip
    else //  No flip flag
        IO_voltage_reg <= IO_voltage_reg; // IO voltage constant
end
```

Combined with the codes above, it goes like this:

```v
module led(
    input  Clock,
    output IO_voltage
);

/********** Counter **********/
//parameter Clock_frequency = 27_000_000; // Crystal oscillator frequency is 27Mhz
parameter count_value       = 13_499_999; // The number of times needed to time 0.5S

reg [23:0]  count_value_reg ; // counter_value
reg         count_value_flag; // IO chaneg flag

always @(posedge Clock) begin
    if ( count_value_reg <= count_value ) begin //not count to 0.5S
        count_value_reg  <= count_value_reg + 1'b1; // Continue counting
        count_value_flag <= 1'b0 ; // No flip flag
    end
    else begin //Count to 0.5S
        count_value_reg  <= 23'b0; // Clear counter,prepare for next time counting.
        count_value_flag <= 1'b1 ; // Flip flag
    end
end

/********** IO voltage flip **********/
reg IO_voltage_reg = 1'b0; // Initial state

always @(posedge Clock) begin
    if ( count_value_flag )  //  Flip flag 
        IO_voltage_reg <= ~IO_voltage_reg; // IO voltage flip
    else //  No flip flag
        IO_voltage_reg <= IO_voltage_reg; // IO voltage constant
end

/***** Add an extra line of code *****/
assign IO_voltage = IO_voltage_reg;

endmodule
```

Because the `IO_voltage` is declared in the port position, which is wire type by default. To connect it to the reg variable `IO_voltage_reg`, we need to use assign. 

## Synthesize, constrain, place&route

### Synthesize

After finishing the code, go to the "Process" interface and double click "Synthesize" to synthesize our code to convert the verilog code content to netlist.

![Synthesize](./../../../../../../../news/others/20k_lite_start/assets/synthesize.png)

### Constraint

After Synthesizing our code, we need to set constrains to bind the ports defined in our code to fpga pins, by which we can realize our module function on fpga. 

Click the FloorPlanner in the top of Synthesize to set constrains.

![FloorPlanner](./../../../../../../../news/others/20k_lite_start/assets/floorplanner.png)

Since this is the first time we create it, the following dialog box will pop up. Click OK and the graphical constraint interface will pop up.

![create_constrain_file](./../../../../../../../news/others/20k_lite_start/assets/create_constrain_file.png)

![floorplanner_intreface](./../../../../../../../news/others/20k_lite_start/assets/floorplanner_interface.png)

The ways to constraint the file can be get from this docs: [SUG935-1.3E_Gowin Design Physical Constraints User Guide.pdf](https://dl.sipeed.com/fileList/TANG/Nano%209K/6_Chip_Manual/EN/General%20Guide/SUG935-1.3E_Gowin%20Design%20Physical%20Constraints%20User%20Guide.pdf)

Here we only use the IO Constraints method shown below to constrain the pins:

![floor_planner_ioconstrain](./../../../../../../../news/others/20k_lite_start/assets/floor_planner_ioconstrain.png)

According to [Schematic of core board](https://dl.sipeed.com/shareURL/TANG/Primer_20K/02_Schematic), we can know the input pin of crystal oscillator is H11。

<img src="./../../../../../../../news/others/20k_lite_start/assets/crystal_port.png" alt="crystal_port" width=45%>

Taking into consideration the IO screen printing on the ext_board, we decide to use the L14 pin on the ext_board for flashing.

![l14_port](./../../../../../../../news/others/20k_lite_start/assets/l14_port.png)

So for the IO Constraints under the FloorPlanner interactive window, we fill in the following values for PORT and Location:

![io_constrain_value](./../../../../../../../news/others/20k_lite_start/assets/io_constrain_value.png)

Finishing filling, use `Ctrl + S` to save constraints file, then close FloorPlanner interactive graphical interface.

Then we see there is a .cst file in our project, and its content are easy to understand. 

![cst_content](./../../../../../../../news/others/20k_lite_start/assets/cst_content.png)

### Place & Route

After finishing constraining, we run Place & Route. The purpose is to synthesize the generated netlist and our defined constraints to calculate the optimal solution through IDE, then allocate resources reasonably on the FPGA chip.

Double click Place&Route marked with red box to run.

![place_route](./../../../../../../../news/others/20k_lite_start/assets/place_route.png)。

Then there is no error, everything works well, we can burn our fpga.

## Burn bitstream

It's suggested use this programmer application [Click me](https://dl.sipeed.com/shareURL/TANG/programmer) ro burn fpga.

### Connection comment

The JTAG pin orders can be found in the back of 20K core board.

<table>
    <tr>
        <td>Core Board</td>
        <td>5V0</td>
        <td>TMS</td>
        <td>TDO</td>
        <td>TCK</td>
        <td>TDI</td>
        <td>RX</td>
        <td>TX</td>
        <td>GND</td>
    </tr>
    <tr>
        <td>Debugger</td>
        <td>5V0</td>
        <td>TMS</td>
        <td>TDO</td>
        <td>TCK</td>
        <td>TDI</td>
        <td>TX</td>
        <td>RX</td>
        <td>GND</td>
    </tr>
</table>

![cable_connect](./../../../../../../../news/others/20k_lite_start/assets/cable_connect.png)

### Scan Device

Click `Program Device` twice to run Programmer application.

![open_programmer](./../../../../../../../news/others/20k_lite_start/assets/open_programmer.png)

Click scan_device marked by red box to scan our device.

![scan_device](./../../../../../../../news/others/20k_lite_start/assets/scan_device.png)

Click OK to burn fpga.

### Burn to SRAM

Normally this mode is used to verify bitstream.

Because of its fast burning characteristics so the use of more, but of course the power will lose data, so if you want to power on the running program you can't choose this mode.

Click the function box below Operation to open the device configuration interface, then select the SRAM Mode option in Access Mode to set to download to SRAM, and finally click the three dots box below to select our generated `.fs` bitstream file . Generally speaking, bitstream firmware file is in the impl -> pnr directory.

![sram_mode](./../../../../../../../news/others/20k_lite_start/assets/sram_mode.png)

Click where the red box is to burn firmware.

![sram_download](./../../../../../../../news/others/20k_lite_start/assets/sram_download.png)

Go to [Questions](https://wiki.sipeed.com/hardware/en/tang/common-doc/questions.html) if you have any trouble。

Here we finished downloading into SRAM。

### Burn into Flash

Burning into sram is used for verifying biststream, but can't store program.
If we want to run application at startup, we need to burn into flash.

This steps are similar to the steps above of burning to SRAM.

Click the function box below Operation to open the device configuration interface, then select the External Flash Mode in the Access Mode to burn into external Flash. Finally click the three dots below to select the.fs we generated to download the firmware. Choose the three dots box below to select our generated `.fs` bitstream file. Generally speaking, bitstream firmware file is in the impl -> pnr directory. Finally, select the Generic Flash device from the following external Flash options.

![flash_mode](./../../../../../../../news/others/20k_lite_start/assets/flash_mode.png)

Click where the red box is to burn firmware.

![flash_download](./../../../../../../../news/others/20k_lite_start/assets/flash_download.png)

Then we can run our program when power on.

### Result

After using PMOD designed by Sipeed，one led flashes like below.

![result](./../../../../../../../news/others/20k_lite_start/assets/result.gif)

## Question

Go to [Questions](https://wiki.sipeed.com/hardware/en/tang/common-doc/questions.html) if you have any trouble。