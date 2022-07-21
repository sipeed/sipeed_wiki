# Tang Primer 20K

> 编辑于2022.07.21

# 前言

作为第六款 FPGA 产品，Tang Primer 20K 一直广受关注。
这次以底板 + 核心板的设计，能够满足大多数用户不同的基础使用需求了。

## 核心板参数

| 项目  | 参数    | 补充  |
| :---- | :------------------------------------------ | :----- |
| 主控  | [GW2A-V18PG256C8IC8I7](http://www.gowinsemi.com.cn/prod_view.aspx?TypeId=10&FId=t3:10:3&Id=167#GW2A) | <table><tr><td>逻辑单元(LUT4)</td><td>20736</td></tr><tr><td>寄存器(FF)</td><td>15552</td></tr><tr><td>分布式静态随机存储器S-SRAM(bits)</td><td>41472</td></tr><tr><td>块状静态随机存储器B-SRAM(bits)</td><td>828K</td></tr><tr><td>块状静态随机存储器数目B-SRAM(个)</td><td>46</td></tr><tr><td>乘法器(18x18 Multiplier)</td><td>48</td></tr><tr><td>锁相环(PLLs)</td><td>4</td></tr><tr><td>I/O Bank 总数</td><td>8</td></tr></table> |
| 内存  | 128M DDR3    | 16 Meg x 16 bits x 4 banks |
| Flash | 32Mbits NOR Flash   | W25Q32JVS                  |
| 调试接口 | Jtag + Uart | JST SH1.0 8Pins 连接器 |
| SD 卡槽 | 一个 | 推拉式 |
| 显示接口 | 8Pins spi lcd 连接器 | |
| 整体封装 | 204P DDR3 Sodimm 金手指 | |