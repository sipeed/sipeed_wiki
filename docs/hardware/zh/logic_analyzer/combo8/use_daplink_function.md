---
title:  作为DAPLink使用
keywords: LogicAnalyzer, debugger, link, RISCV, tool
update:
  - date: 2023-07-23
    version: v0.1
    author: lxo
    content:
      - Release docs
---

SLogic Combo8 具备高速DAP-Link功能，适用于各种常规芯片，尤其是在Windows下使用IDE调试的STM32等芯片

## 开启DAPLink功能

按下切换按键，将指示灯切换为绿色

![slogic_led_green](./assets/use_daplink_function/slogic_led_green.png)

> 验证SLogic功能是否开启的方法:

> Linux：使用lsusb命令可以看到出现了CMSIS-DAP HS的USB设备

### 开始使用

以STM32F103C8T6芯片在Windows MDK IDE为例介绍具体使用步骤：连接，下载、调试固件，演示使用的MDK版本为当前最新版（V5.38）

- 首先通过STM32CUBEMX快速生成工程项目，注意生成项目的最低版本号
- 使用MDK连接DAPLink

![cfg_dap_debugger_of_mdk](./assets/use_daplink_function/cfg_dap_debugger_of_mdk.png)

- 使用MDK下载固件

![download_fw_in_mdk](./assets/use_daplink_function/download_fw_in_mdk.png)

- 使用MDK调试固件

![start_debugger_in_mdk](./assets/use_daplink_function/start_debugger_in_mdk.png)

#### 体验用户测试DAPlink下载功能例子
##### 测试环境：
1. mdk5.36
2. stm32f103zet6

##### SWD下载方式：
###### 步骤1：SLogic Combo8只需要接四根线：
测试时候将该产品切换daplink模式（也就是绿灯，通过产品上面的按钮进行切换）
|  SLogic Combo8  | stm32f103zet6  |
|:--:|:--:|
|  GND  |  GND  |
|:--:|:--:|
|  5V  |  5V  |
|  TCK  |  PA14  |
|  TDI  |  × |
|  TDO  |  × |
|  TMS  |  PA13   |

###### 步骤2：设置下图
![picture 11](https://img2023.cnblogs.com/blog/2915785/202307/2915785-20230731153820805-374617887.png)  


设置上图的原因（注明：如果是autodect可能下载不成功）：  
keil , Debug菜单 - Reset菜单选项（Autodetect/HWreset/sysresetReq/Vectreset）含义：  
1、Reset — HW RESET  
英文含义：performs a hardware reset by asserting the hardware reset (HW RESET) signal.  
中文含义：复位-硬件复位通过置位硬件复位（HW RESET）信号来执行硬件复位。   
2、Reset — SYSRESETREQ  
英文含义：performs a software reset by setting the SYSRESETREQ bit. The Cortex-M core and on-chip peripherals are reset.  
中文含义：通过将SYSRESETREQ位置1来执行软件复位。 Cortex-M内核和片上外设被重置。  
3、Reset — VECTRESET  
英文含义：performs a software reset by setting the VECTRESET bit. Only the Cortex-M core is reset. The on-chip peripherals are not affected. For some Cortex-M devices, VECTRESET is the only way to reset the core. VECTRESET is not supported on Cortex-M0 and Cortex-M1 cores.  
中文含义：复位-VECTRESET通过将VECTRESET位置1来执行软件复位。 仅Cortex-M内核被重置。 片上外设不受影响。 对于某些Cortex-M设备，VECTRESET是重置内核的唯一方法。 Cortex-M0和Cortex-M1内核不支持VECTRESET。  
4、Reset — Autodetect  
英文含义：selects one of the above reset methods based on the target device. The SYSRESETREQ method is used if an unknown device is detected.  
中文含义：重置-自动检测根据目标设备选择上述重置方法之一。 如果检测到未知设备，则使用SYSRESETREQ方法。  
note：
SWD模式下，Debug菜单中，Reset菜单选（Autodetect/HWreset/sysresetReq/Vectreset）默认是AutoDetect，改成SysResetReq即可
#### DAPlink下载失败的可能存在的问题
在设备管理器中能够检测到RV dap，但是keil软件中没有RV dap（如下图）
mdk版本太低如果不支持winusb的dap，可能就会出现该情况，群友提供的解决办法：https://developer.arm.com/documentation/ka003663/latest/， 但是最直接的办法是直接使用最新版的MDK，官网教程是使用的是5.38.
![picture 10](https://img2023.cnblogs.com/blog/2915785/202307/2915785-20230731153822779-1936933410.png)
