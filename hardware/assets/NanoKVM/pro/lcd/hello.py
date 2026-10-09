import mmap
import struct
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 物理屏幕尺寸
PHYSICAL_WIDTH = 172
PHYSICAL_HEIGHT = 320
BPP = 16

class RGB565Display:
    def __init__(self, fb_device="/dev/fb0"):
        self.physical_width = PHYSICAL_WIDTH
        self.physical_height = PHYSICAL_HEIGHT
        self.bpp = BPP
        self.fb_size = self.physical_width * self.physical_height * (self.bpp // 8)
        
        # 打开framebuffer设备
        self.fb_fd = os.open(fb_device, os.O_RDWR)
        self.fb_mmap = mmap.mmap(self.fb_fd, self.fb_size, mmap.MAP_SHARED, mmap.PROT_WRITE)
        self.fb_array = np.frombuffer(self.fb_mmap, dtype=np.uint16).reshape((self.physical_height, self.physical_width))
        
    def rgb_to_rgb565(self, r, g, b):
        return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
    
    def clear_screen(self, color=0x0000):
        self.fb_array.fill(color)
    
    def draw_rotated_content(self):
        """直接在物理屏幕上绘制旋转后的内容"""
        # 创建一个临时的逻辑尺寸图像（横屏320x172）
        logical_img = Image.new('RGB', (320, 172), (0, 0, 0))
        draw = ImageDraw.Draw(logical_img)
        
        # 加载字体
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
        except:
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.ttf", 28)
            except:
                font = ImageFont.load_default()
        
        # 1. 绘制彩色方块
        block_size = 30
        spacing = 10
        total_width = 3 * block_size + 2 * spacing
        start_x = (320 - total_width) // 2
        y_blocks = 20
        
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        for i, color in enumerate(colors):
            x = start_x + i * (block_size + spacing)
            draw.rectangle([x, y_blocks, x + block_size, y_blocks + block_size], fill=color)
        
        # 2. 绘制居中文字
        text = "Hello World"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x_text = (320 - text_width) // 2
        y_text = (172 - text_height) // 2
        draw.text((x_text, y_text), text, fill=(255, 255, 255), font=font)
        
        # 3. 将逻辑图像逆时针旋转90度得到物理图像
        physical_img = logical_img.rotate(90, expand=True)
        
        # 4. 转换为RGB565并直接复制到framebuffer
        rgb_array = np.array(physical_img)
        r = (rgb_array[:,:,0] >> 3).astype(np.uint16)
        g = (rgb_array[:,:,1] >> 2).astype(np.uint16)
        b = (rgb_array[:,:,2] >> 3).astype(np.uint16)
        rgb565 = (r << 11) | (g << 5) | b
        
        # 直接复制整个数组（最快的方法）
        self.fb_array[:,:] = rgb565
    
    def close(self):
        self.fb_mmap.close()
        os.close(self.fb_fd)

def main():
    display = RGB565Display()
    try:
        display.clear_screen(0x0000)
        print("开始绘制...")
        display.draw_rotated_content()
        print("绘制完成！")
        
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n退出")
    finally:
        display.close()

if __name__ == "__main__":
    main()
