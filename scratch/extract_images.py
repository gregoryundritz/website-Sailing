import re
import os
import base64
import hashlib

html_path = 'site/index.html'
images_dir = 'site/images'
os.makedirs(images_dir, exist_ok=True)

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Find all base64 images
pattern = re.compile(r'data:image/(png|jpeg|jpg|webp);base64,([A-Za-z0-9+/=]+)')
matches = pattern.finditer(html)

count = 0
for match in matches:
    ext = match.group(1)
    if ext == 'jpeg': ext = 'jpg'
    data = base64.b64decode(match.group(2))
    
    # Hash to create a unique filename
    h = hashlib.md5(data).hexdigest()[:8]
    filename = f'extracted_{h}.{ext}'
    filepath = os.path.join(images_dir, filename)
    
    with open(filepath, 'wb') as img_f:
        img_f.write(data)
    
    # Replace in HTML
    html = html.replace(match.group(0), f'images/{filename}')
    count += 1

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Extracted {count} images.")
