---
title: Light LED
---

> Edit on 2022.07.13

This tutorial will walk you through the basics of the Gowin IDE, which we'll use to create a simple program to flash the onboard LEDs.

## Create Project

Create Project：File-->NEW-->FPGA Dsign Project-->OK
![Create Project](./../../../../zh/tang/Tang-Nano/assets/LED-1.png)

Set project name and project path (File name and project path should be English)
![Set project name](./../../../../zh/tang/Tang-Nano/assets/LED-2.png)

Choose the correct device: 
![Tang_nano_9k_device_choose](./../../../../zh/tang/Tang-Nano-9K/nano_9k/Tang_nano_9k_Device_choose.png)

## Prepare the code

After creating the project, we can start editing the code. 
To create a new file, we can either click the marked icon (top left of the window) or use Ctrl+N.
Choose Verilog File in the pop-up window.
![Create file](./../../../../zh/tang/Tang-Nano/assets/LED-5.png)

Name the file (it's best to use English for this)
![Name the file](./../../../../zh/tang/Tang-Nano/assets/LED-6.png)

Double click the created file to open it, then edit it in right window.
![OPen file](./../../../../zh/tang/Tang-Nano/assets/LED-7.png)

Here's all the code we're using for this example, either copy/paste it into your file or enter it manually.  

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

Once we're done with the code, we need to tick `Use DONE as regular IO` in Project->Configuration->Place&Route->Dual-Purpose Pin which can be found in the top menu bar to avoid an error.
![img_configuration](./../../../../zh/tang/Tang-Nano-9K/nano_9k/LED_Configuration.png)

## Synthesize, constrain, place&route

### Synthesize

After finishing the steps above, go to the "Process" interface and double click "Synthesize" to synthesize our code. You can also right click "Synthesize" to see its other function
![Synthesize](./../../../../zh/tang/Tang-Nano-9K/nano_9k/nano_9k_synthsize.png)

If the result is the same as shown below, then we can move on to setting our constraints.
![Finish_Synthesize](./../../../../zh/tang/Tang-Nano/assets/LED.png) 

If your synthesis fails, then check the console - it should tell you where the error is.

### Constrain

> Clock constraint is not involved here

For our code to actually do anything, we must bind the ports we defined to the actual pins of the FPGA chip.

Double click the FloorPlanner in the Process interface to set pin constraints (If synthesis fails we can't do this step). 

![FloorPlanner](./../../../../zh/tang/assets/examples/led_pjt_2.png)

The first time we open FloorPlanner it will prompt lack of a ".cst" file, we'll just click ok. 
![cst_file](./../../../../zh/tang/Tang-Nano/assets/LED-9.png)

You can download the full schematic [here](https://dl.sipeed.com/shareURL/TANG/Nano%209K/2_Schematic).
Here is the part of schematic about LEDs on the nano 9k:
![LED_schematic](./../../../../zh/tang/Tang-Nano-9K/nano_9k/LED_Pins.png "nano 9k led pins")

In this GUI interface we have two ways to constrain pins:
- Drag the corresponding port to the pin of the chip
- Enter the pin number corresponding to the port in IO constraints 

Refer to this guide for more information about FloorPlanner : [SUG935-1.3E_Gowin Design Physical Constraints User Guide.pdf](https://dl.sipeed.com/fileList/TANG/Nano%209K/6_Chip_Manual/EN/General%20Guide/SUG935-1.3E_Gowin%20Design%20Physical%20Constraints%20User%20Guide.pdf)

Don't forget bind the clock port and reset port to their pins marked in the [schematic](https://dl.sipeed.com/shareURL/TANG/Nano%209K/2_Schematic)

The following figure shows the example pin constraint of this project
![constraints](./../../../../zh/tang/Tang-Nano-9K/nano_9k/LED_FloorPlanner.png)

### Place&Route

> If it shows error2017, make sure you have enabled `Use DONE as regular IO` (see [prepare the code](#Prepare-the-code))

Double click Place&Route to run it, it will shows as following:
![Finish_place&route](./../../../../zh/tang/Tang-Nano-9K/nano_9k/LED_Place&Route.png)

## Download to device

Visit [here](https://dl.sipeed.com/shareURL/TANG/programmer/docs) to see docs about programmer if you need.

### Start to download

Connect your board to your PC, and select the device as shown in the picture:
![Choose_device](./../../../../zh/tang/Tang-Nano-9K/nano_9k/nano_9k_device_scan.png)

We'll use download to SRAM as an example.

Follow the steps in the figure below to select that operation:
![SRAM_download](./../../../../zh/tang/Tang-Nano-9K/nano_9k/nano_9k_sram_program.png "configure sram download mode")

Click the button shown in the figure to start the firmware download process:
![Verify](./../../../../zh/tang/Tang-Nano-9K/nano_9k/nano_9k_sram_download.png "start sram download")

### Result

Once that's complete, the LEDs start flashing like this：
![Finish](./../../../../zh/tang/Tang-Nano-9K/nano_9k/blink.gif)

## Other

If you need to store firmware with no power, just change Accsess mode and choose your target .fs file .
![Access_mode](./../../../../zh/tang/Tang-Nano-9K/nano_9k/access_mode.png)

Visit [Qustions&Answers](./../../Tang-Nano-Doc/questions.md) if you have trouble

## End

You've reached the end of the tutorial. If you have any suggestion, just leave your message.
