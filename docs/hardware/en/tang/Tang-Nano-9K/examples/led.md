---
title: Light LED
---

> Edit on 2022.07.03

From this essay we can learn the basic usage of Gowin IDE

## Create Project

Create Project：File-->NEW-->FPGA Dsign Project-->OK

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano/assets/LED-1.png?raw=true)

Set project name and project path (File name and project path shoule be English)

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano/assets/LED-2.png?raw=true)

Choose correct device: 

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano-9K/nano_9k/Tang_nano_9k_Device_choose.png?raw=true)

## Prepare codes

After creating project, we can start editing codes. 
To creat a new file, we can click where the arrow points to in the picture or use shortcut key Ctrl+N.
Then choose Verilog File in the pop-up window.

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano/assets/LED-5.png?raw=true)

Name for file (Suggested using English)

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano/assets/LED-6.png?raw=true)

Double click the created file, then edit in right window

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano/assets/LED-7.png?raw=true)

- We use light led as an example, copy the following "LED example codes" into the created file or edit the created file by yourself.  

~~~v
module led (
    input sys_clk,          // clk input
    input sys_rst_n,        // reset input
    output reg [5:0] led    // 6 LEDS pin
);

reg [23:0] counter;

always @(posedge sys_clk or negedge sys_rst_n) begin
    if (!sys_rst_n)
        counter <= 24'd0;
    else if (counter < 24'd1349_9999)       // 0.5s delay
        counter <= counter + 1'b1;
    else
        counter <= 24'd0;
end

always @(posedge sys_clk or negedge sys_rst_n) begin
    if (!sys_rst_n)
        led <= 6'b111110;
    else if (counter == 24'd1349_9999)       // 0.5s delay
        led[5:0] <= {led[4:0],led[5]};
    else
        led <= led;
end

endmodule
~~~

After finishing edit the file, it's necessary to tick the `Use DONE as regular IO` in Project->Configuration->Place&Route->Dual-Purpose Pin to avoid error.

![img_configuration](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano-9K/nano_9k/LED_Configuration.png?raw=true)

## Systhesize, constrain, place&route

### Systhesize

After finishing steps above, go to the "Process" interface, systhesize the edited file, which means running "Systhesize".

![img_configuration](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano-9K/nano_9k/nano_9k_synthsize.png?raw=true)

If the result is the same as shown below

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano/assets/LED.png?raw=true)

It means that there is no bug in our code, we can continue the next steps. 

If there is some thing wrong, please fix by yourself. 

### Constrain

- Clock constraint is not involved here

To realize function of the code on FPGA, we must bind the ports we define with the chip pins.

Double click the FloorPlanner in the Process interface to set pin constrain(This can be continued if failing systhesize). 

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/assets/examples/lcd_pjt_2.png?raw=true)

First time open FloorPlanner it will prompt lack of ".cst" file, we just choose ok. 

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano/assets/LED-9.png?raw=true)

The leds schematic of nano 9k is as shown below:

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano-9K/nano_9k/LED_Pins.png?raw=true)

In this GUI interface we have two ways to constrain pins:
- Drag the corresponding port to the pin of chip
- Type the pin number corresponding to the port in IO constraint(This is shown as below)

So we can do the ordered operations in the opened window as what the following picture shows:

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano-9K/nano_9k/LED_FloorPlanner.png?raw=true)

For more usage about FloorPlanner,please refer to 

关于 FloorPlanner 更多的相关说明，可以参考 [SUG935-1.3_Gowin设计物理约束用户指南.pdf](http://cdn.gowinsemi.com.cn/SUG935-1.3_Gowin%E8%AE%BE%E8%AE%A1%E7%89%A9%E7%90%86%E7%BA%A6%E6%9D%9F%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)。里面的内容都很有用

### Place&Route

> If it shows error 2017, the solve way can be found ahead(Tips: Enable Dual-Purpose Pin) 

After finishing Running "Place&Route" in the Process interface window, the result will be as same as below

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano-9K/nano_9k/LED_Place&Route.png?raw=true)

## Program

Then connect the board with computer, download firmware.
You can select the device according to the following picture.

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano-9K/nano_9k/nano_9k_device_scan.png?raw=true)

We use download to SRAM as an example.
- Configure download mode ("configure sram download mode")

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano-9K/nano_9k/nano_9k_sram_program.png?raw=true)

Download ("start sram download")

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano-9K/nano_9k/nano_9k_sram_download.png?raw=true)

Then the board runs as shown：

![](https://github.com/sipeed/sipeed_wiki/blob/main/docs/hardware/zh/tang/Tang-Nano-9K/nano_9k/blink.gif?raw=true)

If you need to store firmware with no power, just choose download to flash mode.

## End

Now the tutorial ends, if you have any suggestions, just leave a message.
