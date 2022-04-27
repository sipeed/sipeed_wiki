# 无 SD 卡系统烧录方式

- **目前没有在V831上进行过flash系统烧录，V833可以使用一下方式进行烧录，镜像需要发送邮件获取**
- 如需烧录到V831上，需要自行设计底板，引出fel烧录按键

## 获取烧录工具

- 从网上获取 PhoenixSuit(Windows) 烧录工具。
  - [baidu-PhoenixSuit](https://www.baidu.com/s?wd=PhoenixSuit)
  - [bing-PhoenixSuit](https://www.bing.com/search?q=PhoenixSuit&FORM=BESBTB&mkt=zh-CN) 
  - [github-PhoenixSuit](https://github.com/colorfulshark/PhoenixSuit)
  - [lo4d-PhoenixSuit](https://phoenixsuit.en.lo4d.com/windows)

## Windows 上使用 PhoenixSuit 烧录

获取系统镜像（.img） 和烧录工具（.exe） 。解压到你知道的地方。

![](./../img/no_sd_flash.png)

解压后打开 PhoenixSuit_V1.10 烧录工具 PhoenixSuit.exe 选择烧录的 .img 镜像。

![](./../img/no_sd_flash_1.png)

这时候开始插入硬件， 同时按下硬件的两个按键， 其中一个是 fel 烧录模式的触发， 要注意接线头是否联通。 （若是裸板如右图所示先按 FEL 后按 RST 复位）

![](./../img/no_sd_flash_2.png)

按住后， 此时插入电脑的 USB 口， 相当于上电（RST 复位） 进入烧录模式， 务必注意先按键再通电， 之后需要安装相应的 USB 驱动。

> 如果该电脑插入后设备管理器显示驱动未安装， 请手动指向 PhoenixSuit_V1.10 / Drivers 的驱动文件夹完成安装， 安装完成如下显示 Android ADB Interface ， 如果实在搞不定就使用市面上常见的驱动安装软件（如驱动精灵） 帮助安装。

![](./../img/no_sd_flash_3.png)

这时候 PhoenixSuit 软件会提示是否格式化更新， 一直选是即可， 不成功可以重试或检测接线是否牢固。

![](./../img/no_sd_flash_4.png)

进度状态如下， 直到成功。

![](./../img/no_sd_flash_5.png)


<a href="#" onClick="javascript :history.back(-1);">返回上一页(Back)</a>

