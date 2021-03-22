---
title: pye (Micropython Editor)
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: pye (Micropython Editor)
---


In MaixPy, we have built-in an open source editor [Micropython Editor(pye)](https://github.com/robert-hh/Micropython-Editor)

> Note that this function is not included in the `minimum` version of the firmware

Use `os.listdir()` to view the files in the current directory,

Use `pye("hello.py")` to create a file and enter the editing mode, and the instructions for using shortcut keys can be found in [here](https://github.com/robert-hh/Micropython-Editor/blob/master /Pyboard%20Editor.pdf)

For example, we write code

```python
print("hello maixpy")
```

Then press `Ctrl+S` and press `Enter` to save, press `Ctrl+Q` to exit editing

**Note**: The use of this editor has certain requirements for the serial tool used. The `BackSpace` key must be set to the `DEL` function, otherwise pressing `BackSpace` will call the same function as `Ctrl+H` ( That is character replacement).

It is recommended to use `minicom` under Linux, you need to use `sudo minicom -s` to set, refer to [previous tutorial](./../../get_started/env_serial_tools.md)

The same is true under Windows, search the setting method according to the tool you use, such as `xshell` search `xshell How to set backspace to del` to get the result:

`File` -> `Properties` -> `Terminal` -> `Keyboard`,
Change the sequence of delete and backspace to ASCII 127.
