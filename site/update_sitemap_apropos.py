import os

sitemap_path = "/home/gregory/Voilier/site/sitemap.xml"

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
    "mentions-legales.html": "de/impressum.html",
    "a-propos.html": "de/ueber-uns.html"
}

slugs = {
    "index.html": "index.html",
    "tarifs.html": "prices.html",
    "contact.html": "contact.html",
    "galerie.html": "gallery.html",
    "itineraires.html": "itineraries.html",
    "avis.html": "reviews.html",
    "permis-bateau-suisse.html": "sailing-license-switzerland.html",
    "conditions-generales.html": "terms-and-conditions.html",
    "mentions-legales.html": "legal-notice.html",
    "a-propos.html": "about.html"
}

priority = {
    "index.html": "1.0",
    "conditions-generales.html": "0.3",
    "mentions-legales.html": "0.3",
    "a-propos.html": "0.7"
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
