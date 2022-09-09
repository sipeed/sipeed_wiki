# 源码总览

- [源码总览](#源码总览)
  - [tof_mainpy](#tof_mainpy)
  - [streampy](#streampy)
  - [calvolumespy](#calvolumespy)

## tof_mainpy

```python
from fpioa_manager import fm
from machine import UART
import lcd, image

# lcd.init(invert=True)
lcd.init()
img = image.Image()

fm.register(24, fm.fpioa.UART1_TX, force=True)
fm.register(25, fm.fpioa.UART1_RX, force=True)

uart_A = UART(UART.UART1, 115200, 8, 0, 0, timeout=1000, read_buf_len=4096)

def uart_readBytes():
    return uart_A.read()


def uart_hasData():
    return uart_A.any()


def uart_sendCmd(cmd):
    uart_A.write(cmd)

uart_sendCmd(b"AT+BAUD=5\r")

uart_A.deinit()

uart_A = UART(UART.UART1, 921600, 8, 0, 0, timeout=1000, read_buf_len=4096)

jetcolors = [
    (128, 0, 0), (132, 0, 0), (136, 0, 0), (140, 0, 0), (144, 0, 0), (148, 0, 0), (152, 0, 0), (156, 0, 0), (160, 0, 0), (164, 0, 0), (168, 0, 0), (172, 0, 0), (176, 0, 0), (180, 0, 0), (184, 0, 0), (188, 0, 0), (192, 0, 0), (196, 0, 0), (200, 0, 0), (204, 0, 0), (208, 0, 0), (212, 0, 0), (216, 0, 0), (220, 0, 0), (224, 0, 0), (228, 0, 0), (232, 0, 0), (236, 0, 0), (240, 0, 0), (244, 0, 0), (248, 0, 0), (252, 0, 0), (255, 0, 0), (255, 4, 0), (255, 8, 0), (255, 12, 0), (255, 16, 0), (255, 20, 0), (255, 24, 0), (255, 28, 0), (255, 32, 0), (255, 36, 0), (255, 40, 0), (255, 44, 0), (255, 48, 0), (255, 52, 0), (255, 56, 0), (255, 60, 0), (255, 64, 0), (255, 68, 0), (255, 72, 0), (255, 76, 0), (255, 80, 0), (255, 84, 0), (255, 88, 0), (255, 92, 0), (255, 96, 0), (255, 100, 0), (255, 104, 0), (255, 108, 0), (255, 112, 0), (255, 116, 0), (255, 120, 0), (255, 124, 0), (255, 128, 0), (255, 132, 0), (255, 136, 0), (255, 140, 0), (255, 144, 0), (255, 148, 0), (255, 152, 0), (255, 156, 0), (255, 160, 0), (255, 164, 0), (255, 168, 0), (255, 172, 0), (255, 176, 0), (255, 180, 0), (255, 184, 0), (255, 188, 0), (255, 192, 0), (255, 196, 0), (255, 200, 0), (255, 204, 0), (255, 208, 0), (255, 212, 0), (255, 216, 0), (255, 220, 0), (255, 224, 0), (255, 228, 0), (255, 232, 0), (255, 236, 0), (255, 240, 0), (255, 244, 0), (255, 248, 0), (255, 252, 0), (254, 255, 1), (250, 255, 6), (246, 255, 10), (242, 255, 14), (238, 255, 18), (234, 255, 22), (230, 255, 26), (226, 255, 30), (222, 255, 34), (218, 255, 38), (214, 255, 42), (210, 255, 46), (206, 255, 50), (202, 255, 54), (198, 255, 58), (194, 255, 62), (190, 255, 66), (186, 255, 70), (182, 255, 74), (178, 255, 78), (174, 255, 82), (170, 255, 86), (166, 255, 90), (162, 255, 94), (158, 255, 98), (154, 255, 102), (150, 255, 106), (146, 255, 110), (142, 255, 114), (138, 255, 118), (134, 255, 122), (130, 255, 126),
    (126, 255, 130), (122, 255, 134), (118, 255, 138), (114, 255, 142), (110, 255, 146), (106, 255, 150), (102, 255, 154), (98, 255, 158), (94, 255, 162), (90, 255, 166), (86, 255, 170), (82, 255, 174), (78, 255, 178), (74, 255, 182), (70, 255, 186), (66, 255, 190), (62, 255, 194), (58, 255, 198), (54, 255, 202), (50, 255, 206), (46, 255, 210), (42, 255, 214), (38, 255, 218), (34, 255, 222), (30, 255, 226), (26, 255, 230), (22, 255, 234), (18, 255, 238), (14, 255, 242), (10, 255, 246), (6, 255, 250), (2, 255, 254), (0, 252, 255), (0, 248, 255), (0, 244, 255), (0, 240, 255), (0, 236, 255), (0, 232, 255), (0, 228, 255), (0, 224, 255), (0, 220, 255), (0, 216, 255), (0, 212, 255), (0, 208, 255), (0, 204, 255), (0, 200, 255), (0, 196, 255), (0, 192, 255), (0, 188, 255), (0, 184, 255), (0, 180, 255), (0, 176, 255), (0, 172, 255), (0, 168, 255), (0, 164, 255), (0, 160, 255), (0, 156, 255), (0, 152, 255), (0, 148, 255), (0, 144, 255), (0, 140, 255), (0, 136, 255), (0, 132, 255), (0, 128, 255), (0, 124, 255), (0, 120, 255), (0, 116, 255), (0, 112, 255), (0, 108, 255), (0, 104, 255), (0, 100, 255), (0, 96, 255), (0, 92, 255), (0, 88, 255), (0, 84, 255), (0, 80, 255), (0, 76, 255), (0, 72, 255), (0, 68, 255), (0, 64, 255), (0, 60, 255), (0, 56, 255), (0, 52, 255), (0, 48, 255), (0, 44, 255), (0, 40, 255), (0, 36, 255), (0, 32, 255), (0, 28, 255), (0, 24, 255), (0, 20, 255), (0, 16, 255), (0, 12, 255), (0, 8, 255), (0, 4, 255), (0, 0, 255), (0, 0, 252), (0, 0, 248), (0, 0, 244), (0, 0, 240), (0, 0, 236), (0, 0, 232), (0, 0, 228), (0, 0, 224), (0, 0, 220), (0, 0, 216), (0, 0, 212), (0, 0, 208), (0, 0, 204), (0, 0, 200), (0, 0, 196), (0, 0, 192), (0, 0, 188), (0, 0, 184), (0, 0, 180), (0, 0, 176), (0, 0, 172), (0, 0, 168), (0, 0, 164), (0, 0, 160), (0, 0, 156), (0, 0, 152), (0, 0, 148), (0, 0, 144), (0, 0, 140), (0, 0, 136), (0, 0, 132), (0, 0, 128)
]

def show(frameData, res):
    resR = res[0]
    resC = res[1]
    for y in range(resR):
        for x in range(resC):
            pixel_cmap_rgb = jetcolors[frameData[y*resR + x]]
            img.set_pixel(110 + x, 70 + y, pixel_cmap_rgb)
    lcd.display(img)
    img.clear()

FRAME_HEAD = b"\x00\xFF"
FRAME_TAIL = b"\xCC"

from struct import unpack
# send_cmd("AT+BINN=2\r")
uart_sendCmd(b"AT+DISP=5\r")
uart_sendCmd(b"AT+FPS=10\r")

# while True:
#     if uart_hasData():
#         print(uart_readBytes())

rawData = b''
while True:
    if not uart_hasData():
        continue
    rawData += uart_readBytes()
    idx = rawData.find(FRAME_HEAD)
    if idx < 0:
        continue
    rawData = rawData[idx:]
    # print(rawData)
    # check data length 2Byte
    dataLen = unpack("H", rawData[2: 4])[0]
    # print("len: "+str(dataLen))
    frameLen = len(FRAME_HEAD) + 2 + dataLen + 2
    frameDataLen = dataLen - 16

    if len(rawData) < frameLen:
        continue
    # get data
    frame = rawData[:frameLen]
    # print(frame.hex())
    rawData = rawData[frameLen:]

    frameTail = frame[-1]
    # print("tail: "+str(hex(frameTail)))
    _sum = frame[-2]
    # print("checksum: "+str(hex(_sum)))
    # check sum
    # spi has no checksum but i add one
    if frameTail != 0xdd and _sum != sum(frame[:frameLen - 2]) % 256:
        continue

    frameID = unpack("H", frame[16:18])[0]
    # print("frame ID: "+str(frameID))

    resR = unpack("B", frame[14:15])[0]
    resC = unpack("B", frame[15:16])[0]
    res = (resR, resC)
    # print(res)
    # frameData=[ unpack("H", frame[20+i:22+i])[0] for i in range(0, frameDataLen, 2) ]
    frameData = [unpack("B", frame[20+i:21+i])[0]
                    for i in range(0, frameDataLen, 1)]

    show(frameData, res)

    del frameData
```

## streampy

```python
from PIL import Image
import requests
import matplotlib.pyplot as plt
import struct
import numpy as np
import cv2


def frame_config_decode(frame_config):
    '''
        @frame_config bytes

        @return fields, tuple (trigger_mode, deep_mode, deep_shift, ir_mode, status_mode, status_mask, rgb_mode, rgb_res, expose_time)
    '''
    return struct.unpack("<BBBBBBBBi", frame_config)


def frame_config_encode(trigger_mode=1, deep_mode=1, deep_shift=255, ir_mode=1, status_mode=2, status_mask=7, rgb_mode=1, rgb_res=0, expose_time=0):
    return struct.pack("<BBBBBBBBi",
                       trigger_mode, deep_mode, deep_shift, ir_mode, status_mode, status_mask, rgb_mode, rgb_res, expose_time)


def frame_payload_decode(frame_data: bytes, with_config: tuple):
    deep_data_size, rgb_data_size = struct.unpack("<ii", frame_data[:8])
    frame_payload = frame_data[8:]
    # 0:16bit 1:8bit, resolution: 320*240
    deepth_size = (320*240*2) >> with_config[1]
    deepth_img = struct.unpack("<%us" % deepth_size, frame_payload[:deepth_size])[
        0] if 0 != deepth_size else None
    frame_payload = frame_payload[deepth_size:]

    # 0:16bit 1:8bit, resolution: 320*240
    ir_size = (320*240*2) >> with_config[3]
    ir_img = struct.unpack("<%us" % ir_size, frame_payload[:ir_size])[
        0] if 0 != ir_size else None
    frame_payload = frame_payload[ir_size:]

    status_size = (320*240//8) * (16 if 0 == with_config[4] else
                                  2 if 1 == with_config[4] else 8 if 2 == with_config[4] else 1)
    status_img = struct.unpack("<%us" % status_size, frame_payload[:status_size])[
        0] if 0 != status_size else None
    frame_payload = frame_payload[status_size:]

    assert(deep_data_size == deepth_size+ir_size+status_size)

    rgb_size = len(frame_payload)
    assert(rgb_data_size == rgb_size)
    rgb_img = struct.unpack("<%us" % rgb_size, frame_payload[:rgb_size])[
        0] if 0 != rgb_size else None

    if (not rgb_img is None) and (1 == with_config[6]):
        jpeg = cv2.imdecode(np.frombuffer(
            rgb_img, 'uint8', rgb_size), cv2.IMREAD_COLOR)
        if not jpeg is None:
            rgb = cv2.cvtColor(jpeg, cv2.COLOR_BGR2RGB)
            rgb_img = rgb.tobytes()
        else:
            rgb_img = None

    return (deepth_img, ir_img, status_img, rgb_img)


HOST = '192.168.233.1'
PORT = 80


def post_encode_config(config=frame_config_encode(), host=HOST, port=PORT):
    r = requests.post('http://{}:{}/set_cfg'.format(host, port), config)
    if(r.status_code == requests.codes.ok):
        return True
    return False


def get_frame_from_http(host=HOST, port=PORT):
    r = requests.get('http://{}:{}/getdeep'.format(host, port))
    if(r.status_code == requests.codes.ok):
        # print('Get deep image')
        deepimg = r.content
        # print('Length={}'.format(len(deepimg)))
        (frameid, stamp_msec) = struct.unpack('<QQ', deepimg[0:8+8])
        # print((frameid, stamp_msec/1000))
        return deepimg


def show_frame(fig, frame_data: bytes):
    config = frame_config_decode(frame_data[16:16+12])
    frame_bytes = frame_payload_decode(frame_data[16+12:], config)

    depth = np.frombuffer(frame_bytes[0], 'uint16' if 0 == config[1] else 'uint8').reshape(
        240, 320) if frame_bytes[0] else None

    ir = np.frombuffer(frame_bytes[1], 'uint16' if 0 == config[3] else 'uint8').reshape(
        240, 320) if frame_bytes[1] else None

    status = np.frombuffer(frame_bytes[2], 'uint16' if 0 == config[4] else 'uint8').reshape(
        240, 320) if frame_bytes[2] else None

    rgb = np.frombuffer(frame_bytes[3], 'uint8').reshape(
        (480, 640, 3)) if frame_bytes[3] else None

    ax1 = fig.add_subplot(221)
    if not depth is None:
        # center_dis = depth[240//2, 320//2]
        # if 0 == config[1]:
        #     print("%f mm" % (center_dis/4))
        # else:
        #     print("%f mm" % ((center_dis/5.1) ** 2))
        # depth = depth.copy()

        # l,r= 200,5000
        # depth_f = ((depth.astype('float64') - l) * (65535 / (r - l)))
        # depth_f[np.where(depth_f < 0)] = 0
        # depth_f[np.where(depth_f > 65535)] = 65535

        # depth = depth_f.astype(depth.dtype)

        # depth[240//2, 320//2 - 5:320//2+5] = 0x00
        # depth[240//2-5:240//2+5, 320//2] = 0x00
        ax1.imshow(depth, cmap='jet_r')
    ax2 = fig.add_subplot(222)
    if not ir is None:
        ax2.imshow(ir, cmap='gray')
    ax3 = fig.add_subplot(223)
    if not status is None:
        ax3.imshow(status)
    ax4 = fig.add_subplot(224)
    if not rgb is None:
        ax4.imshow(rgb)


if post_encode_config(frame_config_encode(1, 1, 255, 0, 2, 7, 1, 0, 0)):
    # 打开交互模式
    plt.ion()
    figsize = (12, 12)
    fig = plt.figure('2D frame', figsize=figsize)
    while True:
        p = get_frame_from_http()
        show_frame(fig, p)
        # 停顿时间
        plt.pause(0.001)
        # 清除当前画布
        fig.clf()

    plt.ioff()
```

## calvolumespy

```python
from PIL import Image, ImageDraw
import requests
import matplotlib.pyplot as plt
import struct
import numpy as np
import cv2

HOST = '192.168.233.1'
PORT = 80

def depth2xyz(xp, yp, z, fx, fy, cx, cy, depth_scale=1000):
    # h,w=np.mgrid[0:depth_map.shape[0],0:depth_map.shape[1]]
    z = z/depth_scale
    x = (xp-cx)*z/fx
    y = (yp-cy)*z/fy
    # xyz=np.dstack((x,y,z))
    # xyz=cv2.rgbd.depthTo3d(depth_map,depth_cam_matrix)
    return [x, y, z]


def polygon_area(polygon):
    area = 0
    q = polygon[-1]
    for p in polygon:
        area += p[0] * q[1] - p[1] * q[0]
        q = p
    return abs(area) / 2.0

def get_lenscoeff(host=HOST, port=PORT):
    r = requests.get('http://{}:{}/getinfo'.format(host, port))
    if(r.status_code == requests.codes.ok):
        lenscoeff_bin = r.content
        (_fx,_fy,_cx,_cy) = struct.unpack('<ffff', lenscoeff_bin[41:41+4*4])
        # print((frameid, stamp_msec/1000))
        return (_fx,_fy,_cx,_cy)


diff_low = 30
diff_high = 500
fx = 2.265142e+02
fy = 2.278584e+02
cx = 1.637246e+02  # cx
cy = 1.233738e+02  # cy

(fx,fy,cx,cy) = get_lenscoeff()

def cal_volume(d_bk, d_bg):
    img_h, img_w = d_bk.shape[0], d_bk.shape[1]
    d_bk = d_bk.astype(np.float32)  # cvt to mm
    d_bg = d_bg.astype(np.float32)

    diff = (d_bg-d_bk).astype(np.int16)
    diff1 = diff.copy()
    diff1 = np.where(diff1 < diff_low, 0, diff1)
    diff1 = np.where(diff1 > diff_high, 0, diff1)
    diff1 = (np.where(diff1 > 0, 1, 0)*255).astype(np.uint8)
    # plt.imshow(diff1)

    # print(d_bk.shape) (240, 320)
    output = np.zeros((img_h, img_w, 3), np.uint8)

    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        diff1, connectivity=8)
    # print('num_labels = ',num_labels)
    # 连通域的信息：对应各个轮廓的x、y、width、height和面积
    # print('stats = ',stats)
    res = list()
    max_stats = list()
    for i in range(5):
        max_label = 1+np.argmax(stats[1:, 4])
        # print('stats[max_label] = ', stats[max_label])
        if i > 0 and stats[max_label][4] < 700:
            break
        max_stat = stats[max_label]
        max_stats.append(max_stat)
        stats[max_label][4] = 0

        mask = (labels == max_label)
        # (np.random.rand(3)*255).astype(np.uint8)
        output[:, :, :][mask] = [200, 0, 0]
        # plt.imshow(output)
        
        # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        # eroded = cv2.erode(output, kernel)
        # dilated = cv2.dilate(output, kernel)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        # output = dilated
        output=cv2.morphologyEx(output, cv2.MORPH_OPEN, kernel)
        output=cv2.morphologyEx(output, cv2.MORPH_CLOSE, kernel)


        volumes = []
        # points = []
        # areas = []
        for yp in range(img_h):
            for xp in range(img_w):
                if mask[yp, xp]:
                    x1, y1, z1 = depth2xyz(
                        xp, yp, d_bk[yp, xp], fx, fy, cx, cy, depth_scale=1)
                    x0, y0, z0 = depth2xyz(
                        xp, yp, d_bg[yp, xp], fx, fy, cx, cy, depth_scale=1)

                    x = xp-1
                    if x < 0:
                        x = 0
                    y = yp
                    xl, yl, zl = depth2xyz(
                        x, y, d_bk[y, x], fx, fy, cx, cy, depth_scale=1)
                    x = xp+1
                    if x >= img_w:
                        x = img_w-1
                    y = yp
                    xr, yr, zr = depth2xyz(
                        x, y, d_bk[y, x], fx, fy, cx, cy, depth_scale=1)
                    x = xp
                    y = yp-1
                    if y < 0:
                        y = 0
                    xt, yt, zt = depth2xyz(
                        x, y, d_bk[y, x], fx, fy, cx, cy, depth_scale=1)
                    x = xp
                    y = yp+1
                    if y >= img_h:
                        y = img_h-1
                    xb, yb, zb = depth2xyz(
                        x, y, d_bk[y, x], fx, fy, cx, cy, depth_scale=1)
                    
                    area_a = polygon_area(
                        [[xt, yt], [xl, yl], [xb, yb], [xr, yr]])/2

                    dz = z0-z1
                    dx = z1/fx
                    dy = z1/fy
                    area_b = dx*dy*2/2

                    area = (area_a+area_b)/2  # avg get better acc
                    volume = area*dz
                    # areas.append(area)
                    volumes.append(volume)
                    # points.append((x1, y1, dz))
        # areas = np.array(areas)
        volumes = np.array(volumes)
        # points = np.array(points)

        res.append("{}:{} cm3".format(i, int(np.sum(volumes)/1000)))
        # print(res)

    img_pil = Image.fromarray(output)
    draw = ImageDraw.Draw(img_pil)
    for i in range(len(max_stats)):
        max_stat = max_stats[i]
        draw.rectangle([(max_stat[0], max_stat[1]),
                        (max_stat[0] + max_stat[2], max_stat[1] + max_stat[3])], outline="red")
        draw.text((max_stat[0], max_stat[1]),  res[i], fill=(255, 255, 255))
    output = np.array(img_pil)
    
    return output


def frame_config_decode(frame_config):
    '''
        @frame_config bytes

        @return fields, tuple (trigger_mode, deep_mode, deep_shift, ir_mode, status_mode, status_mask, rgb_mode, rgb_res, expose_time)
    '''
    return struct.unpack("<BBBBBBBBi", frame_config)


def frame_config_encode(trigger_mode=1, deep_mode=1, deep_shift=255, ir_mode=1, status_mode=2, status_mask=7, rgb_mode=1, rgb_res=0, expose_time=0):
    return struct.pack("<BBBBBBBBi",
                       trigger_mode, deep_mode, deep_shift, ir_mode, status_mode, status_mask, rgb_mode, rgb_res, expose_time)


def frame_payload_decode(frame_data: bytes, with_config: tuple):
    deep_data_size, rgb_data_size = struct.unpack("<ii", frame_data[:8])
    frame_payload = frame_data[8:]
    # 0:16bit 1:8bit, resolution: 320*240
    deepth_size = (320*240*2) >> with_config[1]
    deepth_img = struct.unpack("<%us" % deepth_size, frame_payload[:deepth_size])[
        0] if 0 != deepth_size else None
    frame_payload = frame_payload[deepth_size:]

    # 0:16bit 1:8bit, resolution: 320*240
    ir_size = (320*240*2) >> with_config[3]
    ir_img = struct.unpack("<%us" % ir_size, frame_payload[:ir_size])[
        0] if 0 != ir_size else None
    frame_payload = frame_payload[ir_size:]

    status_size = (320*240//8) * (16 if 0 == with_config[4] else
                                  2 if 1 == with_config[4] else 8 if 2 == with_config[4] else 1)
    status_img = struct.unpack("<%us" % status_size, frame_payload[:status_size])[
        0] if 0 != status_size else None
    frame_payload = frame_payload[status_size:]

    assert(deep_data_size == deepth_size+ir_size+status_size)

    rgb_size = len(frame_payload)
    assert(rgb_data_size == rgb_size)
    rgb_img = struct.unpack("<%us" % rgb_size, frame_payload[:rgb_size])[
        0] if 0 != rgb_size else None

    if (not rgb_img is None) and (1 == with_config[6]):
        jpeg = cv2.imdecode(np.frombuffer(
            rgb_img, 'uint8', rgb_size), cv2.IMREAD_COLOR)
        if not jpeg is None:
            rgb = cv2.cvtColor(jpeg, cv2.COLOR_BGR2RGB)
            rgb_img = rgb.tobytes()
        else:
            rgb_img = None

    return (deepth_img, ir_img, status_img, rgb_img)


def post_encode_config(config=frame_config_encode(), host=HOST, port=PORT):
    r = requests.post('http://{}:{}/set_cfg'.format(host, port), config)
    if(r.status_code == requests.codes.ok):
        return True
    return False


def get_frame_from_http(host=HOST, port=PORT):
    r = requests.get('http://{}:{}/getdeep'.format(host, port))
    if(r.status_code == requests.codes.ok):
        # print('Get deep image')
        deepimg = r.content
        # print('Length={}'.format(len(deepimg)))
        (frameid, stamp_msec) = struct.unpack('<QQ', deepimg[0:8+8])
        # print((frameid, stamp_msec/1000))
        return deepimg


def show_frame(fig, frame_data: bytes):
    config = frame_config_decode(frame_data[16:16+12])
    frame_bytes = frame_payload_decode(frame_data[16+12:], config)

    depth = np.frombuffer(frame_bytes[0], 'uint16' if 0 == config[1] else 'uint8').reshape(
        240, 320) if frame_bytes[0] else None

    # ir = np.frombuffer(frame_bytes[1], 'uint16' if 0 == config[3] else 'uint8').reshape(
    #     240, 320) if frame_bytes[1] else None

    # status = np.frombuffer(frame_bytes[2], 'uint16' if 0 == config[4] else 'uint8').reshape(
    #     240, 320) if frame_bytes[2] else None

    rgb = np.frombuffer(frame_bytes[3], 'uint8').reshape(
        (480, 640, 3)) if frame_bytes[3] else None

    ax1 = fig.add_subplot(122)
    if not depth is None:
        # center_dis = depth[240//2, 320//2]
        # if 0 == config[1]:
        #     print("%f mm" % (center_dis/4))
        # else:
        #     print("%f mm" % ((center_dis/5.1) ** 2))
        # depth = depth.copy()

        # l,r= 200,5000
        # depth_f = ((depth.astype('float64') - l) * (65535 / (r - l)))
        # depth_f[np.where(depth_f < 0)] = 0
        # depth_f[np.where(depth_f > 65535)] = 65535

        # depth = depth_f.astype(depth.dtype)

        # depth[240//2, 320//2 - 5:320//2+5] = 0x00
        # depth[240//2-5:240//2+5, 320//2] = 0x00

        if not UPDATE_BG[1] is None:
            ax1.imshow(cal_volume(depth, UPDATE_BG[1]))
        else:
            ax1.imshow(depth)

        if UPDATE_BG[0]:
            UPDATE_BG[1] = depth

    # ax2 = fig.add_subplot(222)
    # if not ir is None:
    #     ax2.imshow(ir, cmap='gray')
    # ax3 = fig.add_subplot(223)
    # if not status is None:
    #     ax3.imshow(status)
    ax4 = fig.add_subplot(121)
    if not rgb is None:
        ax4.imshow(rgb)


UPDATE_BG = [False, None]

if post_encode_config(frame_config_encode(1, 0, 255, 0, 2, 7, 1, 0, 0)):
    # 打开交互模式
    def on_key_press(event):
        if event.key == ' ':
            UPDATE_BG[0] = True
        elif event.key == 'c':
            UPDATE_BG[1] = None

    plt.ion()
    figsize = (12, 12)
    fig = plt.figure('2D frame', figsize=figsize)
    fig.canvas.mpl_connect('key_press_event', on_key_press)

    print("按下空格键更新背景图，按下c键清空背景图")
    while True:
        p = get_frame_from_http()
        show_frame(fig, p)
        if UPDATE_BG[0]:
            UPDATE_BG[0] = False
            print("update bg success!")
        # 停顿时间
        plt.pause(0.001)
        # 清除当前画布
        fig.clf()

    plt.ioff()
```