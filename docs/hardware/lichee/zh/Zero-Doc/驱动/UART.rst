UART操作
=============================

.. contents:: 本文目录

基础操作
-----------------------------

首先在dts里使能UART：

:: 

    sun8i-v3s.dtsi:
    uart0_pins_a: uart0@0 { pins = "PB8", "PB9";function = "uart0";bias-pull-up; };
    uart1_pins_a: uart1@0 { pins = "PE21", "PE22";function = "uart1";bias-pull-up; };
    uart2_pins_a: uart2@0 { pins = "PB0", "PB1";function = "uart2";bias-pull-up; };

    sun8i-v3s-licheepi-zero.dts:
    &uart0 { pinctrl-0 = <&uart0_pins_a>;pinctrl-names = "default";status = "okay"; };
    &uart1 { pinctrl-0 = <&uart1_pins_a>;pinctrl-names = "default";status = "okay"; };
    &uart2 { pinctrl-0 = <&uart2_pins_a>;pinctrl-names = "default";status = "okay"; };

然后启动后就能看到ttyS0~ttyS2了

再使用常见串口软件就能使用

波特率分频问题
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

为了串口通信稳定，一般要求波特率误差在2.5%以内。

V3S的uart是挂在APB2下，而APB2时钟是24M，所以对一些高速率的波特率，难以分频到合适的频率。

以921600为例，下面进行修改：

进入 *uboot的arch/arm/mach-sunxi/clock_sun6i.c*，修改uart时钟：

.. code-block:: c

    void clock_init_uart(void)
    {
    #if CONFIG_CONS_INDEX < 5
            struct sunxi_ccm_reg *const ccm =
                    (struct sunxi_ccm_reg *)SUNXI_CCM_BASE;

            /* uart clock source is apb2 */
            writel(APB2_CLK_SRC_OSC24M|      //这里改为APB2_CLK_SRC_PLL6，从内部pll6时钟分频
                APB2_CLK_RATE_N_1|               //这里预分频不变
                APB2_CLK_RATE_M(1),
                &ccm->apb2_div);

pll6时钟默认为600MHz，可以分出比较高的串口波特率。

600/0.9216/16=40.69， 舍入为41，相对误差为0.75%

.. code-block:: c
   :caption: 然后再修改include/configs/sunxi-common.h

    /* ns16550 reg in the low bits of cpu reg */
    #define CONFIG_SYS_NS16550_CLK          24000000    //这里改为600000000
    #ifndef CONFIG_DM_SERIAL

剩余的就是按照原有方法修改波特率了。
