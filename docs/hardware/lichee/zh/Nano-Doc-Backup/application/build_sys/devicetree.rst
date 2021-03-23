设备树添加节点
================================

.. contents:: 本文目录

Nano 设备树简介
--------------------------------

Nano的设备树在源码的 :menuselection:`linux --> arch --> arm --> boot --> dts --> suniv-f1c100s-licheepi-nano.dts`；

该文件描述了各类外设的定义与配置，以下做简要描述；

    - 其中由 / { ... } 包裹的为根节点，定义了各类总线、外设的配置；
    - &xxx { ... } 所包裹的内容为引用，其定义来自于 suniv.dtsi (suniv系列设备通用的定义)
    - compatible 属性，将与驱动源码中的 compatible 定义对应，进行识别选择；
    - 设备树各部分的编写，可参考 :menuselection:`linux --> Documentation --> devicetree --> bindings` 下各个模组
    - 设备树整体的详细介绍，请参考 `Device_Tree <https://elinux.org/Device_Tree_Reference>`_ ， `zero文档 <http://zero.lichee.pro/%E9%A9%B1%E5%8A%A8/Device_Tree_Intro.html>`_ 中也有较为详细的描述；

修改设备树中 LCD 配置
-------------------------------

当前默认的 LCD配置 为480X272大小的屏幕，

    .. centered:: *"qiaodian,qd43003c0-40", "simple-panel"*


若要修改为适配800X480的屏，此处应当：

    / { } 所包裹的根节点目录下，panel属性下的compatible，应修改为：
        
        .. centered:: *"lg,lb070wv8", "simple-panel"*

    :menuselection:`linux --> drivers --> gpu --> drm --> panel` 下有许多屏幕的配置，可挑选合适的进行配置；

添加底板上的 RGB LED 节点配置
-------------------------------

.. code-block:: bash
   :caption: / { } 所包裹的根节点目录下进行添加

    leds {
		compatible = "gpio-leds";

		blue_led {
			label = "licheepi:blue:usr";
			gpios = <&pio 4 4 GPIO_ACTIVE_LOW>; /* PE4 */
		};

		green_led {
			label = "licheepi:green:usr";
			gpios = <&pio 4 5 GPIO_ACTIVE_LOW>; /* PE5 */
			default-state = "on";
		};

		red_led {
			label = "licheepi:red:usr";
			gpios = <&pio 5 6 GPIO_ACTIVE_LOW>; /* PE6 */
		};
	};

添加电容触摸屏的支持
------------------------------

电容触摸屏的控制芯片为GT911，使用I2C接口，我们要在设备树文件中添加定义；

.. code-block:: bash
    :caption: （笔者此处直接在 suniv.dtsi 内进行修改）
    
    // 添加在soc节点下
    // 此处添加的属性与配置，来自于查找用户手册以及兼容设备

    i2c0: i2c@1C27000 {
			compatible = "allwinner,sun6i-a31-i2c";
			reg = <0x01C27000 0x400>;
			interrupts = <7>;
			clocks = <&ccu CLK_BUS_I2C0>;
			resets = <&ccu RST_BUS_I2C0>;
			pinctrl-names = "default";
			pinctrl-0 = <&i2c0_pins>;
			status = "disabled";
			#address-cells = <1>;
			#size-cells = <0>;
		};

    // 在pio节点下，添加i2c引脚定义

    i2c0_pins: i2c0 {
			pins = "PE11", "PE12";
			function = "i2c0";
		};

.. code-block:: bash
    :caption: 在suniv-f1c100s-licheepi-nano.dts中添加引用

    /* 首先要添加的头文件： */
    #include <dt-bindings/input/input.h>
    #include <dt-bindings/interrupt-controller/irq.h>

    /* 添加引用 */
    &i2c0 {
        pinctrl-0 = <&i2c0_pins>;
        pinctrl-names = "default";
        status = "okay";

        gt911: touchscreen@14 {
            compatible = "goodix,gt911";
            reg = <0x14>;
            interrupt-parent = <&pio>;
            interrupts = <4 10 IRQ_TYPE_EDGE_FALLING>; /* (PE10) */
            pinctrl-names = "default";
            pinctrl-0 = <&ts_reset_pin>;
            irq-gpios = <&pio 4 10 GPIO_ACTIVE_HIGH>; /* (PE10) */
            reset-gpios = <&pio 4 9 GPIO_ACTIVE_HIGH>; /* RST (PE9) */
            /* touchscreen-swapped-x-y */
        };
    }; 

    &pio {
        ts_reset_pin: ts_reset_pin@0 {
            pins = "PE9";
            function = "gpio_out";
        };
    };

完成添加～若测试的触摸屏的xy方向颠倒，请添加或去掉gt911节点下的 *touchscreen-swapped-x-y* 属性。

编译生成 dtb文件
--------------------------------

``make ARCH=arm CROSS_COMPILE=arm-linux-gnueabi- dtbs -j4``

生成的 dtb文件 在 dts同级目录下，将其放入 TF卡第一分区。

.. admonition:: 交流与答疑

    对于本节内容，如有疑问，欢迎到 `主线linux 编译交流帖 <http://bbs.lichee.pro/d/22-linux>`_ 提问或分享经验。