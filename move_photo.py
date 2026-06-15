import glob
import re

html_files = ['site/galerie.html', 'site/de/galerie.html', 'site/en/gallery.html']

for html_file in html_files:
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the line containing galerie_18.webp
        # We need to extract the exact div and remove it from its current place
        # e.g., <div class="gal-item"><img src="img/galerie/galerie_18.webp" loading="lazy" alt="Voilier Neuchâtel"></div>
        # or <div class="gal-item"><img src="../img/galerie/galerie_18.webp" ...
        
        match_18 = re.search(r'\s*<div class="gal-item"><img src="[^"]*galerie_18\.webp".*?</div>', content)
        if not match_18:
            print(f"galerie_18 not found in {html_file}")
            continue
            
        div_18 = match_18.group(0)
        
        # Remove it from its current position
        content = content.replace(div_18, '', 1)
        
        # Insert it after galerie_3.webp
        match_3 = re.search(r'\s*<div class="gal-item"><img src="[^"]*galerie_3\.webp".*?</div>', content)
        if match_3:
            div_3 = match_3.group(0)
            content = content.replace(div_3, div_3 + div_18, 1)
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Moved galerie_18 to position 4 in {html_file}")
        else:
            print(f"galerie_3 not found in {html_file}")
            
    except Exception as e:
        print(f"Error updating {html_file}: {e}")
