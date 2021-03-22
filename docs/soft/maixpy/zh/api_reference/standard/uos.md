---
title: uos – 基本的“操作系统”服务
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: uos – 基本的“操作系统”服务
---



该模块实现了相应CPython模块的子集，如下所述。有关更多信息，请参阅原始CPython文档：[os](https://docs.python.org/3.5/library/os.html#module-os)。

`uos`模块包含用于文件系统访问和挂载，终端重定向和复制以及`uname`和`urandom`等函数。

## 常用函数

### uos.uname()

返回一个元组（可能是一个命名了的元组），其中包含有关底层机器和/或其操作系统的信息。元组按以下顺序有五个字段，每个字段都是一个字符串：

* sysname  - 底层系统的名称
* nodename  - 节点名（/板子名称）（可以与sysname相同）
* release  - 底层系统的版本
* version -  MicroPython版本和构建日期
* machine  - 底层硬件的标识符（例如，板，CPU）


### uos.urandom(n)

返回一个包含n个随机字节的字节对象。只要有可能，它就由硬件随机数生成器生成。

## 文件系统访问

### uos.chdir(path)

更改当前目录。

### uos.getcwd()

获取当前目录。

### uos.ilistdir([dir])

此函数返回一个迭代器，然后生成与列出的目录中的条目对应的元组。如果不传参数，它列出了当前目录，否则它列出了dir给出的目录。

元组具有形式（名称，类型，inode [，大小]）：

* name： 是一个字符串（如果dir是一个字节对象，则为字节），并且是条目的名称;
* type： 是一个整数，指定条目的类型，目录为 0x4000，常规文件为 0x8000;
* inode： 是对应于文件inode的整数，对于没有这种概念的文件系统可以是0。
* 某些平台可能会返回包含条目大小的4元组。对于文件条目，size是表示文件大小的整数，如果未知则为-1。目前条目的含义目前尚未定义。


### uos.listdir([dir])

如果没有参数，请列出当前目录。否则列出给定目录。

### uos.mkdir(path)

创建一个新目录。

### uos.remove(path)

删除文件。

### uos.rmdir(path)

删除目录。

### uos.rename（old_path，new_path）

重命名文件。

### uos.stat(path)

获取文件或目录的状态。

### uos.statvfs(path)

获取文件系统的状态。

按以下顺序返回包含文件系统信息的元组：

* f_bsize  - 文件系统块大小
* f_frsize  - 片段大小
* f_blocks  -  f_frsize单位中fs的大小
* f_bfree  - 空闲块数
* f_bavail  - 无特权用户的空闲块数
* f_files  -  inode数量
* f_ffree  - 免费inode的数量
* f_favail  - 无特权用户的免费inode数
* f_flag  - 挂载标志
* f_namemax  - 最大文件名长度

与inode相关的参数：`f_files`，`f_ffree`，`f_avail`和`f_flags`参数可能返回'0`，因为它们在特定于硬件的实现中不可用。

### uos.sync()

同步所有文件系统。

## 终端重定向和复制

### uos.dupterm(stream_object，index = 0)

在给定的`stream`类对象上复制或切换MicroPython终端（REPL）。 stream_object参数必须实现`readinto（）`和`write（）`方法。流应处于非阻塞模式，如果没有可用于读取的数据，`readinto（）`应返回'None`。

调用此函数后，将在此流上重复所有终端输出，并且流上可用的任何输入都将传递到终端输入。

index参数应为非负整数，并指定设置的复制槽。给定端口可以实现多个槽（槽0将始终可用），并且在这种情况下，终端输入和输出在所有设置的槽上复制。

如果`None`作为stream_object传递，则在索引给出的槽上取消复制。

该函数返回给定槽中的前一个类似流的对象。

##  文件系统挂载

某些端口提供虚拟文件系统（VFS）以及在此VFS中安装多个“真实”文件系统的功能。文件系统对象可以安装在VFS的根目录中，也可以安装在根目录中的子目录中。这允许Python程序看到的文件系统的动态和灵活配置。具有此功能的端口提供`mount（）`和`umount（）`函数，以及可能由VFS类表示的各种文件系统实现。

### uos.mount(fsobj，mount_point，*，readonly)

将文件系统对象fsobj挂载到mount_point字符串指定的VFS中的位置。 fsobj可以是一个具有`mount（）`方法或块设备的VFS对象。如果它是块设备，则会自动检测文件系统类型（如果未识别文件系统，则会引发异常）。 mount_point可以是'/'在根目录下挂载fsobj，或者'/ <name>'挂载到根目录下的子目录中。

如果readonly为“True”，则文件系统以只读方式挂载。

在mount过程中，在文件系统对象上调用`mount（）`方法。

如果mount_point已经挂载，将引发`OSError（EPERM）`。

### uos.umount(mount_point)

卸载文件系统。 mount_point可以是命名安装位置的字符串，也可以是先前安装的文件系统对象。在卸载过程中，在文件系统对象上调用方法`umount（）`。

如果找不到mount_point，会引发`OSError（EINVAL）`。

### class uos.VfsFat(block_dev)

创建使用FAT文件系统格式的文件系统对象。 FAT文件系统的存储由block_dev提供。可以使用`mount（）`挂载由此构造函数创建的对象。

#### static mkfs(block_dev)

在block_dev上构建FAT文件系统。

##  文件系统格式化

在MaixPy中，我们提供了对flash进行文件系统格式化的操作。如果用户想要清空flash文件系统那么可以使用该接口 `flash_format` 来实现

### uos.flash_format()

该接口不需要传入参数，直接使用将对开发板的 flash 进行格式化。请注意，格式化将清空所有文件，在使用前请确认 flash 中文件都是需要删除的

## 块设备

块设备是实现块协议的对象，块协议是由 `AbstractBlockDev` 类在下面描述的一组方法。该类的具体实现通常允许访问类似存储器的功能作为硬件（如闪存）。特定文件系统驱动程序可以使用块设备来存储其文件系统的数据。


### class uos.AbstractBlockDev()...)

构造块设备对象。构造函数的参数取决于特定的块设备。

#### readblocks(block_num, buf)

从索引block_num给出的块开始，将块从设备读入buf（字节数组）。要读取的块数由buf的长度给出，该长度将是块大小的倍数。

#### writeblocks(block_num, buf)

从索引block_num给出的块开始，将buf（字节数组）中的块写入设备。要写入的块数由buf的长度给出，该长度将是块大小的倍数。

#### ioctl(op, arg)

控制块设备并查询其参数。要执行的操作由op给出，它是以下整数之一：

* 1  - 初始化设备（arg未使用）
* 2  - 关闭设备（arg未使用）
* 3  - 同步设备（arg未使用）
* 4  - 获取块数的计数，应该返回一个整数（arg未使用）
* 5  - 获取块中的字节数，应该返回一个整数，或者“None”，在这种情况下使用默认值512（arg未使用）

### 例程

#### 例程1

以fat32举例，下面的类将实现一个块设备，它使用`bytearray`将其数据存储在RAM中：

```python
class RAMBlockDev:
    def __init__(self, block_size, num_blocks):
        self.block_size = block_size
        self.data = bytearray(block_size * num_blocks)

    def readblocks(self, block_num, buf):
        for i in range(len(buf)):
            buf[i] = self.data[block_num * self.block_size + i]

    def writeblocks(self, block_num, buf):
        for i in range(len(buf)):
            self.data[block_num * self.block_size + i] = buf[i]

    def ioctl(self, op, arg):
        if op == 4: # get number of blocks
            return len(self.data) // self.block_size
        if op == 5: # get block size
            return self.block_size
```

或者：

```python
import uos

bdev = RAMBlockDev(512, 50)
uos.VfsFat.mkfs(bdev)
vfs = uos.VfsFat(bdev)
uos.mount(vfs, '/ramdisk')
```
#### 例程2

以spiffs举例，下面的类将实现一个块设备，它使用`bytearray`将其数据存储在RAM中：

```python

class RAMFlashDev:
    def __init__(self):
            self.fs_size = 256*1024
            self.fs_data = bytearray(256*1024)
            self.erase_block = 32*1024
            self.log_block_size = 64*1024
            self.log_page_size = 4*1024
    def read(self,buf,size,addr):
            for i in range(len(buf)):
                buf[i] = self.fs_data[addr+i]
    def write(self,buf,size,addr):
            for i in range(len(buf)):
                self.fs_data[addr+i] = buf[i]
    def erase(self,size,addr):
            for i in range(size):
                self.fs_data[addr+i] = 0xff

```

```python

blkdev = RAMFlashDev.RAMFlashDev()
vfs = uos.VfsSpiffs(blkdev)
vfs.mkfs(vfs)
uos.mount(vfs,'/ramdisk')

```

