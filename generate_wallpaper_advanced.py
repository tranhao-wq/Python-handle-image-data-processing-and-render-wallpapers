import numpy as np
from PIL import Image, ImageDraw
import random
import time
import os

# Kích thước hình ảnh
WIDTH, HEIGHT = 1920, 1080

# --- ĐỊNH NGHĨA CÁC CHỦ ĐỀ HÌNH NỀN ---
THEMES = {
    "ocean_waves": {
        "background": (5, 25, 50),
        "palette": [
            (10, 80, 150, 70), (20, 100, 180, 80), (50, 150, 220, 90),
            (100, 200, 255, 60), (30, 120, 200, 75)
        ],
        "param_ranges": {
            "layers": (4, 7),
            "amplitude": (150, 400),
            "frequency": (0.002, 0.006)
        }
    },
    "sunset_dunes": {
        "background": (60, 20, 20),
        "palette": [
            (255, 180, 50, 60), (252, 140, 30, 75), (240, 90, 40, 90),
            (180, 50, 30, 100), (100, 30, 20, 110)
        ],
        "param_ranges": {
            "layers": (3, 6),
            "amplitude": (200, 450),
            "frequency": (0.001, 0.005)
        }
    },
    "aurora_sky": {
        "background": (10, 0, 20),
        "palette": [
            (10, 200, 150, 30), (50, 220, 180, 40), (150, 50, 200, 35),
            (80, 180, 250, 25), (200, 100, 220, 45)
        ],
        "param_ranges": {
            "layers": (5, 9),
            "amplitude": (100, 500),
            "frequency": (0.003, 0.009)
        }
    },
    "monochrome": {
        "background": (10, 10, 10),
        "palette": [
            (200, 200, 200, 20), (150, 150, 150, 30), (100, 100, 100, 40),
            (50, 50, 50, 50), (220, 220, 220, 25)
        ],
        "param_ranges": {
            "layers": (4, 8),
            "amplitude": (200, 400),
            "frequency": (0.002, 0.007)
        }
    }
}

def generate_random_layer(theme_config):
    amplitude = random.uniform(*theme_config["param_ranges"]["amplitude"])
    frequency = random.uniform(*theme_config["param_ranges"]["frequency"])
    phase_shift = random.uniform(0, WIDTH)
    color = random.choice(theme_config["palette"])
    frequency2 = random.uniform(0.01, 0.03)
    amplitude2_ratio = random.uniform(0.1, 0.4)
    return {
        "amplitude": amplitude, "frequency": frequency,
        "amplitude2": amplitude * amplitude2_ratio, "frequency2": frequency2,
        "phase_shift": phase_shift, "color": color
    }

def generate_wallpaper(width, height, theme_name="random", output_dir="output_wallpapers"):
    if theme_name == "random":
        theme_name = random.choice(list(THEMES.keys()))
        print(f"Chế độ ngẫu nhiên đã chọn chủ đề: '{theme_name}'")
    theme_config = THEMES[theme_name]
    image = Image.new("RGB", (width, height), theme_config["background"])
    draw = ImageDraw.Draw(image, "RGBA")
    num_layers = random.randint(*theme_config["param_ranges"]["layers"])
    layers = [generate_random_layer(theme_config) for _ in range(num_layers)]
    for x in range(width):
        for layer in layers:
            y = (height / 2) + \
                layer["amplitude"] * np.sin((x + layer["phase_shift"]) * layer["frequency"]) + \
                layer["amplitude2"] * np.sin((x + layer["phase_shift"]) * layer["frequency2"])
            y0 = min(y, height)
            y1 = max(y, height)
            draw.rectangle([(x, y0), (x + 1, y1)], fill=layer["color"])
    timestamp = int(time.time())
    # Tạo thư mục nếu chưa có
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"wallpaper_{theme_name}_{timestamp}.png")
    image.save(filename)
    print(f"✅ Đã tạo thành công hình nền tại: {filename}")
    image.show()

if __name__ == "__main__":
    print("Chào mừng đến với Trình tạo Hình nền Trừu tượng!")
    print("Đang tự động tạo 10 hình nền ngẫu nhiên...")
    for i in range(10):
        generate_wallpaper(WIDTH, HEIGHT, theme_name="random", output_dir="output_wallpapers")
    print("Đã tạo xong 10 hình nền!") 