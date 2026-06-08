import os
import re

sitemap_path = "/home/gregory/Voilier/site/sitemap.xml"
with open(sitemap_path, "r", encoding="utf-8") as f:
    content = f.read()

slugs = {
    "index.html": "index.html",
    "tarifs.html": "prices.html",
    "contact.html": "contact.html",
    "galerie.html": "gallery.html",
    "itineraires.html": "itineraries.html",
    "avis.html": "reviews.html",
    "permis-bateau-suisse.html": "sailing-license-switzerland.html",
    "conditions-generales.html": "terms-and-conditions.html",
    "mentions-legales.html": "legal-notice.html"
}

# Add hreflang="en" to existing <url> blocks
for fr_k, en_v in slugs.items():
    en_url = f"https://voilier-neuchatel.ch/en/{en_v}"
    if en_url.endswith("/index.html"): en_url = en_url[:-10]
    
    # regex to find the block for a specific loc and add the en link
    # We will just append the en link before x-default
    # But it's easier to just use string replace on x-default
    
    find_str = '<xhtml:link rel="alternate" hreflang="x-default"'
    replace_str = f'<xhtml:link rel="alternate" hreflang="en" href="{en_url}" />\n    <xhtml:link rel="alternate" hreflang="x-default"'
    
    # We only want to do this once per <url> block... actually it's easier to recreate the sitemap
    pass

# Recreate sitemap
fr_de_slugs = {
    "index.html": "index.html",
    "tarifs.html": "de/preise.html",
    "contact.html": "de/kontakt.html",
    "galerie.html": "de/galerie.html",
    "itineraires.html": "de/toerns.html",
    "avis.html": "de/bewertungen.html",
    "permis-bateau-suisse.html": "de/segelpruefung-schweiz.html",
    "conditions-generales.html": "de/agb.html",
    "mentions-legales.html": "de/impressum.html"
}

priority = {
    "index.html": "1.0",
    "conditions-generales.html": "0.3",
    "mentions-legales.html": "0.3"
}

xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n  xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'

for fr, de in fr_de_slugs.items():
    en = slugs[fr]
    prio = priority.get(fr, "0.8")
    
    url_fr = "https://voilier-neuchatel.ch/" + (fr if fr != "index.html" else "")
    url_de = "https://voilier-neuchatel.ch/" + (de if de != "index.html" else "de/")
    url_en = "https://voilier-neuchatel.ch/en/" + (en if en != "index.html" else "")
    
    # FR Block
    xml += f'''  <url>
    <loc>{url_fr}</loc>
    <xhtml:link rel="alternate" hreflang="fr" href="{url_fr}" />
    <xhtml:link rel="alternate" hreflang="de" href="{url_de}" />
    <xhtml:link rel="alternate" hreflang="en" href="{url_en}" />
    <xhtml:link rel="alternate" hreflang="x-default" href="{url_fr}" />
    <priority>{prio}</priority>
    <changefreq>weekly</changefreq>
  </url>\n'''
  
    # DE Block
    xml += f'''  <url>
    <loc>{url_de}</loc>
    <xhtml:link rel="alternate" hreflang="fr" href="{url_fr}" />
    <xhtml:link rel="alternate" hreflang="de" href="{url_de}" />
    <xhtml:link rel="alternate" hreflang="en" href="{url_en}" />
    <xhtml:link rel="alternate" hreflang="x-default" href="{url_fr}" />
    <priority>{prio}</priority>
    <changefreq>weekly</changefreq>
  </url>\n'''

    # EN Block
    xml += f'''  <url>
    <loc>{url_en}</loc>
    <xhtml:link rel="alternate" hreflang="fr" href="{url_fr}" />
    <xhtml:link rel="alternate" hreflang="de" href="{url_de}" />
    <xhtml:link rel="alternate" hreflang="en" href="{url_en}" />
    <xhtml:link rel="alternate" hreflang="x-default" href="{url_fr}" />
    <priority>{prio}</priority>
    <changefreq>weekly</changefreq>
  </url>\n'''

xml += '</urlset>\n'

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(xml)

print("Sitemap updated.")
