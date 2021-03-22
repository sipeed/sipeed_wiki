---
title: Summary
keywords: maixpy, k210, AIOT, 边缘计算
desc: maixpy doc: Summary
---


* [简介](README.md)
* [MaixPy 能做哪些事](./what_maix_do.md)
* [MaixPy 发展历程](./maixpy_history.md)
* [致谢](./thanks.md)


## 入门必看指南

* [如何正确阅读本文 (重要！！！)](./how_to_read.md)
* [如何优雅提问 (重要！！！)](./how_to_ask.md)
* 开发板和配件选购指南
  - [开发板选购指南(对比)](./develop_kit_board/get_hardware.md)
  - 开发板介绍
    - [Maix Dock](./develop_kit_board/maix_dock.md)
    - [Maix Bit](./develop_kit_board/maix_bit.md)
    - [Maix Amigo](./develop_kit_board/maix_amigo.md)
    - [Maix Duino](./develop_kit_board/maix_duino.md)
    - [Maix Cube](./develop_kit_board/maix_cube.md)
    - [Maix Go](./develop_kit_board/maix_go.md)
    - [Maix Nano](./develop_kit_board/maix_nano.md)
  - 外设模组（配件）
    - [SP-MOD](./modules/sp_mod/README.md)
    - [Grove](./modules/grove/README.md)
    - [其它](./modules/others/README.md)
* 基础知识
  - [MaixPy 语法基础知识](./get_started/knowledge_micropython.md)
  - [git 和 github](./get_started/knowledge_git_github.md)
  - [MaixPy 图像基础知识](./get_started/knowledge_image.md)
  - [MaixPy 音频基础知识](./get_started/knowledge_audio.md)
* 开发环境准备
  - [安装驱动](./get_started/env_install_driver.md)
    - [Maix Dock](./get_started/install_driver/dock.md)
    - [Maix Bit](get_started/install_driver/bit.md)
    - [Maix Amigo](get_started/install_driver/amigo.md)
    - [Maix Cube](get_started/install_driver/cube.md)
    - [Maix Go](get_started/install_driver/go.md)
    - [Maix Nano](get_started/install_driver/nano.md)
  - [更新 MaixPy 固件](./get_started/upgrade_maixpy_firmware.md)
  - [使用串口终端工具](./get_started/env_serial_tools.md)
  - [MaixPy IDE 使用说明](./get_started/env_maixpyide.md)
  - 更新 WIFI 模块固件
    - [更新板载 ESP32 固件](./get_started/upgrade_esp32_firmware.md)
    - [更新板载 ESP8285 固件](./get_started/upgrade_esp8285_firmware.md)
* 上手
  - [上电](/get_started/get_started_power_on.md)
  - [第一个程序: 使用屏幕和摄像头](./get_started/get_started_cam_lcd.md)
  - [第二个程序: 点亮 LED](./get_started/get_started_led_blink.md)
  - [存储系统介绍](./get_started/get_started_fs.md)
  - [编辑并运行脚本](./get_started/get_started_edit_file.md)
  - [上传脚本到开发板](./get_started/get_started_upload_script.md)
  - [开机自动运行脚本](./get_started/get_started_boot.md)
  - [开发板配置文件](./api_reference/builtin_py/board_info.md)
  - [上手视频教程](./get_started/maixpy_get_started_video.md)
* 固件定制
  - [为什么需要定制固件](./firmware/why_customize_firware.md)
  - [在线编译](./firmware/online_compile.md)
  - [源码编译](./firmware/compile.md)


## MaixPy 手把手教程

* [教程说明](./course/readme.md)
* 基本图像处理
  * 图像获取和显示
    * [图像获取](./course/image/basic/get_images.md)
    * [图像显示](./course/image/basic/display_images.md)
  * [MaixPy 图像及常用操作](./course/image/basic/vary.md)
  * [基本画图、写字](./course/image/basic/draw.md)
  * [硬件加速的图像处理](./course/image/basic/acc_image_deal.md)
* MaixPy AI
  * [深度神经网络基础知识](./course/ai/basic/dnn_basic.md)
  * [MaixPy AI 硬件加速基础知识](./course/ai/basic/maixpy_hardware_ai_basic.md)
  * 图像处理
    * [人脸检测](./course/ai/image/face_detect.md)
    * [1000 种物体分类](./course/ai/image/1000_type_classifier.md)
    * [人脸识别](./course/ai/image/face_recognization.md)
    * [自学习分类](./course/ai/image/self_learn_classifier.md)
  * 音频处理
    * [语音识别](./course/speech/recognizer_cnn.md)
* 模型训练
  * 训练自己的分类和检测模型
    * [MaixHub 云端训练](./course/ai/train/maixhub.md)
    * [本地训练](./course/ai/train/local.md)
* 传统算法
  * 图像处理
    - [寻找色块](./course/image/find_color_blob.md)
    - [二维码识别](course/image/find_qrcodes.md)
  * 音频处理
    - [FFT](course/speech/fft.md)
    - [FFT 瀑布图](course/speech/fft_waterfall.md)
    - [关键词识别](./course/speech/recognizer_mfcc.md)
* 外设
  * 片上外设
    - [I2C](modules/on_chip/i2c.md)
    - [PWM](modules/on_chip/pwm.md)
    - [SPI](modules/on_chip/spi.md)
    - [Timer](modules/on_chip/timer.md)
    - [UART](modules/on_chip/uart.md)
    - [I2S](modules/on_chip/i2s.md)
    - [WDT](modules/on_chip/wdt.md)
  * [SP-MOD](./modules/sp_mod/README.md)
    - [BT 蓝牙透传](./modules/sp_mod/sp_bt.md)
    - [LoRa 无线通信](./modules/sp_mod/sp_lora.md)
    - [RFID 射频识别](./modules/sp_mod/sp_rfid.md)
    - [TOF 测距](./modules/sp_mod/sp_tof.md)
    - [Eink 电子墨水屏](./modules/sp_mod/sp_eink.md)
    - [Lcd1.14 IPS屏](./modules/sp_mod/sp_lcd1.14.md)
    - [Weather 气象模块](./modules/sp_mod/sp_weather.md)
    - [Ethernet 有线网口](modules/sp_mod/sp_ethernet.md)
  * [Grove](./modules/grove/README.md)
    - [Ultrasonic Ranger 测距](modules/grove/grove_ultrasonic_ranger.md)
    - [Chainable RGB LED 灯](modules/grove/grove_chainable_rgb_led.md)
    - [RGB LED Ring 灯条](modules/grove/grove_rgb_led_ring.md)
  * 更多外设
    - [Sipeed 麦克风阵列](./develop_kit_board/module_microphone.md)
    - [双摄模块](modules/others/binocular_camera.md)
    - [MLX90640 串口红外镜头](modules/others/mlx90640.md)
    - [HTPA 红外镜头](modules/others/htpa.md)
    - [舵机](modules/others/servo.md)
    - [ESP32 ADC](./modules/others/esp32_read_adc.md)
    - [onwire 单总线](modules/others/onewire.md)
* 更多功能
  * 系统
    - [主频、复位等](./course/others/system.md)
    - [内存配置与查看](./course/others/mem.md)
  * GUI
    - [中文等多国语言支持](./course/image/image_draw_font/image_draw_font.md)
    - [Maix UI](./course/others/maixui.md)
    - [Lvgl](./course/others/lvgl.md)
    - [编辑器 pye](./course/others/pye.md)
  * 网络
    - [配置 network 网卡](./course/network/network_config.md)
    - [使用 socket 通信](./course/network/socket_usage.md)
  * 多媒体
    - [audio](./course/media/audio.md)
    - [video](./course/media/video.md)
  * 游戏
    - [NES 游戏机](./api_reference/media/nes.md)

## API手册

* [标准库](./api_reference/standard/README.md)
  - [cmath](./api_reference/standard/cmath.md)
  - [gc](./api_reference/standard/gc.md)
  - [math](./api_reference/standard/math.md)
  - [sys](./api_reference/standard/sys.md)
  - [ubinascii](./api_reference/standard/ubinascii.md)
  - [ucollections](./api_reference/standard/ucollections.md)
  - [uctypes](./api_reference/standard/uctypes.md)
  - [uerrno](./api_reference/standard/uerrno.md)
  - [uhashlib](./api_reference/standard/uhashlib.md)
  - [uheapq](./api_reference/standard/uheapq.md)
  - [ujson](./api_reference/standard/ujson.md)
  - [uos](./api_reference/standard/uos.md)
  - [ure](./api_reference/standard/ure.md)
  - [usocket](./api_reference/standard/usocket.md)
  - [ustruct](./api_reference/standard/ustruct.md)
  - [utime](./api_reference/standard/utime.md)
  - [uzlib](./api_reference/standard/uzlib.md)
* [machine](./api_reference/machine/README.md)
  - [I2C](./api_reference/machine/i2c.md)
  - [PWM](./api_reference/machine/pwm.md)
  - [SPI](./api_reference/machine/spi.md)
  - [Timer](./api_reference/machine/timer.md)
  - [UART](./api_reference/machine/uart.md)
  - [network](./api_reference/machine/network.md)
  - [WDT](api_reference/machine/wdt.md)
* [Maix](./api_reference/Maix/README.md)
  - [FPIOA](./api_reference/Maix/fpioa.md)
  - [GPIO](./api_reference/Maix/gpio.md)
  - [KPU](./api_reference/Maix/kpu.md)
  - [FFT](./api_reference/Maix/fft.md)
  - [I2S](./api_reference/Maix/i2s.md)
  - [freq](./api_reference/Maix/freq.md)
  - [utils](./api_reference/Maix/utils.md)
* [helper](./api_reference/builtin_py/README.md)
  - [fpioa_manager](./api_reference/builtin_py/fm.md)
  - [board_info](./api_reference/builtin_py/board_info.md)
  - [Micropython Editor](./api_reference/application/pye.md)
* [media](./api_reference/machine_vision/README.md)
  - [lcd](./api_reference/machine_vision/lcd.md)
  - [sensor](./api_reference/machine_vision/sensor.md)
  - [image](api_reference/machine_vision/image/image.md)
  - [video](./api_reference/media/video.md)
  - [audio](./api_reference/media/audio.md)
  - [nes](./api_reference/media/nes.md)
  - [lvgl](./course/others/lvgl.md)
  - [isolated_word](./api_reference/machine_vision/isolated_word.md)
  - [maix_asr](./api_reference/machine_vision/maix_asr.md)
* [extend](./api_reference/extend/README.md)
  - [touchscreen](./api_reference/extend/touchscreen.md)
  - [modules.ultrasonic](./api_reference/extend/ultrasonic.md)
  - [modules.ws2812](./api_reference/extend/ws2812.md)
  - [modules.htpa](./api_reference/extend/htpa.md)
  - [modules.onewire](./api_reference/extend/onewire.md)


## 常见问题 FAQ

* [MaixPy 常见问题 FAQ](./others/maixpy_faq.md)
* [MaixHub 平台 FAQ](./others/maixhub_faq.md)


## 进阶

* 进阶开发
  - [源码目录结构](./course/advance/project_framework.md)
  - [如何编译 MaixPy 工程](course/advance/compile.md)
  - [如何用 C 添加一个 MaixPy 模块](./course/advance/add_c_module.md)
  - [打包文件系统](./course/advance/pack_fs.md)

* 参与贡献
  - [参与文档编写（规范）](./contribute/doc_convention.md)
  - [代码编写规范](./contribute/code_convention.md)


## 社区 & 分享

- [精选文章](./share/recommend_articles.md)
- [开源项目](./share/open_projects.md)
- 大家的经验分享
  * [参与经验分享/分享模板](./share/my_share/README.md)

