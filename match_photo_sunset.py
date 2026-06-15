import os
import glob
from PIL import Image

screenshot_path = '/home/gregory/.gemini/antigravity-ide/brain/7e774966-6f64-4ea6-bde9-b91165bded85/media__1781528879696.png'
galerie_dir = 'site/img/galerie'

try:
    with Image.open(screenshot_path) as s_img:
        s_img = s_img.convert("RGB").resize((16, 16))
        s_pixels = list(s_img.getdata())
except Exception as e:
    print("Error opening screenshot:", e)
    exit(1)

best_match = None
min_diff = float('inf')

for img_path in glob.glob(os.path.join(galerie_dir, '*.webp')):
    try:
        with Image.open(img_path) as img:
            img = img.convert("RGB").resize((16, 16))
            pixels = list(img.getdata())
            
            diff = sum(abs(s[0]-p[0]) + abs(s[1]-p[1]) + abs(s[2]-p[2]) for s, p in zip(s_pixels, pixels))
            
            if diff < min_diff:
                min_diff = diff
                best_match = img_path
    except Exception as e:
        pass

print(f"Best match for sunset boat: {best_match} with diff {min_diff}")
