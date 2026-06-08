import os
import glob
import re

site_dir = "/home/gregory/Voilier/site"

# 1. Rename 'en' directory to '_en_backup'
en_dir = os.path.join(site_dir, "en")
backup_dir = os.path.join(site_dir, "_en_backup")

if os.path.exists(en_dir):
    os.rename(en_dir, backup_dir)
    print("Renamed 'en' directory to '_en_backup'.")

# 2. Find all HTML files in base and 'de' directories
html_files = []
for f in glob.glob(os.path.join(site_dir, "*.html")):
    html_files.append(f)
for f in glob.glob(os.path.join(site_dir, "de", "*.html")):
    html_files.append(f)

# 3. Clean files
for filepath in html_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove EN from lang selector
    # It looks like: <span>|</span><a href="/en/..." class="...">EN</a>
    content = re.sub(r'<span>\|</span><a href="/en/[^"]*" class="[^"]*">EN</a>', '', content)
    
    # Remove hreflang="en"
    # It looks like: <link rel="alternate" hreflang="en" href="...">
    content = re.sub(r'<link rel="alternate" hreflang="en" href="[^"]*">\s*', '', content)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Removed EN links from all FR and DE files.")

# 4. Re-generate sitemap.xml without EN
sitemap_path = os.path.join(site_dir, "sitemap.xml")

fr_de_slugs = {
    "index.html": "index.html",
    "tarifs.html": "de/preise.html",
    "contact.html": "de/kontakt.html",
    "galerie.html": "de/galerie.html",
    "itineraires.html": "de/toerns.html",
    "avis.html": "de/bewertungen.html",
    "permis-bateau-suisse.html": "de/segelpruefung-schweiz.html",
    "conditions-generales.html": "de/agb.html",
    "mentions-legales.html": "de/impressum.html",
    "a-propos.html": "de/ueber-uns.html"
}

priority = {
    "index.html": "1.0",
    "conditions-generales.html": "0.3",
    "mentions-legales.html": "0.3",
    "a-propos.html": "0.7"
}

xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n  xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'

for fr, de in fr_de_slugs.items():
    prio = priority.get(fr, "0.8")
    
    url_fr = "https://voilier-neuchatel.ch/" + (fr if fr != "index.html" else "")
    url_de = "https://voilier-neuchatel.ch/" + (de if de != "index.html" else "de/")
    
    # FR Block
    xml += f'''  <url>
    <loc>{url_fr}</loc>
    <xhtml:link rel="alternate" hreflang="fr" href="{url_fr}" />
    <xhtml:link rel="alternate" hreflang="de" href="{url_de}" />
    <xhtml:link rel="alternate" hreflang="x-default" href="{url_fr}" />
    <priority>{prio}</priority>
    <changefreq>weekly</changefreq>
  </url>\n'''
  
    # DE Block
    xml += f'''  <url>
    <loc>{url_de}</loc>
    <xhtml:link rel="alternate" hreflang="fr" href="{url_fr}" />
    <xhtml:link rel="alternate" hreflang="de" href="{url_de}" />
    <xhtml:link rel="alternate" hreflang="x-default" href="{url_fr}" />
    <priority>{prio}</priority>
    <changefreq>weekly</changefreq>
  </url>\n'''

xml += '</urlset>\n'

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(xml)

print("Sitemap updated without EN.")
