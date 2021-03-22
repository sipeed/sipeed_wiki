---
title: Code frame structure
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: code frame structure
---




## Directory Introduction

| Directory | Sub-directory | Sub-directory 2 | Sub-directory 3 | Content summary |
| --- | --- | --- | --- | --- |
| assets | | | | Resource files |
| projects | | | | Project files, one project per folder |
| tools | | | | Tools |
| components|┐ | | | components |
| | └-boards | | | Board code |
| | └-drivers | | | Drive |
| | └-micropython |┐ | | micropython related code |
| | |└-core | | micropython source code |
| | |└-port|┐ | maixpy ​​custom part source code |
| | | |└-builtin_py | maixpy ​​default built-in class |
| | | |└-include | Porting some header files |
| | | |└-src | Function module source code |
| | └-spiffs | | | SPIFFS file system |
| | └-utils | | | Tools (Function) |


> The current code is not very well structured in the `components/micropython/port/src` directory due to historical reasons. The future code should follow the current framework as much as possible to achieve a hierarchy


## Add code

The project is organized using `CMake`, and the project supports multiple configurable options (`Kconfig`)

* If you do not add folders and configuration items, you can add files and compile them in the existing folders
* If you need to add modules, you can modify `CMakeLists.txt` to add content, you can refer to the less content [c_cpp_project_framework](https://github.com/Neutree/c_cpp_project_framework)
* If you need to add configuration items, you can modify the `Kconfig` file to achieve the goal. All configuration items will generate macro definitions and add them to `global_config.h` (generated files) during compilation, and in `CmakeLists.txt` This macro definition can be used in all files.
> For example, define `config BOARD_M5STICK` in Kconfig, in CMakeLists.txt, you can determine whether to compile specific code by judging whether CONFIG_BOARD_M5STICK is true. When compiling, you can choose whether to check it through `python3 project.py menuconfig`
