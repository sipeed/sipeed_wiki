---
title: 一键镜像烧录指南
---

简介：最方便的镜像烧录方法，类似于ghost一键装机

两面性：

- 优点：装机速度快，无需任何专业知识，直接安装，方便效验成果
- 缺点：不适合开发过程，不利于学习

资源获取：

​	下载[Etcher](https://www.balena.io/etcher/ "Etcher")

​	下载[SD Card Formatter](https://www.sdcard.org/downloads/formatter/eula_windows/SDCardFormatterv5_WinEN.zip "SDCardFormatter")

操作步骤：

1.  打开SD卡格式化工具

    - SD Format或SDA 插入内存卡
    - 选调整分区大小 ON
    - 注意盘符的选择
    - 然后点击格式化

2.  打开Etcher

    - 解压镜像，得到 .img镜像文件
    - 点击`Flash from file`,选中dd镜像包
    - 点击`Select target`选中sd卡
    - 点击`Flash`烧录
    - 待烧录完成
    ![95133](./../static/System_Development/95133.gif)

3.  插卡

    > 上电
    > 启动
    > 至此，一键烧录完成！



恭喜！您已成功安装荔枝派Zero系统！
