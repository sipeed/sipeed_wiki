# 下载

进入官网 http://www.gowinsemi.com.cn/faq.aspx ，可以看到如下图的软件列表，选择适合电脑的系统的版本进行下载

![1-1](../../assets/gowin_down.png)

# 安装

**Windows** 用户：

双击下载好的 exe 安装文件，选择安装语言、安装位置，鼠标点击下一步就可以完成安装了

完成安装时提示安装的驱动请务必安装

![2-1](../../assets/gowin_install.png)

勾选安装驱动后点击完成后，就会进行驱动的安装

**Linux** 用户：

TODO

# license

现目前有两种方式进行 license

**第一种：使用单机版 licence(需要申请 licence)**

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

![3-5](../../assets/lic_file_5.png)

然后需要添加 synplifypro 的 licence 的路径到系统变量，下面只简单的介绍一种添加方法，在 `第二种：使用 sipeed 的 licence 服务器联网激活` 中，有更详细的介绍

**Windows** 用户在键盘上按 win+r 键，在弹出的运行窗口输入 `cmd`，点击确定后会弹出黑色命令行窗口，在里面输入下面命令，`path_to_the_file` 是你 `gowin_Synplifypro.lic` 的路径

```
setx LM_LICENSE_FILE path_to_the_file
```

**第二种：使用 sipeed 的 licence 服务器联网激活**

这种方式配置起来简单，不过没有网络的情况下无法使用软件

下载好软件打开后，软件会提示需要 licence，在弹出框中填入服务器地址 `45.33.107.56` 即可，IDE端口：10559

![3-6](../../assets/lic_remote_1.png)

synopsys 高级功能的激活需要在系统中添加环境变量 `LM_LICENSE_FILE=27020@45.33.107.56`

**Windows** 用户在键盘上按 win+r 键，在弹出的运行窗口输入 `cmd`，点击确定后会弹出黑色命令行窗口，在里面输入下面命令

```
setx LM_LICENSE_FILE 27020@45.33.107.56
```

Windows 除了命令行的方式添加，也可以通过 右键电脑->属性->环境变量 ，然后如下图进行添加

![3-7](../../assets/lic_remote_2.png)

**Linux** 用户需要在 `~/.bashrc` 中添加

```
export LM_LICENSE_FILE 27020@45.33.107.56
```

进入 IDE 后，点击 Tools 中的 `Synplify Pro`

![3-8](../../assets/lic_remote_3.png)

随后会弹出界面如下图，这时需要等待一小会，等 licence 初始化完毕就可以使用

![3-9](../../assets/lic_remote_4.png)

# 使用方法

参考官方文档[Gowin云源软件用户指南](http://cdn.gowinsemi.com.cn/SUG100-1.8_Gowin%E4%BA%91%E6%BA%90%E8%BD%AF%E4%BB%B6%E7%94%A8%E6%88%B7%E6%8C%87%E5%8D%97.pdf)，第5章 云源软件使用

# 参考文档

+ [高云软件简介和安装](http://cdn.gowinsemi.com.cn/%E9%AB%98%E4%BA%91%E8%BD%AF%E4%BB%B6%E7%AE%80%E4%BB%8B%E5%92%8C%E5%AE%89%E8%A3%85.pdf)

