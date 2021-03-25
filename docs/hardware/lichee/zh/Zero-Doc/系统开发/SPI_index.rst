SPI Flash 杂谈
============================================

在一些低成本应用场景，需要在SPI flash上启动系统，这需要对Uboot和系统镜像做些适配。

本节将对SPI flash的编译及相关应用作详细描述。

.. toctree::
   :maxdepth: 2

   SPI Flash 系统编译 <SPI_flash_build>
   sunxi-fel增加对16M以上Flash的支持 <SPI_falsh_doc1>
   overlayfs的使用 <SPI_falsh_doc2>
   jffs2文件系统挂载不上的常见原因 <SPI_falsh_doc3>
   JFFS2文件系统简介 <SPI_falsh_doc4>
   uboot 对SPI flash 的识别 <SPI_falsh_doc5>
   关于系统reboot <SPI_falsh_doc6>
