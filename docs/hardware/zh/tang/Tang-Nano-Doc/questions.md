---
title: Note
---

> 编辑于2022.05.12

这里汇总一些常见问题，持续更新

## Programmer 相关

**首先确定设备管理器里面有两个converter，在进行下面的操作**

![](./../../assets/questions/converter.png)

与上图中一样的话说明电脑与板子连接没问题；不存在的话请更改 usb口 或者重新安装驱动。

### 下载失败

对于Programmer(下载程序)建议使用 
https://dl.sipeed.com/shareURL/TANG/programmer 里面的文件。
下载后解压替换掉Gowin对应安装目录的Programmer文件夹即可。
不会替换的话可以在下载解压后的Programmer程序中手动添加对应下载文件来进行烧录。

### ID code mismatch

这种情况是工程芯片与下载芯片不一致。

重新检查工程中的芯片型号（比如工程设置、引脚约束、各个IP中的型号），与板子上的芯片丝印对应上。

### 下载卡住

不要选中带有 Verify 选项的。

![](./../assets/questions/never_choose_verify.png)

### 找不到下载文件

一般来说生成的下载文件（拓展后缀为.fs）在工程目录下的 impl/pnr 文件夹里面。

<details>
  <summary><font color="#4F84FF">点开查看相关图文说明</font></summary>
  <img src="./../assets/questions/fs_path.png">
  <p> 在上图中可以看到这个下载文件的路径为 /fpga_project1/impl/pnr/fpga_project1.fs </p>
  <p></p>
  <p> 其中 fpga_project1 为工程目录，impl 为 IDE 生成的目录，然后所需要的文件位于 pnr 文件夹内</p>
  <p></p>
  <p> 然后那个拓展名为 .fs 的文件就是下载到 fpga 的文件</p>
</details>

### No Gowin devices found

这种情况可以和上面的 [下载失败](#下载失败) 里面的内容一样替换 Programmer 文件夹。

### Cabel open failed

参考上一步 No Gowin devices found 的操作后，再 programmer 里面进行下面操作：

点击顶部菜单栏的 Edit->Cable Setting->Cable->Query，然后 Save 即可

<details>
  <summary><font color="#4F84FF">点开查看操作步骤图片</font></summary>
  <img src="./../assets/questions/cable.png">
  <p>点击下图中的 Query</p>
  <img src="./../assets/questions/click_query.png" >
  <p>接着再点击 Save 即可</p>
</details>


## IDE 使用相关

### 使用GAO

目前测试过IDE v1.9.8.1和之前的版本可使用。其他新版的不行