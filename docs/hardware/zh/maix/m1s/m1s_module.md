---
title: M1s 模组
keywords: M1s ,模组
update:
  - date: 2022-11-09
    version: v0.2
    author: wonder
    content:
      - 修改部分描述错误
      - 增加注意事项
      - 增加软件描述栏目
  - date: 2022-10-18
    version: v0.1
    author: wonder
    content:
      - 初次编写文档
---

## 模组概述

Sipeed M1s 模组是基于[博流智能科技](http://www.bouffalolab.com/)的 BL808 芯片所设计的一款 AIOT 模组，主控芯片包含三个核心，具有 WiFi/BT/BLE/Zigbee 等无线互联单元，包含多个 CPU 以及音频编码译码器、视频编码译码器和 AI 硬件加速器（BLAI-100），适用于各种高性能和低功耗应用领域。

购买链接：[淘宝](https://item.taobao.com/item.htm?id=691108452443)

<img src="./assets/m1s_module/m1s_module_outlook.png" alt="m1s_module_outlook" width=35%>

## 模组特点

- 主芯片 BL808 RV64 480MHz + RV32 320MHz + NPU BLAI 100GOPS
- 板载 SPI FLASH（默认 16MByte）
- 支持2.4G WIFI / BT / BLE
- 支持 IPEX 一代天线座子和 PCB 板载天线
- 邮票孔引出所有 IO

## 模组参数

<table>
    <thead>
        <tr>
            <th colspan = "2" > M1s 模组 </th>   
        </tr>
    </thead>
    <tbody>
    <tr>    
        <td rowspan="8" style="white-space:nowrap">主控 BL808 处理器</td>
    </tr>
    <tr>
        <td>三核异构RISC-V CPUs：<br>· RV64GCV 480MHz <br>· RV32GCP 320MHz <br>· RV32EMC 160MHz</td>
    </tr>
    <tr>
        <td>AI NN 通用硬件加速器：<br>· BLAI-100 用于视频/音频检测/识别，100GOPS 算力</td>
    </tr>
    <tr>
        <td>内置 768KB SRAM + 64MB UHS PSRAM</td>
    </tr>
    <tr>
        <td>编解码：<br>- MJPEG and H264(Baseline/Main)<br>- 1920x1080@30fps + 640x480@30fps
        </td>
    </tr>
    <tr>
        <td>接口：<br>- 摄像头接口 ：DVP 和 MIPI-CSI<br>- 显示接口：SPI、DBI、DPI(RGB)</td>
    </tr>
    <tr>
        <td>无线：<br>- 支持 Wi-Fi 802.11 b/g/n<br>- 支持 Bluetooth 5.x Dual-mode(BT+BLE)<br>- 支持 Wi-Fi / 蓝牙 共存</td>
    </tr>
    <tr>
      <td>USB 2.0 HS OTG</td>
    </tr>
    <tr>    
        <td rowspan="3" style="white-space:nowrap"> 板载部件 </td>
    </tr>
    <tr>
        <td>板载 SPI FLASH（可选容量）</td>
    </tr>
    <tr>
        <td>支持 IPEX 一代天线座子和 PCB 板载天线</td>
    </tr>
    </tbody>
    <tr>    
        <td rowspan="6" style="white-space:nowrap"> 其他说明 </td>
    </tr>
    <tr>
        <td>
        尺寸：31mm (L) x 18mm (W)
        </td>
    </tr>
    <tr>
      <td>
        3D 模型文件下载：<a href="https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/5_3D_file">点击跳转</a>
      </td>
    </tr>
    <tr>
        <td>外部供电需求：<br>VDDIO4/VDDIO3/VDDIO1/ 和 3V3 这几路电源必须给模块提供才能正常工作</td>
    </tr>
    <tr>
        <td>温升: &lt;30K</td>
    </tr>
    <tr>
        <td>工作温度范围:-10℃ ~ 65℃</td>
    </tr>
    </tbody>    
</table>

<img src="./assets/m1s_module/m1s_module_size.png" alt="m1s_module_size" width=35%>

## 引脚分布

<img src="./assets/m1s_module/m1s_pins.png" alt="m1s_pins" width=55%>

## 产品对比

<table>
<thead>
<tr>
  <th style="text-align:left">项目</th>
  <th style="text-align:left">M1(K210)</th>
  <th style="text-align:left">M1s(BL808)</th>
  <th style="text-align:left">ESP32-S3-WROOM-N16R8</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="text-align:left">CPU</td>
  <td style="text-align:left">RV64@400MHz x2</td>
  <td style="text-align:left">· RV64GCV@480MHz<br>· RV32GCP@320MHz<br>· RV32EMC@160MHz</td>
  <td style="text-align:left;white-space:nowrap">Xtensa LX7@240MHz x2</td>
</tr>
<tr>
  <td style="text-align:left">RAM</td>
  <td style="text-align:left">8MB SRAM</td>
  <td style="text-align:left;white-space:nowrap">· 768KB SRAM <br>·  64MB UHS PSRAM(2000MHz)</td>
  <td style="text-align:left">· 512KB SRAM<br>· 8MB PSRAM</td>
</tr>
<tr>
  <td style="text-align:left">Flash</td>
  <td style="text-align:left">16MB</td>
  <td style="text-align:left">16MB</td>
  <td style="text-align:left">16MB</td>
</tr>
<tr>
  <td style="text-align:left">OS</td>
  <td style="text-align:left">· FreeRTOS<br>· No-mmu Linux</td>
  <td style="text-align:left">· FreeRTOS<br>· Linux</td>
  <td style="text-align:left">RTOS</td>
</tr>
<tr>
  <td style="text-align:left">NPU</td>
  <td style="text-align:left;white-space:nowrap">230GOPS with limited OPS</td>
  <td style="text-align:left;white-space:nowrap">100GOPS with rich OPS</td>
  <td style="text-align:left"></td>
</tr>
<tr>
  <td style="text-align:left">Camera</td>
  <td style="text-align:left">DVP, up to VGA</td>
  <td style="text-align:left">MIPI + DVP, up to 1080P h264</td>
  <td style="text-align:left">DVP</td>
</tr>
<tr>
  <td style="text-align:left">Display</td>
  <td style="text-align:left">· SPI<br>· 8bits MCU LCD</td>
  <td style="text-align:left">· SPI<br>· 8bits MCU LCD<br>· RGB LCD</td>
  <td style="text-align:left">· SPI<br>· 8bits MCU LCD</td>
</tr>
<tr>
  <td style="text-align:left">Audio</td>
  <td style="text-align:left">I2S</td>
  <td style="text-align:left">· I2S<br>· Analog Audio Input/Output</td>
  <td style="text-align:left">I2S</td>
</tr>
<tr>
  <td style="text-align:left">Wireless</td>
  <td style="text-align:left"></td>
  <td style="text-align:left">WIFI+BLE+Zigbee</td>
  <td style="text-align:left">WIFI + BLE</td>
</tr>
<tr>
  <td style="text-align:left">USB</td>
  <td style="text-align:left"></td>
  <td style="text-align:left">USB2.0 OTG HS</td>
  <td style="text-align:left">USB1.1 OTG</td>
</tr>
<tr>
  <td style="text-align:left">Accelerator</td>
  <td style="text-align:left">FFT</td>
  <td style="text-align:left">· Scaler<br>·  OSD<br>·  MJPED<br>·  G2D<br>·  H264</td>
  <td style="text-align:left"></td>
</tr>
<tr>
  <td style="text-align:left">Perpheral</td>
  <td style="text-align:left">UART, SPI, IIC</td>
  <td style="text-align:left">UART, SPI, IIC, SDIO ETH(RMII), ADC/DAC</td>
  <td style="text-align:left">UART, SPI, IIC, SDIO, ADC</td>
</tr>
<tr>
  <td style="text-align:left">Size</td>
  <td style="text-align:left">25.4 x 25.4 mm</td>
  <td style="text-align:left">31 x 18 mm</td>
  <td style="text-align:left">25.5 x 18 mm</td>
</tr>
<tr>
  <td style="text-align:left">Price</td>
  <td style="text-align:left">$6</td>
  <td style="text-align:left">$6</td>
  <td style="text-align:left">$4.3(digikey)</td>
</tr>
</tbody>
</table>

## 软件描述

<table>
    <thead>
        <tr>
            <th colspan = "2" > M1s 模组 </th>   
        </tr>
    </thead>
    <tbody>
        <tr>
          <td>OS</td>
          <td>· 完备支持FreeRTOS<br>· 基础支持Linux</td>
        </tr>
        <tr>
          <td>开发方式</td>
          <td>· 原生C SDK<br>· MaixHAL C 模块<br>· pikascript python 脚本</td>
        </tr>
        <tr>
          <td>固件下载</td>
          <td>· 串口下载<br>· 虚拟磁盘拖拽式更新</td>
        </tr>
        <tr>
          <td>AI 推理框架</td>
          <td>· 支持原生SDK的BLAI加速推理引擎<br>· 支持通用TinyMaix推理引擎</td>
        </tr>
        <tr>
          <td>AI 模型下载</td>
          <td>· <a herf="https://maixhub.com/">MaixHub</a> 下载。支持 人脸检测，识别，姿态检测，手势检测 等</td>
        </tr>
        <tr>
          <td>Sipeed 参考示例</td>
          <td>· https://gitee.com/sipeed/M1s_BL808_example</td>
        </tr>
    </tbody>
</table>

## 模组资料

- [规格书](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/1_Specification)
- [原理图](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/2_Schematic)
- [封装库](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/7_Package)
- [位号图](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/3_Bit_number_map)
- [尺寸图](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/4_Dimensional_drawing)
- [3D 模型文件](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/5_3D_file)
- [芯片数据手册](https://dl.sipeed.com/shareURL/MAIX/M1s/M1s/6_Chip_Manual)

---

- [SDK](https://gitee.com/sipeed/M1s_BL808_SDK) (gitee) 
- [Examples](https://gitee.com/sipeed/M1s_BL808_example)（gitee）
- 交流 QQ 群：`592731168` 。[点我加群](https://jq.qq.com/?_wv=1027&k=uyKNhTeu)
- 论坛：[bbs.sipeed.com](https://bbs.sipeed.com/)

## 注意事项

<table>
    <tr>
        <th>项目</th>
        <th>注意事项</th>
    </tr>
    <tr>
        <td>静电防护</td>
        <td>请避免静电打到 PCBA 上；接触 PCBA 之前请把手的静电释放掉</td>
    </tr>
    <tr>
        <td>容忍电压</td>
        <td> 每个 GPIO 的工作电压已经在原理图中标注出来，请不要让 GPIO 的实际工作的电压超过额定值，否则会引起 PCBA 的永久性损坏 </td>
    </tr>
    <tr>
        <td>FPC 座子</td>
        <td>在连接 FPC 软排线的时候，请确保排线无偏侈地完整地插入到排线中</td>
    </tr>
    <tr>
        <td>插拔</td>
        <td>请完全断电后才进行插拔操作</td>
    </tr>
    <tr>
        <td>避免短路</td>
        <td>请在上电过程中，避免任何液体和金属触碰到 PCBA 上的元件的焊盘，否则会导致路，烧毁 PCBA</td>
    </tr>
    <tr>
        <td>设计建议</td>
        <td>为该模组设计底板时，建议先看这个帖子 <a href="https://bbs.sipeed.com/thread/1721">https://bbs.sipeed.com/thread/1721</a></td>
    </tr>
    <tr>
        <td>BANK 划分</td>
        <td>
            VDDIO1：GPIO 0-8，1.8V/3.3V<br>
            VDDIO2：GPIO 11-15，GPIO 40-41, 3.3V only<br>
            VDDIO3：GPIO 16-23，1.8V/3.3V<br>
            VDDIO4：GPIO 24-39，1.8V/3.3V<br>        
        </td>
    </tr>    
    <tr>
        <td>BOOT 模式选择</td>
        <td>
        在启动时，芯片判定 BOOT 引脚的电平，选择两个启动选项之一<br>
        · BOOT 高电平：从 FLASH 存储启动
        · BOOT 低电平：进入串口下载模式
        </td>
    </tr>
</table>

## 联系方式

M1s 模组可以在多种场景实现客户不同方面的需要，技术支持和商业合作请联系使用邮箱 [support@sipeed.com](support@sipeed.com)
