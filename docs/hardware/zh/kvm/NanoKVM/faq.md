---
title: F&Q
keywords: NanoKVM, Remote desktop, Lichee, PiKVM, RISCV, tool
---

## 异常修复

**以下解决方法都基于最新的应用，如果遇到问题，请先更新应用，若无法在网页端更新，请参照以下步骤完成强制更新：**
  1. 参考[这里](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/updating.html#%E8%8E%B7%E5%8F%96-IP)连接开发板
  2. 执行：`python /etc/kvm/update-nanokvm.py`
  > 国外用户可能因为DNS原因下载失败，请在 `/etc/resolv.conf` 添加`nameserver 119.29.29.29`或`nameserver 223.5.5.5`后再试
  > 早期版本应用可能不存在该脚本文件，请下载 https://github.com/sipeed/NanoKVM/blob/main/kvmapp/system/update-nanokvm.py 解压赋予执行权限后再试

### 关于密码

  1. 更新至 2.1.5 版本应用后，若之前没有设置过网页密码，登录后会提示修改密码，修改密码时，后台的`root`密码也会同步修改成网页密码，若之前已经修改过网页密码，后台`root`密码不会主动修改，请在终端使用`passwd`或网页设置中点击重置密码以修改;
  2. 应用版本大于 2.1.5 时，若忘记密码，可以按下机身`BOOT`按键10s以上（NanoKVM-Cube的BOOT按键位于USB-HID接口右边，PCIe版本BOOT按键可在面板上找到，较老版本的NanoKVM Full可能没有在对应位置开孔，需要拆机操作）
  3. 若长按无法重置密码，可能是应用版本小于 2.1.5 ，参考[这里](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/flashing.html)重新烧录镜像，注意，重烧镜像后会丢失所有配置信息。

### HID键鼠不工作
  1. 使用网页中 "重置HID" 功能
  2. 部分主机系统对USB键鼠要求较高，需要使用“仅HID”模式，该模式下USB仅模拟键鼠设备，请通过网页鼠标图标中切换该模式
  3. 部分主板系统要求HID键鼠设备带有BIOS标识,NanoKVM可在/boot下创建BIOS来启用该功能,执行`touch /boot/BIOS && restart`
  4. 检查USB接口是否稳定连接, 可查看 OLED 上 HID 图标是否亮起, 或在网页终端使用 `cat /sys/class/udc/4340000.usb/state`, 如果显示未连接, 则认为 USB 线缆接触不良, 请更换 USB 线缆后再试

### BIOS 不识别HID键鼠
  1. 部分主机系统对USB键鼠要求较高，需要使用“仅HID”模式，该模式下USB仅模拟支持BIOS的键鼠设备，请通过网页鼠标图标中切换该模式
  2. 使用网页中 "重置HID" 功能

### 非英文键盘键位错误
  + 键盘的键盘布局需要在被控主机系统设置中修改，以Ubuntu+修改法语键盘为例：
  设置->键盘->输入源->‘+’->添加->搜索"French"，添加

### STA LED 无法正常闪烁

  STA灯用于指示NanoKVM的运行状态，正常工作时，STA灯在不规律闪烁，当STA灯出现长亮/长灭或者 规律性间断熄灭时认为NanoKVM出现故障
  1. 上电后 STA LED 规律性间断熄灭：系统未检测到TF卡中的系统，请检查TF卡是否正确插入，重新烧录TF镜像
  2. STA LED 长时间熄灭：一般在无供电情况下导致，请查看电源状况

  > 若仅使用 USB-HID 供电，在电脑关机时可能会断开USB电源，请参考相关资料，在BIOS中设置USB常供电，或使用辅助供电。
  > 当不慎接入非常规电源后，NanoKVM 可能会烧坏，也会导致 STA LED 熄灭

  3. STA LED 长时间亮起，不闪烁：NanoKVM 正式系统和应用一般不会出现该情况，若在NanoKVM系统内配置其他自定义功能，有概率导致系统卡死，STA LED长亮，建议重新烧录镜像

### 无法获取IP地址

  1. Lite用户首先检查有无插卡, Lite 版本默认不带卡出货,需用户自备TF卡,按照[此处](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/flashing.html)的说明烧卡后重试;
  2. 检查网络交换机是否支持100M, 部分新交换机不支持100M的连接, 请更换交换机后重试
  3. NanoKVM Cube（包括NanoKVM Full 和 NanoKVM Lite）在接入少数电源/HDMI时会导致无法获取IP，请进行以下确认：
  > 拔出所有接口，使用充电宝供电，接入网线，查看是否能获取IP
  > 若可以获取IP，插入HDMI/电脑USB查看IP是否存在
  > 若仅充电宝供电时IP存在，插入HDMI/电脑USB后IP消失则确认出现了该问题，请联系客服购买隔离器以解决

### 登录浏览器界面后，无画面
  1. 被控主机可能处于睡眠状态，按下键盘任意按键尝试唤醒
  2. 非Chrome浏览器可能存在H264无图像而MJPEG模式正常显示，请使用Chrome浏览器再试
  3. PCIe版本可尝试点击`视频`图标下的重置HDMI
  4. Cube版本可打开网页后重新拔插HDMI线缆
  5. 查看OLED上分辨率/或在网页终端输入`echo "$(cat /kvmapp/kvm/width) * $(cat /kvmapp/kvm/height)"`，与被控主机分辨率对比是否相同，如果不同可使用`echo xxx > /kvmapp/kvm/width && echo xxx > /kvmapp/kvm/height` 手动设置分辨率
  > 若主机系统为Windows,显示设置中的分辨率很可能与实际分辨率不符,需在高级->活动信号分辨率中查看
  6. 早期内测版 Full NanoKVM 使用普通排线连接 HDMI 采集板，可能因接触不良导致检测不到 HDMI 信号，可按下图所示重新连接排线，或联系客服购买专用排线
  ![](./../../../assets/NanoKVM/guide/Old_fix.png)
  7. 尝试重启解决：在网页终端中执行`reboot`
  8. 若上述方式无法锁定问题，请在网页终端中执行`cat /proc/cvitek/vi_dbg`
  > 若 `VIDevFPS` 为0，则认为NanoKVM无法获取到HDMI输入，排查以下问题：主机是否输出视频信号、HDMI线缆损坏、Cube是否为早期版本，存在接触不良的情况
  > 若 `VIDevFPS` 非0 、`VIFPS` 为0 ，则认为NanoKVM没有正确配置HDMI参数，Cube可以重新插拔HDMI重新自动获取，PCIe可点击`视频`下`重置HDMI`自动获取
  > 查看 `VIInImgWidth` 和 `VIInImgHeight`与实际HDMI分辨率是否一致，若不同，则认为NanoKVM没有自动获取到正确的HDMI参数，按照第4点手动配置分辨率参数

### 主机休眠唤醒后无画面

  1. 检查是否使用廉价的DP转HDMI（无源转换头）；这类转换接口没有完善的唤醒机制，无法通知 NanoKVM 画面已经恢复
  2. PCIe 版本可以点击重置HDMI按钮来强制重新获取画面
  3. Cube/Lite版本缺少重置功能，请更换有源DP转换接头

### 内网环境下画面延迟异常严重

  1. 尝试更换交换机或电源
  2. 若无效,请联系售后

### OLED上正常显示信息，但无法打开网页
  1. 请强制更新应用

### OLED不亮
  NanoKVM Full和PCIe版本自带OLED用于显示IP等信息，若OLED无法点亮请按一下步骤排查
  1. `2.1.4`版本的应用后添加了OLED休眠功能，按下BOOT按钮可以临时打开OLED
  2. 若 STA LED 闪烁异常，请先考虑系统是否正常启动，按上述`STA LED 无法正常闪烁`步骤排查故障
  3. 尝试强制更新或重新烧录系统

### 关于内存
  1. NanoKVM 总内存(RAM)空间为256MB, 其中视频图像处理使用一块专用的ion内存区域, 在用户空间查看内存会小于256MB
  2. 固件版本号小于 1.3.0 的镜像仅为用户空间保留 128MB 的内存, 1.3.0以及之后的所有镜像, 内存大小扩展到158MB, 有利于Tailscale长时间运行, 请有需要的用户根据[这里](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/flashing.html)的步骤更新镜像
  3. 在设置中启用'内存优化'

### 主机异常重启
  + 早期内测版 Full NanoKVM ATX小板连接主机RESET引脚, 重启NanoKVM时主机可能被重启, 请断开RESET跳线或联系客服购买稳定版配件

### 电流倒灌
  + 早期内测版 Full NanoKVM 存在电流倒灌问题: 主机关机且USB无电源输出, 当连接辅助供电电源时电流会倒灌入主机
  1. 首先建议设置主机关机后USB保持供电
  2. Full版用户: 按下图位置使用电烙铁断开5V电阻或排针短接处, 仅使用辅助供电口供电
      ![](./../../../assets/NanoKVM/guide/fix2.png)

### 尝试断电重启解决未知问题

### 更新过程中如果出现断网等异常情况，可能导致更新失败，请参照以下解决方法：
  1. 参考[这里](https://wiki.sipeed.com/hardware/zh/kvm/NanoKVM/system/updating.html#%E8%8E%B7%E5%8F%96-IP)连接开发板
  2. 执行 `rm -r /kvmapp && cp -r /root/old/ / && mv /old/kvmapp && reboot` 恢复上一版本
  3. 按最上方的方法进行手动强制更新
  4. 重新烧录系统

### 若上述方法不能解决异常，请在论坛,GitHub或QQ群说明您购买的型号和遇到的问题，我们会耐心解答
  + 反馈时，请注明您使用的NanoKVM版本，在什么样的使用环境下（主板型号，系统名称等信息），在什么样的系统配置中（如镜像版本号1.4.0;应用版本号2.2.5;H264;1080P;画质高;帧率30），遇到了什么问题，这样有助于我们复现并解决
  + 若出现无图像显示的问题，请在异常时分别执行以下命令，将输出的log粘贴至issue
  ```shell
  cat /etc/kvm/hw
  cat /etc/kvm/hdmi_version
  cat /etc/kvm/hdmi_mode
  ```
  + 部分问题需要收集运行时的应用log，请按照以下步骤操作：
  ```shell
  # 在网页中打开SSH功能（设置->设备->SSH）
  # 使用网页中设置的密码登录ssh，如果没有设置，默认密码为root
  ssh root@xxx.xxx.xxx.xxx
  # 修改log等级：/etc/kvm/server.yaml->logger->level：info 修改为 debug
  vi /etc/kvm/server.yaml
  # 使用‘i’编辑；使用 ‘Esc’ + :wq 退出
  # 重启KVM服务
  /etc/init.d/S95nanokvm restart
  # 复制log
  ```

## 反馈方式

* MaixHub 论坛：https://maixhub.com/discussion/nanokvm
* GitHub ：https://github.com/sipeed/NanoKVM
* QQ 群: 703230713