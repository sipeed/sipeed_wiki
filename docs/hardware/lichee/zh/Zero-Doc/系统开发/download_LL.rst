分区镜像烧录
===================================

简介：

一步步来的镜像烧录，适合调节各个部位的代码，方便一些特别的底层运作方式

推荐镜像下载位址：hack to 环荣内网 then //192.168.1.89/musume/Lichee/all-2017/all.rar

此镜像中的文件介绍：
   （当时在外出差刚好缺个路由器，于是就做了个路由器镜像）

Lichee_main_gpt.bin
   主GPT头和分区表

Lichee_Zero_ac.bin
   仿基带，就是区分设备用的

eazyboot.mbn
   类似BIOS的界面，其实就是个设置菜单，有个看看用的磁盘检测功能，可以观看进度条在跑，并不检测磁盘，不会衰减磁盘使用寿命

bootlist.mbn
   真正的系统启动选单

Misc.img
   驱动跟一堆底层的东西

splash.img
   里面就一张开机图片，直接将原版的 *drivers/video/logo/logo_linux_clut224.ppm* 移植过来的，可以任意修改

system.img
   路由器系统，需配合Zero底板与TF-Wifi-Card，LCD小屏使用

recovery.img
   仅恢复cache与Set，无其他功能，跟戳路由器复位效果差不多

userdata.img
  初账号：Lichee Zero
  
  密码：88888888

Web.img
   就一个荔枝派Zero的欢迎页面，单独放着方便大家修改成自己喜欢的页面

步骤：
   见云汉荔枝派板块系统名称帖子
