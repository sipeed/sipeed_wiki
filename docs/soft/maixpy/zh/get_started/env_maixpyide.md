---
title: MaixPy IDE 安装与使用
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: MaixPy IDE 安装与使用
---


![maixpy_ide_start](../../assets/maixpy/maixpy_ide_start.png)

## 关于 MaixPy IDE



![MaixPy IDE](../../assets/maixpy/maixpy_ide.png)

首先需要弄清： **MaixPy** 使用 `Micropython` 脚本语法，所以不像 `C` 语言 一样需要编译，其实不用 `IDE` 也能愉快使用： 使用串口终端工具，前面已经安装了

使用 `IDE` 则会方便在电脑上实时编辑脚本并上传到开发板以及直接在开发板上执行脚本，以及在电脑上实时查看摄像头图像、保存文件到开发板等

当然， 使用 `IDE` 因为压缩、传输需要耗费一部分资源，所以性能会有所降低，而且如果MaixPy宕机也没有串口终端好发现问题



## MaixPy 固件

要使用 `MaixPy IDE` , 固件必须是 `v0.3.1` 版本以上, 否则MaixPyIDE 上会连接不上， 使用前尽量检查固件版本和 IDE 版本，都更新到最新版以保障能正常使用

## 下载安装包

[dl.sipeed.com](http://dl.sipeed.com/MAIX/MaixPy/ide/)

文件列表等说明 请看 最新版本文件夹下的 `readme.txt` 文件， 如果下载速度慢请使用 cdn 链接下载

## 安装

#### 如果是安装程序(**推荐**，简单方便)

`Windows`直接双击`exe`文件运行安装程序; `Linux`命令行给运行权限然后执行

```
chmod +x maixpy-ide-linux-x86_64-0.2.2.run
./maixpy-ide-linux-x86_64-0.2.2.run
```

#### 如果是压缩包(`7z`)

则解压到文件夹

> 如果系统不支持 `7z`， 则需要 [下载 `7z`解压缩工具](https://www.7-zip.org/)，然后用 `7z`

在`Linux`下也可以双击压缩包进行解压！

如果需要使用终端解压， 可以参考以下命令：

```bash
sudo apt install p7zip-full
7z x maixpy-ide-linux-x86_64-0.2.2-installer-archive.7z -r -omaixpy-ide
# `-o` 后面直接跟解压缩的路径, 中间没有空格.
```

* 解压后, 执行
  * 如果是 `Windows`： 直接双击`maixpyide`来执行，可以右键固定到开始页面或者固定到任务栏方便后面使用
  * `Linux`： 执行

```
chmod +x setup.sh
./setup.sh
./bin/maipyide.sh
```



## 测试运行

打开 MaixPy IDE, 上方工具栏里面选择开发板的型号。**amigo，cube 开发板请选择 Maixduino 进行连接**。

`Tool-> Select Board` (工具->选择开发板)

点击 `connect` 连接 `MaixPy IDE`

![connect-icon.png](../../assets/maixpy/maixpy_connect_icon.png)

连接成功之后，链接按钮会由绿变红．

![connect-success.png](../../assets/maixpy/maixpy_connect-success.png)

连接按钮下方是运行按钮，会执行当前编辑区的`py`文件．



![helloworld-run.png](../../assets/maixpy/maixpy_helloworld.png)

再次点击运行按钮(红色), 停止运行当前代码．

## 上传文件

在 **Tool/工具** 菜单中可以选择发送文件


## 注意

* 点击连接后，不用和终端工具同时使用，否则会出现串口占用无法打开
* 如果一直无法成功连接成功， 检查：
  * 请检查是否开发板型号选择错误；
  * 观察开发板屏幕是否有变化，如果没有反应可能是串口选择错误；
  * 尝试升级到最新的 [master 分支固件](http://cn.dl.sipeed.com/MAIX/MaixPy/release/master)， 以及最新的 MaixPy IDE 软件


## 根据错误提示寻找原因

程序运行出错时会弹框提示错误，但是错误信息不一定完整，请**在终端输出里面查找更详细的错误信息**

如有必要，请断开 IDE， 仅使用串口终端运行程序（也许你需要先把程序保存到文件，然后运行文件）查看打印以排错

如果提交问题（bbs、群、github issue等），为了使问题快速得到解决，请务必带上上面所述完整信息


