# 使用PicoRV32软核在lcd屏幕上绘制图形

> 编辑于2022.06.22

- 原文链接:https://bbs.sipeed.com/thread/1483   有改动

## 摘要

此工程在 LCD 屏幕绘制了两个长方形——一个实心的；另一个空心的。其中空心的边框宽度作为参数可调，并且绘图的颜色还可以通过按钮调整，现已支持红、绿、蓝和白，共四种颜色。
整体的硬件设计基于半导体提供的 PicoRV32 软核IP，在 OPEN AHB INTERFACE 的处，挂载了 128Kbits 的 BSRAM 用作显存。
该 128Kbits 的显存，本质上是一颗双端口的 SRAM ，使得 CPU 和自定义的 LCD IP 共同使用该“显存”。LCD IP 独立于CPU工作，节省 CPU 资源，达到 FPGA 加速的效果。

## 设计

### AHB 接口例化

AHB接口用于与CPU交互，LCD接口与LCD IP交互。代码接口如下：

```verilog
ahb2bram ahb2bram(
    .clk_i(clk50),
    .reset_i(~sys_rstn),

    .hrdata_o(hrdata),
    .hresp_o(hresp),
    .hready_o(hready),
    .haddr_i(haddr),
    .hwrite_i(hwrite),
    .hsize_i(hsize),
    .hburst_i(hburst),
    .hwdata_i(hwdata),
    .hsel_i(hsel),
    .htrans_i(htrans),

    .lcd_clk_i(clk10),
    .lcd_rd_i(lcd_rd),
    .lcd_addr_i(lcd_addr),
    .lcd_data_o(lcd_data)
);
```

### 生成长方形

在这个系统中，CPU主要负责图形的“渲染”，这个在大型系统中常常是GPU来做的。
这里描述有点夸张了，其实所谓的“渲染”就是画个长方形，CPU 根据 C代码中的顶点坐标，把对应的显存地址填入1或者0。所封装的画实心的API如下

```c
void draw_rectangle(uint8_t top_x, uint8_t top_y, uint8_t btm_x, uint8_t btm_y)
{
        uint8_t i,j;
        uint8_t calc_x;
        uint8_t calc_y;

        calc_x = top_x/32;
        calc_y = top_y/32;
  
        for(i=0; i<Y_MAX; i++)
                for(j=0; j<X_MAX; j++)
                {
                        if(j>=calc_x && j<=calc_y && i>=top_y && i<=btm_y)
                                PCIO_AHBSRAM->SRAM[i*X_MAX+j] = RGB;
                }
}
```

### 例化 LCD 

CPU 运行起来后，会根据 C代码 访问 AHB总线，发出读写命令。自定义的 AHB2BRAM 模块，会将总线地址转换成显存地址进行数据读写。将绘制的图形保存在显存中，只要不掉电，就不会丢失。同时，LCD IP 只负责从显存中取数据，按照行场扫描的时序，就可以完完整整的将图形显示在LCD屏幕上了，LCD IP 的接口如下。

```verilog
VGAMod VGAMod
(
    .nRST(sys_rstn),
    .PixelClk(clk10),

    .lcd_rd_o(lcd_rd),
    .lcd_addr_o(lcd_addr),
    .lcd_data_i(lcd_data),

    .LCD_DE(LCD_DE),
    .LCD_HSYNC(LCD_HSYNC),
    .LCD_VSYNC(LCD_VSYNC),

    .LCD_B(LCD_B_t),
    .LCD_G(LCD_G_t),
    .LCD_R(LCD_R_t)
);
```

### 结语

受限于资源，此文实现的系统只有 128Kbits 的显存，而笔者使用的 LCD 的分辨率是480*272，RGB565。如果需要存一幅完整图形需要将显存扩大16倍，似乎超过了Nano 9K板载的这颗FPGA极限。因此，选择折中，不去保存RGB565，而是简单的复制扩展保存的1bit信息到RGB565中，这样颜色深度无法达到65536，只支持红、绿、蓝和白四种颜色。

其实FPGA内封的PSRAM有 64Mbits，足够这块LCD的显存了。以后有机会可以尝试着用这些内存来运行一下 lvgl。

!