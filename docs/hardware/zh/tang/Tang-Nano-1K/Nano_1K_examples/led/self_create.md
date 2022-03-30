---
title: 点灯LED RGB
---

## 新建项目
1. 新建工程：File-->NEW-->FPGA Dsign Project-->OK
    ![](./../../../Tang-Nano/assets/LED-1.png)

2. 弹出的选项框选择存储路径和工程名称（路径和文件名称要求是英文路径）
    ![](./../../../Tang-Nano/assets/LED-2.png)

3. 选择对应的型号：
    ![Tang_nano_1k_device_choose](./../../assets/Nano_1K_device_choose.png)

## 准备代码

4. 新建工程之后接下来进行代码编辑，在Design工作栏内新建“Verilog File”,如下图所示：
    ![](./../../../Tang-Nano/assets/LED-5.png)
5. 为文件命名（要求写英文名，不然后续综合很容易报错）；
   一般来说文件名称应该和文件内容模块名称相同
    ![](./../../../Tang-Nano/assets/LED-6.png)
    ![](./../../../Tang-Nano/assets/LED-7.png)
6. 双击文件，可以在右侧的编辑框中进行代码的编写。
以流水灯为例，将下方的“LED例程代码”粘贴到自己的文件中，也可以自己编写自己的代码。

```verilog
module led (
    input sys_clk,          // clk input
    input sys_rst_n,        // reset input
    output reg [2:0] led    // 110 B, 101 G,001 R
);

reg [23:0] counter;

always @(posedge sys_clk or negedge sys_rst_n) begin
    if (!sys_rst_n)
        counter <= 24'd0;
    else if (counter < 24'd1349_9999)       // 0.5s delay
        counter <= counter + 1;
    else
        counter <= 24'd0;
end

always @(posedge sys_clk or negedge sys_rst_n) begin
    if (!sys_rst_n)
        led <= 3'b110;
    else if (counter == 24'd1349_9999)       // 0.5s delay
        led[2:0] <= {led[1:0],led[2]};
    else
        led <= led;
end

endmodule

 ```

## 综合、约束、布局布线

### 综合
7. 代码编辑结束后转到“Process”界面下，对编辑好的代码进行综合，即运行“Systhesize”
    ![](./../../../Tang-Nano-9K/nano_9k/nano_9k_synthsize.png)
    运行的结果如上图出现 ![](./../../../Tang-Nano/assets/LED.png) 的形状，且下方结果栏不出现任何从报错，说明前面编辑的代码无误，如果有错，根据错误提示进行改正即可。

### 约束
8.  接下来通过  双击Process界面里的FloorPlanner来设置管脚约束（前面的综合如果运行失败，这一步无法进行），第一次打开会弹出缺少.cst文件.选择“OK”即可；
    ![](./../../../Tang-Nano/assets/LED-9.png)

### 布局布线
9. nano 1k的rgb led电路图如下所示
    ![](./../../assets/Nano_1K_RGB_pins.png "nano 1k rgb pins")
    因此在打开的界面中按照序号的顺序来进行相应的操作（两种方式选择一种即可）
    ![](./../../assets/RGB_LED_Constrains.png)

    **完成约束后记得保存~**


11. 到“Process”下运行“Place&Route”，即运行管脚布局布线，运行结果如下图所示：
    ![](./../../assets/RGB_LED_Place&Route.png)

## 烧录

- 成功完成上面步骤后就已经生成高云的比特流文件了，可以进行下面的步骤来将文件烧录到板子了。

12. 接下来是进行连接板子，烧录固件。在Process界面双击`Program Device` 后打开烧录工具
    ![](./../../assets/Open_Programmer.png)


13. 接下来选择 SRAM下载 即可验证程序。
    没有自行焊接外部 FLASH 的话固化应当选择内部FLASH。

点灯验证到此结束。


