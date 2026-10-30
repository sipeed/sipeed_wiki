import mmap
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import time
import requests
import json
from datetime import datetime, timedelta

# Physical screen dimensions
PHYSICAL_WIDTH = 172
PHYSICAL_HEIGHT = 320
BPP = 16

class CryptoChart:
    def __init__(self):
        self.symbols = ['BTC', 'ETH', 'BNB', 'ADA', 'DOT', 'SOL', 'XRP', 'DOGE']
        self.current_symbol_index = 0
        self.price_data = {}
        self.last_update = 0
        self.update_interval = 30  # Update data every 30 seconds
        self.symbol_switch_interval = 1  # Switch symbol every 5 seconds
        
    def fetch_cryptocompare_data(self, symbol='BTC'):
        """Fetch cryptocurrency data from CryptoCompare API"""
        try:
            # Get current price
            price_url = "https://min-api.cryptocompare.com/data/price"
            price_params = {'fsym': symbol, 'tsyms': 'USD'}
            
            response = requests.get(price_url, params=price_params, timeout=10)
            response.raise_for_status()
            price_data = response.json()
            
            current_price = price_data.get('USD', 0)
            
            # Get historical data for chart (last 24 hours)
            hist_url = "https://min-api.cryptocompare.com/data/v2/histohour"
            hist_params = {
                'fsym': symbol,
                'tsym': 'USD',
                'limit': 24,  # Last 24 hours
            }
            
            hist_response = requests.get(hist_url, params=hist_params, timeout=10)
            hist_response.raise_for_status()
            hist_data = hist_response.json()
            
            # Process historical data into OHLC format
            ohlc_data = []
            if hist_data.get('Response') == 'Success':
                for candle in hist_data['Data']['Data']:
                    ohlc_data.append({
                        'time': candle['time'],
                        'open': candle['open'],
                        'high': candle['high'],
                        'low': candle['low'],
                        'close': candle['close'],
                        'volume': candle['volumeto']
                    })
            
            # Calculate 24h price change
            if len(ohlc_data) >= 2:
                first_close = ohlc_data[0]['close']
                price_change = current_price - first_close
                change_percent = (price_change / first_close) * 100
            else:
                price_change = 0
                change_percent = 0
            
            return {
                'symbol': symbol,
                'price': current_price,
                'change': price_change,
                'change_percent': change_percent,
                'ohlc': ohlc_data,
                'timeframe': '24H'
            }
            
        except Exception as e:
            print(f"Error fetching CryptoCompare data for {symbol}: {e}")
            return None
    
    def fetch_simple_price(self, symbol='BTC'):
        """Simple price fetch when historical data fails"""
        try:
            url = "https://min-api.cryptocompare.com/data/price"
            params = {'fsym': symbol, 'tsyms': 'USD'}
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            current_price = data.get('USD', 0)
            
            # Generate simple mock chart data based on current price
            ohlc_data = []
            base_price = current_price
            for i in range(24):
                change = (i - 12) * 0.01  # Create a simple trend
                price = base_price * (1 + change * 0.02)
                ohlc_data.append({
                    'time': int(time.time()) - (24 - i) * 3600,
                    'open': price * 0.99,
                    'high': price * 1.01,
                    'low': price * 0.98,
                    'close': price,
                    'volume': 1000000
                })
            
            return {
                'symbol': symbol,
                'price': current_price,
                'change': 0,  # Unknown without historical data
                'change_percent': 0,
                'ohlc': ohlc_data,
                'timeframe': '24H'
            }
            
        except Exception as e:
            print(f"Error fetching simple price for {symbol}: {e}")
            return None
    
    def get_current_symbol(self):
        """Get current symbol and auto-switch every 5 seconds"""
        return self.symbols[self.current_symbol_index]
    
    def switch_to_next_symbol(self):
        """Switch to next symbol"""
        self.current_symbol_index = (self.current_symbol_index + 1) % len(self.symbols)
        return self.get_current_symbol()
    
    def get_current_data(self):
        """Get current cryptocurrency data"""
        current_time = time.time()
        current_symbol = self.get_current_symbol()
        
        # Update data if needed (every 30 seconds or if no data for this symbol)
        if (current_time - self.last_update > self.update_interval or 
            current_symbol not in self.price_data):
            
            print(f"Fetching data for {current_symbol}...")
            
            # Try full data first
            data = self.fetch_cryptocompare_data(current_symbol)
            if not data:
                # Fallback to simple price
                data = self.fetch_simple_price(current_symbol)
            
            if data:
                self.price_data[current_symbol] = data
                self.last_update = current_time
                print(f"Successfully fetched {current_symbol}: ${data['price']:.2f}")
            else:
                print(f"Failed to fetch data for {current_symbol}")
        
        return self.price_data.get(current_symbol)

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
    
    def draw_loading_screen(self, message="Fetching Data", current_symbol=None):
        """Display loading screen while fetching data"""
        logical_img = Image.new('RGB', (320, 172), (15, 15, 30))  # Dark blue background
        draw = ImageDraw.Draw(logical_img)
        
        try:
            font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
            font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
            font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
        except:
            font_large = font_medium = font_small = ImageFont.load_default()
        
        # Draw loading message
        text_width = draw.textlength(message, font=font_large)
        text_x = (320 - text_width) // 2
        draw.text((text_x, 60), message, fill=(100, 200, 255), font=font_large)
        
        # Draw current symbol if provided
        if current_symbol:
            symbol_text = f"Symbol: {current_symbol}"
            symbol_width = draw.textlength(symbol_text, font=font_medium)
            symbol_x = (320 - symbol_width) // 2
            draw.text((symbol_x, 90), symbol_text, fill=(200, 200, 200), font=font_medium)
        
        # Draw loading animation dots
        dot_time = int(time.time() * 2) % 4
        dots = "." * dot_time
        dots_width = draw.textlength(dots, font=font_large)
        dots_x = text_x + text_width + 5
        draw.text((dots_x, 60), dots, fill=(100, 200, 255), font=font_large)
        
        # Draw info text
        draw.text((80, 120), "Crypto Price Monitor", fill=(150, 150, 200), font=font_medium)
        draw.text((100, 140), "Auto-switch: 5s", fill=(120, 120, 160), font=font_small)
        
        self._display_image(logical_img)
    
    def draw_candlestick_chart(self, chart_data, symbol_index=0, total_symbols=8):
        """Draw candlestick chart with price information"""
        if not chart_data or 'ohlc' not in chart_data or len(chart_data['ohlc']) == 0:
            return self.draw_error_message("No data available")
        
        # Create logical size image (landscape 320x172)
        logical_img = Image.new('RGB', (320, 172), (10, 10, 20))  # Dark blue background
        draw = ImageDraw.Draw(logical_img)
        
        try:
            font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
            font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
            font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
        except:
            font_small = font_medium = font_large = ImageFont.load_default()
        
        ohlc_data = chart_data['ohlc']
        symbol = chart_data['symbol']
        current_price = chart_data['price']
        change = chart_data['change']
        change_percent = chart_data['change_percent']
        timeframe = chart_data.get('timeframe', '24H')
        
        # Calculate chart dimensions
        chart_top = 40
        chart_bottom = 140
        chart_height = chart_bottom - chart_top
        chart_left = 20
        chart_right = 300
        chart_width = chart_right - chart_left
        
        # Find price range for scaling
        all_prices = []
        for candle in ohlc_data:
            all_prices.extend([candle['high'], candle['low']])
        
        max_price = max(all_prices)
        min_price = min(all_prices)
        price_range = max_price - min_price
        
        # Add some padding to price range
        if price_range == 0:
            price_range = max_price * 0.1  # 10% range if no variation
        max_price += price_range * 0.1
        min_price -= price_range * 0.1
        price_range = max_price - min_price
        
        # Draw chart title and info
        title_color = (255, 255, 255)
        draw.text((10, 5), f"{symbol}/USD", fill=title_color, font=font_large)
        
        # Draw symbol counter
        counter_text = f"{symbol_index + 1}/{total_symbols}"
        counter_width = draw.textlength(counter_text, font=font_small)
        draw.text((320 - counter_width - 10, 5), counter_text, fill=(150, 150, 200), font=font_small)
        
        # Draw current price and change
        price_color = (0, 255, 0) if change >= 0 else (255, 50, 50)
        price_text = f"${current_price:,.2f}"
        change_text = f"{change:+.2f} ({change_percent:+.1f}%)"
        
        price_width = draw.textlength(price_text, font=font_medium)
        draw.text((320 - price_width - 10, 25), price_text, fill=price_color, font=font_medium)
        
        change_width = draw.textlength(change_text, font=font_small)
        draw.text((320 - change_width - 10, 45), change_text, fill=price_color, font=font_small)
        
        # Draw price scale
        scale_steps = 3
        for i in range(scale_steps + 1):
            price_val = min_price + (price_range * i / scale_steps)
            y_pos = chart_bottom - (chart_height * i / scale_steps)
            price_str = f"${price_val:,.0f}"
            draw.text((5, y_pos - 6), price_str, fill=(150, 150, 150), font=font_small)
            draw.line([(chart_left, y_pos), (chart_right, y_pos)], fill=(50, 50, 70), width=1)
        
        # Draw candlesticks
        candle_count = len(ohlc_data)
        candle_width = max(2, chart_width // candle_count - 1)
        
        for i, candle in enumerate(ohlc_data):
            x_center = chart_left + (i * chart_width // candle_count) + (chart_width // candle_count) // 2
            
            # Calculate y positions
            open_y = chart_bottom - int(((candle['open'] - min_price) / price_range) * chart_height)
            close_y = chart_bottom - int(((candle['close'] - min_price) / price_range) * chart_height)
            high_y = chart_bottom - int(((candle['high'] - min_price) / price_range) * chart_height)
            low_y = chart_bottom - int(((candle['low'] - min_price) / price_range) * chart_height)
            
            # Determine candle color (green for up, red for down)
            is_green = candle['close'] >= candle['open']
            candle_color = (0, 255, 100) if is_green else (255, 80, 80)
            
            # Draw high-low line
            draw.line([(x_center, high_y), (x_center, low_y)], fill=candle_color, width=1)
            
            # Draw candle body
            body_top = min(open_y, close_y)
            body_bottom = max(open_y, close_y)
            body_height = max(1, body_bottom - body_top)
            
            if body_height > 0:
                draw.rectangle([
                    (x_center - candle_width//2, body_top),
                    (x_center + candle_width//2, body_bottom)
                ], fill=candle_color)
        
        # Draw footer info
        draw.text((10, 150), "Data: CryptoCompare", fill=(180, 180, 180), font=font_small)
        draw.text((10, 160), f"Switch: 5s | Update: 30s", fill=(180, 180, 180), font=font_small)
        
        # Rotate and display
        self._display_image(logical_img)
    
    def draw_error_message(self, message):
        """Display error message"""
        logical_img = Image.new('RGB', (320, 172), (20, 10, 10))  # Dark red background
        draw = ImageDraw.Draw(logical_img)
        
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
        except:
            font = ImageFont.load_default()
        
        text_width = draw.textlength(message, font=font)
        text_x = (320 - text_width) // 2
        draw.text((text_x, 80), message, fill=(255, 100, 100), font=font)
        draw.text((120, 110), "Retrying...", fill=(200, 200, 200), font=font)
        
        self._display_image(logical_img)
    
    def _display_image(self, logical_img):
        """Rotate and display image on physical screen"""
        # Rotate logical image 90 degrees counterclockwise
        physical_img = logical_img.rotate(90, expand=True)
        
        # Convert to RGB565
        rgb_array = np.array(physical_img)
        r = (rgb_array[:,:,0] >> 3).astype(np.uint16)
        g = (rgb_array[:,:,1] >> 2).astype(np.uint16)
        b = (rgb_array[:,:,2] >> 3).astype(np.uint16)
        rgb565 = (r << 11) | (g << 5) | b
        
        # Copy to framebuffer
        self.fb_array[:,:] = rgb565
    
    def close(self):
        """Close resources"""
        self.fb_mmap.close()
        os.close(self.fb_fd)

def main():
    display = RGB565Display()
    chart = CryptoChart()
    
    print("Cryptocurrency Chart Display Started!")
    print("Supported symbols:", chart.symbols)
    print("Auto-switch: 5 seconds")
    print("Data update: 30 seconds")
    print("Data source: CryptoCompare API")
    
    last_switch_time = time.time()
    last_symbol_index = -1
    
    try:
        while True:
            current_time = time.time()
            current_symbol = chart.get_current_symbol()
            
            # Show loading screen when switching to new symbol or fetching data
            if chart.current_symbol_index != last_symbol_index:
                #display.draw_loading_screen("Fetching Data", current_symbol)
                last_symbol_index = chart.current_symbol_index
            
            # Get current data
            data = chart.get_current_data()
            
            if data:
                # Display chart
                display.draw_candlestick_chart(data, chart.current_symbol_index, len(chart.symbols))
                print(f"Displaying {data['symbol']} - Price: ${data['price']:.2f}")
            else:
                display.draw_error_message(f"Failed: {current_symbol}")
                print(f"Failed to fetch data for {current_symbol}")
            
            # Switch to next symbol every 5 seconds
            if current_time - last_switch_time >= chart.symbol_switch_interval:
                next_symbol = chart.switch_to_next_symbol()
                print(f"Switching to: {next_symbol}")
                last_switch_time = current_time
            
            # Wait before next update
            time.sleep(0.5)  # Short sleep for responsive UI
            
    except KeyboardInterrupt:
        print("\nChart display stopped")
    finally:
        display.close()

if __name__ == "__main__":
    main()
