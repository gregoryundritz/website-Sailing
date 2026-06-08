import os
import glob
import re
import xml.etree.ElementTree as ET

# Paths
site_dir = "/home/gregory/Voilier/site"
fr_index = os.path.join(site_dir, "index.html")
de_index = os.path.join(site_dir, "de", "index.html")
en_index = os.path.join(site_dir, "en", "index.html")

fr_dest = os.path.join(site_dir, "a-propos.html")
de_dest = os.path.join(site_dir, "de", "ueber-uns.html")
en_dest = os.path.join(site_dir, "en", "about.html")

fr_tpl = os.path.join(site_dir, "avis.html")
de_tpl = os.path.join(site_dir, "de", "bewertungen.html")
en_tpl = os.path.join(site_dir, "en", "reviews.html")

# 1. Extract Apropos block
def extract_section(filepath, section_id):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(f'<section id="{section_id}".*?</section>', content, flags=re.DOTALL)
    return match.group(0) if match else ""

fr_apropos = extract_section(fr_index, "apropos")
de_apropos = extract_section(de_index, "apropos")
en_apropos = extract_section(en_index, "apropos")

# Adjust styling slightly for a standalone page: add padding-top
fr_apropos = fr_apropos.replace('style="background:var(--sand);"', 'style="background:var(--sand); padding-top: 120px; padding-bottom: 80px;"')
de_apropos = de_apropos.replace('style="background:var(--sand);"', 'style="background:var(--sand); padding-top: 120px; padding-bottom: 80px;"')
en_apropos = en_apropos.replace('style="background:var(--sand);"', 'style="background:var(--sand); padding-top: 120px; padding-bottom: 80px;"')

# 2. Create standalone pages using avis.html as template
def create_page(tpl_path, dest_path, apropos_content, title, desc, url_slug):
    with open(tpl_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace the main avis section
    content = re.sub(r'<!-- AVIS -->.*?</section>', apropos_content, content, flags=re.DOTALL)
    
    # Replace title & meta
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content)
    content = re.sub(r'<meta name="description"\s*content="[^"]*">', f'<meta name="description"\n    content="{desc}">', content)
    content = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{title}">', content)
    content = re.sub(r'<meta property="og:description"\s*content="[^"]*">', f'<meta property="og:description"\n    content="{desc}">', content)
    content = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{title}">', content)
    content = re.sub(r'<meta name="twitter:description"\s*content="[^"]*">', f'<meta name="twitter:description"\n    content="{desc}">', content)
    
    # Replace URL
    content = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="https://voilier-neuchatel.ch/{url_slug}">', content)
    content = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="https://voilier-neuchatel.ch/{url_slug}">', content)

    # Replace Hreflang
    hreflang_block = f'''<link rel="alternate" hreflang="fr" href="https://voilier-neuchatel.ch/a-propos.html">
  <link rel="alternate" hreflang="de" href="https://voilier-neuchatel.ch/de/ueber-uns.html">
  <link rel="alternate" hreflang="en" href="https://voilier-neuchatel.ch/en/about.html">
  <link rel="alternate" hreflang="x-default" href="https://voilier-neuchatel.ch/a-propos.html">'''
    content = re.sub(r'(<link rel="alternate" hreflang="[^"]+" href="[^"]+">\s*)+', hreflang_block + '\n', content)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(content)

create_page(fr_tpl, fr_dest, fr_apropos, "À propos - Gregory, navigateur passionné", "Skipper depuis plus de vingt ans, j'ai navigué sur les lacs suisses comme en mer. Découvrez mon parcours et le voilier Maxus 21.", "a-propos.html")
create_page(de_tpl, de_dest, de_apropos, "Über uns - Gregory, leidenschaftlicher Segler", "Als Skipper mit über zwanzig Jahren Erfahrung bin ich sowohl auf Schweizer Seen als auch auf dem Meer gesegelt.", "de/ueber-uns.html")
create_page(en_tpl, en_dest, en_apropos, "About - Gregory, passionate sailor", "Skipper for over twenty years, I have sailed on Swiss lakes as well as at sea. Discover my journey and the Maxus 21 sailboat.", "en/about.html")

# 3. Remove apropos from index.html
def remove_section(filepath, section_id):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    content = re.sub(f'<!-- À PROPOS -->\s*<section id="{section_id}".*?</section>', '', content, flags=re.DOTALL)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

remove_section(fr_index, "apropos")
remove_section(de_index, "apropos")
remove_section(en_index, "apropos")

# 4. Update all links globally
html_files = glob.glob(os.path.join(site_dir, "**/*.html"), recursive=True)

link_map_fr = [
    (r'href="index\.html#apropos"', 'href="a-propos.html"'),
    (r'href="/index\.html#apropos"', 'href="/a-propos.html"'),
    (r'href="#apropos"', 'href="a-propos.html"'),
]
link_map_de = [
    (r'href="index\.html#apropos"', 'href="ueber-uns.html"'),
    (r'href="/de/index\.html#apropos"', 'href="/de/ueber-uns.html"'),
    (r'href="#apropos"', 'href="ueber-uns.html"'),
]
link_map_en = [
    (r'href="index\.html#apropos"', 'href="about.html"'),
    (r'href="/en/index\.html#apropos"', 'href="/en/about.html"'),
    (r'href="#apropos"', 'href="about.html"'),
]

for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "/de/" in filepath:
        for old, new in link_map_de:
            content = re.sub(old, new, content)
    elif "/en/" in filepath:
        for old, new in link_map_en:
            content = re.sub(old, new, content)
    else:
        for old, new in link_map_fr:
            content = re.sub(old, new, content)
            
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Extraction and global link updates complete.")
