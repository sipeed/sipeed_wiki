荔枝派Nano 全流程指南
=================================================

荔枝派 Nano，开启你的极客之心。这是一款仅有2.54cm X 3.3cm大小的精致小板，相当于一张SD卡大小，只要您愿意，即可将一颗极客芯随身携带。

.. figure:: https://fdvad021asfd8q.oss-cn-hangzhou.aliyuncs.com/migrate/DSC_0455.png
  :width: 500px
  :align: center

  实物图

.. figure:: https://fdvad021asfd8q.oss-cn-hangzhou.aliyuncs.com/migrate/DSC_0459-min%20(1).JPG
  :width: 500px
  :align: center

  与SD卡对比

荔枝派Nano以不可能的价格，提供了尽可能的能力：

- 3 X TWI
- 2 X SPI
- 3 X UART
- SDIO
- USB OTG
- JTAG
- KEYADC
- RTP
- IR
- OWA out

这些它都能轻松应对，更何况它还支持：

- CSI Camera
- Full HD Video Engine（H.264,H.263,JPEG/MJPEG,etc.）
- RGB LCD Interface
- CVBS Input/Output
- Audio Codec
- I2S/PCM
- SD/eMMc

这都得益于荔枝派Nano的主芯片---全志F1C100s；Arm9架构，16KB D-Cache，32KB I-Cache，支持从SPI Flash或TF卡启动，支持USB OTG载入更新。

荔枝派 Nano 延续了前一代的巧妙设计，2.54mm普通插针焊孔+1.27mm邮票孔贴片设计，方便您自己动手DIY的同时，也支持贴片生产，制作更为复杂的应用。


.. figure:: https://fdvad021asfd8q.oss-cn-hangzhou.aliyuncs.com/migrate/Pin%20Map.png
  :width: 500px
  :align: center

  Pin Map

此外，荔枝派自从初代One以来，不断适配外设，已有TF-Wifi、RGB to VGA、40 pin RGB、 LCD、RGB to GPIO、Camera等经过广泛实践验证过的成熟模块。

.. figure:: https://fdvad021asfd8q.oss-cn-hangzhou.aliyuncs.com/migrate/module.png
  :width: 500px
  :align: center

  部分模块

荔枝派Nano 现已可选 TF版 与 wifi版：

.. figure:: https://img.alicdn.com/imgextra/i4/272610009/TB2L22ihQKWBuNjy1zjXXcOypXa_!!272610009.png
  :width: 500px
  :align: center

  对比图

荔枝派 Nano现已获得RT-Thread的官方支持，您可应用RT-Thread丰富的生态资源，快速高效地进行原型设计；

荔枝派提倡开发者协同开发，即将推出有偿外设驱动适配任务，以及提供快餐式外包项目，欢迎各位技术大神为开发者们贡献技术力量！

欢迎各位加入 `荔枝派交流群826307240 <https://jq.qq.com/?_wv=1027&k=52cCEVU>`_ | `荔枝派Telegram电报群 <https://t.me/sipeed>`_ | `荔枝派社区 <http://bbs.lichee.pro>`_。

.. figure:: https://fdvad021asfd8q.oss-cn-hangzhou.aliyuncs.com/migrate/QQ_Group_2.jpg
   :width: 250px
   :align: center

.. toctree::
   :maxdepth: 2
   :caption: 上手体验篇

   初见 <get_started/first_eye>
   即食 <get_started/first_eat>

.. toctree::
   :maxdepth: 2
   :caption: 系统适配篇

   总述 <build_sys/build_index>
   镜像包一键烧录 <build_sys/onekey>
   docker快速搭建环境 <build_sys/docker>
   uboot传递参数 <build_sys/bootargs>
   主线Linux编译 <build_sys/kernel>
   设备树添加节点 <build_sys/devicetree>
   根文件系统编译 <build_sys/rootfs>
   SPI-Flash 系统编译 <build_sys/build_flash>

.. toctree::
   :maxdepth: 2
   :caption: 驱动开发篇

   电容触摸屏适配 <driver/touchscreen>

.. toctree::
   :maxdepth: 2
   :caption: 从挖坑到填坑篇

   开箱介绍 <step_by_step/one_openbox>
   编译使用sunxi-tools <step_by_step/two_sunxi-tools>
   编译测试uboot <step_by_step/three_uboot>
   编译测试linux <step_by_step/four_linux>

.. toctree::
  :maxdepth: 2
  :caption: 应用开发篇

  littlevGL的使用 <application/littlevgl>

.. toctree::
   :maxdepth: 2
   :caption: 贡献投稿篇

   前言 <contribution/introduction>
   Todolist <contribution/todolist>
   快餐任务相关小事项 <contribution/task_tips>
   文档任务相关小事项 <contribution/doc_tips>
   文档构建 <contribution/build_doc>
