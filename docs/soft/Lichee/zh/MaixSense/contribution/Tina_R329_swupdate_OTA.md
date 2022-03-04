---
title: Tina R329 swupdate OTA 步骤 
keyword: R329, Lichee, Lichee RV, RiscV, linux 
---
- 本文需要有一定的基础，关于镜像源码和镜像烧录方法可以参考以下链接：
> [镜像源码地址](https://github.com/sipeed/R329-Tina-jishu)
> [R329镜像烧录方法](https://wiki.sipeed.com/hardware/zh/maixII/M2A/flash_system.html)

## 进行相关设置
编译路径执行make menuconfig和make ota_menuconfig中分别选中：
- Allwinner > swupdate
- Allwinner > swupdate > Swupdate Settings > General Configuration > MTD support
- Allwinner > swupdate > Image Handlers > ubivol

## 更改相关参数
sys_config.fex中的storage_type 参数改成5（spi nand）
diff --git a/configs/evb5/sys_config.fex b/configs/evb5/sys_config.fex
index e168eb2..076e56d 100755
--- a/configs/evb5/sys_config.fex
+++ b/configs/evb5/sys_config.fex
-23,7 +23,7 eraseflag = 0
;----------------------------------------------------------------------------------
\[target]
boot_clock = 1008
-storage_type = -1
+storage_type = 5

## 编译镜像
编译路径执行 `make -j & pack` 编译主系统并打包，此时会生成文件out/r329-evb5/tina_r329-evb5_uart0.img

## 编译OTA系统
编译路径执行`swupdate_make_recovery_img` 编译OTA系统
此时会生成文件out/r329-evb5/boot_initramfs_recovery.img

## 生成OTA文件
编译路径执行 `swupdate_pack_swu` ，此时会生成文件out/r329-evb5/swupdate/tina-r329-evb5.swu

## 将OTA文件传送至设备
烧写主系统img，再用adb把OTA文件推到设备下：`adb push tina-r329-evb5.swu /mnt/UDISK/`

实际使用的时候就从网络拿到OTA文件即可

## 执行OTA升级
OTA升级，设备端执行：
`swupdate_cmd.sh -i /mnt/UDISK/tina-r329-evb5.swu -e stable,upgrade_recovery`

执行后设备会重启并在重启过程中OTA，因为原log太长，因此仅附部分log:
```shell{.line-numbers}
root@TinaLinux:/rom/sbin# swupdate_cmd.sh -i /mnt/UDISK/tina-r329-evb5.swu -e st
able,upgrade_recovery                                                           
config new swupdate
swu_input: ##-i /mnt/UDISK/tina-r329-evb5.swu -e stable,upgrade_recovery##      
## set swupdate_param done ##                                                   
swu_param: ##-i /mnt/UDISK/tina-r329-evb5.swu##                                 
swu_software: ##stable##                                                        
swu_mode: ##upgrade_recovery##                                                  
###now do swupdate###                                                           
###log in /mnt/UDISK/swupdate.log###                                            
## swupdate -v  -i /mnt/UDISK/tina-r329-evb5.swu -e stable,upgrade_recovery ##  
Connected to SWUpdate via /tmp/swupdateprog                                     
                                                                                
Update started !         
                                                                                
### 此处省略大约一千三百行log                                                            
                                                                                
BusyBox v1.27.2 () built-in shell (ash)                                         
                                                                                
 _____  _              __     _                                                 
|_   _||_| ___  _ _   |  |   |_| ___  _ _  _ _                                  
  | |   _ |   ||   |  |  |__ | ||   || | ||_'_|                                 
  | |  | || | || _ |  |_____||_||_|_||___||_,_|                                 
  |_|  |_||_|_||_|_|  Tina is Based on OpenWrt!                                 
 ----------------------------------------------                                 
 Tina Linux (Neptune, 5C1C9C53)                                                 
 ----------------------------------------------                                 
root@TinaLinux:/#        
```                                           
