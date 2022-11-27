---
title: Tang Primer 20K 流水灯
keywords: Tang Primer 20K ,例程, 上手
update:
  - date: 2022-11-25
    version: v0.1
    author: wonder
    content:
      - 初稿
---

## 说明

本例程使用 Dock 底板上 LED0、LED1、LED2、LED3、LED4、LED5 共六个 LED 灯。

依次只点亮底板上一个 LED 灯，LED 灯切换间隔为 0.5S。

在前面的 [计数器亮灯中](./led.md)，已经点亮了一个灯了。这次只是将所点亮的灯的状态 “转移” 到别的灯上，这里使用环形 [移位寄存器](https://baike.baidu.com/item/%E7%A7%BB%E4%BD%8D%E5%AF%84%E5%AD%98%E5%99%A8%E5%AD%98%E5%82%A8%E5%99%A8/22232752) 就可以完成灯的效果转移目标。在 FPGA 上，可以使用位拼接运算符 `{` 和 `}` 来实现移位寄存器的效果。

### 移位寄存器

移位寄存器是是一种在若干相同时间脉冲下工作的以触发器为基础的器件，数据以并行或串行的方式输入到该器件中，然后每个时间脉冲依次向左或右移动一个比特，在输出端进行输出。

对于使用移位寄存器来实现流水灯，我们需要保证最低要有一个灯亮着，这个时候我们选择环形移位寄存器。将普通移位寄存器的输出作为它自己的输入即可看作为环形移位寄存器。

在 verilog 中，使用类似于下面的代码就可以很容易的实现上面的状态值转移表：

```v
reg [5:0] q;
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        q[5:0] <= 6'b000001; // 复位
    end begin
        q[5:0] <= {q[4:0],q[5]}; //最高位作为最低位输入
        // q[5:0] <= {q[0],q[5:1]}; //最低位作为最高位输入
    end
end
```

<!-- 对应的真值表状态转移如下：
其中以 M[5:0] 来表示底板上的 LED0 到 LED5；clk 表示移位脉冲，每 0.5s 一次；N[5:0] 表示经移动脉冲后的 LED0到 LED5 的状态值。

| rst | clk | M[5:0] | N[5:0] |
| --- | --- | ---    |--- |
| 0 | x | 000001 | xxxxxx |
| 0 | 1 | 000001 | 000001 |
| 0 | 1 | 000001 | xxxxxx |
| 0 | 1 | 000001 | xxxxxx |
| 0 | 1 | 000001 | xxxxxx |
| 0 | 1 | 000001 | xxxxxx |
| 0 | 1 | 000001 | xxxxxx |

在 verilog 中，使用类似于下面的代码就可以很容易的实现上面的状态值转移表：

```v
always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        M[5:0] <= 6'b000001; // 复位
        N[5:0] <= 6'b000001; // 复位
    end
    else begin


    end
end
``` -->


## 操作

### 引脚复用

- READY
- DONE
- SSPI

### 端口和引脚

| Port | Direction | Location |
| --- | --- | --- |
| rst_n | input | T10 |
| Clock  | input | H11 |
| led[5] | output | L16 |
| led[4] | output | L14 |
| led[3] | output | N14 |
| led[2] | output | N16 |
| led[1] | output | A13 |
| led[0] | output | C13 |

### 代码

.. tabset::

    ## water_led.v
    Verilog文件；
    定义了一个复位输入，一个时钟输入和六个输出端口。复位有效时重置输出端口的电平状态。 
    ```verilog
    module led(
        input  rst_n,
        input  Clock,
        output [5:0] led
    );

    /**********计时部分**********/
    //parameter Clock_frequency = 27_000_000; // 时钟频率为27Mhz
    parameter count_value       = 13_499_999; // 计时 0.5S 所需要的计数次数

    reg [23:0]  count_value_reg ; // 计数器
    reg         count_value_flag; // IO 电平标志

    always @(posedge Clock or negedge rst_n) begin
        if (!rst_n) begin
            count_value_reg  <= 23'b0; // 清零计数器
            count_value_flag <= 1'b0 ; // 清零标志位
        end
        else if ( count_value_reg <= count_value ) begin //没有计数到 0.5S
            count_value_reg  <= count_value_reg + 1'b1; // 继续计数
            count_value_flag <= 1'b0 ; // 不产生移位标志
        end
        else begin //计数到 0.5S 了
            count_value_reg  <= 23'b0; // 清零计数器，为重新计数最准备
            count_value_flag <= 1'b1 ; // 产生移位标志
        end
    end

    /**********电平状态移位部分**********/
    reg [5:0] led_reg = 6'b000001; //初始化输出 IO 电平状态
    always @(posedge Clock or negedge rst_n) begin
        if (!rst_n) begin
            led_reg[5:0] <= 6'b000001 ; // 复位后输出 IO 电平状态
        end
        else if ( count_value_flag )  //  电平移位标志有效
            led_reg[5:0]  <= { led_reg[4:0],led_reg[5] } ; // IO 电平移位
        else //  电平移位标志无效
            led_reg[5:0]  <= led_reg[5:0] ; // IO 电平不变
    end


    /**********寄存器变量与端口连接**********/
    assign led[5:0] = led_reg[5:0] ;

    endmodule
    ```

    ## water_led.cst
    物理约束文件；
    将 verilog 代码里的端口绑定到 FPGA 引脚上面
    ```txt
    IO_LOC "led[5]" L16;
    IO_PORT "led[5]" PULL_MODE=UP DRIVE=8;
    IO_LOC "led[4]" L14;
    IO_PORT "led[4]" PULL_MODE=UP DRIVE=8;
    IO_LOC "led[3]" N14;
    IO_PORT "led[3]" PULL_MODE=UP DRIVE=8;
    IO_LOC "led[2]" N16;
    IO_PORT "led[2]" PULL_MODE=UP DRIVE=8;
    IO_LOC "led[1]" A13;
    IO_PORT "led[1]" PULL_MODE=UP DRIVE=8;
    IO_LOC "led[0]" C13;
    IO_PORT "led[0]" PULL_MODE=UP DRIVE=8;
    IO_LOC "Clock" H11;
    IO_PORT "Clock" PULL_MODE=UP;
    IO_LOC "rst_n" T10;
    IO_PORT "rst_n" PULL_MODE=UP;
    ```

## 效果

按下 S0 按键，LED0 灭，其余 LED 均亮。
松开 S0 按键，LED0 到 LED5 依次只熄灭一个，LED5 熄灭后是 LED0 熄灭，形成了闭环的效果。

<!-- |松开 S0 按键|按下 S0 按键|
|---|---|
|<img src="./assets/key_led_on/led_off.png" alt="led_off">|<img src="./assets/key_led_on/led_on.png" alt="led_on">| -->

## 补充

如果将 `water_led.v` 文件里最后部分的

```verilog
assign led[5:0] = led_reg[5:0] ;
```

改成

```verilog
assign led[5:0] = ~led_reg[5:0] ;
```

那么每次只会有一个 LED 亮起来，而不是五个 LED 亮着。

<p id="back">
    <a href="#" onClick="javascript :history.back(-1);">返回上一页(Back)</a>
</p>