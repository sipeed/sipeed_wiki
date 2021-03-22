---
title: 如何用 C 添加一个 MaixPy 模块
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: 如何用 C 添加一个 MaixPy 模块
---



## 预备知识

在 `python` 中万物皆对象

需要先知道 module，type， function， class 分别是什么，有什么关系和区别 

* module（模块）

在`MaixPy`中，把每个类别的功能放到一个 模块 中，
比如内置的 `uos`,`usys`,`machine`，
另外我们自己新建的文件， 比如`test.py` 也可以是一个模块，
我们使用模块都这样使用：
```python
import uos
import machine
import test
```
> 在 C 源码中就是 `mp_type_module`

* type（类型）

用来表示一个基本的类型， 它可以包含一些方法或者变量

> 在 C 源码中就是 `mp_type_type`

* class（类）

一个 class 其实就是一个 `type`，比如
```python
class A:pass
print(type(A))
```
会输出
```
<class 'type'>
```

当对`A`进行了实例化
```
class A:pass
a = A()
print(type(a))
```
会输出
```
<class 'A'>
```
表示`a`是`A`的一个实例（对象）

> 在 C 中定义一个类其实就是定义一个 `mp_type_type`

## 在 C 中添加模块

我们的目标是实现在`MaixPy`层面可以使用以下代码：
```python
import my_lib
print(my_lib.__name__)
my_lib.hello()
```


### 在`components/port/src`目录下新建一个文件夹比如取名`my_lib`

### 然后在`my_lib`文件夹下新建`my_lib.c`文件

### 编辑`my_lib.c`添加代码
#### 定义一个模块：
```c
#include "obj.h"

const mp_obj_module_t my_lib_module = {
    .base = { &mp_type_module },
    .globals = (mp_obj_dict_t*)&mp_module_my_lib_globals_dict,
};
```
这里`my_lib_module`是定义的`my_lib`模块对象,
`mp_type_module`表明是一个模块，
`mp_module_my_lib_globals_dict`是模块的全局变量和函数，是一个`dict`对象，有我们自己定义， 现在还没定义

#### 定义模块的全局变量

```c
STATIC mp_obj_t hello()
{
    mp_printf(&mp_plat_print, "hello from my_lib");
    return mp_const_none;
}

MP_DEFINE_CONST_FUN_OBJ_0(my_lib_func_hello_obj, my_lib_func_hello);

STATIC const mp_map_elem_t my_lib_globals_table[] = {
    { MP_OBJ_NEW_QSTR(MP_QSTR___name__), MP_OBJ_NEW_QSTR(MP_QSTR_my_lib) },
    { MP_OBJ_NEW_QSTR(MP_QSTR_hello), (mp_obj_t)&my_lib_func_hello_obj },
    
};

STATIC MP_DEFINE_CONST_DICT (
    mp_module_my_lib_globals_dict,
    my_lib_globals_table
);
```

这里定义了一组键值对数组，键值对数值, `mp_map_elem_t`的定义如下：
```c
typedef struct _mp_map_elem_t {
    mp_obj_t key;
    mp_obj_t value;
} mp_map_elem_t;
```

* 第一个值是`key`，类型是`str`对象， 即在`MaixPy`层面使用`my_lib.key`来调用。这里用了`MP_OBJ_NEW_QSTR(MP_QSTR___name__)`生成了一个值为`__name__`的`str`对象，你可能有疑问`__name__`这个`c`变量定义在哪里，这是在编译阶段使用工具自动生成`c`变量，总之记住这样可以写可以生成一个常量`str`对象保存在固件里就好了
* 第二个值是数值，类型是一个对象，可以是`str/function/int/float/tuple/list/dict`等， 方式如下：
  * `str`: 这里同样是定义了一个`str`类型的值为`my_lib`,即在`MaixPy`层面使用`my_lib.__name__`得到结果`my_lib`。
  * `其它常量对象`： 可以使用`mp_obj_new_xxx`,比如`int`变量`mp_obj_new_int(10)`， 函数在`obj.h`中搜索
  * `函数`： 这里的`key``hello`对应的值为为`(mp_obj_t)&my_lib_func_hello_obj`，是一个函数对象，注意不是`C`函数，前面说了`python`中一切皆对象， 这里也是使用了一个函数对象，然后去地址强制转换成 `mp_obj_t`。这个函数对象使用了`MP_DEFINE_CONST_FUN_OBJ_0`宏定义将`my_lib_func_hello`这个`C`函数定义为`my_lib_func_hello_obj`这个对象，注意`hello`函数需要返回一个值`mp_const_none`,注意不能返回`NULL`， 因为`NULL`不是一个(`MaixPy`)对象， 这个返回值也就是`MaixPy`层面调用`hello()`函数时的返回值
  > 除了`MP_DEFINE_CONST_FUN_OBJ_0`即没有参数之外，还有`1/2/3/n`个参数，以及带关键字参数，这些请翻阅源码举一反三学习


然后使用`MP_DEFINE_CONST_DICT`宏定义将`my_lib_globals_table`这个键值对变成`MaixPy`层面能理解的`dict`对象（`mp_map_elem_t`只是`C`层面能理解）`mp_module_my_lib_globals_dict`, 这个对象也被上一步中定义模块的时候使用

到此一个模块就定义完成了， 在 `MaixPy`层面，理论上可以使用如下语句进行使用了
```python
import my_lib
print(my_lib.__name__)
my_lib.hello()
```

但是我们还没编译

#### 将模块添加到固件， 并进行编译

* 在`my_lib.c`文件末尾添加:

```c
MP_REGISTER_MODULE(MP_QSTR_my_lib, my_lib_module, MODULE_MY_LIB_ENABLED);

```

这行代码注册这个模块，但是是否编译进固件取决与`MODULE_MY_LIB_ENABLED`这个宏定义在`mpconfigport.h`中是否定义为`1`

* 所以我们打开`mpconfigport.h`文件，在里面添加

```c
#define MODULE_MY_LIB_ENABLED (1)
```

* 打开`components/micropython/CMakeLists.txt`编辑

找到文件中有`############## Add source files ###############` 的地方，
在后面添加
```cmake
append_srcs_dir(MPY_PORT_SRCS "port/src/my_lib")
```
到此，项目才会将`my_lib`这个文件夹编译到固件

然后`python project.py rebuild`编译固件即可，因为新增了文件，一定要用`rebuild`命令而不是`build`，注意编译提示，如果有报错，注意修改


## 在模块中添加一个 type

前面定义了一个`my_lib`模块，现在我们希望在`my_lib`中定义一个类，叫`A`，如下

```python
import my_lib

a = my_lib.A()
print(a.add(1, 2))
```

这里只讲大致上的思路，然后提供样例，聪明的你一下就能理解了

* 定义一个`mp_obj_type_t` 对象，正如前面定义`mp_obj_module_t`一样
* 同样的，给这个类对象一个`dict`对象，作为这个类的成员，成员可以是常量或者函数甚至是另一个`type`对象
* 将这个类对象注册到前面的`my_lib`模块

定义`mp_obj_type_t`对象和成员定义可以参考`port/src/standard_lib/machine/machine_i2c.c`中的实现
> 定义`mp_obj_type_t`时有一个`make_new`成员，这个函数是用来新建对象时会被调用的函数，比如`a = my_lib.A(); a.add(1,2)`
> 如果不新建对象，直接调用类方法或变量，这个函数不会被调用`A.var_a`

比如我们定义了一个`const mp_obj_type_t my_lib_A_type ... `

然后在`my_lib/my_lib.c`中 `my_lib_globals_table`中添加这个对象，并将其映射到`key` `A`即可
```c
{ MP_ROM_QSTR(MP_QSTR_A),  MP_ROM_PTR(&my_lib_A_type) },
```



## 使用 C 语言编写固件时需要注意

* `mp_printf` vs `printk` vs `printf`：
因为`IDE`使用了串口通信协议，所以在`C`层面不要直接使用`printk`或者`printf`函数打印消息，**必须**使用`mp_printf`函数来打印，不然会导致 `IDE` 运行时收到不理解的数据而断开连接！！

当然平时调试可以使用`printk`，因为这个函数不会触发系统中断，可以在中断函数里面调用，但是仅限调试时使用， 实际提交代码时一定要删除掉！！





