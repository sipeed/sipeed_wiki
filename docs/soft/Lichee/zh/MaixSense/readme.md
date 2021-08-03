# MaixSense开发板介绍
MaixSense开发板是Sipeed基于[全志MaixSense芯片](https://aijishu.armchina.com/blog/allwinnertech)设计的开发板，它通过内置的周易AIPU处理器同时支持智能语音和视频图像处理，开发者可以直接在开发板上跑通相关CV,NLP等AI模型。下面是产品相关介绍。
![3052168180-60ed58fc4ace8.png](https://bbs.sipeed.com/storage/attachments/2021/07/28/XrtkR7aqKOEkZj8eMo9EDyazZTJDqRveKS8qDzmY_thumb.png "1522")

![3771179095-60d4495544991.png](https://bbs.sipeed.com/storage/attachments/2021/07/28/DUt7moHKhYn7mK6yXU9V8n0sK1qwfVNGYCoB3RZF_thumb.png "1523")

## 特性

* 主模块:Maix-II A模块(R239 主芯片+ Wi-Fi & BLE+预留SPI Flash焊盘)
* 搭载两个USB-C接口: 1个USB转TTL, 1个USB OTG
* 搭载以太网PHY接口，(以24P 0.5mm间距FPC的形式引出)
* 丰富的外设: LCD接口+模拟双Mic+3W扬声器+4P MX1.25接口
* 1.5英寸LCD+USB HD 720P摄像头(USB-C OTG形式，支持正反插)
* 按键:底板:1个复位按键和4个用户按键;核心板: 1个烧录按键
* 两侧2.54mm间距排母:引出26个I0引脚和4个电源引脚
* 搭载TF卡槽，使用TF卡作为主存储器(可自行焊接使用SPI NAND)
* 较为小巧的体积

**注意**:所有电源域所能承受的反向电压不能超过_-0.3V
**警告!** 表中列出为额定值。高于上表中列出的值可能会对设备造成久性损坏。
  在额定值最大以上或最小以下的条件下，设备的运行可能会出现不可预期的偏差。
  长时间在绝对最大值下运行可能会降低设备寿命。
  ![1647796359-60ed3510295d5.png](https://bbs.sipeed.com/storage/attachments/2021/07/28/KVFWeBP1Kg8WCvpsjOG90eBYLzOv01XY2GDNkZ5K_thumb.png "1531")
  产品框图

![1658277296-60ed353c0b084.png](https://bbs.sipeed.com/storage/attachments/2021/07/28/AbBCGuT72yHrHr1NxIFRNAQMNRu0hlcGLILgbQ5M_thumb.png "1532")
核心板概览

![2430576215-60ed3558a6a35.png](https://bbs.sipeed.com/storage/attachments/2021/07/28/pdbG0FnEFIi8vHKmjd0qg4jSruLQeNzezAAPdWFj_thumb.png "1533")
底板概览

![1703240212-60ed357c419e5.png](https://bbs.sipeed.com/storage/attachments/2021/07/28/rdP8FQSfUk3wBjbXWMrsYXoCWzpOah3MofMNFfgp_thumb.png "1534")![3636190839-60ed35d5d04bb.png](https://bbs.sipeed.com/storage/attachments/2021/07/28/zq9WtHLDNXZzWTJMd6bPLImm2JqSwWqSd9SDJCij_thumb.png "1535")![863027303-60ed35ed4b39a.png](https://bbs.sipeed.com/storage/attachments/2021/07/28/qfHAEcE2vzJDOfiyqEV36mEYhj8y0eGgPjxbuNeE_thumb.png "1536")![989767600-60ed35ff6dade.png](https://bbs.sipeed.com/storage/attachments/2021/07/28/2ZLyWFvARkShsm1IKihypthgzvJKmFa8y8FPzRXl_thumb.png "1537")

底板下方1.2mm 4Pin连接器
![937914899-60ed360dba9d0.png](https://bbs.sipeed.com/storage/attachments/2021/07/28/lCUDvXdTp9FH6wjVcoZDJEKkR9G7OmbB9N4Hyibs_thumb.png "1538")

> 更多关于R932的教程请到MaixSense分区