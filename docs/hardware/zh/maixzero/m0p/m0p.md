---
title: M0P 模组
keywords: M0P ,模组, bl618, BL618
update:
  - date: 2023-03-09
    version: v0.1
    author: wonder
    content:
      - 初次编写文档
---

## 模组概述

Sipeed M0P 模组是基于[博流智能科技](http://www.bouffalolab.com/)的 BL618 芯片所设计的一款 AIOT 模组，支持 WIFI6、蓝牙 5.2 等无线协议，邮票孔的让它能快速应用在多种 AIOT 场合。

购买链接：[淘宝](https://item.taobao.com/item.htm?id=710359411812)

<img src="./assets/m0p/m0p_module_outlook.png" alt="m0p_module_outlook" width=15%>

## 模组特点

- 主芯片 BL618 RV32 320MHz RISC-V
- 支持 2.4G WIFI6（IEEE 802.11 b/g/n/ax）
- 支持蓝牙 5.x 双模（BT+BLE）
- 支持 Zigbee / IEEE 802.15.4
- 支持 USB 2.0 HS OTG（480Mhz）
- 支持IPEX一代天线座子和 PCB 板载天线
- 板载 SPI FLASH（可选容量）
- 邮票孔引出所有 IO

## 模组参数

<table>
    <thead>
        <tr>
            <th colspan="3"> M0P 模组 </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="18" style="white-space:nowrap">主控 BL618 处理器</td>
        </tr>
        <tr>
            <td colspan="2">RISC-V CPUs：RV32 320MHz</td>
        </tr>
        <tr>
            <td colspan="2">SRAM: 480KB + 4MB </td>
        </tr>
        <tr>
            <td rowspan="15"> 支持接口 </td>
        </tr>
        <tr>
            <td>DVP Camera</td>
        </tr>
        <tr>
            <td>Display（QSPI、DBI）</td>
        </tr>
        <tr>
            <td>USB2.0 HS OTG(High-Speed 480Mhz)</td>
        </tr>
        <tr>
            <td>SPI</td>
        </tr>
        <tr>
            <td>UART * 2</td>
        </tr>
        <tr>
            <td>IIC * 2</td>
        </tr>
        <tr>
            <td>IIS</td>
        </tr>
        <tr>
            <td>10bit-GPDAC</td>
        </tr>
        <tr>
            <td>12~16bit GPADC</td>
        </tr>
        <tr>
            <td>ACOMP</td>
        </tr>
        <tr>
            <td>PWM</td>
        </tr>
        <tr>
            <td>SDIO2.0</td>
        </tr>
        <tr>
            <td>Audio Codec</td>
        </tr>
        <tr>
            <td>无线：<br>· 支持Wi-Fi 802.11 b/g/n/ax（WiFi6）<br>· 支持蓝牙 5.x 双模(BT+BLE)<br>· 支持Wi-Fi / 蓝牙/Zigbee 共存</td>
        </tr>
        <tr>
            <td rowspan="3" style="white-space:nowrap"> 板载部件 </td>
        </tr>
        <tr>
            <td colspan="2">板载 SPI FLASH： 8MByte</td>
        </tr>
        <tr>
            <td colspan="2">支持 IPEX 一代天线座子和 PCB 板载天线</td>
        </tr>
    </tbody>
    <tr>
        <td rowspan="5" style="white-space:nowrap"> 其他说明 </td>
    </tr>
    <tr>
        <td colspan="2">
            尺寸：25.5mm (L) x 18mm (W)
        </td>
    </tr>
    <tr>
        <td colspan="2">
            KICAD 格式封装文件下载：<a href="https://dl.sipeed.com/shareURL/Maix-Zero/M0P/M0P/4_Package">点击跳转</a>
        </td>
    </tr>
    <tr>
        <td colspan="2">温升: &lt;30K</td>
    </tr>
    <tr>
        <td colspan="2">工作温度范围:-10℃ ~ 65℃</td>
    </tr>
</table>

## 尺寸大小

<img src="./assets/m0p/m0p_size.png" alt="m0p_size" width=35%>

## 引脚分布

前往原理图查看：[点我](https://dl.sipeed.com/shareURL/Maix-Zero/M0P/M0P/2_Schematic)

## 软件描述

<table>
    <thead>
        <tr>
            <th colspan = "2" > M0P 模组 </th>   
        </tr>
    </thead>
    <tbody>
        <tr>
          <td>OS</td>
          <td> 支持FreeRTOS</td>
        </tr>
        <tr>
          <td>开发方式</td>
          <td>· 原生C SDK<br>· MaixHAL C 模块<br>· PikaPython </td>
        </tr>
        <tr>
          <td> SDK </td>
          <td><a href="https://github.com/bouffalolab/bouffalo_sdk"> github </a></td>
        </tr>
        <tr>
          <td>Examples</td>
          <td><a href="https://github.com/sipeed/M0P_BL618_examples"> github </a></td>
        </tr>
    </tbody>
</table>

## 模组资料

- [模组规格书](https://dl.sipeed.com/shareURL/Maix-Zero/M0P/M0P/1_datasheet)
- [模组原理图](https://dl.sipeed.com/shareURL/Maix-Zero/M0P/M0P/2_Schematic)
- [模组封装库](https://dl.sipeed.com/shareURL/Maix-Zero/M0P/M0P/4_Package)
- [模组尺寸图](https://dl.sipeed.com/shareURL/Maix-Zero/M0P/M0P/3_Dimensional_drawing)

---

- [博流官方文档](https://dev.bouffalolab.com/home/)
- [BL618 数据手册](https://gitee.com/wonderfullook/bl_docs/tree/main/BL616_DS/zh_CN) (gitee)
- [BL618 参考手册](https://gitee.com/wonderfullook/bl_docs/tree/main/BL616_RM/zh_CN) (gitee)

---


- [Sipeed Examples](https://github.com/sipeed/M0P_BL618_examples)（github）
- [Bouffalolab SDK](https://github.com/bouffalolab/bouffalo_sdk) (github)
- 交流 QQ 群：`816177882` 。[点我加群](https://jq.qq.com/?_wv=1027&k=4lroNFnI)
- 论坛：[bbs.sipeed.com](https://bbs.sipeed.com/)

## 注意事项

<table>
    <tr>
        <th>项目</th>
        <th>注意事项</th>
    </tr>
    <tr>
        <td>静电防护</td>
        <td>· 请注意避免静电打到 PCBA 上；接触 PCBA 之前请把手的静电释放掉<br>· 在底板设计时，必须要从 ESD 防护角度进行设计（串电阻、加 ESD 二极管等）</td>
    </tr>
    <tr>
        <td>容忍电压</td>
        <td> 所有 GPIO 都是 3.3V 电平，请不要让 GPIO 的实际工作的电压超过额定值，否则会引起 PCBA 的永久性损坏 </td>
    </tr>
    <tr>
        <td>避免短路</td>
        <td>请在上电过程中，避免任何液体和金属触碰到 PCBA 上的元件的焊盘，否则会导致短路，烧毁 PCBA</td>
    </tr>
    <tr>
        <td>BOOT 模式选择</td>
        <td>
        在启动时，芯片判定 BOOT 引脚的电平，选择两个启动选项之一<br>
        · BOOT 低电平：从 FLASH 加载固件<br>
        · BOOT 高电平：进入 USB 下载模式
        </td>
    </tr>
</table>

## 联系方式

M0P 模组可以在多种场景实现客户不同方面的需要，技术支持和商业合作请联系邮箱 [support@sipeed.com](support@sipeed.com)