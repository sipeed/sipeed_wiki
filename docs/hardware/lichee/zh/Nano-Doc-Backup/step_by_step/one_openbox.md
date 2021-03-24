入手lichee-pi-nano
==================

* * * * *

到荔枝淘宝购买
-----------------

[此处购买](https://item.taobao.com/item.htm?spm=a230r.1.14.7.2a311bf5BmOgwm&id=584657396198&ns=1&abbucket=8#detail)

拆箱
-------

- lichee-pi-nano kit套餐 :
    ![](./../_static/step_by_step/nano_kit.jpg)
- lichee-pi-nano F(16M) :
    ![](./../_static/step_by_step/nanoF(16).jpg)
- lichee-pi-nano F(8M) :
    ![](./../_static/step_by_step/nanoF(8).jpg)
- lichee-pi-nano (9.9) :
    ![](./../_static/step_by_step/nanoF(9.9).jpg)
- LCDC(带电容触摸) :
    ![](./../_static/step_by_step/LCDC.jpg)
- LCD :
    ![](./../_static/step_by_step/LCD.jpg)

准备工具
-----------

- 准备一个usb转ttl,用于查看console打印:
    ![](./../_static/step_by_step/usb_to_ttl.jpg)
- 准备一根usb线,一般mp4那种,用于下载固件到spi\_flash和sdram,方便调试.
    ![](./../_static/step_by_step/micro_usb_line.jpg)

# 焊接

- 焊接
    ![](./../_static/step_by_step/seal.jpg)

测试板子是否正常
-------------------

-   使用一键镜像包构建启动固件并下载到spiflash或tf卡

    教程地址:
    [一键烧录镜像包](./../build_sys/onekey.md)
    固件下载完后是使用杜邦线连接nano和电脑, 在终端输入sudo minicom
    -s,配置好串口参数(115200 8N1).

-   正常运行的打印截图

![](../_static/step_by_step/console_run_is_ok.png)

-   正常运行的液晶显示
![](../_static/step_by_step/lcd_run_is_ok.jpg)
