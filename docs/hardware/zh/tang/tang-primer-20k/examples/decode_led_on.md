---
title: Tang Primer 20K 译码器亮灯
keywords: Tang Primer 20K ,例程, 上手
update:
  - date: 2022-09-30
    version: v0.1
    author: wonder
    content:
      - 初稿
---

## 说明

本例程使用 Dock 底板上的 S0、S1 按键，和 LED0、LED1、LED2、LED3 四个 LED 灯。

使用两个按键来控制 4 个LED灯的状态，进行的操作与对应的结果如下：

<table>
    <tr>       
        <th colspan="2" >按键</th>
        <th colspan="4">LED 状态</th>
        <th >真值表达式</th>
    </tr>
    <tr>
        <td>S0</td>
        <td>S1</td>
        <td>LED0</td>
        <td>LED1</td>
        <td>LED2</td>
        <td>LED3</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td>亮</td>
        <td></td>
        <td></td>
        <td></td>
        <td>$$ LED0 = S0\cdot S1 $$</td>
    </tr>
    <tr>
        <td>按下</td>
        <td></td>
        <td></td>
        <td>亮</td>
        <td></td>
        <td></td>
        <td>$$ LED0 = \overline{S0}\cdot S1 $$</td>
    </tr>
    <tr>
        <td></td>
        <td>按下</td>
        <td></td>
        <td></td>
        <td>亮</td>
        <td></td>
        <td>$$ LED0 = S0\cdot \overline{S1} $$</td>
    </tr>
    <tr>
        <td>按下</td>
        <td>按下</td>
        <td></td>
        <td></td>
        <td></td>
        <td>亮</td>
        <td>$$ LED0 = \overline{S0}\cdot \overline{S1} $$</td>
    </tr>
</table>

从前面的 [按键亮灯](./examples/key_led_on.md) 已知：当 FPGA 与 LED 所连接的引脚为低电平时，对应的 LED 灯会亮；按下按键，对应的 FPGA 引脚为低电平状态。

上面那个表格的输出是以 1 为结果，为了根据原理图来点灯，需要将上面的真值表结果取反来实现最终的效果：

<table>
    <tr>       
        <th colspan="2">  按键  </th>
        <th colspan="4">LED 电平状态</th>
        <th > 真值表达式 </th>
    </tr>
    <tr>
        <td>S0</td>
        <td>S1</td>
        <td>LED0</td>
        <td>LED1</td>
        <td>LED2</td>
        <td>LED3</td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td>0</td>
        <td></td>
        <td></td>
        <td></td>
        <td>$$ LED0= \overline{S0\cdot S1} $$</td>
        <!-- <td> LED1 = ! ( S0 & S1 ) </td> -->
    </tr>
    <tr>
        <td>0</td>
        <td></td>
        <td></td>
        <td>0</td>
        <td></td>
        <td></td>
        <td>$$ LED1 = \overline{\overline{S0}\cdot S1} $$</td>
        <!-- <td> LED1 = ! (!S0 & S1 ) </td> -->
    </tr>
    <tr>
        <td></td>
        <td>0</td>
        <td></td>
        <td></td>
        <td>0</td>
        <td></td>
        <td>$$ LED2 = \overline{S0\cdot \overline{S1}} $$</td>
        <!-- <td> LED2 = ! ( S0 & !S1) </td> -->
    </tr>
    <tr>
        <td>0</td>
        <td>0</td>
        <td></td>
        <td></td>
        <td></td>
        <td>0</td>
        <td>$$ LED3 = \overline{\overline{S0}\cdot \overline{S1}} = S0+S1 $$</td>
        <!-- <td> LED3 =   ( S0 | S1 )  </td> -->
    </tr>
</table>

## 操作

### 引脚复用

- READY
- DONE
- SSPI

### 端口和引脚

| Port | Direction | Location |
| --- | --- | --- |
| key[0] | input | T10 |
| key[1] | input | T3 |
| led[0] | output | C13 |
| led[1] | output | A13 |
| led[2] | output | N16 |
| led[3] | output | N14 |

### 代码

.. tabset::

    ## decode_led_on.v
    Verilog文件；
    定义了两个按键输入端口，和四个输出端口。根据按键输入的状态，译码输出到对应的端口。
    ```verilog
    module decode_led_on(
        input  [1:0] key,
        output [3:0] led
    );
        assign led[0] = !( key[0] & key[1] ) ;
        assign led[1] = !(!key[0] & key[1] ) ;
        assign led[2] = !( key[0] &!key[1] ) ;
        assign led[3] =  ( key[0] | key[1] ) ;
    endmodule
    ```

    ## decode_led_on.cst
    物理约束文件；
    将 verilog 代码里的端口绑定到 FPGA 引脚上面
    ```txt
    IO_LOC "led[3]" N14;
    IO_LOC "led[2]" N16;
    IO_LOC "led[1]" A13;
    IO_LOC "led[0]" C13;
    IO_LOC "key[1]" T3;
    IO_LOC "key[0]" T10;
    IO_PORT "led[3]" PULL_MODE=UP DRIVE=8;
    IO_PORT "led[2]" PULL_MODE=UP DRIVE=8;
    IO_PORT "led[1]" PULL_MODE=UP DRIVE=8;
    IO_PORT "led[0]" PULL_MODE=UP DRIVE=8;
    IO_PORT "key[1]" PULL_MODE=UP;
    IO_PORT "key[0]" PULL_MODE=UP;
    ```

## 效果

默认只有 LED0 亮；按下 S0 按键 LED1 亮；按下 S1 按键 LED1 亮；按下 S0 和 S2 按键 LED3 亮；

<table>
    <tr>       
        <th colspan="2" >按键</th>
        <th colspan="4">LED 状态</th>
    </tr>
    <tr>
        <td>S0</td>
        <td>S1</td>
        <td>LED0</td>
        <td>LED1</td>
        <td>LED2</td>
        <td>LED3</td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td>亮</td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td>按下</td>
        <td></td>
        <td></td>
        <td>亮</td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td>按下</td>
        <td></td>
        <td></td>
        <td>亮</td>
        <td></td>
    </tr>
    <tr>
        <td>按下</td>
        <td>按下</td>
        <td></td>
        <td></td>
        <td></td>
        <td>亮</td>
    </tr>
</table>

<p id="back">
    <a href="#" onClick="javascript :history.back(-1);">返回上一页(Back)</a>
</p>