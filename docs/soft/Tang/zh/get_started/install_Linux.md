# Linux的开发环境配置

## 安装TD 

想要进行FPGA开发需要安装TD，可以通过[下载站](https://dl.sipeed.com/shareURL/TANG/Premier/IDE)，下载TD安装包和license，如果下载速度过慢的时候，建议使用[百度网盘](https://eyun.baidu.com/s/3i6FbQzr)进行下载

![install_TD_linux](./../../assets/get_started/install_TD_linux.png)

下载安装程序存档后，打开终端并 cd 进入该目录。 

```
cd <安装程序存档目录的路径 >
```

/opt 目录是为所有不属于默认安装的软件和附加包保留的。 为您的 TD IDE 安装创建一个目录

```
sudo mkdir /opt/TD_DECEMBER2018
```

将 TD 解压到 /opt/TD_DECEMBER2018 目录中：

```
sudo tar -xvf  TD_5.0.3_28716_NL_Linux.zip -d /opt/TD_DECEMBER2018/
```   

<div>
    <script>
    </script>
</div>
