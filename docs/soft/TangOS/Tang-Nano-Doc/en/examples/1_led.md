# Instance process

New Project -> Add Source Code File -> Add Timing, Pin Constraints -> Synthesis -> Programe

Before reading this document, please make sure you have seen [Gowin Cloud Source Software User Guide] (http://cdn.gowinsemi.com.cn/SUG100-1.8_Gowin%E4%BA%91%E6%BA%90%E8%BD%AF%E4%BB%B6%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf), Chapter 5 Cloud Source Software Usage

The source code of this experiment: [https://github.com/sipeed/Tang-Nano-examples/tree/master/example_led](https://github.com/sipeed/Tang-Nano-examples/tree/master/ Example_led)

# Verilog Prerequisites

Here only introduce the relevant syntax that will be used next, more can refer to [Verilog Tutorial](http://www.asic-world.com/verilog/veritut.html)

The basic design unit of Verilog is the module, and each Verilog program consists of four main parts: port definition, I/O description, internal signal declaration and function definition.

The module is like the black box we usually mentioned. When we implement the module, we don't need to care about the inside of the module. We only need to instantiate the module according to the input and output format defined by the module, and provide input to the module. Already working

a module grows like this

```
module block (input a, output b);
reg [width-1:0] R_1;

assign b = a;
always @(posedge clk or negedge reset_n)
begin
// do something
end

endmodule
```

The overall structure of the module consists of module and endmodule. The module is followed by the definition of the module interface, which declares whether the direction of the port is input or output.

Internal signals are sometimes used inside the module, and the internal signals are of type wire and reg.

The definition of the function can be done through the assign and always blocks. Assign is one of the most common methods for describing combinatorial logic; always a block machine can be used to describe combinatorial logic, as well as to describe sequential logic

# Pin usage

The onboard is a RGB(tri-color) LED, the schematic is as follows

![](../../assets/examples/led_pjt_1.png)

The pin distribution used by the entire program is as follows

| port | I/O | pin | desc |
| --------- | ------ | --- | ---------- |
| sys_clk | input | 35 | Clock Input Pin |
| sys_rst_n | input | 15 | System Reset Foot |
| led[0] | output | 16 | Green LED |
| led[1] | output | 17 | Blue LED |
| led[2] | output | 18 | Red LED |

# Programming

The clock of this system is 24Mhz, one machine cycle is 1/24M s, which means 0.5s every 12000000 clock cycles.

In the program, calculate 12000000 clock cycles by counter, and wait for 0.5s. After the time is up, set counter to 0 and change the color of the LED.

```
module led (
    input sys_clk, // clk input
    input sys_rst_n, // reset input
    output reg [2:0] led // 110 G, 101 R, 011 B
);

reg [23:0] counter;

always @(posedge sys_clk or negedge sys_rst_n) begin
    if (!sys_rst_n)
        counter <= 24'd0;
    else if (counter < 24'd1200_0000) // 0.5s delay
        counter <= counter + 1;
    else
        counter <= 24'd0;
end

always @(posedge sys_clk or negedge sys_rst_n) begin
    if (!sys_rst_n)
        led <= 3'b110;
    else if (counter == 24'd1200_0000) // 0.5s delay
        led[2:0] <= {led[1:0], led[2]};
    else
        led <= led;
end

endmodule
```

# Pin constraint

In order for fpga to implement the function of the code, it is also necessary to constrain the pin operations involved in the code to the actual pins of fpga.

As shown below, click process in the workspace on the left, then double-click FloorPlanner

![](../../assets/examples/led_pjt_2.png)

The first click in the project, you may be prompted to create a file, click OK

In the pop-up window, switch to Package View, drag the port under Ports to the corresponding pin of fpga, save it, as shown below

![](../../assets/examples/led_pjt_3.png)

# Synthesis

In the workspace on the left, right-click Synthesize or Place&Route, there will be a run option, click

![](../../assets/examples/led_pjt_4.png)

# Programe

There are two options, one is to burn to sram, the other is to burn to flash.

Burning to sram is faster, but there is no firmware in fpga after power-off; burning to flash can save the firmware before burning after the system is powered off.

Burning is done through the Programer

Double-click on the Program Device in the left workspace to open the Programer.

![](../../assets/examples/led_pjt_5.png)

However, before using Programer, you need to be aware that you can use Programer after both Synthesize and Place&Route are completed, otherwise the software will report error `Bitstream file dose not exists`

![](../../assets/examples/led_pjt_6.png)

Linux users need to pay attention

> The programmer in the Linux installation package is for Linux version Red Hat 5.10. For the Red Hat 6/7 version of the programmer, please download the installation on the official website and replace the installation package with the file in the Gowin cloud source software installation package. Clip "Programmer".

## Change the burning position

To select the location where the firmware is programmed, you can click Edit -> Configure Device when the chip is selected.

![](../../assets/examples/led_pjt_7.png)

In the pop-up window, select the location you want to burn. The flash is selected here. The default burning location is sram.

![](../../assets/examples/led_pjt_8.png)

## Burning

After selecting the burning location, you can burn the firmware, click on the menu bar to burn.

![](../../assets/examples/led_pjt_9.png)

