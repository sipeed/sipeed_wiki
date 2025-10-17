"""
Usage: 
Open a browser or KVM software on the local machine, open the remote desktop, 
and keep the upper-left part of the remote desktop as a light-colored static background (e.g., desktop or Notepad). 
Make sure to confirm that the POS1 & POS2 positions are light-colored. 
Then, run the script, and it will automatically perform round times of mouse movement delay tests, 
plot a chart, and record the delay data to an .npy file.

使用方法：在本机上打开浏览器或者kvm软件，打开远程桌面，
并保持远程桌面左上部分为浅色静态背景(如桌面或者记事本), 
注意确认pos1&pos2位置为浅色。
然后运行脚本，就会自动执行round次鼠标移动延迟测试，绘制图表和记录延迟数据到npy.
"""

import time
import numpy as np
import cv2, sys
import pyautogui
from mss import mss
import matplotlib
matplotlib.use('Agg')  # 非 GUI 后端
import matplotlib.pyplot as plt


if len(sys.argv) < 2:
    print("Usage: python lat_mouse.py rounds pic_name")
    sys.exit(1)

# -------------------------------
# configs
# -------------------------------
# two mouse position
pos1 = (200, 500)
pos2 = (300, 500)

# mouse region size
region_size = 10

# test counts
rounds = int(sys.argv[1]) 
# histogram pic save prefix
pic_name = sys.argv[2]

# screen capture tool
sct = mss()

# -------------------------------
# tool func
# -------------------------------
def grab_region(center):
    """mouse pos is left upper corner of region"""
    x, y = center
    region = {
        "top": y ,
        "left": x ,
        "width": region_size,
        "height": region_size,
    }
    img = np.array(sct.grab(region))
    gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    #return cv2.mean(gray)[0]
    return gray, time.time()  #cv2.mean(gray)[0]

def wait_for_change(patch0, center, threshold=1.0):
    """wait for region changes (mouse position update) , return timestamp"""
    gray0 = cv2.mean(patch0)[0]
    while True:
        patch1, t1 = grab_region(center)
        #print(before, after)
        diff = abs(gray0-cv2.mean(patch1)[0]) #cv2.absdiff(before, after)
        if np.mean(diff) > threshold:
            return patch1, t1

def save_report(latencies, pic_name):
    mid_latency = np.median(latencies)
    if len(latencies) < 2:
        print("Error: Not enough data to create plots.")
        return

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
    
    # Draw a histogram
    ax1.hist(latencies, bins=20, color='skyblue', edgecolor='black')
    ax1.set_xlabel('Latency (ms)')
    ax1.set_ylabel('Frequency')
    ax1.set_title(f'End-to-End Latency Distribution (Avg: {mid_latency:.2f} ms)')

    # Draw a line chart
    x = np.arange(0, len(latencies), 1)
    ax2.plot(x, latencies, marker='o', linestyle='-', color='blue')
    ax2.set_xlabel('Sample Index')
    ax2.set_ylabel('Latency (ms)')
    ax2.set_title('Latency over Time')
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig(pic_name+"_%dms.png"%(round(mid_latency)))
    print(f"Plot saved successfully to {pic_name}")
    return 


# -------------------------------
# main loop
# -------------------------------
def measure_latency():
    latencies = np.zeros(rounds)
    current_pos = pos1

    pyautogui.moveTo(current_pos[0], current_pos[1], duration=0)
    time.sleep(0.3)

    for i in range(rounds):
        next_pos = pos2 if current_pos == pos1 else pos1
        patch0, t0 = grab_region(current_pos)
        pyautogui.moveTo(next_pos[0], next_pos[1], duration=0)
        t1 = time.time()
        patch1, t2 = wait_for_change(patch0, current_pos)
        latency = (t2 - t0) * 1000  # ms
        latencies[i] = latency
        print("%d: %.2f ms"%(i+1, latency), end="\n", flush=True)
        current_pos = next_pos
        time.sleep(0.1)

    # cal avg
    mid_latency = np.median(latencies) 
    lat_le100_cnt=len(latencies[latencies <= 100])
    lat_100150_cnt=len(latencies[(latencies > 100) & (latencies <=150)])
    lat_150200_cnt=len(latencies[(latencies > 150) & (latencies <=200)])
    lat_200300_cnt=len(latencies[(latencies > 200) & (latencies <=300)])
    lat_gt300_cnt=len(latencies[latencies >300])
    lat_le100_rate=lat_le100_cnt/len(latencies)
    lat_100150_rate=lat_100150_cnt/len(latencies)
    lat_150200_rate=lat_150200_cnt/len(latencies)
    lat_200300_rate=lat_200300_cnt/len(latencies)
    lat_gt300_rate=lat_gt300_cnt/len(latencies)

    print("%d: %dms, <100:100~150:150~200:200~300:>300(ms) = %.2f:%.2f:%.2f:%.2f:%.2f"%\
        (rounds, round(mid_latency), lat_le100_rate, lat_100150_rate, lat_150200_rate, lat_200300_rate, lat_gt300_rate))
    print(f"\nMedian: {mid_latency:.2f} ms")
    save_report(latencies, pic_name)
    np.save(pic_name+".npy", np.array(latencies))


if __name__ == "__main__":
    measure_latency()
