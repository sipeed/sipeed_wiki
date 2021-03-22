---
title: 代码框架结构
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 代码框架结构
---




## 目录简介

| 目录 | 子目录 | 子目录2 | 子目录3 | 内容梗概 | 
| -- | -- | -- | -- | -- |
|  assets  |  |  | | 资源文件 |
|  projects  |  | | | 工程文件， 每个文件夹一个工程 | 
|  tools | | | | 工具 |
| components|┐ | | | 组件 |
|               | └-boards | | | 板级代码 |
|               | └-drivers | | | 驱动 |
|               | └-micropython |┐ | | micropython 相关代码 |
|               |                |└-core | | micropython 源码 |
|               |                |└-port|┐ | maixpy 自定义部分源码 |
|               |                |          |└-builtin_py | maixpy 默认内置类 |
|               |                |          |└-include | 移植部分头文件 |
|               |                |          |└-src | 功能模块源码 |
|               | └-spiffs | | | SPIFFS 文件系统 |
|               | └-utils | | | 工具类（函数） |


> 现在的代码因为历史遗留原因在 `components/micropython/port/src` 目录下代码结构不是很好，以后的代码尽量按照现在的框架做到层次分明


## 添加代码

工程使用 `CMake` 进行组织， 并且工程支持多个可配置选项（`Kconfig`）

* 如果不添加文件夹和配置项，可以在现有的文件夹内添加文件编译即可
* 如果需要添加模块，可以修改 `CMakeLists.txt` 来添加内容， 可以参考内容更少的[c_cpp_project_framework](https://github.com/Neutree/c_cpp_project_framework)
* 如果需要添加配置项， 可以通过修改 `Kconfig` 文件来达到目的，所有配置项在编译时会生成宏定义添加到`global_config.h`(生成的文件)中去， 而且在 `CmakeLists.txt` 文件中都可以使用该宏定义。
> 比如在 Kconfig 中定义 `config BOARD_M5STICK`, 在 CMakeLists.txt 中可以通过判断CONFIG_BOARD_M5STICK 是否为真来决定是否编译特定的代码。 编译时就可以通过`python3 project.py menuconfig`来选择是否勾选了


