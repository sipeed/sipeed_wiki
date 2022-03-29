# RGB LCD 示例

- 本文涉及基础时序分析

## 先介绍时序

RGB LCD 显示图像的原理和 VGA 类似，都是在计算机内部以数字的方式生成需要显示的图像信息，再通过模数转换的方式，将这些数字的图像信息转变为 RGB 三原色模拟信号、以及行、场同步信号。

下面就介绍 VGA 的时序

![](./../../assets/examples/lcd_pjt_1.png)

上图分别是 VGA 在数据传输中的行同步、场同步时序

从时序图中可以看出，不论是显示一行数据还是一列数据，都需要一个对应的同步(sync)信号，数据的传输在两个同步信号的脉冲之间完成

每一行的数据包括显示前沿(back porch)、有效数据(active viedo)、显示后沿(front porch)三个阶段

其中的有效数据就是我们常说的分辨率，而显示前后沿的参数需要参考具体的分辨率与帧数进行设置，相关参数可以参考典型参数，链接在此： http://www.tinyvga.com/vga-timing

这块屏幕的控制时序略有不同，相关参数的设置可以查看[规格书](https://dl.sipeed.com/shareURL/TANG/Premier/HDK/Datasheet)(点开链接后选择AT050TN43文件)

下面为这块 LCD 时序相关的截图

![](./../../assets/examples/lcd_pjt_2.png)

![](./../../assets/examples/lcd_pjt_3.png)

上面一张图是时序中的参数表，下面的图是时序图

从时序图中看出，这块屏幕可以不用设置前后沿，可以只设置消影(blanking)时间，通过实际的程序证明，两种方式都是可以的

## 生成屏幕时钟


板载的晶振时钟为 24MHz ，但是我们的屏幕要求 33.3MHZ 的时钟，所以我们需要使用对应的ip核来生成相应的时钟

### pll


这里需要使用到 `IP Core Generate` ，位置在 Tools -> IP Core Generate

![](./../../assets/examples/lcd_pjt_4.png)

双击 `PLL` ，在弹出窗口 language 选择 Verilog ，CLKIN 为 24MHz ，CLKOUT 为 200MHz，CLKOUTD 要选择 Enable，然后生成时钟为 33.33MHz，Tolerance 选择 0.2%

![](./../../assets/examples/lcd_pjt_5.png)

### osc

系统的时钟可以由外部时钟提供，也可以使用 OSC 生成的时钟

同样也是使用 `IP Core Generate`

找到 `OSC` 并双击打开进行分频的设置

在帮助页面可以知道，GW1N-1 系列的 fpga 的 OSC 是从 240MHz 进行分频的，所以要产生 24MHz 的时钟，只需要进行 10 的分频

## 屏幕驱动代码

### 端口定义
首先需要先定义出驱动屏幕所需要的端口
```verilog
module VGAMod
(
    input                   CLK,
    input                   nRST,

    input                   PixelClk,

    output                  LCD_DE,
    output                  LCD_HSYNC,
    output                  LCD_VSYNC,

	output          [4:0]   LCD_B,
	output          [5:0]   LCD_G,
	output          [4:0]   LCD_R
);
```
本例程使用RGB565作为驱动方式；

### 时序常量
接着定义出时序图上所要求的常量

```verilog
localparam      V_BackPorch = 16'd6; //0 or 45
localparam      V_Pluse 	= 16'd5; 
localparam      HightPixel  = 16'd480;
localparam      V_FrontPorch= 16'd62; //45 or 0

localparam      H_BackPorch = 16'd182; 	
localparam      H_Pluse 	= 16'd1; 
localparam      WidthPixel  = 16'd800;
localparam      H_FrontPorch= 16'd210;

localparam      PixelForHS  =   WidthPixel + H_BackPorch + H_FrontPorch;  	
localparam      LineForVS   =   HightPixel + V_BackPorch + V_FrontPorch;
```

首先是设置时序相关的参数：前沿、后沿、有效像素

关于显示前沿、后沿，前面也说了，可以合并为一个消影时间，就是可以把其中一个设置为0，另一个设置为消影时间。反正前后沿的时间加起来符合表中的时间要求就可以

### 同步信号
这段代码产生同步信号，需要注意的是，这块屏幕的同步信号是负极性使能

```verilog
always @(  posedge PixelClk or negedge nRST  )begin
    if( !nRST ) begin
        LineCount       <=  16'b0;    
        PixelCount      <=  16'b0;
        end
    else if(  PixelCount  ==  PixelForHS ) begin
        PixelCount      <=  16'b0;
        LineCount       <=  LineCount + 1'b1;
        end
    else if(  LineCount  == LineForVS  ) begin
        LineCount       <=  16'b0;
        PixelCount      <=  16'b0;
        end
end

//注意这里HSYNC和VSYNC负极性
assign  LCD_HSYNC = (( PixelCount >= H_Pluse)&&( PixelCount <= (PixelForHS-H_FrontPorch))) ? 1'b0 : 1'b1;
assign  LCD_VSYNC = ((( LineCount  >= V_Pluse )&&( LineCount  <= (LineForVS-0) )) ) ? 1'b0 : 1'b1;
```

### 使能信号
这段代码设置 LCD 使能图像显示，这块屏幕需要控制一个管脚用作显示开关，实际这个信号就是传输图像有效的那 800*480 的数据时置 1
  
```verilog
assign  LCD_DE = (  ( PixelCount >= H_BackPorch )&&
                    ( PixelCount <= PixelForHS-H_FrontPorch ) &&
                    ( LineCount >= V_BackPorch ) &&
                    ( LineCount <= LineForVS-V_FrontPorch-1 ))  ? 1'b1 : 1'b0;
                    //这里不减一，会抖动
```

- 这段代码用来产生 LCD 的测试数据，产生彩条显示

```verilog
assign  LCD_R   =   (PixelCount<200)? 5'b00000 : 
                    (PixelCount<240 ? 5'b00001 :    
                    (PixelCount<280 ? 5'b00010 :    
                    (PixelCount<320 ? 5'b00100 :    
                    (PixelCount<360 ? 5'b01000 :    
                    (PixelCount<400 ? 5'b10000 :  5'b00000 )))));

assign  LCD_G   =   (PixelCount<400)? 6'b000000 : 
                    (PixelCount<440 ? 6'b000001 :    
                    (PixelCount<480 ? 6'b000010 :    
                    (PixelCount<520 ? 6'b000100 :    
                    (PixelCount<560 ? 6'b001000 :    
                    (PixelCount<600 ? 6'b010000 :  
                    (PixelCount<640 ? 6'b100000 : 6'b000000 ))))));

assign  LCD_B   =   (PixelCount<640)? 5'b00000 : 
                    (PixelCount<680 ? 5'b00001 :    
                    (PixelCount<720 ? 5'b00010 :    
                    (PixelCount<760 ? 5'b00100 :    
                    (PixelCount<800 ? 5'b01000 :    
                    (PixelCount<840 ? 5'b10000 :  5'b00000 )))));
```


**当然在最后的驱动文件最后别忘记换行加上 endmodule** 

到这里驱动模块的编写已经完成了。

## 在顶层模块中例化

```verilog
module TOP
(
	input			nRST,
    input           XTAL_IN,

	output			LCD_CLK,
	output			LCD_HYNC,
	output			LCD_SYNC,
	output			LCD_DEN,
	output	[4:0]	LCD_R,
	output	[5:0]	LCD_G,
	output	[4:0]	LCD_B,

    output          LED_R,
    output          LED_G,
    output          LED_B

);

	wire		CLK_SYS;	
	wire		CLK_PIX;

    wire        oscout_o;

`define internel_clock //注释之后使用的是外部晶振

    //例化内部时钟
    Gowin_OSC chip_osc(
        .oscout(oscout_o) //output oscout
    );

    //例化pll
    Gowin_PLL chip_pll(
        .clkout(CLK_SYS), //output clkout      //200M
        .clkoutd(CLK_PIX), //output clkoutd   //33.33M
`ifndef internel_clock
        .clkin(XTAL_IN)    //input clkin
`else
        .clkin(oscout_o)    //input clkin
`endif
    );	

	VGAMod	VGAMod_inst //例化vga驱动
	(
		.CLK		(	CLK_SYS     ),
		.nRST		(	nRST		),

		.PixelClk	(	CLK_PIX		),
		.LCD_DE		(	LCD_DEN	 	),
		.LCD_HSYNC	(	LCD_HYNC 	),
    	.LCD_VSYNC	(	LCD_SYNC 	),

		.LCD_B		(	LCD_B		),
		.LCD_G		(	LCD_G		),
		.LCD_R		(	LCD_R		)
	);

	assign		LCD_CLK		=	CLK_PIX;

    //RGB LED TEST
    reg 	[31:0] Count;
    reg     [1:0] rgb_data;
	always @(  posedge CLK_SYS or negedge nRST  )
	begin
		if(  !nRST  )
		begin
		Count		<= 32'd0;
        rgb_data    <= 2'b00;
		end
		else if ( Count == 100000000 )
		begin
			Count <= 4'b0;
            rgb_data <= rgb_data + 1'b1;
		end
		else
		Count <= Count + 1'b1;
	end
    assign  LED_R = ~(rgb_data == 2'b01);
    assign  LED_G = ~(rgb_data == 2'b10);
    assign  LED_B = ~(rgb_data == 2'b11);

endmodule
```
## 管脚约束
进行管脚约束前需要先将工程综合一次，即在 Process 界面双击一下 Synthesize，然后选择Process 里的 User Constrains -> FloorPlanner。
对应的管脚约束如下；如果感觉麻烦的话也可以直接复制准备好的[文件(点我)](./lcd_constrains.md)

|   PORT   |    PIN   |   PORT   |    PIN   |  
|   :---:  |   :---:  |  :---:  |   :---:  |  
|   LED_B   |    18   |   LED_G   |    17   |    
|   LED_R   |    16   |   LCD_B[4]   |    45   |    
|   LCD_B[3]   |    44   |  LCD_B[2]   |    43   |    
|   LCD_B[1]   |    42   |  LCD_B[0]   |    41   |    
|   LCD_G[5]   |    40   |  LCD_G[4]   |    39   |    
|   LCD_G[3]   |    38   |  LCD_G[2]   |    34   |    
|   LCD_G[1]   |    33   |  LCD_G[0]   |    32   |    
|   LCD_R[4]   |    31   |  LCD_R[3]   |    30   |    
|   LCD_R[2]   |    29   |  LCD_R[1]   |    28   |    
|   LCD_R[0]   |    27   |  LCD_DEN   |    5   |    
|   LCD_SYNC   |    46   |  LCD_HYNC   |    10   |    
|   LCD_CLK   |    11   |   nRST   |    14   |    
|   XTAL_IN   |    35   |   


## 烧录
管脚约束之后，可以进行布局布线，生成比特流，烧录开发板了。


整个工程可以参考 [这里](https://github.com/sipeed/Tang-Nano-examples/tree/master/example_lcd) 

