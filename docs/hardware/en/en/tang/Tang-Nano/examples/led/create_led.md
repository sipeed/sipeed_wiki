# Blink led

> Edit on 2022.04.18

From this essay we can learn the basic usage of Gowin IDE

## Create project

Create Project：File-->NEW-->FPGA Dsign Project-->OK
![](./../../../../../zh/tang/Tang-Nano/assets/LED-1.png)

Set project name and project path (File name and project path shoule be English)
![](./../../../../../zh/tang/Tang-Nano/assets/LED-2.png)

Choose correct device: 
![Tang_nano_device_choose](./../../../../../zh/tang/Tang-Nano/examples/led/assets/Nano_device_choose.png)

## Prepare codes

After creating project, we can start editing codes. 
To creat a new file, we can click where the arrow points to in the picture or use shortcut key Ctrl+N.
Then choose Verilog File in the pop-up window.
![](./../../../../../zh/tang/Tang-Nano/assets/LED-5.png)

Name for file (Suggested using English)
![](./../../../../../zh/tang/Tang-Nano/assets/LED-6.png)

Double click the created file, then edit in right window
![](./../../../../../zh/tang/Tang-Nano/assets/LED-7.png)

- We use light led as an example, copy the following "LED example codes" into the created file or edit the created file by yourself.  

### Verilog description

Here I just introduction some basic grammer which we will use in our code about verilog, for more knowledge please refer to the official verilog grammer.

The basic Verilog design unit is module, a module is build from 2 parts, one part describes the ports, another part describes the logic functions which show the relations between ports.

Module is like a black box we normally said, we don't care what's inside the module, we only need to instantiate the module according to the input and output format defined by the module, provide input to the module, and let the module work on its own.

A module is normally like following:

```v
module module_name 
#(parameter)
(port) ;
    Function description;
endmodule
```

The module start with `module` and ends with `endmodule`. After declaring `module` we will declare the `module name`, then we can set `parameter` to make our module change automaticly to meet out depmands. Then `Port` is the singal dealing with this module.`Function description` is a kind of description how we will realize our depmands.

There are 2 signal types in a module, wire type and reg type.

`Function description` contains `always` and `assign` 2 functions. `assign` function is used for describing combinatorial logic. `alyays` function can be used for describing combinatorial logic, as well as timing logic.

### Example codes

~~~v
module led (
    input sys_clk,
    input sys_rst_n,
    output reg [2:0] led // 110 B, 101 R, 011 G
);

reg [23:0] counter;

always @(posedge sys_clk or negedge sys_rst_n) begin
    if (!sys_rst_n)
        counter <= 24'd0;
    else if (counter < 24'd1199_9999)       // 0.5s delay
        counter <= counter + 1'b1;
    else
        counter <= 24'd0;
end

always @(posedge sys_clk or negedge sys_rst_n) begin
    if (!sys_rst_n)
        led <= 3'b110;
    else if (counter == 24'd1199_9999)       // 0.5s delay
        led[2:0] <= {led[1:0],led[2]};
    else
        led <= led;
end

endmodule
~~~

## Synthesize, constrain, place&route

### Synthesize

After finishing steps above, go to the "Process" interface, synthesize the edited file, which means running "Synthesize". 
![](./../../../../../zh/tang/Tang-Nano-9K/nano_9k/nano_9k_synthsize.png)

If the result is the same as shown below
![](./../../../../../zh/tang/Tang-Nano/assets/LED.png) 

It means that there is no bug in our code, we can continue the next steps. 

If there is some thing wrong, please fix by yourself. 

### Constrain

- Clock constraint is not involved here

To realize function of the code on FPGA, we must bind the ports we define with the chip pins.

Double click the FloorPlanner in the Process interface to set pin constrain(This can be continued if failing Synthesize). 

![](./../../../../../zh/tang/assets/examples/led_pjt_2.png)

First time open FloorPlanner it will prompt lack of ".cst" file, we just choose ok. 
![](./../../../../../zh/tang/Tang-Nano/assets/LED-9.png)

The led schematic of nano is as shown below:
![](./../../../../../zh/tang/Tang-Nano/examples/led/assets/nano_led_pins.png)

In this GUI interface we have two ways to constrain pins:
- Drag the corresponding port to the pin of chip
- Type the pin number corresponding to the port in IO constraint(This is shown as below)

So we can do the ordered operations in the opened window as what the following picture shows:(Just choose one way)
![](./../../../../../zh/tang/Tang-Nano/examples/led/assets/pin_constrain_1.png)
![](./../../../../../zh/tang/Tang-Nano/examples/led/assets/pin_constrain_2.png)

### Place&Route

After finishing Running "Place&Route" in the Process interface window, the result will be as same as below
![](./../../../../../zh/tang/Tang-Nano/examples/led/assets/RGB_LED_Place&Route.png)

## Program

Then connect the board with computer, download firmware.

Double click `Program Device` in Process interface to open programmer application
![](./../../../../../zh/tang/Tang-Nano/examples/led/assets//Open_Programmer.png)

You can config download mode according to the following picture.
We use download to SRAM as an example.
![](./../../../../../zh/tang/Tang-Nano/examples/led/assets/tang-nano-programmer-config.png)

If you need to store firmware with no power, just choose download to flash mode.

## End

Now the tutorial ends, if you have any suggestions, just leave a message.
