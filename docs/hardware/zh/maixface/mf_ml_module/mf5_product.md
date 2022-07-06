# MF5

## MF5 外观一览


## MF5 板载接口

<table border="2">
    <tr>
        <th colspan=6>MaixFace 5 引脚信息</th>
    </tr>
    <tr>
        <td colspan=3><img src="./../assets/mf_module/mf5/mf5_if_1.png" height=400></td>
        <td colspan=3><img src="./../assets/mf_module/mf5/mf5_if_2.png" height=400></td>
    </tr>
    <tr>
        <td>Maix Face Slik</td>
        <td>K210 IO</td>
        <td>ESP8285 IO</td>
        <td>Function</td>
        <td>Remark</td>
        <td>IO Voltage</td>
    </tr>
    <tr>
        <td>VIN</td>
        <td>-</td>
        <td>-</td>
        <td>电源输入正极</td>
        <td>12V</td>
        <td rowspan=22>3.3V</td>
    </tr>
    <tr>
        <td>GND</td>
        <td>-</td>
        <td>-</td>
        <td>电源输入负极</td>
        <td>电源GND</td>
    </tr>
    <tr>
        <td>NC</td>
        <td>-</td>
        <td>-</td>
        <td>继电器常闭触点</td>
        <td rowspan=3>继电器</td>
    </tr>
    <tr>
        <td>COM</td>
        <td>-</td>
        <td>-</td>
        <td>继电器公共触点</td>
    </tr>
    <tr>
        <td>NO</td>
        <td>-</td>
        <td>-</td>
        <td>继电器常开触点</td>
    </tr>
    <tr>
        <td>GND</td>
        <td>-</td>
        <td>-</td>
        <td>韦根接口RETURN</td>
        <td rowspan=3>韦根接口</td>
    </tr>
    <tr>
        <td>WGD0</td>
        <td>IO14</td>
        <td>-</td>
        <td>韦根接口 D0</td>
    </tr>
    <tr>
        <td>WGD1</td>
        <td>IO15</td>
        <td>-</td>
        <td>韦根接口 D1</td>
    </tr>
    <tr>
        <td>GND</td>
        <td>-</td>
        <td>-</td>
        <td>开门信号地</td>
        <td rowspan=2>开门信号 低电平: Open</td>
    </tr>
    <tr>
        <td>OPEN</td>
        <td>IO16</td>
        <td>-</td>
        <td>开门信号输入</td>
    </tr>
    <tr>
        <td>3V3</td>
        <td>-</td>
        <td>-</td>
        <td>3.3V</td>
        <td rowspan=6>以太网/刷卡接口</td>
    </tr>
    <tr>
        <td>CS</td>
        <td>IO24</td>
        <td>-</td>
        <td>SPI CS</td>
    </tr>
    <tr>
        <td>MISO</td>
        <td>IO2</td>
        <td>-</td>
        <td>SPI MISO</td>
    </tr>
    <tr>
        <td>SCLK</td>
        <td>IO1</td>
        <td>-</td>
        <td>SPI SCLK</td>
    </tr>
    <tr>
        <td>MOSI</td>
        <td>IO3</td>
        <td>-</td>
        <td>SPI MOSI</td>
    </tr>
    <tr>
        <td>GND</td>
        <td>-</td>
        <td>-</td>
        <td>GND</td>
    </tr>
    <tr>
        <td>5V</td>
        <td>-</td>
        <td>-</td>
        <td>5V</td>
        <td rowspan=6>串口/K210下载</td>
    </tr>
    <tr>
        <td>RST</td>
        <td>IO54</td>
        <td>-</td>
        <td>K210复位</td>
    </tr>
    <tr>
        <td>BOOT</td>
        <td>IO16</td>
        <td>-</td>
        <td>K210进入ISP模式</td>
    </tr>
    <tr>
        <td>ISPTX</td>
        <td>IO5</td>
        <td>-</td>
        <td>ISPTX</td>
    </tr>
    <tr>
        <td>ISPRX</td>
        <td>IO4</td>
        <td>-</td>
        <td>ISPRX</td>
    </tr>
    <tr>
        <td>GND</td>
        <td>-</td>
        <td>-</td>
        <td>GND</td>
    </tr>
</table>

## MF5 固件说明

MF5 为人脸识别门禁成品，默认烧录的固件不支持串口协议；

在烧录串口协议固件之后，协议串口为 WGD0-IO14(RX)，WGD1-1O15(TX)。
