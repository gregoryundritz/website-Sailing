import os

ROUTE_MAP = {
    'index.html': {'de': 'index.html', 'en': 'index.html'},
    'tarifs.html': {'de': 'preise.html', 'en': 'prices.html'},
    'contact.html': {'de': 'kontakt.html', 'en': 'contact.html'},
    'galerie.html': {'de': 'galerie.html', 'en': 'gallery.html'},
    'itineraires.html': {'de': 'toerns.html', 'en': 'itineraries.html'},
    'avis.html': {'de': 'bewertungen.html', 'en': 'reviews.html'},
    'permis-bateau-suisse.html': {'de': 'segelpruefung-schweiz.html', 'en': 'sailing-license-switzerland.html'},
    'conditions-generales.html': {'de': 'agb.html', 'en': 'terms-and-conditions.html'},
    'mentions-legales.html': {'de': 'impressum.html', 'en': 'legal-notice.html'},
    'a-propos.html': {'de': 'ueber-uns.html', 'en': 'about.html'}
}

PRIORITY = {
    'index.html': 1.0,
    'tarifs.html': 0.8,
    'contact.html': 0.8,
    'galerie.html': 0.8,
    'itineraires.html': 0.8,
    'avis.html': 0.8,
    'permis-bateau-suisse.html': 0.8,
    'a-propos.html': 0.7,
    'conditions-generales.html': 0.3,
    'mentions-legales.html': 0.3
}

base_url = "https://voilier-neuchatel.ch"

def gen_entry(loc, fr_loc, de_loc, en_loc, priority):
    return f"""  <url>
    <loc>{loc}</loc>
    <xhtml:link rel="alternate" hreflang="fr" href="{fr_loc}" />
    <xhtml:link rel="alternate" hreflang="de" href="{de_loc}" />
    <xhtml:link rel="alternate" hreflang="en" href="{en_loc}" />
    <xhtml:link rel="alternate" hreflang="x-default" href="{fr_loc}" />
    <priority>{priority}</priority>
    <changefreq>weekly</changefreq>
  </url>"""

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'

for fr_page, trans in ROUTE_MAP.items():
    fr_url = f"{base_url}/" if fr_page == "index.html" else f"{base_url}/{fr_page}"
    de_url = f"{base_url}/de/" if trans['de'] == "index.html" else f"{base_url}/de/{trans['de']}"
    en_url = f"{base_url}/en/" if trans['en'] == "index.html" else f"{base_url}/en/{trans['en']}"
    pri = PRIORITY.get(fr_page, 0.5)
    
    sitemap += gen_entry(fr_url, fr_url, de_url, en_url, pri) + "\n"
    sitemap += gen_entry(de_url, fr_url, de_url, en_url, pri) + "\n"
    sitemap += gen_entry(en_url, fr_url, de_url, en_url, pri) + "\n"

sitemap += "</urlset>"

with open('/home/gregory/Voilier/site/sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap)
print("Sitemap generated successfully.")
