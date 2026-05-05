import os
from PIL import Image

images_dir = 'site/images'
for filename in os.listdir(images_dir):
    if filename.startswith('extracted_') and not filename.endswith('.webp'):
        filepath = os.path.join(images_dir, filename)
        webp_filename = filename.rsplit('.', 1)[0] + '.webp'
        webp_filepath = os.path.join(images_dir, webp_filename)
        
        try:
            with Image.open(filepath) as img:
                img.save(webp_filepath, 'WEBP', quality=85)
            # Remove original file
            os.remove(filepath)
            
            # Update HTML
            with open('site/index.html', 'r', encoding='utf-8') as f:
                html = f.read()
            html = html.replace(f'images/{filename}', f'images/{webp_filename}')
            with open('site/index.html', 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Converted {filename} to {webp_filename}")
        except Exception as e:
            print(f"Error converting {filename}: {e}")
