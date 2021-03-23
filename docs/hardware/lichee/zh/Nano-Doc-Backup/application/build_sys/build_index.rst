TF卡分区
==========================

本章主要描述内核与根文件系统的构建；

在TF卡上构建系统
--------------------------

在前文我们已经成功构建了 bootloader，我们接下来需要放进TF卡的内容有：

第一分区： 
    - boot.scr  
    - zImage
    - suniv-f1c100s-licheepi-nano.dtb
第二分区： 
    - 根文件系统内容

在TF卡上构建系统之前，我们需要将TF卡进行分区与格式化；

.. code-block:: bash

   sudo fdisk -l     # 首先查看电脑上已插入的TF卡的设备号
   sudo umount /dev/sdXx # 若自动挂载了TF设备，请先卸载
   sudo fdisk /dev/sdX   # 进行分区操作 
   # 若已存分区即按 d 删除各个分区
   # 通过 n 新建分区，第一分区暂且申请为32M(足够大了...)，剩下的空间都给第二分区
   # w 保存写入并退出
   sudo mkfs.vfat /dev/sdX1 # 将第一分区格式化成FAT
   sudo mkfs.ext4 /dev/sdX2 # 将第一分区格式化成EXT4

具体分区操作，可参考github上的 `write_all.sh <https://github.com/Zepan/ilichee/tree/master/%E8%B5%84%E6%BA%90%E6%96%87%E4%BB%B6/%E9%95%9C%E5%83%8F%E7%83%A7%E5%86%99>`_ 脚本

.. tip:: Nano一键快速烧录镜像包地址为： https://pan.baidu.com/s/1smzuGS9 ，便于快速验证，无需分区操作 ...


后文 `一键烧录及脚本使用说明 <./onekey.html>`_ 将对各部分内容的构建进行详细描述；

.. admonition:: 交流与答疑

    对于本章内容，如有疑问，欢迎到 `荔枝派 Nano <http://bbs.lichee.pro/t/nano>`_ 提问或分享经验。
