import os
import glob
from PIL import Image

galerie_dir = 'site/img/galerie'
candidates = []

for img_path in glob.glob(os.path.join(galerie_dir, '*.webp')):
    try:
        with Image.open(img_path) as img:
            img = img.convert("RGB")
            # Resize to a very small image to get average colors quickly
            small = img.resize((50, 50))
            pixels = list(small.getdata())
            
            # Count pixels that are "dark blue" (blue > red + 30, blue > green + 30)
            blue_count = 0
            wood_count = 0 # brown/orange (red > green > blue)
            for r, g, b in pixels:
                if b > r + 30 and b > g + 30 and b > 50:
                    blue_count += 1
                if r > g + 20 and g > b + 20 and r > 100:
                    wood_count += 1
                    
            blue_ratio = blue_count / 2500
            wood_ratio = wood_count / 2500
            
            if blue_ratio > 0.05 and wood_ratio > 0.05:
                candidates.append((img_path, blue_ratio, wood_ratio))
    except Exception as e:
        pass

candidates.sort(key=lambda x: x[1]*x[2], reverse=True)
for c in candidates:
    print(f"{os.path.basename(c[0])} - Blue: {c[1]:.2f}, Wood: {c[2]:.2f}")
