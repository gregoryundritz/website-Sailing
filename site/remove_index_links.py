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

    # Remove FR menu items pointing to index anchors
    content = re.sub(r'^\s*<li><a href="([^"]*)#bateau">[^<]*</a></li>\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*<li><a href="([^"]*)#emplacement">[^<]*</a></li>\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^\s*<li><a href="([^"]*)#infos">[^<]*</a></li>\n', '', content, flags=re.MULTILINE)

    # Note: The regex '([^"]*)#bateau' matches 'index.html#bateau', '#bateau', '/de/#bateau', etc.

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Removed index links from menu in all HTML files.")
