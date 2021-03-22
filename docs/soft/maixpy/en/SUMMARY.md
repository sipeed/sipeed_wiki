---
title: Summary
keywords: maixpy, k210, AIOT, edge computing
desc: maixpy ​​doc: Summary
---


* [Introduction](README.md)
* [What can MaixPy do](./what_maix_do.md)
* [MaixPy Development History](./maixpy_history.md)
* [Thanks](./thanks.md)


## Getting started must see guide

* [How to read this article correctly (important!!!)](./how_to_read.md)
* [How to ask questions elegantly (important!!!)](./how_to_ask.md)
* Development board and accessories selection guide
  -[Development Board Selection Guide (Comparison)](./develop_kit_board/get_hardware.md)
  -Development board introduction
    -[Maix Dock](./develop_kit_board/maix_dock.md)
    -[Maix Bit](./develop_kit_board/maix_bit.md)
    -[Maix Amigo](./develop_kit_board/maix_amigo.md)
    -[Maix Duino](./develop_kit_board/maix_duino.md)
    -[Maix Cube](./develop_kit_board/maix_cube.md)
    -[Maix Go](./develop_kit_board/maix_go.md)
    -[Maix Nano](./develop_kit_board/maix_nano.md)
  -Peripheral modules (accessories)
    -[SP-MOD](./modules/sp_mod/README.md)
    -[Grove](./modules/grove/README.md)
    -[Other](./modules/others/README.md)
* Basic knowledge
  -[MaixPy Grammar Basics](./get_started/knowledge_micropython.md)
  -[git and github](./get_started/knowledge_git_github.md)
  -[MaixPy image basics](./get_started/knowledge_image.md)
  -[MaixPy Audio Basic Knowledge](./get_started/knowledge_audio.md)
* Development environment preparation
  -[Install Driver](./get_started/env_install_driver.md)
    -[Maix Dock](./get_started/install_driver/dock.md)
    -[Maix Bit](get_started/install_driver/bit.md)
    -[Maix Amigo](get_started/install_driver/amigo.md)
    -[Maix Cube](get_started/install_driver/cube.md)
    -[Maix Go](get_started/install_driver/go.md)
    -[Maix Nano](get_started/install_driver/nano.md)
  -[Update MaixPy firmware](./get_started/upgrade_maixpy_firmware.md)
  -[Use serial terminal tool](./get_started/env_serial_tools.md)
  -[MaixPy IDE Instructions for Use](./get_started/env_maixpyide.md)
  -Update WIFI module firmware
    -[Update onboard ESP32 firmware](./get_started/upgrade_esp32_firmware.md)
    -[Update onboard ESP8285 firmware](./get_started/upgrade_esp8285_firmware.md)
* Get started
  -[Power on](/get_started/get_started_power_on.md)
  -[First program: Use screen and camera](./get_started/get_started_cam_lcd.md)
  -[Second program: turn on the LED](./get_started/get_started_led_blink.md)
  -[Storage System Introduction](./get_started/get_started_fs.md)
  -[Edit and run script](./get_started/get_started_edit_file.md)
  -[Upload script to development board](./get_started/get_started_upload_script.md)
  -[Automatically run script at boot](./get_started/get_started_boot.md)
  -[Development board configuration file](./api_reference/builtin_py/board_info.md)
  -[Getting started video tutorial](./get_started/maixpy_get_started_video.md)
* Firmware customization
  -[Why custom firmware is needed](./firmware/why_customize_firware.md)
  -[Online Compile](./firmware/online_compile.md)
  -[Source code compilation](./firmware/compile.md)


## MaixPy hands-on tutorial

* [Tutorial Description](./course/readme.md)
* Basic image processing
  * Image acquisition and display
    * [Image Acquisition](./course/image/basic/get_images.md)
    * [Image display](./course/image/basic/display_images.md)
  * [MaixPy image and common operations](./course/image/basic/vary.md)
  * [Basic drawing, writing](./course/image/basic/draw.md)
  * [Hardware accelerated image processing](./course/image/basic/acc_image_deal.md)
* MaixPy AI
  * [Basic knowledge of deep neural networks](./course/ai/basic/dnn_basic.md)
  * [MaixPy AI hardware acceleration basic knowledge](./course/ai/basic/maixpy_hardware_ai_basic.md)
  * Image Processing
    * [Face Detection](./course/ai/image/face_detect.md)
    * [1000 object classification](./course/ai/image/1000_type_classifier.md)
    * [Face Recognition](./course/ai/image/face_recognization.md)
    * [Self-learning classification](./course/ai/image/self_learn_classifier.md)
  * Audio processing
    * [Speech recognition](./course/speech/recognizer_cnn.md)
* Model training
  * Train your own classification and detection model
    * [MaixHub Cloud Training](./course/ai/train/maixhub.md)
    * [Local Training](./course/ai/train/local.md)
* Traditional algorithm
  * Image Processing
    -[Find color blocks](./course/image/find_color_blob.md)
    -[QR code recognition](course/image/find_qrcodes.md)
  * Audio processing
    -[FFT](course/speech/fft.md)
    -[FFT waterfall chart](course/speech/fft_waterfall.md)
    -[Keyword recognition](./course/speech/recognizer_mfcc.md)
* Peripherals
  * On-chip peripherals
    -[I2C](modules/on_chip/i2c.md)
    -[PWM](modules/on_chip/pwm.md)
    -[SPI](modules/on_chip/spi.md)
    -[Timer](modules/on_chip/timer.md)
    -[UART](modules/on_chip/uart.md)
    -[I2S](modules/on_chip/i2s.md)
    -[WDT](modules/on_chip/wdt.md)
  * [SP-MOD](./modules/sp_mod/README.md)
    -[BT Bluetooth transparent transmission](./modules/sp_mod/sp_bt.md)
    -[LoRa Wireless Communication](./modules/sp_mod/sp_lora.md)
    -[RFID Radio Frequency Identification](./modules/sp_mod/sp_rfid.md)
    -[TOF Ranging](./modules/sp_mod/sp_tof.md)
    -[Eink electronic ink screen](./modules/sp_mod/sp_eink.md)
    -[Lcd1.14 IPS screen](./modules/sp_mod/sp_lcd1.14.md)
    -[Weather Weather Module](./modules/sp_mod/sp_weather.md)
    -[Ethernet wired network port](modules/sp_mod/sp_ethernet.md)
  * [Grove](./modules/grove/README.md)
    -[Ultrasonic Ranger](modules/grove/grove_ultrasonic_ranger.md)
    -[Chainable RGB LED light](modules/grove/grove_chainable_rgb_led.md)
    -[RGB LED Ring strip](modules/grove/grove_rgb_led_ring.md)
  * More peripherals
    -[Sipeed Microphone Array](./develop_kit_board/module_microphone.md)
    -[Dual camera module](modules/others/binocular_camera.md)
    -[MLX90640 serial infrared lens](modules/others/mlx90640.md)
    -[HTPA infrared lens](modules/others/htpa.md)
    -[Servo](modules/others/servo.md)
    -[ESP32 ADC](./modules/others/esp32_read_adc.md)
    -[onwire single bus](modules/others/onewire.md)
* More features
  * System
    -[Main frequency, reset, etc.](./course/others/system.md)
    -[Memory Configuration and View](./course/others/mem.md)
  * GUI
    -[Multi-language support including Chinese](./course/image/image_draw_font/image_draw_font.md)
    -[Maix UI](./course/others/maixui.md)
    -[Lvgl](./course/others/lvgl.md)
    -[Editor pye](./course/others/pye.md)
  * The internet
    -[Configure network card](./course/network/network_config.md)
    -[Use socket communication](./course/network/socket_usage.md)
  * Multimedia
    -[audio](./course/media/audio.md)
    -[video](./course/media/video.md)
  * Game
    -[NES game console](./api_reference/media/nes.md)

## API Manual

* [Standard Library](./api_reference/standard/README.md)
  -[cmath](./api_reference/standard/cmath.md)
  -[gc](./api_reference/standard/gc.md)
  -[math](./api_reference/standard/math.md)
  -[sys](./api_reference/standard/sys.md)
  -[ubinascii](./api_reference/standard/ubinascii.md)
  -[ucollections](./api_reference/standard/ucollections.md)
  -[uctypes](./api_reference/standard/uctypes.md)
  -[uerrno](./api_reference/standard/uerrno.md)
  -[uhashlib](./api_reference/standard/uhashlib.md)
  -[uheapq](./api_reference/standard/uheapq.md)
  -[ujson](./api_reference/standard/ujson.md)
  -[uos](./api_reference/standard/uos.md)
  -[ure](./api_reference/standard/ure.md)
  -[usocket](./api_reference/standard/usocket.md)
  -[ustruct](./api_reference/standard/ustruct.md)
  -[utime](./api_reference/standard/utime.md)
  -[uzlib](./api_reference/standard/uzlib.md)
* [machine](./api_reference/machine/README.md)
  -[I2C](./api_reference/machine/i2c.md)
  -[PWM](./api_reference/machine/pwm.md)
  -[SPI](./api_reference/machine/spi.md)
  -[Timer](./api_reference/machine/timer.md)
  -[UART](./api_reference/machine/uart.md)
  -[network](./api_reference/machine/network.md)
  -[WDT](api_reference/machine/wdt.md)
* [Maix](./api_reference/Maix/README.md)
  -[FPIOA](./api_reference/Maix/fpioa.md)
  -[GPIO](./api_reference/Maix/gpio.md)
  -[KPU](./api_reference/Maix/kpu.md)
  -[FFT](./api_reference/Maix/fft.md)
  -[I2S](./api_reference/Maix/i2s.md)
  -[freq](./api_reference/Maix/freq.md)
  -[utils](./api_reference/Maix/utils.md)
* [helper](./api_reference/builtin_py/README.md)
  -[fpioa_manager](./api_reference/builtin_py/fm.md)
  -[board_info](./api_reference/builtin_py/board_info.md)
  -[Micropython Editor](./api_reference/application/pye.md)
* [media](./api_reference/machine_vision/README.md)
  -[lcd](./api_reference/machine_vision/lcd.md)
  -[sensor](./api_reference/machine_vision/sensor.md)
  -[image](api_reference/machine_vision/image/image.md)
  -[video](./api_reference/media/video.md)
  -[audio](./api_reference/media/audio.md)
  -[nes](./api_reference/media/nes.md)
  -[lvgl](./course/others/lvgl.md)
  -[isolated_word](./api_reference/machine_vision/isolated_word.md)
  -[maix_asr](./api_reference/machine_vision/maix_asr.md)
* [extend](./api_reference/extend/README.md)
  -[touchscreen](./api_reference/extend/touchscreen.md)
  -[modules.ultrasonic](./api_reference/extend/ultrasonic.md)
  -[modules.ws2812](./api_reference/extend/ws2812.md)
  -[modules.htpa](./api_reference/extend/htpa.md)
  -[modules.onewire](./api_reference/extend/onewire.md)


## Frequently Asked Questions FAQ

* [MaixPy Frequently Asked Questions FAQ](./others/maixpy_faq.md)
* [MaixHub platform FAQ](./others/maixhub_faq.md)


## Advanced

* Advanced development
  -[Source directory structure](./course/advance/project_framework.md)
  -[How to compile MaixPy project](course/advance/compile.md)
  -[How to add a MaixPy module with C](./course/advance/add_c_module.md)
  -[Packing File System](./course/advance/pack_fs.md)

* Participate in contribution
  -[Participate in document writing (specification)](./contribute/doc_convention.md)
  -[Code Writing Specification](./contribute/code_convention.md)


## Community & Share

-[Featured Articles](./share/recommend_articles.md)
-[Open source project](./share/open_projects.md)
-Everyone's experience sharing
  * [Participation in experience sharing/sharing template](./share/my_share/README.md)
