import os
import glob
from PIL import Image

img_dir = '/home/gregory/Voilier/site/img'
images = glob.glob(os.path.join(img_dir, '*.png')) + glob.glob(os.path.join(img_dir, '*.jpg')) + glob.glob(os.path.join(img_dir, '*.jpeg')) + glob.glob(os.path.join(img_dir, '*.JPEG'))

count = 0
saved_bytes = 0

for img_path in images:
    size = os.path.getsize(img_path)
    if size > 300_000: # only optimize images larger than 300KB
        try:
            with Image.open(img_path) as img:
                original_format = img.format
                changed = False
                
                # Resize if width > 1920
                if img.width > 1920:
                    ratio = 1920 / img.width
                    new_size = (1920, int(img.height * ratio))
                    img = img.resize(new_size, Image.Resampling.LANCZOS)
                    changed = True
                
                # PNG handling
                if img_path.lower().endswith('.png'):
                    if 'logo' in img_path.lower() and img.width > 800:
                        ratio = 800 / img.width
                        new_size = (800, int(img.height * ratio))
                        img = img.resize(new_size, Image.Resampling.LANCZOS)
                    img.save(img_path, format='PNG', optimize=True)
                # JPEG handling
                else:
                    if img.mode != 'RGB':
                        img = img.convert('RGB')
                    img.save(img_path, format='JPEG', quality=80, optimize=True)
                
            new_size = os.path.getsize(img_path)
            saved = size - new_size
            if saved > 0:
                saved_bytes += saved
                count += 1
                print(f"Optimized {os.path.basename(img_path)}: saved {saved/1024/1024:.2f} MB")
        except Exception as e:
            print(f"Error optimizing {img_path}: {e}")

print(f"\nDone! Optimized {count} images, saved {saved_bytes/1024/1024:.2f} MB in total.")
