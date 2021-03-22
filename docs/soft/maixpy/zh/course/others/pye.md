---
title: pye (Micropython Editor)
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: pye (Micropython Editor)
---


在 MaixPy 中, 我们内置了一款编开源编辑器 [Micropython Editor(pye)](https://github.com/robert-hh/Micropython-Editor)

> 注意在`minimum`版本的固件中不包含此功能

使用 `os.listdir()` 可以查看当前目录下的文件,

使用 `pye("hello.py")` 可以创建文件并进入编辑模式, 快捷键等使用说明可以在[这里查看](https://github.com/robert-hh/Micropython-Editor/blob/master/Pyboard%20Editor.pdf)

比如我们写入代码

```python
print("hello maixpy")
```

然后按 `Ctrl+S` 按 `Enter` 键保存, 按 `Ctrl+Q` 退出编辑

**注意**： 使用这款编辑器对使用的串口工具有一定要求, 必须将 `BackSpace` 按键设置为 `DEL` 功能, 否则按 `BackSpace` 调用的是 `Ctrl+H` 一样的功能（即字符替换）。

Linux 下推荐使用 `minicom`, 需要使用 `sudo minicom -s` 来设置,参考[前面的教程](./../../get_started/env_serial_tools.md)

Windows 下也一样, 根据自己使用的工具上网搜设置方法, 比如 `xshell` 搜 `xshell如何设置backspace为del` 得到结果：

`文件` -> `属性` -> `终端` -> `键盘`,
把 delete 和 backspace 序列改为 ASCII 127 即可.




