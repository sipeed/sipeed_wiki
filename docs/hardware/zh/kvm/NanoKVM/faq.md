---
title: F&Q
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
---

## 异常修复

### 无法获取IP地址
  1. Lite用户首先检查有无插卡, Lite 版本默认不带卡出货,需用户自备TF卡,按照[此处](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/flashing.html)的说明烧卡后重试;
  2. 检查网络交换机是否支持100M, 部分新交换机不支持100M的连接, 请更换交换机后重试
  3. 尝试更换电源, 部分电源可能导致 NanoKVM 获取不到IP, 或影响网速

### 登录浏览器界面后，无画面
  1. 确保HDMI有输出信号, 重新拔插HDMI线缆
  2. 进入网页终端，执行 `/etc/init.d/S95nanokvm restart` 重启服务。
  3. 如果上述方式无法恢复正常，点击界面上的检查更新，更新应用
  4. 早期内测版 Full NanoKVM 使用普通排线连接 HDMI 采集板，可能因接触不良导致检测不到 HDMI 信号，可按下图所示拆解，并重新连接排线
      ![](./../../../assets/NanoKVM/guide/Old_fix.png)

### OLED上正常显示信息，但无法打开网页
  1. 参考[这里](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/updating.html#%E8%8E%B7%E5%8F%96-IP)连接开发板
  2. 输入指令`rm /etc/kvm/server.yaml`
  3. 执行 `reboot` 重启系统

### HID键鼠不工作
  1. 使用网页中 "重置HID" 功能
  2. 检查USB接口是否稳定连接, 可查看 OLED 上 HID 图标是否亮起, 或在网页终端使用 `cat /sys/class/udc/4340000.usb/state`, 如果显示未连接, 则认为 USB 线缆接触不良, 请更换 USB 线缆后再试

### BIOS 不识别HID键鼠
  + 部分主板BIOS要求HID键鼠设备带有BIOS标识,NanoKVM可在/boot下创建BIOS来启用该功能,
  1. 执行`touch /boot/BIOS && restart`

### 关于内存
  + NanoKVM 总内存(RAM)空间为256MB, 其中视频图像处理使用一块专用的ion内存区域, 在用户空间查看内存会小于256MB
  + 固件版本号小于 1.3.0 的镜像仅为用户空间保留 128MB 的内存, 1.3.0以及之后的所有镜像, 内存大小扩展到158MB, 有利于Tailscale长时间运行, 请有需要的用户根据[这里](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/flashing.html)的步骤更新镜像

### 主机异常重启
  + 早期内测版 Full NanoKVM ATX小板连接主机RESET引脚, 重启NanoKVM时主机可能被重启, 请断开RESET跳线

### 电流倒灌
  + 早期内测版 Full NanoKVM 存在电流倒灌问题: 主机关机且USB无电源输出, 当连接辅助供电电源时电流会倒灌入主机
  1. 首先建议设置主机关机后USB保持供电
  2. Full版用户: 按下图位置使用电烙铁断开5V电阻或排针短接处, 仅使用辅助供电口供电
      ![](./../../../assets/NanoKVM/guide/fix2.png)

### 尝试断电重启解决未知问题

### 更新过程中如果出现断网等异常情况，可能导致更新失败，若旧应用也无法启动时，请参照以下解决方法：
  1. 参考[这里](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/updating.html#%E8%8E%B7%E5%8F%96-IP)连接开发板
  2. 执行 `rm -r /kvmapp && cp -r /root/old/ / && mv /old/kvmapp`
  3. 执行 `reboot` 重启系统
  4. 重新烧录系统
  5. 手动更新: 可以下载后执行 python 更新脚本, 来手动完成更新过程
        1. 下载[update-nanokvm.py.zip](https://github.com/user-attachments/files/16939944/update-nanokvm.py.zip)并解压
        2. 执行: `python update-nanokvm.py`
        3. 等待更新完成

### 若上述方法不能解决异常，请在论坛,GitHub或QQ群说明您购买的型号和遇到的问题，我们会耐心解答

## 反馈方式

* MaixHub 论坛：https://maixhub.com/discussion/nanokvm
* GitHub ：https://github.com/sipeed/NanoKVM
* QQ 群: 703230713