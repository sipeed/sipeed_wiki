---
title: 安装IDE 
keywords: Sipeed, Gowin, Tang, Nano, fpga, 矽速
---

使用高云的FPGA需要用到GOWIN这个软件，附上文档链接：
<http://www.gowinsemi.com.cn/down.aspx?FId=n14:14:26>


- 用户安装请根据自己电脑系统进行IDE选择，例如Windows系统的用户用选择带有Win版本的IDE。
- 不推荐使用教育版本，教育版本安装之后可选芯片仅包含教育使用芯片型号，可选型号稀少。
- **网络版license仅适用于1.9.8之前的版本**


## 安装软件

此处以安装 **Gowin_V1.9.8_win** 为例进行安装示范。
其他版本用户根据需要自己选择安装。
- 下文中有关联网激活ide的方式仅限于1.9.8之前的版本

按照文档对IDE有了初步了解之后根据文档说明可自行进行IDE的安装。云源软件链接 http://www.gowinsemi.com.cn/faq.aspx

![IDE](./assets/IDE-1.png)

> 由于高云的IDE在不断的更新中，上图为2021年11月30号截图

进入链接后选择“云源软件历史版本”，往下拉找到历史版本中最新版本进行下载，下载到本地的文件夹是一个压缩包格式的文件，进行解压后得到安装包“Gowin_V1.9.8_win.exe”，直接双击开始进行安装：

![IDE](./assets/IDE-2.png)
![IDE](./assets/IDE-3.png)
- 下图的两个都需要安装上

![IDE](./assets/IDE-4.png)
- 下图的安装路径个人按照自己需要设置
  
![IDE](./assets/IDE-5.png)
- 安装中...
  
![IDE](./assets/IDE-6.png)
- 下面这一步不要更改任何东西，按照默认的点击`Finish`就行

![IDE](./assets/IDE-7.png)
- 上面的`Finish`后会出现下面的内容，这是安装驱动的。

![IDE](./assets/IDE-8.png)
![IDE](./assets/IDE-9.png)
- 这里需要选择接受协议才能继续安装
  
![IDE](./assets/IDE-10.png)
![IDE](./assets/IDE-11.png)
- 前面的完成后桌面上会出现下面这种图的图标
  
![IDE](./assets/IDE-12.png)

这样我们就完成了软件的安装

## license 激活

接下来是进行 **license** 的申请，有两种方式：

### 使用单机版 license (需要自己申请 license)

发送申请邮件到 support@sipeed.com 来申请license，标题为 [Apply Tang Lic]MAC: xxxxxx ，内容模板如下：

```
公司名称:
公司网站:
部门:
联系人姓名:
联系人电话:
联系人邮箱:
联系人省份:
计算机MAC地址:
license类型:共享型 仅本机
操作系统类型:Windows Linux
代理商推荐:群策电子 致远达科技 算科电子 欣华隆科技 北高智科技 晶立达科技 其他
```

打开高云 IDE 的时候，在弹出的 license 管理中，选择自己本地 license 的文件

![IDE](./assets/IDE-13.png)

下面是另一种添加方法， 使用 sipeed 的 license 服务器联网激活

### 使用 sipeed 的 license 服务器联网激活

> 在线许可服务器仅适用于 GoWin V1.9.8 及更低版本，推荐使用 V1.9.6

这种方式配置简单，不过没有网络的情况下无法使用软件。

安装好软件并打开后，软件会提示需要 license，在弹出框中填入服务器地址 `45.33.107.56` 即可，端口：10559

![IDE](./assets/IDE-14.png)





在此主要以“Use Floating License server”一栏进行测试

![IDE](./assets/IDE-15.png)

输入后点击“Save”,在联网的情况下重新打开应用可以直接进入使用界面：

![IDE](./assets/IDE-16.png)

到此，安装结束。


## 拓展
- IDE 的安装路径下主要有如下几个文件夹：IDE、Programmer、uninst.exe；
- **IDE** 文件夹：主要介绍次路径下的 **doc** 文件夹，用户在安装完之后可以在这个路径下进行对 IDE 的基本了解，主要包含文件如下图所示：

![IDE](./assets/IDE-17.png)

> “Programmer”：附带的烧录软件

> “uninst.exe”：卸载工具


## 使用方法

参考官方文档[Gowin云源软件用户指南](http://cdn.gowinsemi.com.cn/SUG100-1.8_Gowin%E4%BA%91%E6%BA%90%E8%BD%AF%E4%BB%B6%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)，第5章 云源软件使用

## 参考文档

+ [高云软件简介和安装](http://cdn.gowinsemi.com.cn/%E9%AB%98%E4%BA%91%E8%BD%AF%E4%BB%B6%E7%AE%80%E4%BB%8B%E5%92%8C%E5%AE%89%E8%A3%85.pdf)

## 其他链接
[Linux系统下烧录方法](./flash_in_linux.md)