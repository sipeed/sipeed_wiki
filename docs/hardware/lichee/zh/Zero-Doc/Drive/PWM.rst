PWM输出
=============================

.. contents:: 本文目录

PWM驱动
-----------------------------

dtsi: 增加PWM0，1的引脚 

:: 

    pwm0_pins: pwm0 {
            pins = "PB4";
            function = "pwm0";
    };
    pwm1_pins: pwm1 {
            pins = "PB5";
            function = "pwm1";
    };

:: 

    pwm: pwm@01c21400 {
                compatible = "allwinner,sun7i-a20-pwm";		//这里选a20是因为v3s和a20一样有两路pwm
                reg = <0x01c21400 0xC>;
                clocks = <&osc24M>;
                #pwm-cells = <3>;
                status = "okay";
        };   

dts中使能PWM：

:: 

    &pwm {
            pinctrl-names = "default";
            pinctrl-0 = <&pwm0_pins>, <&pwm1_pins>;
            status = "okay";
    };

sysfs里使能：

:: 

    echo 0 > /sys/class/pwm/pwmchip0/export
    echo 1000000 > /sys/class/pwm/pwmchip0/pwm0/period
    echo 500000 > /sys/class/pwm/pwmchip0/pwm0/duty_cycle
    echo 1 > /sys/class/pwm/pwmchip0/pwm0/enable

    echo 1 > /sys/class/pwm/pwmchip0/export
    echo 1000000 > /sys/class/pwm/pwmchip0/pwm1/period
    echo 200000 > /sys/class/pwm/pwmchip0/pwm1/duty_cycle	
    echo 1 > /sys/class/pwm/pwmchip0/pwm1/enable		//注意一定要配置好参数后再使能，否则会报参数错误

- polarity：接受normal或inversed两个参数.
- period：表示pwm波的周期(单位：纳秒)；
- duty_cycle：在normal模式下，表示一个周期内高电平持续的时间（单位：纳秒），所以duty_cycle <= period；在reversed模式下，表示一个周期中低电平持续的时间（单位：纳秒）；
- enable：向其中写入1表示启动pwm，写入0，表示关闭pwm；

注意V3S的PWM由24M分频而来，无法生成太高频的pwm。

PWM驱动分析
----------------------------------

PWM驱动在 *drivers/pwm/pwm-sun4i.c* 中。

插入驱动：

.. code-block:: c

    static int sun4i_pwm_probe(struct platform_device *pdev)
    {
        struct sun4i_pwm_chip *pwm;
        struct resource *res;
        int ret;
        const struct of_device_id *match;

        match = of_match_device(sun4i_pwm_dt_ids, &pdev->dev);	//在设备树中查找节点

        pwm = devm_kzalloc(&pdev->dev, sizeof(*pwm), GFP_KERNEL);
        if (!pwm)
            return -ENOMEM;

        res = platform_get_resource(pdev, IORESOURCE_MEM, 0);	
        pwm->base = devm_ioremap_resource(&pdev->dev, res);	//申请寄存器的内存空间
        if (IS_ERR(pwm->base))
            return PTR_ERR(pwm->base);

        pwm->clk = devm_clk_get(&pdev->dev, NULL);
        if (IS_ERR(pwm->clk))
            return PTR_ERR(pwm->clk);

        pwm->data = match->data;
        pwm->chip.dev = &pdev->dev;
        pwm->chip.ops = &sun4i_pwm_ops;
        pwm->chip.base = -1;
        pwm->chip.npwm = pwm->data->npwm;
        pwm->chip.of_xlate = of_pwm_xlate_with_flags;
        pwm->chip.of_pwm_n_cells = 3;

        spin_lock_init(&pwm->ctrl_lock);

        ret = pwmchip_add(&pwm->chip);	//在/sys/class/pwm/下创建pwmchip0X
        if (ret < 0) {
            dev_err(&pdev->dev, "failed to add PWM chip: %d\n", ret);
            return ret;
        }

        platform_set_drvdata(pdev, pwm);

        return 0;
    }   
