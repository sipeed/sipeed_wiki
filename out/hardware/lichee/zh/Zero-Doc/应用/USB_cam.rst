USB摄像头使用
===================================

.. contents:: 本文目录

内核选项
-----------------------------------

插入USB摄像头，lsusb 可见：（摄像头PID:VID视你插入的USB摄像头型号而定）

   ``Bus 001 Device 003: ID 1908:2311 GEMBIRD``

在dev下可见 *video0* 设备。

fswebcam
-----------------------------------

fswebcam可以用来抓取摄像头图片。可以通过apt-get直接安装。

   ``fswebcam -d /dev/video0 --no-banner -r 320x240 capture.jpg``

抓取一帧图片。

:: 

    root@LicheePi:~# fswebcam --help
    Usage: fswebcam [<options>] <filename> [[<options>] <filename> ... ]

    Options:

    -?, --help                   Display this help page and exit.
    -c, --config <filename>      Load configuration from file.
    -q, --quiet                  Hides all messages except for errors.
    -v, --verbose                Displays extra messages while capturing
        --version                Displays the version and exits.
    -l, --loop <seconds>         Run in loop mode.
    -b, --background             Run in the background.
    -o, --output <filename>      Output the log to a file.
    -d, --device <name>          Sets the source to use.
    -i, --input <number/name>    Selects the input to use.
    -t, --tuner <number>         Selects the tuner to use.
    -f, --frequency <number>     Selects the frequency use.
    -p, --palette <name>         Selects the palette format to use.
    -D, --delay <number>         Sets the pre-capture delay time. (seconds)
    -r, --resolution <size>      Sets the capture resolution.
        --fps <framerate>        Sets the capture frame rate.
    -F, --frames <number>        Sets the number of frames to capture.
    -S, --skip <number>          Sets the number of frames to skip.
        --dumpframe <filename>   Dump a raw frame to file.
    -s, --set <name>=<value>     Sets a control value.
        --revert                 Restores original captured image.
        --flip <direction>       Flips the image. (h, v)
        --crop <size>[,<offset>] Crop a part of the image.
        --scale <size>           Scales the image.
        --rotate <angle>         Rotates the image in right angles.
        --deinterlace            Reduces interlace artifacts.
        --invert                 Inverts the images colours.
        --greyscale              Removes colour from the image.
        --swapchannels <c1c2>    Swap channels c1 and c2.
        --no-banner              Hides the banner.
        --top-banner             Puts the banner at the top.
        --bottom-banner          Puts the banner at the bottom. (Default)
        --banner-colour <colour> Sets the banner colour. (#AARRGGBB)
        --line-colour <colour>   Sets the banner line colour.
        --text-colour <colour>   Sets the text colour.
        --font <[name][:size]>   Sets the font and/or size.
        --no-shadow              Disables the text shadow.
        --shadow                 Enables the text shadow.
        --title <text>           Sets the main title. (top left)
        --no-title               Clears the main title.
        --subtitle <text>        Sets the sub-title. (bottom left)
        --no-subtitle            Clears the sub-title.
        --timestamp <format>     Sets the timestamp format. (top right)
        --no-timestamp           Clears the timestamp.
        --gmt                    Use GMT instead of local timezone.
        --info <text>            Sets the info text. (bottom right)
        --no-info                Clears the info text.
        --underlay <PNG image>   Sets the underlay image.
        --no-underlay            Clears the underlay.
        --overlay <PNG image>    Sets the overlay image.
        --no-overlay             Clears the overlay.
        --jpeg <factor>          Outputs a JPEG image. (-1, 0 - 95)
        --png <factor>           Outputs a PNG image. (-1, 0 - 10)
        --save <filename>        Save image to file.
        --exec <command>         Execute a command and wait for it to complete.

mjpeg-streamer
-----------------------------------

前置软件：

.. code-block:: bash

    sudo apt-get update
    sudo apt-get install g++ libjpeg62-turbo-dev imagemagick libv4l-dev cmake git
    sudo git clone https://github.com/jacksonliam/mjpg-streamer.git
    cd mjpg-streamer/mjpg-streamer-experimental
    make all
    sudo make install

设置环境变量

    ``export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib/mjpg-streamer``

开启web服务器

   ``mjpg_streamer -i "input_uvc.so -d /dev/video0 -r 640x480" -o "output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www"``

然后在同个局域网内的电脑的浏览器上访问 zero ip:8080即可看到图像。

.. code-block:: bash

    mjpg_streamer -i "input_uvc.so -f 10 -r 320*240 -y" -o "output_http.so -c "ruoyun:liufeng" -w www -p 8888" -o "output_file.so -d 1000 -f /mnt "  
    -i 输入
    "input_uvc.so -f 10 -r 320*240 -y"
    input_uvc.so：UVC输入组件
    -f  10             ：表示10帧
    -r 320*240     ：分辨率
    -y                   ：YUV格式输入（有卡顿），不加表示MJPG输入（需要摄像头支持）

    -o输出
        "output_http.so -c "ruoyun:liufeng" -w www -p 8888" 
        output_http.so          ：网页输出组件
        -c "ruoyun:liufeng"       ：用户名：ruoyun        密码：liufeng
        -w www                                  : 网页输出
        -p 8888                                   ：端口   8888

        "output_file.so -d 1000 -f /mnt "   
        output_file.so                  ：图片输出组件
        -d 1000                                   ： 时间1S
        -f /mnt                                       ：输出图片放在哪，我是开机直接把/mnu挂载到本地文件夹了

总体帮助

.. code-block:: bash

    root@LicheePi:~# mjpg_streamer --help
    -----------------------------------------------------------------------
    Usage: mjpg_streamer
    -i | --input "<input-plugin.so> [parameters]"
    -o | --output "<output-plugin.so> [parameters]"
    [-h | --help ]........: display this help
    [-v | --version ].....: display version information
    [-b | --background]...: fork to the background, daemon mode
    -----------------------------------------------------------------------
    Example #1:
    To open an UVC webcam "/dev/video1" and stream it via HTTP:
    mjpg_streamer -i "input_uvc.so -d /dev/video1" -o "output_http.so"
    -----------------------------------------------------------------------
    Example #2:
    To open an UVC webcam and stream via HTTP port 8090:
    mjpg_streamer -i "input_uvc.so" -o "output_http.so -p 8090"
    -----------------------------------------------------------------------
    Example #3:
    To get help for a certain input plugin:
    mjpg_streamer -i "input_uvc.so --help"
    -----------------------------------------------------------------------
    In case the modules (=plugins) can not be found:
    * Set the default search path for the modules with:
    export LD_LIBRARY_PATH=/path/to/plugins,
    * or put the plugins into the "/lib/" or "/usr/lib" folder,
    * or instead of just providing the plugin file name, use a complete
    path and filename:
    mjpg_streamer -i "/path/to/modules/input_uvc.so"
    -----------------------------------------------------------------------

输入插件帮助

.. code-block:: bash

    root@LicheePi:~# mjpg_streamer -i "input_uvc.so --help"
    MJPG Streamer Version.: 2.0
    ---------------------------------------------------------------
    Help for input plugin..: UVC webcam grabber
    ---------------------------------------------------------------
    The following parameters can be passed to this plugin:

    [-d | --device ].......: video device to open (your camera)
    [-r | --resolution ]...: the resolution of the video device,
                            can be one of the following strings:
                            QQVGA QCIF CGA QVGA CIF PAL 
                            VGA SVGA XGA HD SXGA UXGA 
                            FHD 
                            or a custom value like the following
                            example: 640x480
    [-f | --fps ]..........: frames per second
                            (activates YUYV format, disables MJPEG)
    [-q | --quality ] .....: set quality of JPEG encoding
    [-m | --minimum_size ].: drop frames smaller then this limit, useful
                            if the webcam produces small-sized garbage frames
                            may happen under low light conditions
    [-e | --every_frame ]..: drop all frames except numbered
    [-n | --no_dynctrl ]...: do not initalize dynctrls of Linux-UVC driver
    [-l | --led ]..........: switch the LED "on", "off", let it "blink" or leave
                            it up to the driver using the value "auto"
    [-t | --tvnorm ] ......: set TV-Norm pal, ntsc or secam
    [-u | --uyvy ] ........: Use UYVY format, default: MJPEG (uses more cpu power)
    [-y | --yuv  ] ........: Use YUV format, default: MJPEG (uses more cpu power)
    [-fourcc ] ............: Use FOURCC codec 'argopt', 
                            currently supported codecs are: RGBP 
    ---------------------------------------------------------------

    Optional parameters (may not be supported by all cameras):

    [-br ].................: Set image brightness (auto or integer)
    [-co ].................: Set image contrast (integer)
    [-sh ].................: Set image sharpness (integer)
    [-sa ].................: Set image saturation (integer)
    [-cb ].................: Set color balance (auto or integer)
    [-wb ].................: Set white balance (auto or integer)
    [-ex ].................: Set exposure (auto, shutter-priority, aperature-priority, or integer)
    [-bk ].................: Set backlight compensation (integer)
    [-rot ]................: Set image rotation (0-359)
    [-hf ].................: Set horizontal flip (true/false)
    [-vf ].................: Set vertical flip (true/false)
    [-pl ].................: Set power line filter (disabled, 50hz, 60hz, auto)
    [-gain ]...............: Set gain (auto or integer)
    [-cagc ]...............: Set chroma gain control (auto or integer)
    ---------------------------------------------------------------

    input_init() return value signals to exit

输出插件帮助

.. code-block:: bash

    root@LicheePi:~# mjpg_streamer -o "output_http.so --help"
    MJPG Streamer Version.: 2.0
    ---------------------------------------------------------------
    Help for output plugin..: HTTP output plugin
    ---------------------------------------------------------------
    The following parameters can be passed to this plugin:

    [-w | --www ]...........: folder that contains webpages in 
                            flat hierarchy (no subfolders)
    [-p | --port ]..........: TCP port for this HTTP server
    [-l ] --listen ]........: Listen on Hostname / IP
    [-c | --credentials ]...: ask for "username:password" on connect
    [-n | --nocommands ]....: disable execution of commands
    ---------------------------------------------------------------
    output_init() return value signals to exit
