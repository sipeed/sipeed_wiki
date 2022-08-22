---
title: Primer 20K Lite 初见
keywords: Primer 20K, Lite, FPGA
desc: Primer 20K 上手
date: 2022-08-22
tags: FPGA, Primer 20K
cover: ./assets/cover.png
---

拿到 Primer 20K Lite 后上手点个灯

<!-- more -->

## 前言

本篇文档引导新用户熟悉 IDE 流程并且完成点灯操作。

出货固件已经默认为用户可用全 IO 闪灯，因此长期通电会发热，介意的话可以先擦除 Flash 或者根据本文走到最后烧录时将电脑与板子连接起来。

## 安装 IDE

参考 [安装IDE](https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-Doc/get_started/install-the-ide.html) 来完成我们需要准备的软件环境。

对于 Windows 用户需要额外下载一下 [Programmer](https://dl.sipeed.com/shareURL/TANG/programmer) 烧录专用软件可以降低我们在烧录的时候出现问题的可能性。

对于 Linux 用户的话建议使用 [openfpgaLoader](https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-Doc/get_started/flash_in_linux.html) 这软件来烧录 GW2A-18。

## 新建工程

文件 -> 新建 -> FPGA Design -> Project

<div>
    <img src="./assets/new_project.png" width=58% alt="new_project">
    <img src="./assets/fpga_project.png" width=35% alt="fpga_project">
</div>

设置工程名称，要求只用英文的下划线命名，存放路径中不要有中文字符或者空格等。

![project_path](./assets/project_path.png)

然后在下面的芯片型号中选择 GW2A-LV18PG256C8/I7，使用上面的筛选能够更快地选择到正确的型号，注意 Device 那一栏为 GW2A-18C
![device_choose](./assets/device_choose.png)

然后点击确定后就可以进行最终项目预览了。确认无误后就完成工程创建了。

## 编写代码

### 新建文件

高云 IDE 提供了三种新建文件的方法。在此我们直接使用快捷键 `Ctrl + N` 来新建文件，其他两种不在此讲述。

在弹出的窗口中选择 `Verilog File`，会 VHDL 的也可以选择下面的 `VHDL File`，这篇文章只用 Verilog 来做点灯示例。

<img src="./assets/new_verilog_file.png" width=50% alt="new_verilog_file">
    
点击 OK 之后会提示让我们输入文件名称，此处以 `led` 为文件名做示范。

<img src="./assets/file_name.png" width=75% alt="file_name">

到这里我们就完成文件的创建了，可以直接编写代码了。

![created_file](./assets/created_file.png)

### Verilog 简单说明

Verilog 是一种硬件描述语言，用来对数字电路进行抽象化描述。

Verilog 的基本设计单元是“模块”(module)。

一个模块是由两部分组成的：一部分描述接口，另一部分描述内部逻辑功能，即定义输入是如何影响输出的。

一个模块长成这样：

```v
module module_name
#(parameter)
(port) ;
    function   
endmodule
```

模块整体结构由 module 和 endmodule 组成，module 后面跟着的是模块的名称(module_name)，可传递变量参数(parameter)，端口及其方向的申明(port)，紧接着就是内部逻辑功能描述(function) ,最后用 endmodule 来表示这一个模块，描述完毕。

内部逻辑功能通常由 assign 和 always 块完成；其中 assign 语句描述逻辑功能，always 块常用于描述时序功能。

### 代码思路

写代码前我们需要先想清楚代码目的：每隔 0.5S 灯闪一次。

对此所画的需求框图如下：

![block_method](./assets/block_method.png)

然后对于 0.5S 我们需要一个计数器来计时，LED 灯闪就是 IO 翻转

![count_block](./assets/time_count.png)

把上面的思维框图具体到实际使用的话，就变成下面的样式了:

![clock_time_count](./assets/clock_time_count.png)

其中 Clock 为时钟源，用来给计时器提供准确的时间。

### 代码描述

根据上文 Verilog 简单说明和所描述的框图，可以所要编写 Verilog 模块有 Clock 和 IO电平 两个端口；

```v
module led(
    input  Clock,
    output IO_voltage
);

endmodule
```

对于内部的计时模块，Primer 20K 核心板上的晶振为 27MHZ，因此我们每秒钟会有 27000000 个时钟上升沿，想要 0.5S 计数的话那么只需要计数 13500000 次上升沿就好。计数是从 0 开始的，数 13500000 的话就是从 0 数到 13499999。计数完后我们需要设置一个标志位，来通知 LED 的 IO 翻转一下电平。整体计数代码如下：

```v
//parameter Clock_frequency = 27_000_000; // 时钟频率为27Mhz
parameter count_value       = 13_499_999; // 计时 0.5S 所需要的计数次数

reg [23:0]  count_value_reg ; // 计数器
reg         count_value_flag; // IO 电平翻转标志

always @(posedge Clock) begin
    if ( count_value_reg <= count_value ) begin //没有计数到 0.5S
        count_value_reg  <= count_value_reg + 1'b1; // 继续计数
        count_value_flag <= 1'b0 ; // 不产生翻转标志
    end
    else begin //计数到 0.5S 了
        count_value_reg  <= 23'b0; // 清零计数器，为重新计数最准备
        count_value_flag <= 1'b1 ; // 产生翻转标志
    end
end
```

对于 LED IO 电平翻转代码如下：

```v
reg IO_voltage_reg = 1'b0; // 声明 IO 电平状态用于达到计时时间后的翻转，并赋予一个低电平初始态

always @(posedge Clock) begin
    if ( count_value_flag )  //  电平翻转标志有效
        IO_voltage_reg <= ~IO_voltage_reg; // IO 电平翻转
    else //  电平翻转标志无效
        IO_voltage_reg <= IO_voltage_reg; // IO 电平不变
end
```

将上面的代码整合后就变成了下面的内容:

```v
module led(
    input  Clock,
    output IO_voltage
);

/**********计时部分**********/
//parameter Clock_frequency = 27_000_000; // 时钟频率为27Mhz
parameter count_value       = 13_499_999; // 计时 0.5S 所需要的计数次数

reg [23:0]  count_value_reg ; // 计数器
reg         count_value_flag; // IO 电平翻转标志

always @(posedge Clock) begin
    if ( count_value_reg <= count_value ) begin //没有计数到 0.5S
        count_value_reg  <= count_value_reg + 1'b1; // 继续计数
        count_value_flag <= 1'b0 ; // 不产生翻转标志
    end
    else begin //计数到 0.5S 了
        count_value_reg  <= 23'b0; // 清零计数器，为重新计数最准备
        count_value_flag <= 1'b1 ; // 产生翻转标志
    end
end
reg IO_voltage_reg = 1'b0; // 声明 IO 电平状态用于达到计时时间后的翻转，并赋予一个低电平初始态

/**********电平翻转部分**********/
always @(posedge Clock) begin
    if ( count_value_flag )  //  电平翻转标志有效
        IO_voltage_reg <= ~IO_voltage_reg; // IO 电平翻转
    else //  电平翻转标志无效
        IO_voltage_reg <= IO_voltage_reg; // IO 电平不变
end


/**********补充一行代码**********/
assign IO_voltage = IO_voltage_reg;

endmodule
```

上面代码最后面补充了一行代码，是因为 IO_voltage 声明在了 port 位置，默认为 wire 型，想要将它与 reg 变量 IO_voltage_reg 连接起来，需要用到 assign 语句。

## 综合，约束，布局布线

### 综合

代码保存后，可以双击 IDE 内部的 Process -> Synthesize 来进行代码综合，将 verilog 代码内容转换为综合网表。

![synthesize](./assets/synthesize.png)

关于网表有兴趣的可以自己去查阅相关资料，此处不再额外说明。

### 约束

综合完之后我们需要进行管脚约束，才能将所编写的模块端口与 FPGA 引脚相对应，并且实现模块的功能。

点击上图 Synthesize 上面的 FloorPlanner 来进行管脚约束。

![floorplanner](./assets/floorplanner.png)

由于是首次创建，所以会弹出下面的对话框，点击 OK 后就弹出了图形化约束交互界面。

![create_constrain_file](./assets/create_constrain_file.png)

![floorplanner_intreface](./assets/floorplanner_interface.png)

关于约束的方法可以查看 [SUG935-1.3_Gowin设计物理约束用户指南.pdf](http://cdn.gowinsemi.com.cn/SUG935-1.3_Gowin%E8%AE%BE%E8%AE%A1%E7%89%A9%E7%90%86%E7%BA%A6%E6%9D%9F%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)

此处因个人喜所以仅使用下图中 IO Constranins 方法来约束引脚：

![floor_planner_ioconstrain](./assets/floor_planner_ioconstrain.png)

根据[核心板原理图](https://dl.sipeed.com/fileList/TANG/Primer_20K/02_Schematic/Tang_Primer_20K_Core_board_3690.pdf)，我们可以知道晶振所输入的引脚为 H11。

<img src="./assets/crystal_port.png" alt="crystal_port" width=45%>

然后结合底板上的 IO 丝印，决定用地板上的 L14 引脚进行点灯。

![l14_port](./assets/l14_port.png)

因此对于在 FloorPlanner 交互窗口下面的 IO Constranins 中填入下面的值：

![io_constrain_value](./assets/io_constrain_value.png)

输入完毕后快捷键 Ctrl + S 来保存一下约束，然后接可以关闭 FloorPlanner 的交互图形界面了。

接着发现在工程项目里面多出来刚刚创建的 cst 文件了，里面的内容也比较好理解。

![cst_content](./assets/cst_content.png)

### 布局布线

完成约束后就要开始运行布局布线了，目的是为了把综合所生成的网表和我们自己定义的约束来通过 IDE 算出最优解然后将资源合理的分配在 FPGA 芯片上。

双击下体红框处的 Place&Route 就开始运行了。
![place_route](./assets/place_route.png)。

紧接着没有报错，全部通过。就饿可以开始进行烧录了。

## 烧录固件

如果使用的是 bl702 下载器，那么要求使用  [此处](https://dl.sipeed.com/shareURL/TANG/programmer) 链接内的 Programmer 软件来进行烧录，来避免 Programmer 软件识别不到芯片等一系列问题。

下载后解压替换掉 Gowin 对应安装目录的 Programmer 文件夹即可。
不会替换的话可以在下载解压后的 Programmer 程序中手动添加需要下载的 .fs 文件来进行烧录。

### 接线说明

由于需要将核心板与下载器进行连线，这里说明一下所连接的对应端口。

<table>
    <tr>
        <td>核心板</td>
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
        <td>调试器</td>
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

![cable_connect](./assets/cable_connect.png)

### 扫描设备

双击下图中的 下载程序(Program Device) 来运行 Programmer 软件

![open_programmer](./assets/open_programmer.png)

正确运行我们所提供下载的 Programmer 软件的话软件上面所显示的软件名称为 `Programmer 2` ，点击下图红框处来扫描设备，且在设备选择中选择 GW2A-18C 。

![scan_device](./assets/scan_device.png)

点击 OK 后就可以进行烧录操作了。

烧录相关的文档可以参考 [SUG502-1.3_Gowin_Programmer用户指南.pdf](http://cdn.gowinsemi.com.cn/SUG502-1.3_Gowin_Programmer%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)

### 下载到 SRAM

一般来说这个模式是以用来快速要证所生成的固件是否满足自己目的的。

因为其烧录快的特性所以使用的较多，然是当然断电会丢失数据，所以如果想上电运行程序的话是不能选这个的。

点击 Operation 下面的功能框来打开设备设置界面，接着在 Operation 框中选择 SRAM Program 选项来设置为下载到 SRAM ，最后点击下面的那三个点点框来选择我们所生成的 .fs 下载固件。通常来说下载固件生成与工程文件目录下的 impl -> pnr 目录下。

![sram_mode](./assets/sram_mode.png)

接着来点击红框处开始进行烧录 

![sram_download](./assets/sram_download.png)

有问题的话可以前往 [常见问题](https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-Doc/questions.html) 自行排查。

到这里就下载完成了。

### 下载到 Flash

上面说过下载到 SRAM 是为了快速验证，但是不能上电运行程序。
所以想要上电运行的话我们需要设置下载到 Flash。

和上面下载到 SRAM 的步骤几乎类似，先点开 Operation 下面的功能框来打开设备设置界面，接着在 Operation 框中选择 External Flash Mode 选项来设置为下载到外部 Flash ，最后点击下面的那三个点点框来选择我们所生成的 .fs 下载固件，通常来说下载固件生成与工程文件目录下的 impl -> pnr 目录下。最后在下面的外部 Flash 选项中选择设备为 Generic Flash 。

![flash_mode](./assets/flash_mode.png)

接着来点击红框处开始进行烧录 

![flash_download](./assets/flash_download.png)

然后我们的程序重新上电也能照样运行了。

### 代码效果

使用 Sipeed 的 SPMOD 后，如下图所示有一个灯在闪。

![result](./assets/result.gif)