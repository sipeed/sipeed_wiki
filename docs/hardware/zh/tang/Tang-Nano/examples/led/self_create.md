# 自己点灯

## 新建项目

新建工程：File-->NEW-->FPGA Design Project-->OK
    ![](./../../assets/LED-1.png)

弹出的选项框选择存储路径和工程名称（路径和文件名称要求是英文路径）
    ![](./../../assets/LED-2.png)

选择对应的型号：
    ![Tang_nano_1k_device_choose](./assets/Nano_device_choose.png)
    
## 编写代码

新建好工程之后接下来进行代码编辑，在Design工作栏内新建“Verilog File”,如下图所示：
    ![](./../../assets/LED-5.png)
    
为文件命名（要求写英文名，不然后续综合很容易报错）； 
   一般来说对于verolog文件建议文件名称与文件module名称应当相同
    ![](./../../assets/LED-6.png)

双击新建的 .v 文件，可以在右侧的编辑框中编写代码。
    ![](./../../assets/LED-7.png)


### Verilog 预备知识

这里只介绍接下来会用到的相关语法，更多的可以参考 《Verilog 数字系统设计教程》

Verilog 的基本设计单元是模块，一个模块是由两部分组成的，一部分描述接口，另一部分描述逻辑功能，即描述输出和输入的关系的。

模块就像我们平时提到的黑匣子，当我们实现了模块后，就不需要去关心模块内部，只需要根据模块定义的输入输出格式，将模块实例化，给模块提供输入，就可以让模块自己工作了

一个模块长成这样

```v
module module_name 
#(parameter)
(port) ;
    Function description;
endmodule
```

模块整体结构由 module 和 endmodule 组成，module 后面跟着的是模块的名称，可传递变量参数，接口的定义，声明了端口的方向

模块内部有时候会使用内部的信号，内部信号有 wire 和 reg 类型

功能的定义可以通过 assign 和 always 块完成。 assign 是描述组合逻辑最常用的方法之一； always 可用于描述组合逻辑，也可描述时序逻辑

### 示例代码

以流水灯为例；将下方的代码粘贴到自己的文件中，也可以自己编写代码。

```verilog
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

 ```

## 综合、约束、布局布线

### 综合

保存编辑的代码后转到“Process”界面下，对编辑好的代码进行综合，即双击“Systhesize”
    ![](./../../../Tang-Nano-9K/nano_9k/nano_9k_synthsize.png)

运行之后如没有报错而且 Synthesize 变成下图里的图标
    ![](./../../../Tang-Nano/assets/LED.png) 

说明前面编辑的代码无误；如果有错，根据错误提示进行改正即可。        

### 约束

- 此处未涉及时钟约束

想让 Fpga 实现代码的功能，必须将代码中涉及的 端口 绑定到 Fpga 实际的引脚上。

如下图，在左边的工作区点击 process，然后双击 FloorPlanner

![](./../../../assets/examples/led_pjt_2.png)

接下来通过 双击 Process 界面里的FloorPlanner来设置管脚约束。第一次打开会弹出缺少.cst文件.选择“OK”即可；
    ![](./../../assets/LED-9.pngassets/LED-9.png)

nano 的 rgb led电路图如下所示
    ![](./assets/nano_led_pins.png "nano rgb pins")

整个项目需要约束的引脚如下

| port      | I/O    | pin | desc       |
| --------- | ------ | --- | ---------- |
| sys_clk   | input  | 35  | 时钟输入脚  |
| sys_rst_n | input  | 15  | 系统复位脚  |
| led[0]    | output | 16  | 绿灯       |
| led[1]    | output | 17  | 蓝灯       |
| led[2]    | output | 18  | 红灯       |

对于交互式管脚约束有下图中的两种方法
- 将对应的端口拖拽到芯片引脚上
- 在IO约束中输入端口对应的引脚编号

在打开的界面中按照序号的顺序来进行相应的操作（两种方式选择一种即可）
![](./assets/pin_constrain_1.png)
![](./assets/pin_constrain_2.png)

- 直接编写约束文件方法用户自行研究

关于 FloorPlanner 更多的相关说明，可以参考 [SUG935-1.3_Gowin设计物理约束用户指南.pdf](http://cdn.gowinsemi.com.cn/SUG935-1.3_Gowin%E8%AE%BE%E8%AE%A1%E7%89%A9%E7%90%86%E7%BA%A6%E6%9D%9F%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)。里面的内容都很有用

### 布局布线

到“Process”下运行“Place&Route”，即运行管脚布局布线，运行结果如下图所示：
    ![](./assets/RGB_LED_Place&Route.png)
    
## 烧录

接下来是连接板子，烧录固件。在Process界面双击 `Program Device` 后打开烧录工具
    ![](./assets/Open_Programmer.png)

可以在图中进行相应的修改
    ![](./../../../../../zh/tang/Tang-Nano/examples/led/assets/tang-nano-programmer-config.png)

接下来选择sram烧录即可验证程序。
    ![](./assets/Success_led.png)
    
点灯验证到此结束。

## 结语

有问题的话可以在下方留言。

<p id="back">
    <a href="#" onClick="javascript :history.back(-1);">返回上一页(Back)</a>
</p>