.. Lichee zero documentation master file, created by
   sphinx-quickstart on Wed Feb 14 19:21:19 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

荔枝派Zero 用户指南
=======================================

荔枝派Zero是一款精致迷你的Cortex-A7核心板/开发板，适用于初学者学习linux或商用产品开发。

**联系我们：** `Q群 <https://jq.qq.com/?_wv=1027&k=52cCEVU>`_ |
`github <https://github.com/Lichee-Pi>`_ |
`论坛 <http://bbs.lichee.pro>`_ |
`淘宝 <https://shop152705481.taobao.com/category-1266972912.htm>`_ |
`邮箱 <mailto:zepanwucai@gmail.com>`_ | _____ **文档来源：**  `看云 <https://www.kancloud.cn/lichee/lpi0>`_


.. figure:: https://box.kancloud.cn/fb63cd12ae1def9dd50710d2a32dc5c1_1095x740.png
   :width: 800px
   :align: center

   设计框图

.. toctree::
   :maxdepth: 2
   :caption: 初来乍到篇:

   荔枝派与创作者的自我介绍 <入门/intro_cn>
   Linux使用小贴士 <入门/tips>
   认识zero的硬件 <入门/board_intro>
   Docker环境简明教程 <入门/docker_index>


.. toctree::
   :maxdepth: 2
   :caption: 系统开发篇:

   Zero的开发环境分类 <系统开发/type>
   UBOOT适配 <系统开发/uboot_index>
   Linux内核编译 <系统开发/kernel_index>
   BSP内核编译 <系统开发/bsp_index>
   根文件系统编译 <系统开发/filesys_index>
   SPI系统杂谈 <系统开发/SPI_index>
   Zero 镜像烧录 <系统开发/download_index>
   Zero Imager的使用 <系统开发/Imager>

.. toctree::
   :maxdepth: 2
   :caption: 驱动开发篇:

   设备树简介 <驱动/Device_Tree_Intro>
   外设适配 <驱动/peripheral_index>
   设备驱动 <驱动/device_index>


.. toctree::
   :maxdepth: 2
   :caption: 应用开发篇:

   开机自启动 <应用/autorun>
   Segment Fault调试 <应用/debug>
   Zero通过otg与PC共享网络 <应用/otg2PC>
   USB摄像头使用 <应用/USB_cam>
   基于QT的GUI开发 <应用/QT_index>

.. toctree::
   :maxdepth: 2
   :caption: 贡献投稿篇:

   荔枝派任务领取 <贡献/todolist>
   投稿文章精选 <贡献/contents>
   文档构建 <贡献/build_doc>
