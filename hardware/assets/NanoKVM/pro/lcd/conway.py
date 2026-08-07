import mmap
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import time
import random

# Physical screen dimensions
PHYSICAL_WIDTH = 172
PHYSICAL_HEIGHT = 320
BPP = 16

class GameOfLife:
    def __init__(self, width=80, height=43):  # Reduced grid size to fit screen
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=bool)
        self.generation = 0
        
    def random_grid(self, density=0.3):
        """Initialize grid with random cells"""
        self.grid = np.random.random((self.height, self.width)) < density
        
    def clear_grid(self):
        """Clear all cells from grid"""
        self.grid.fill(False)
        
    def add_glider(self, x, y):
        """Add glider pattern"""
        pattern = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
        ]
        self._add_pattern(x, y, pattern)
        
    def add_lightweight_spaceship(self, x, y):
        """Add lightweight spaceship pattern"""
        pattern = [
            [0, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [0, 0, 0, 0, 1],
            [1, 0, 0, 1, 0]
        ]
        self._add_pattern(x, y, pattern)
        
    def add_pulsar(self, x, y):
        """Add pulsar oscillator pattern"""
        pattern = [
            [0,0,1,1,1,0,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [0,0,1,1,1,0,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,0,0,0,1,1,1,0,0],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,0,0,0,1,1,1,0,0]
        ]
        self._add_pattern(x, y, pattern)
        
    def add_glider_gun(self, x, y):
        """Add Gosper glider gun pattern"""
        pattern = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
            [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]
        self._add_pattern(x, y, pattern)
        
    def add_beacon(self, x, y):
        """Add beacon oscillator pattern"""
        pattern = [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1]
        ]
        self._add_pattern(x, y, pattern)
        
    def _add_pattern(self, x, y, pattern):
        """Add pattern to grid at specified position"""
        for i, row in enumerate(pattern):
            for j, cell in enumerate(row):
                if (0 <= y+i < self.height and 0 <= x+j < self.width and cell == 1):
                    self.grid[y+i, x+j] = True
                    
    def next_generation(self):
        """Calculate next generation using Conway's Game of Life rules"""
        # Count neighbors for each cell
        neighbors = np.zeros((self.height, self.width))
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                # Use modulo for toroidal boundary conditions
                neighbors += np.roll(np.roll(self.grid, i, axis=0), j, axis=1)
        
        # Apply Conway's Game of Life rules
        new_grid = np.zeros((self.height, self.width), dtype=bool)
        # Rule 1: Live cells with 2 or 3 neighbors survive
        new_grid[(self.grid == 1) & ((neighbors == 2) | (neighbors == 3))] = True
        # Rule 2: Dead cells with exactly 3 neighbors become alive
        new_grid[(self.grid == 0) & (neighbors == 3)] = True
        
        self.grid = new_grid
        self.generation += 1
        
    def get_patterns(self):
        """Return available pattern types"""
        return {
            "random": "Random",
            "glider": "Glider", 
            "spaceship": "Spaceship",
            "pulsar": "Pulsar",
            "glider_gun": "Glider Gun",
            "beacon": "Beacon"
        }

class RGB565Display:
    def __init__(self, fb_device="/dev/fb0"):
        self.physical_width = PHYSICAL_WIDTH
        self.physical_height = PHYSICAL_HEIGHT
        self.bpp = BPP
        self.fb_size = self.physical_width * self.physical_height * (self.bpp // 8)
        
        # Open framebuffer device
        self.fb_fd = os.open(fb_device, os.O_RDWR)
        self.fb_mmap = mmap.mmap(self.fb_fd, self.fb_size, mmap.MAP_SHARED, mmap.PROT_WRITE)
        self.fb_array = np.frombuffer(self.fb_mmap, dtype=np.uint16).reshape((self.physical_height, self.physical_width))
        
    def rgb_to_rgb565(self, r, g, b):
        """Convert 8-bit RGB to RGB565 format"""
        return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
    
    def clear_screen(self, color=0x0000):
        """Clear screen with specified color"""
        self.fb_array.fill(color)
    
    def draw_game_frame(self, game, current_pattern, show_info=True):
        """Draw current game frame with rotation"""
        # Create logical size image (landscape 320x172)
        logical_img = Image.new('RGB', (320, 172), (0, 0, 0))
        draw = ImageDraw.Draw(logical_img)
        
        # Calculate cell size and position for centering
        cell_size = 3
        margin_x = (320 - game.width * cell_size) // 2
        margin_y = (172 - game.height * cell_size) // 2
        
        # Draw grid background
        grid_color = (20, 20, 40)  # Dark blue grid
        for i in range(game.height + 1):
            y = margin_y + i * cell_size
            draw.line([(margin_x, y), (margin_x + game.width * cell_size, y)], fill=grid_color)
        for j in range(game.width + 1):
            x = margin_x + j * cell_size
            draw.line([(x, margin_y), (x, margin_y + game.height * cell_size)], fill=grid_color)
        
        # Draw live cells
        live_color = (0, 255, 128)  # Cyan-green
        for i in range(game.height):
            for j in range(game.width):
                if game.grid[i, j]:
                    x1 = margin_x + j * cell_size + 1
                    y1 = margin_y + i * cell_size + 1
                    x2 = x1 + cell_size - 2
                    y2 = y1 + cell_size - 2
                    draw.rectangle([x1, y1, x2, y2], fill=live_color)
        
        # Display information text
        if show_info:
            try:
                font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
                font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
            except:
                font_small = font_large = ImageFont.load_default()
            
            info_color = (200, 200, 200)  # Light gray
            info_text = [
                f"Generation: {game.generation}",
                f"Live Cells: {np.sum(game.grid)}",
                f"Pattern: {current_pattern}"
            ]
            
            for idx, text in enumerate(info_text):
                draw.text((10, 10 + idx * 15), text, fill=info_color, font=font_small)
        
        # Rotate logical image 90 degrees counterclockwise for physical display
        physical_img = logical_img.rotate(90, expand=True)
        
        # Convert to RGB565 and copy to framebuffer
        rgb_array = np.array(physical_img)
        r = (rgb_array[:,:,0] >> 3).astype(np.uint16)
        g = (rgb_array[:,:,1] >> 2).astype(np.uint16)
        b = (rgb_array[:,:,2] >> 3).astype(np.uint16)
        rgb565 = (r << 11) | (g << 5) | b
        
        # Direct array copy (fastest method)
        self.fb_array[:,:] = rgb565
    
    def close(self):
        """Close resources"""
        self.fb_mmap.close()
        os.close(self.fb_fd)

def main():
    display = RGB565Display()
    game = GameOfLife()
    
    # Available patterns
    patterns = game.get_patterns()
    pattern_names = list(patterns.keys())
    current_pattern_index = 0
    
    try:
        # Initialize with first pattern
        current_pattern = pattern_names[current_pattern_index]
        pattern_display_name = patterns[current_pattern]
        print(f"Initial pattern: {pattern_display_name}")
        
        # Set up initial pattern
        if current_pattern == "random":
            game.random_grid(0.2)
        elif current_pattern == "glider":
            game.add_glider(10, 10)
        elif current_pattern == "spaceship":
            game.add_lightweight_spaceship(5, 5)
        elif current_pattern == "pulsar":
            game.add_pulsar(10, 10)
        elif current_pattern == "glider_gun":
            game.add_glider_gun(5, 5)
        elif current_pattern == "beacon":
            game.add_beacon(15, 15)
        
        print("Conway's Game of Life Started!")
        print("Press Ctrl+C to exit")
        print("Available patterns:", list(patterns.values()))
        
        frame_count = 0
        last_time = time.time()
        
        while True:
            # Switch pattern every 100 generations
            if game.generation % 100 == 0 and game.generation > 0:
                current_pattern_index = (current_pattern_index + 1) % len(pattern_names)
                current_pattern = pattern_names[current_pattern_index]
                pattern_display_name = patterns[current_pattern]
                game.clear_grid()
                game.generation = 0
                
                # Set up new pattern
                if current_pattern == "random":
                    game.random_grid(0.2)
                elif current_pattern == "glider":
                    game.add_glider(10, 10)
                elif current_pattern == "spaceship":
                    game.add_lightweight_spaceship(5, 5)
                elif current_pattern == "pulsar":
                    game.add_pulsar(10, 10)
                elif current_pattern == "glider_gun":
                    game.add_glider_gun(5, 5)
                elif current_pattern == "beacon":
                    game.add_beacon(15, 15)
                
                print(f"Switched to pattern: {pattern_display_name}")
            
            # Draw current frame
            display.draw_game_frame(game, pattern_display_name)
            
            # Calculate next generation
            game.next_generation()
            
            # Calculate FPS
            frame_count += 1
            if frame_count % 30 == 0:
                current_time = time.time()
                fps = 30 / (current_time - last_time)
                last_time = current_time
                print(f"Generation: {game.generation}, FPS: {fps:.1f}")
            
            # Control animation speed
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\nGame Ended")
    finally:
        display.close()

if __name__ == "__main__":
    main()
