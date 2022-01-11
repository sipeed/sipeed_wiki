# 安装IDE 

高云云源软件是专门为高云半导体芯片配套的集成电路设计与实现工具。覆盖了FPGA芯片全类型的设计功能，具体功能可以自行到高云官网进行查阅，在此不进行赘述。附上文档链接：<http://www.gowinsemi.com.cn/down.aspx?FId=n14:14:26>


1. 用户安装请根据自己电脑系统进行IDE选择，例如Windows系统的用户用选择带有Win版本的IDE。
2. 不推荐使用教育版本，教育版本安装之后可选芯片仅包含教育使用芯片型号，可选型号稀少。
3. 1.9.8之前的版本已经进行了单机版和联网版license的申请


## 安装软件

此处以安装 **Gowin_V1.9.8_win** 为例进行说明：

按照文档对IDE有了初步了解之后根据文档说明可自行进行IDE的安装。云源软件链接 http://www.gowinsemi.com.cn/faq.aspx

![IDE](./assets/IDE-1.png)

> 由于高云的IDE在不断的更新中，上图为2021年11月30号截图

进入链接后选择“云源软件历史版本”，往下拉找到历史版本中最新版本进行下载，下载到本地的文件夹是一个压缩包格式的文件，进行解压后得到安装包“Gowin_V1.9.8_win.exe”，直接双击开始进行安装：

![IDE](./assets/IDE-2.png)![IDE](./assets/IDE-3.png)![IDE](./assets/IDE-4.png)![IDE](./assets/IDE-5.png)![IDE](./assets/IDE-6.png)![IDE](./assets/IDE-7.png)

到这一步注意如果不清楚就直接选择“Finish”不要把勾选去掉，确保让他自动安装USB驱动

![IDE](./assets/IDE-8.png)![IDE](./assets/IDE-9.png)![IDE](./assets/IDE-10.png)![IDE](./assets/IDE-11.png)![IDE](./assets/IDE-12.png)

到此安装结束一部分

## licence 激活

接下来是进行 **licence** 的申请，有两种方式：

### 使用单机版 licence (需要申请 licence)

发送申请邮件到 `Support@sipeed.com` ，标题为 `【Apply Tang Lic】MAC: xxxxxx`，内容模板如下

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
操作系统类型:Windows Linus
代理商推荐:群策电子 致远达科技 算科电子 欣华隆科技 北高智科技 晶立达科技 其他
```

在打开高云 IDE 的时候，在弹出的 licence 管理中，选择自己本地的 license 的路径，即可

![IDE](./assets/IDE-13.png)

然后需要添加 synplifypro 的 licence 的路径到系统变量，下面只简单的介绍一种添加方法，在 [使用 sipeed 的 licence 服务器联网激活](#使用-sipeed-的-licence-服务器联网激活) 中，有更详细的介绍

**Windows** 用户在键盘上按 win+r 键，在弹出的运行窗口输入 `cmd`，点击确定后会弹出黑色命令行窗口，在里面输入下面命令，`path_to_the_file` 是你 `gowin_Synplifypro.lic` 的路径

```
setx LM_LICENSE_FILE path_to_the_file
```

### 使用 sipeed 的 licence 服务器联网激活

这种方式配置起来简单，不过没有网络的情况下无法使用软件

下载好软件打开后，软件会提示需要 licence，在弹出框中填入服务器地址 `45.33.107.56` 即可，IDE端口：10559

![IDE](./assets/IDE-14.png)

> 在线许可服务器仅适用于 GoWin V1.9.8 及更低版本，推荐使用 V1.9.6
双击打开“Gowin_V1.9.8”会看到



在此主要以“Use Floating License server”一栏进行测试

![IDE](./assets/IDE-15.png)

输入后点击“Save”,在联网的情况下重启颗直接键入编辑界面：

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

