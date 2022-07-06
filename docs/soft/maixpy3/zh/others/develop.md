---
title: MaixPy3 开发文档
keywords: MaixPy, MaixPy3, Python, Python3, MicroPython
desc: maixpy doc: 如何参与项目（开发文档）
---

MaixPy3 并不是为了某一款芯片平台制作的，它的初衷就是为了通过 Python 编程简化用户在嵌入式 Linux 上开发程序的过程，所以是建立在所有 Linux 设备都能使用的基础上去设计的，但由于 Sipeed 官方的能力有限，难以同时照顾所有开源硬件的同步开发，所以提供一些官方的基本芯片移植参考，方便第三方的开源爱好者提交其他芯片平台、镜像、工具推送到 MaixPy3 的环境中。

## 一般开发流程

从 MaixPy3 仓库的 [setup.py](https://github.com/sipeed/MaixPy3/blob/main/setup.py) 进行项目的编译。

对于一台 Linux X86 的个人计算机而言，我们使用如下命令进行构建。

- 编译 `python3 setup.py build`
- 清理 `python3 setup.py clean`
- 安装 `pip3 install .`

```bash
juwan@juwan-N85-N870HL:~/Desktop/v831_toolchain_linux_x86/MaixPy3$ python3 setup.py build
running build
running build_py
running egg_info
writing MaixPy3.egg-info/PKG-INFO
writing dependency_links to MaixPy3.egg-info/dependency_links.txt
writing entry points to MaixPy3.egg-info/entry_points.txt
writing requirements to MaixPy3.egg-info/requires.txt
writing top-level names to MaixPy3.egg-info/top_level.txt
writing manifest file 'MaixPy3.egg-info/SOURCES.txt'
running build_ext
juwan@juwan-N85-N870HL:~/Desktop/v831_toolchain_linux_x86/MaixPy3$ python3 setup.py clean
running clean
juwan@juwan-N85-N870HL:~/Desktop/v831_toolchain_linux_x86/MaixPy3$ pip3 install .Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
Processing /home/juwan/Desktop/v831_toolchain_linux_x86/MaixPy3
Requirement already satisfied: Pillow in /usr/lib/python3/dist-packages (from MaixPy3==0.2.9) (7.0.0)
Requirement already satisfied: evdev in /home/juwan/.local/lib/python3.8/site-packages (from MaixPy3==0.2.9) (1.4.0)
Requirement already satisfied: gpiod in /home/juwan/.local/lib/python3.8/site-packages (from MaixPy3==0.2.9) (1.4.0)
Requirement already satisfied: numpy in /home/juwan/.local/lib/python3.8/site-packages (from MaixPy3==0.2.9) (1.19.4)
Requirement already satisfied: opencv-python in /home/juwan/.local/lib/python3.8/site-packages (from MaixPy3==0.2.9) (4.5.1.48)
Requirement already satisfied: pyserial in /usr/local/lib/python3.8/dist-packages (from MaixPy3==0.2.9) (3.4)
Requirement already satisfied: rpyc in /home/juwan/.local/lib/python3.8/site-packages (from MaixPy3==0.2.9) (5.0.1)
Requirement already satisfied: spidev in /home/juwan/.local/lib/python3.8/site-packages (from MaixPy3==0.2.9) (3.5)
Requirement already satisfied: plumbum in /home/juwan/.local/lib/python3.8/site-packages (from rpyc->MaixPy3==0.2.9) (1.6.9)
Building wheels for collected packages: MaixPy3
  Building wheel for MaixPy3 (setup.py) ... done
  Created wheel for MaixPy3: filename=MaixPy3-0.2.9-cp38-cp38-linux_x86_64.whl size=115611 sha256=54f70f181ccc629f1eaf470bf30eccd20389c6333814d7145e16a31db7f6cdcd
  Stored in directory: /tmp/pip-ephem-wheel-cache-9bf1q3wt/wheels/53/7d/47/6cd374fab930089f96a0a3185f5677e52a9b71dbbee769935d
Successfully built MaixPy3
Installing collected packages: MaixPy3
  Attempting uninstall: MaixPy3
    Found existing installation: MaixPy3 0.2.8
    Uninstalling MaixPy3-0.2.8:
      Successfully uninstalled MaixPy3-0.2.8
Successfully installed MaixPy3-0.2.9
juwan@juwan-N85-N870HL:~/Desktop/v831_toolchain_linux_x86/MaixPy3$ 
```

而对于不能在目标平台上编译安装的环境，就需要使用预编译的 whl 包来辅助安装，以 Maix V831 为例。

- 编译 `python3.8 setup.py maix_v831 bdist_wheel`

- 安装 `export TMPDIR=/root && pip install ./dist/*.whl`

```bash
root@sipeed:/# export TMPDIR=/root && pip install maixpy3 --upgrade
Collecting maixpy3
  Downloading MaixPy3-0.1.9-cp38-cp38-linux_armv7l.whl (1.0 MB)
     |████████████████████████████████| 1.0 MB 43 kB/s 
Collecting pexpect
  Downloading pexpect-4.8.0-py2.py3-none-any.whl (59 kB)
     |████████████████████████████████| 59 kB 71 kB/s 
Collecting rpyc
  Downloading rpyc-5.0.1-py3-none-any.whl (68 kB)
     |████████████████████████████████| 68 kB 42 kB/s 
Requirement already satisfied, skipping upgrade: Pillow in /usr/lib/python3.8/site-packages (from maixpy3) (7.2.0)
Collecting ptyprocess>=0.5
  Downloading ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)
Collecting plumbum
  Downloading plumbum-1.6.9-py2.py3-none-any.whl (115 kB)
     |████████████████████████████████| 115 kB 84 kB/s 
Installing collected packages: ptyprocess, pexpect, plumbum, rpyc, maixpy3
Successfully installed maixpy3-0.1.9 pexpect-4.8.0 plumbum-1.6.9 ptyprocess-0.7.0 rpyc-5.0.1
WARNING: You are using pip version 20.1.1; however, version 21.0 is available.
You should consider upgrading via the '/usr/bin/python3 -m pip install --upgrade pip' command.

root@sipeed:/# 
```

对于一些安装失败，缺少了依赖库的场合，需要从外部去引入该包的安装，例如这个问题 [error happened when install maixpy3](https://github.com/sipeed/MaixPy3/issues/4) ，这通常需要升级镜像来解决，或手动安装相关的依赖包。

至此以后，在发布软件包的时候可以通过 `export TMPDIR=/root && pip install maixpy3` 让目标机器直接安装 maixpy3 的包即可使用。

## 一般测试流程

项目引入 tox 进行软件接口交互的自动化测试，通常用它进行虚拟 Python 环境测试，确保软件代码的依赖关系和接口逻辑测试，如测试 `from xxx import *` 是否可行。

```bash
juwan@juwan-N85-N870HL:~/Desktop/v831_toolchain_linux_x86/MaixPy3$ tox
GLOB sdist-make: /home/juwan/Desktop/v831_toolchain_linux_x86/MaixPy3/setup.py
py38 inst-nodeps: /home/juwan/Desktop/v831_toolchain_linux_x86/MaixPy3/.tox/.tmp/package/1/MaixPy3-0.1.2.zip
py38 installed: attrs==20.3.0,iniconfig==1.1.1,packaging==20.8,Pillow==8.1.0,pluggy==0.13.1,py==1.10.0,pyparsing==2.4.7,pytest==6.2.1,MaixPy3 @ file:///home/juwan/Desktop/v831_toolchain_linux_x86/MaixPy3/.tox/.tmp/package/1/MaixPy3-0.1.2.zip,scripttest==1.3,toml==0.10.2
py38 run-test-pre: PYTHONHASHSEED='820562099'
py38 run-test: commands[0] | py.test
======================================= test session starts ========================================
platform linux -- Python 3.8.5, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
cachedir: .tox/py38/.pytest_cache
rootdir: /home/juwan/Desktop/v831_toolchain_linux_x86/MaixPy3
collected 5 items                                                                                  

ext_modules/_maix/example/test__maix.py .                                                    [ 20%]
tests/test_maix.py ....                                                                      [100%]

======================================== 5 passed in 0.05s =========================================
_____________________________________________ summary ______________________________________________
  py38: commands succeeded
  congratulations :)
```

对于硬件模块，通常不好自动化测试，所以会做成 example 提供。

关于代码覆盖性测试，暂时不做。

## 一般发布流程

2021年02月21日 关于自动化构建，还在考虑到导入多个平台的编译链编译的问题，暂时还没有准备好。

## Python 模块编译说明

MaixPy3 使用面向模块接口开发，链接跨平台的 Python 或 C 包，统一加载到 Python3 环境当中。

目前支持的 Python3 环境如下：

- [PC x86_64 的 Pyhon3 环境](https://www.python.org/downloads/release/python-380/)

- [Sipeed v831 的 Python3 交叉编译环境](https://github.com/sipeed/MaixPy3/releases/tag/20210613) (需要使用 source toolchain_v83x_linux_x86/envsetup.sh 获得链接 V831 编译链的 python3.8 环境，注意这不是本机的 Python3 环境！！！)

通常拿到一个 Python 模块，对它的 `setup.py` 执行 `python setup.py build` 即可进行构建，它的内容通常有如下示例（只是举例）。

```python

from setuptools import setup, Extension, find_packages

_maix_module = Extension('_maix', include_dirs=['ext_modules/_maix/include'], sources=get_srcs('ext_modules/_maix'), libraries=['jpeg'])

libi2c_module = Extension('pylibi2c',  include_dirs=['ext_modules/libi2c/src'], sources=get_srcs('ext_modules/libi2c/src'))

setup(
    name='MaixPy3',
    version='0.1.2',
    license='MIT',
    author='Sipeed',
    author_email="support@sipeed.com",
    url='https://github.com/sipeed/MaixPy3',
    description="MaixPy Python3 library",
    long_description=open('README.md').read(),
    install_requires=["Pillow"],
    ext_modules=[
        _maix_module,
        libi2c_module,
    ],
    packages = find_packages(), # find __init__.py packages
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)

```

只需要关心 setup 函数的参数中 packages 、 ext_modules 定义下的模块。

- find_packages() 会自动寻找根目录下所有带有 `__init__.py` 的包导入到 Python3 的 site-packages 中，import 的时候就会找到它。
- ext_modules 是需要经过编译的 C 模块。

## 通用 Python 模块开发

以 maix 模块为例，完全用 Python 实现的模块需要按以下结构进行构建。

- maix/`__init__.py`
- maix/video.py
- maix/xxxxx.py

首先 setuptools 打包系统会找到该模块的 maix 文件夹并将其安装到 `site-packages/maix` 下，这样用户就可以在 Python3 中 `import maix` 了，注意它与 setup.py 的相对目录（`/maix`）与安装目录（`site-packages/maix`）位置保持一致。

如何控制 from maix import * 的内容可以看 `__init__.py` 了解。

```python
from .video import camera
from .import display

__all__ = ['display', 'video', 'camera']
```

其中 `__all__` 可以控制 import 加载的模块、对象或变量，这样一个最基本的 Python 模块就制作完成了。

关于编写后的测试看 [test_maix.py](https://github.com/sipeed/MaixPy3/tree/main/tests/test_maix.py) 代码可知，关于 tox 测试框架会在最后简单说明。 

## 关于 C 拓展模块开发

以 [libi2c](https://github.com/amaork/libi2c) 举例说明原生 C 开发的模块。

如果是用 C 开发就需要配合 Makefile 的规则来操作，可以直接在 MaixPy3/ext_modules/libi2c 目录下直接运行 `make all` 进行构建，此时就会得到 `libi2c.so \ libi2c.a \ pylibi2c.so` 等模块。

这样目标系统就可以通过 C 代码链接(-l)该 libi2c 模块执行，而 `pylibi2c.so` 模块是可以直接在 Python 里面直接 import 就可以使用的。

```shell
juwan@juwan-N85-N870HL:~/Desktop/v831_toolchain_linux_x86/MaixPy3/ext_modules/libi2c$ python3
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pylibi2c
>>> pylibi2c
<module 'pylibi2c' from '/home/juwan/Desktop/v831_toolchain_linux_x86/MaixPy3/ext_modules/libi2c/pylibi2c.cpython-38-x86_64-linux-gnu.so'>
>>> 
```

注意 `pylibi2c.so` 是经过 `python3 setup.py build_ext --inplace` 命令编译 [ext_modules/libi2c/src/pyi2c.c](https://github.com/sipeed/MaixPy3/tree/main/ext_modules/libi2c/src/pyi2c.c) 得到的模块。

其中 `#include <Python.h>` 的是来自于系统的 `usr/include` 目录，这取决于你的编译环境。

> 注意，编译通过不代表可以运行，如果发现运行时丢失函数（undefined symbol），可以通过 ldd 查询 .so 依赖函数, 通过 nm -D 查询 .a 函数，通过 readelf -e 查询程序编译版本，有些平台可能没有 ldd 的话，就用 `readelf -d /bin/ls | grep "Shared library"` 来查看了，缺啥就往环境里补就对了。

### 导入 pyXXX.c 的 C 拓展模块

对于 make / gcc 的模块包以 ext_modules/xxxx 方式加入 MaixPy3 的编译环境（setup.py）， 请确保该包可以跨平台编译通过后，同步修改 [MaixPy3/envs/general.py](https://github.com/sipeed/MaixPy3/blob/main/envs/general.py) 的 ext_modules 模块。

```python

from setuptools import Extension
from .utils import get_srcs

libi2c_module = Extension('pylibi2c',  include_dirs=[
                          'ext_modules/libi2c/src'], sources=get_srcs('ext_modules/libi2c/src'))

_maix_module = Extension('_maix', include_dirs=['ext_modules/_maix/include'],
                         sources=get_srcs('ext_modules/_maix'),
                         libraries=[
    "jpeg"
],
)

_maix_camera_module = Extension('_maix_camera', include_dirs=['ext_modules/_maix_camera/include'],
                                sources=get_srcs('ext_modules/_maix_camera'),
                                )

_maix_display_module = Extension('_maix_display', include_dirs=['ext_modules/_maix_display/include'],
                                 sources=get_srcs('ext_modules/_maix_display'),
                                 )

_maix_modules = [
    libi2c_module,
    _maix_module,
    _maix_camera_module,
    _maix_display_module
]

_maix_data_files = [

]

_maix_py_modules = [
    "numpy",
    "opencv-python3",
    "opencv-python",
    "Pillow",
    "rpyc",
    "gpiod",
    "evdev",
    "spidev",
    "pyserial"
]
```

以 _maix_module 为例，在加入编译之前，该包结构如下（目录结构可能会过时）。

- ext_modules/_maix
- ext_modules/_maix/include/_maix.h
- ext_modules/_maix/_maix.c
- ext_modules/_maix/setup.py
- /example/test__maix.py

此时我们可以在 MaixPy3 根目录下使用 `python3 setup.py build` 调用 [setup.py](https://github.com/sipeed/MaixPy3/blob/main/setup.py) 進行构建，默认构建 linux_x86_64 的包。

```python
#!/usr/bin/env python

"""
setup.py file for MaixPy3
"""

import sys
from setuptools import setup, Extension, find_packages

ext_modules = []
data_files = []
py_modules = []

if 'maix_v831' in sys.argv:
  sys.argv.remove('maix_v831')
  from envs.maix_v831 import _maix_modules, _maix_data_files, _maix_py_modules
else:
  from envs.general import _maix_modules, _maix_data_files, _maix_py_modules
  
ext_modules.extend(_maix_modules)
data_files.extend(_maix_data_files)
py_modules.extend(_maix_py_modules)

```

如果在本机 Python 编译时出现如下错误：

```shell
ext_modules/_maix/pyCamera.c:4:10: fatal error: jpeglib.h: 没有那个文件或目录
    4 | #include "jpeglib.h"
      |          ^~~~~~~~~~~
compilation terminated.
```

运行 `sudo apt-get install libjpeg-dev` 后会在本机 usr/include 和 usr/bin 中加入 libjpeg 的模块，其他编译链同理。

注意 Extension 的代码的链接时的相对地址（include_dirs & sources），以及本地打包时链接时缺少的（.h）文件，注意 [MANIFEST.in](https://github.com/sipeed/MaixPy3/tree/main/MANIFEST.in) 会链接本地的文件加入 Python 模块的打包。

> 默认配置下打包中不会带入模块的（.h）文件，这会导致运行 tox 自动化打包构建模块时出错。

```in
include ext_modules/libi2c/src/*.h
include ext_modules/_maix/include/*.h
```

> 关于 setup.py 的用法可以参考 [2021年，你应该知道的Python打包指南](https://frostming.com/2020/12-25/python-packaging)

### 编写 C 拓展模块的参考

接下来说明 CPython 的代码编写规范说明：

- 如何编写一个 CPython 模块（PyModule）。
- 如何 CPython 模块添加类对象（全局对象）、全局函数、全局变量。
- 一个 PyObject 类对象的结构代码。
- 标准 CPython 模块的命令规则。

以 MaixPy3/ext_modules/_maix 模块为例，首先提供一个 C 实现的 Python 模块入口 [_maix.c](https://github.com/sipeed/MaixPy3/tree/main/ext_modules/_maix/_maix.c) 。

```c

#include "_maix.h"

#define _VERSION_ "0.1"
#define _NAME_ "_maix"

PyDoc_STRVAR(_maix_doc, "MaixPy Python3 library.\n");

static PyObject *_maix_help() {
    return PyUnicode_FromString(_maix_doc);
}

static PyMethodDef _maix_methods[] = {
    {"help", (PyCFunction)_maix_help, METH_NOARGS, _maix_doc},
    {NULL}
};

void define_constants(PyObject *module) {
    PyModule_AddObject(module, "_VERSION_", Py_BuildValue("H", _VERSION_));
}

static struct PyModuleDef _maixmodule = {
    PyModuleDef_HEAD_INIT,
    _NAME_,         /* Module name */
    _maix_doc,	/* Module _maixMethods */
    -1,			    /* size of per-interpreter state of the module, size of per-interpreter state of the module,*/
    _maix_methods,
};

PyMODINIT_FUNC PyInit__maix(void)
{

    PyObject *module;

    if (PyType_Ready(&CameraObjectType) < 0) {
        return NULL;
    }

    module = PyModule_Create(&_maixmodule);
    PyObject *version = PyUnicode_FromString(_VERSION_);

    /* Constants */
    define_constants(module);

    /* Set module version */
    PyObject *dict = PyModule_GetDict(module);
    PyDict_SetItemString(dict, "__version__", version);
    Py_DECREF(version);

    /* Register CameraObjectType */
    Py_INCREF(&CameraObjectType);
    PyModule_AddObject(module, Camera_name, (PyObject *)&CameraObjectType);

    return module;
}


```

此时 Python 在 import 该模块的时候就会调用 PyInit_xxxx 函数进行初始化，在 Python 里 import 该模块只会执行一次，想要再次执行需要 reload 函数（`from imp import reload`）。

通过 `PyModule_AddObject` 注册 PyObject 对象到该模块中，而该对象被公开到一个头文件当中进行交换，从而给 PyModule 提供多个 PyObject 的实现，添加模块的全局变量与此同理。

```c
static PyMethodDef _maix_methods[] = {
    {"help", ()_maix_help, METH_NOARGS, _maix_doc},
    {NULL}
};
```

通过 `_maix_methods` 结构体为模块添加全局函数，如果你认为某个函数是公共函数，则将其放置模块顶层，表示全局公共函数。

### PyObject 的结构参考

一个基础的格式参考如下：

定义一个对象必要的对外引用，将模块和对象实现分离，模块再通过（.h）文件链接对象实现，可见 [MaixPy3/ext_modules/_maix_camera/include/_maix_camera.h](https://github.com/sipeed/MaixPy3/blob/main/ext_modules/_maix_camera/include/_maix_camera.h) 。

```c

#ifndef _MAIX_CAMERA_H
#define _MAIX_CAMERA_H

#ifdef  __cplusplus
extern "C" {
#endif

#include <Python.h>

/* Macros needed for Python 3 */
#ifndef PyInt_Check
#define PyInt_Check PyLong_Check
#define PyInt_FromLong PyLong_FromLong
#define PyInt_AsLong PyLong_AsLong
#define PyInt_Type PyLong_Type
#endif

PyDoc_STRVAR(VirtualCamera_name, "VirtualCamera");
extern PyTypeObject VirtualCameraObjectType;

// #define V831Camera
#ifdef V831Camera
PyDoc_STRVAR(V831Camera_name, "V831Camera");
extern PyTypeObject V831CameraObjectType;
#endif

#ifdef  __cplusplus
}
#endif

#endif

```

此时（PyInit__maix）就可以加载该对象（CameraObjectType）到 _maix 模块当中。

```c
if (PyType_Ready(&VirtualCameraObjectType) < 0) {
    return NULL;
}

/* Register VirtualCameraObjectType */
Py_INCREF(&VirtualCameraObjectType);
PyModule_AddObject(module, VirtualCamera_name, (PyObject *)&VirtualCameraObjectType);

```

现在看到 PyObject 的实现参考，以 [MaixPy3/ext_modules/_maix_camera/_camera_virtual.c](https://github.com/sipeed/MaixPy3/blob/main/ext_modules/_maix_camera/_camera_virtual.c) 为范本。

```c

PyDoc_STRVAR(VirtualCameraObject_type_doc, "VirtualCamera(width, height) -> VirtualCamera object.\n");
typedef struct
{
  PyObject_HEAD;
  unsigned int width, height;
} VirtualCameraObject;

static PyGetSetDef VirtualCamera_getseters[] = {
    {"width", (getter)VirtualCamera_get_width, (setter)VirtualCamera_set_width, VirtualCamera_width_doc},
    {"height", (getter)VirtualCamera_get_height, (setter)VirtualCamera_set_height, VirtualCamera_height_doc},
    {NULL},
};

PyTypeObject VirtualCameraObjectType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    VirtualCamera_name,                           /* tp_name */
    sizeof(VirtualCameraObject),                      /* tp_basicsize */
    0,                                        /* tp_itemsize */
    (destructor)VirtualCamera_free,                   /* tp_dealloc */
    0,                                        /* tp_print */
    0,                                        /* tp_getattr */
    0,                                        /* tp_setattr */
    0,                                        /* tp_compare */
    0,                                        /* tp_repr */
    0,                                        /* tp_as_number */
    0,                                        /* tp_as_sequence */
    0,                                        /* tp_as_mapping */
    0,                                        /* tp_hash */
    0,                                        /* tp_call */
    VirtualCamera_str,                                /* tp_str */
    0,                                        /* tp_getattro */
    0,                                        /* tp_setattro */
    0,                                        /* tp_as_buffer */
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE, /* tp_flags */
    VirtualCameraObject_type_doc,                     /* tp_doc */
    0,                                        /* tp_traverse */
    0,                                        /* tp_clear */
    0,                                        /* tp_richcompare */
    0,                                        /* tp_weaklistoffset */
    0,                                        /* tp_iter */
    0,                                        /* tp_iternext */
    VirtualCamera_methods,                            /* tp_methods */
    0,                                        /* tp_members */
    VirtualCamera_getseters,                          /* tp_getset */
    0,                                        /* tp_base */
    0,                                        /* tp_dict */
    0,                                        /* tp_descr_get */
    0,                                        /* tp_descr_set */
    0,                                        /* tp_dictoffset */
    (initproc)VirtualCamera_init,                     /* tp_init */
    0,                                        /* tp_alloc */
    VirtualCamera_new,                                /* tp_new */
};
```

实现任何模块时需重点关注如下基本函数接口实现，忽略（Camera）前缀，且下文函数只做举例。

- xxxxx_new （对象构造函数）
- xxxxx_free （对象析构函数）
- xxxxx_init （对象初始化函数）
- xxxxx_getseters （对象属性定义结构）
- xxxxx_methods （对象方法定义结构）

开发上遵循基本结构即可，展示 PyArg_ParseTupleAndKeywords 传递参数用法，以 Camera_init 为例，如果不想写 keyword （kwlist） 就用 PyArg_ParseTuple 函数。

```c
static int Camera_init(CameraObject *self, PyObject *args, PyObject *kwds)
{
  // default init value
  self->width = 640, self->height = 480;

  static char *kwlist[] = {"width", "height", NULL};

  if (!PyArg_ParseTupleAndKeywords(args, kwds, "|ii:__init__", kwlist,
                                   &self->width, &self->height))
  {
    return -1;
  }

  return 0;
}
```

为 PyObject 对象链接函数符号的时候可以看 xxxxx_getseters 和 xxxxx_methods 的结构定义。

```c
static PyMethodDef Camera_methods[] = {

    {"close", (PyCFunction)Camera_close, METH_NOARGS, Camera_close_doc},
    {"__enter__", (PyCFunction)Camera_enter, METH_NOARGS, NULL},
    {"__exit__", (PyCFunction)Camera_exit, METH_NOARGS, NULL},
    {NULL},
};

static PyGetSetDef Camera_getseters[] = {
    {"width", (getter)Camera_get_width, (setter)Camera_set_width, Camera_width_doc},
    {"height", (getter)Camera_get_height, (setter)Camera_set_height, Camera_height_doc},
    {NULL},
};
```

以 Python3 的 _maix.Camera 为例：

```python

import _maix

tmp = _maix.Camera()

print("this is method", Camera.close)

print("this is var", Camera.width)

```

一个简单的 PyCFunction 函数实现方法如下：

```c
/* str */
static PyObject *Camera_str(PyObject *object)
{
  PyObject *dev_desc = PyUnicode_FromString("Camera_str");

  return dev_desc;
}
```

如果是定义模块的全局函数则可以配置 METH_NOARGS 并移除函数参数，参考如下代码。

```c

static PyObject *_maix_help() {
    return PyUnicode_FromString(_maix_doc);
}

static PyMethodDef _maix_methods[] = {
    {"help", (PyCFunction)_maix_help, METH_NOARGS, _maix_doc},
    {NULL}
};

```

关于编写 CPython 模块的参考资料很多，这里只说明 MaixPy3 模块常用的程序设计，具体到函数的如何实现的细节就不在此赘述。

### CPython 的内存标记用法

可知 Python 拥有自动回收内存的 gc 机制，但在使用 Python C/C++ API 扩展 Python 模块时，对象指针标记不当可能会导致扩展的模块存在内存泄漏，可以使用 Py_INCREF（增加） & Py_DECREF（减少） 指针引用计数。

```c
Py_INCREF(ref);
......
Py_DECREF(ref); // Py_XDECREF(ref);
```

对应 Python 代码就是：

```python
ref = 1
....
del ref
```

可以理解为想要 gc 主动释放一个对象，就需要将其引用标志减少到无（0）。

关于标记指针的说明上有用的文章。

- 在开发时的注意事项请查阅 [使用 C 写 Python 模块时内存回收管理，Py_INCREF() 和 Py_DECREF() 的使用方式和注意点](https://neucrack.com/p/340)
- 关于原理性的源码解析 [解密Python中的垃圾回收机制](https://www.cnblogs.com/traditional/p/13698244.html)

如果你不能确定当前指针是否已经被回收，则你可以在使用前对 PyObject 结构指针进行引用计数的判断，也可以对该结构的类型做判断，从而确保可以操作该对象。

```c

assert(self->ob_refcnt > 0);

PyAPI_DATA(PyTypeObject) PyBool_Type;
#define PyBool_Check(x) Py_IS_TYPE(x, &PyBool_Type)

```

这样你就可以放心的操作内部创建的对象实例了。

### CPython 模块的编写约束

因为强调面向接口编程，所以 Python 模块下的 libXXXX 模块都是在各自的仓库编译通过后，再通过 setup.py 模块定义接口之间进行链接的，有些子仓库就是这么来的。

也就是说不对编写代码风格做约束，但会对模块的接口做约束。

要求每个模块的层次关系分离，以模块（PyModule）、对象（PyObject）、方法（PyCFunction）为接口参考，有如下结构。

```shell
+----------+         +-------------+
|          +---------+ PyCFunction | 全局函數
| PyModule |         +-------------+
|          +<---+
+----------+    |
                |模块对象
             +--+-------+
             | PyObject +<---+
             +----------+    |
                             |
                     +-------+-----+
                     | PyCFunction | 成员函數
                     +-------------+
```

因此请遵循该接口设计进行 Python 模块的开发。

## 一些额外的内容

### 使用 bdist_wheel 打包对应平台 wheel 包

打包成对应平台的 wheel 的 bdist_wheel 的命令需要 setuptools 中支持。

> 而 distutils 只可以构建 bdist 包。

bdist_wheel 是将当前代码构建的最终文件都打包好，然后在安装的时候只需要释放到具体的安装目录下就结束了，这对于一些不能进行编译工作的硬件来说是极好的。

确认 wheel 包是否可以被安装，只需要看名称就知道了，例如 `python3_maix-0.1.2-cp38-cp38-linux_x86_64.whl` 包，我们可以看到 `cp38-cp38-linux_x86_64` 标识。

pip 在安装的时候就会通过 `from pip._internal.utils.compatibility_tags import get_supported` 函数判断当前系统是否可以支持这个包，如果你改名了，它也是可以安装进去的,但能不能运行就取决于系统环境了，注意 armv7.whl 和 armv7l.whl 并不相同。

> 细节阅读 [2021 年 当安装 wheel 出现 whl is not a supported wheel on this platform. 的时候](https://www.cnblogs.com/juwan/p/14250104.html)

###  自动化测试框架 tox 的使用说明

在本机上使用 `pip3 install tox` 完成安装，接着在 MaixPy3 根目录下运行 tox 即可。

它会自动构建指定的 Python 虚拟测试环境，进行打包构建，安装解包的测试，最后会收集整个目录下的 `test_*.py` 的代码加入到自动测试当中，如果你不想让个别代码参与测试，你可以改名成 `no_test_*.py` 方便排除和保留文件。

更多请自行查阅 [Python 任务自动化工具 tox 教程](https://www.cnblogs.com/daniumiqi/p/12179453.html) 和官方文档 [tox.readthedocs.io](tox.readthedocs.io) 。

### *关于 V831 或其他平台芯片如何使用

以上文档为通用说明，使用方法差异的地方在于调用 Python 指令有所不同。

例如加载 V831 等其他平台的 SDK 环境后，要将上述命令中的 python3 改成对应 SDK 环境的 python3.8 用以调用交叉编译的 Python 解释器，从而完成目标 arm 平台的交叉编译，这是由 SDK 提供时决定的，其他平台统一按这个结构载入即可。

### 调用 get-pip.py 手动为 Python pip 安装指定包。

有时候一些交叉编译里面的 Python 环境可能会缺少 pip ，如果想要安装包，就可以用这样的方式从外部装进去。

- `./python3.7 get-pip.py Cython --target=../usr/lib/python3.7/site-packages/`

