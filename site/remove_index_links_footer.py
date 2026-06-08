import os
import glob
import re

site_dir = "/home/gregory/Voilier/site"

html_files = []
for f in glob.glob(os.path.join(site_dir, "*.html")):
    html_files.append(f)
for f in glob.glob(os.path.join(site_dir, "de", "*.html")):
    html_files.append(f)

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove links from the footer that point to #bateau, #emplacement, #infos
    # They look like: <a href="#bateau">Le bateau</a>
    # or <a href="#emplacement" onclick="...">Emplacement</a>
    
    # We will use regex to remove the entire <a> tag for these 3 anchors, accounting for potential onclick or other attributes.
    content = re.sub(r'^\s*<a href="[^"]*#bateau"[^>]*>[^<]*</a>\n', '', content, flags=re.MULTILINE)
    
    # Emplacement is tricky because it has a newline inside the tag in index.html:
    # <a href="#emplacement"
    #   onclick="event.preventDefault(); document.getElementById('emplacement').scrollIntoView({ behavior: 'smooth', block: 'center' });">Emplacement</a>
    # We can match from <a href="[^"]*#emplacement" to </a>
    content = re.sub(r'\s*<a href="[^"]*#emplacement"[^>]*>.*?</a>\n', '\n', content, flags=re.DOTALL)
    
    content = re.sub(r'^\s*<a href="[^"]*#infos"[^>]*>[^<]*</a>\n', '', content, flags=re.MULTILINE)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Removed index links from footer in all HTML files.")
