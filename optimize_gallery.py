import os
import glob
from PIL import Image

galerie_dir = 'site/img/galerie'
max_dimension = 1200
quality_setting = 75

# 1. Optimize ALL existing images
print("Optimizing existing images...")
for img_path in glob.glob(os.path.join(galerie_dir, '*.*')):
    try:
        if not img_path.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            continue
            
        with Image.open(img_path) as img:
            # Convert to RGB if necessary
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
                
            width, height = img.size
            needs_resize = False
            
            if width > max_dimension or height > max_dimension:
                needs_resize = True
                if width > height:
                    new_width = max_dimension
                    new_height = int(max_dimension * height / width)
                else:
                    new_height = max_dimension
                    new_width = int(max_dimension * width / height)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Save as webp
            base_name = os.path.splitext(os.path.basename(img_path))[0]
            new_path = os.path.join(galerie_dir, base_name + '.webp')
            img.save(new_path, 'WEBP', quality=quality_setting)
            
            # Remove old file if format changed
            if img_path != new_path:
                os.remove(img_path)
    except Exception as e:
        print(f"Error processing {img_path}: {e}")

# 2. Add the two new images
print("Adding new images...")
new_images = [
    '/home/gregory/.gemini/antigravity-ide/brain/7e774966-6f64-4ea6-bde9-b91165bded85/media__1781526614313.jpg',
    '/home/gregory/.gemini/antigravity-ide/brain/7e774966-6f64-4ea6-bde9-b91165bded85/media__1781526629410.jpg'
]

new_img_basenames = []
current_id = 34

for img_path in new_images:
    if not os.path.exists(img_path):
        print(f"Warning: {img_path} not found.")
        continue
        
    try:
        with Image.open(img_path) as img:
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
                
            width, height = img.size
            if width > max_dimension or height > max_dimension:
                if width > height:
                    new_width = max_dimension
                    new_height = int(max_dimension * height / width)
                else:
                    new_height = max_dimension
                    new_width = int(max_dimension * width / height)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            new_basename = f"galerie_{current_id}"
            new_path = os.path.join(galerie_dir, new_basename + '.webp')
            img.save(new_path, 'WEBP', quality=quality_setting)
            new_img_basenames.append(new_basename)
            current_id += 1
            print(f"Added {new_basename}.webp")
    except Exception as e:
        print(f"Error adding {img_path}: {e}")

# 3. Update HTML files
print("Updating HTML files...")
html_files = ['site/galerie.html', 'site/de/galerie.html', 'site/en/gallery.html']

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        anchor = '<div class="gal-item"><img src="img/galerie/galerie_33.webp" loading="lazy" alt="Voilier Neuchâtel"></div>'
        
        if anchor in content:
            new_html = anchor
            for basename in new_img_basenames:
                # Add english alt if needed, but keeping it simple as before
                alt_text = "Voilier Neuchâtel"
                new_html += f'\n        <div class="gal-item"><img src="img/galerie/{basename}.webp" loading="lazy" alt="{alt_text}"></div>'
                
            content = content.replace(anchor, new_html)
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {html_file}")
        else:
            print(f"Anchor not found in {html_file}")
    except Exception as e:
        print(f"Error updating {html_file}: {e}")

print("Done.")
