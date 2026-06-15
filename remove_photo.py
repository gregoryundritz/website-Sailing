import glob
import re
import os

html_files = ['site/galerie.html', 'site/de/galerie.html', 'site/en/gallery.html']

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Match the div containing galerie_17.webp
        pattern = r'\s*<div class="gal-item"><img src="[^"]*galerie_17\.webp".*?</div>'
        
        if re.search(pattern, content):
            new_content = re.sub(pattern, '', content)
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed galerie_17.webp from {html_file}")
        else:
            print(f"galerie_17.webp not found in {html_file}")
            
    except Exception as e:
        print(f"Error updating {html_file}: {e}")

# Delete the image file
try:
    if os.path.exists('site/img/galerie/galerie_17.webp'):
        os.remove('site/img/galerie/galerie_17.webp')
        print("Deleted site/img/galerie/galerie_17.webp")
except Exception as e:
    print(f"Error deleting image: {e}")
