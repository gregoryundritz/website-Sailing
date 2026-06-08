import os
import glob
import re
import shutil

site_dir = "/home/gregory/Voilier/site"
fr_files = glob.glob(os.path.join(site_dir, "*.html"))
de_files = glob.glob(os.path.join(site_dir, "de", "*.html"))
en_dir = os.path.join(site_dir, "en")

# 1. Rename files in EN to English slugs
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

# Rename the files that were just copied
for fr_name, en_name in slugs.items():
    old_path = os.path.join(en_dir, fr_name)
    new_path = os.path.join(en_dir, en_name)
    if os.path.exists(old_path) and old_path != new_path:
        os.rename(old_path, new_path)

en_files = glob.glob(os.path.join(en_dir, "*.html"))
all_files = fr_files + de_files + en_files

# 2. Update Hreflang and Lang Selector in ALL files
for filepath in all_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine current language
    if "/de/" in filepath:
        lang = "de"
    elif "/en/" in filepath:
        lang = "en"
    else:
        lang = "fr"

    basename = os.path.basename(filepath)
    
    # Map to FR basename to find equivalents
    fr_equiv = basename
    if lang == "de":
        # reverse map
        de_slugs = {
            "index.html": "index.html",
            "preise.html": "tarifs.html",
            "kontakt.html": "contact.html",
            "galerie.html": "galerie.html",
            "toerns.html": "itineraires.html",
            "bewertungen.html": "avis.html",
            "segelpruefung-schweiz.html": "permis-bateau-suisse.html",
            "agb.html": "conditions-generales.html",
            "impressum.html": "mentions-legales.html"
        }
        fr_equiv = de_slugs.get(basename, basename)
    elif lang == "en":
        # reverse map
        en_slugs_rev = {v: k for k, v in slugs.items()}
        fr_equiv = en_slugs_rev.get(basename, basename)

    # Now get the 3 equivalents
    fr_url = "https://voilier-neuchatel.ch/" + (fr_equiv if fr_equiv != "index.html" else "")
    de_url = "https://voilier-neuchatel.ch/de/" + (list({"index.html": "index.html", "tarifs.html": "preise.html", "contact.html": "kontakt.html", "galerie.html": "galerie.html", "itineraires.html": "toerns.html", "avis.html": "bewertungen.html", "permis-bateau-suisse.html": "segelpruefung-schweiz.html", "conditions-generales.html": "agb.html", "mentions-legales.html": "impressum.html"}.keys())[list({"index.html": "index.html", "tarifs.html": "preise.html", "contact.html": "kontakt.html", "galerie.html": "galerie.html", "itineraires.html": "toerns.html", "avis.html": "bewertungen.html", "permis-bateau-suisse.html": "segelpruefung-schweiz.html", "conditions-generales.html": "agb.html", "mentions-legales.html": "impressum.html"}.values()).index(basename)] if lang == "de" else {"index.html": "index.html", "tarifs.html": "preise.html", "contact.html": "kontakt.html", "galerie.html": "galerie.html", "itineraires.html": "toerns.html", "avis.html": "bewertungen.html", "permis-bateau-suisse.html": "segelpruefung-schweiz.html", "conditions-generales.html": "agb.html", "mentions-legales.html": "impressum.html"}.get(fr_equiv, fr_equiv))
    en_url = "https://voilier-neuchatel.ch/en/" + slugs.get(fr_equiv, fr_equiv)

    if de_url.endswith("/index.html"): de_url = de_url[:-10]
    if en_url.endswith("/index.html"): en_url = en_url[:-10]

    # Generate Hreflang block
    hreflang_block = f'''<link rel="alternate" hreflang="fr" href="{fr_url}">
  <link rel="alternate" hreflang="de" href="{de_url}">
  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="alternate" hreflang="x-default" href="{fr_url}">'''

    # Replace existing hreflang
    content = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+">\s*<link rel="alternate" hreflang="[^"]+" href="[^"]+">', hreflang_block, content, flags=re.MULTILINE)
    # Also catch cases where there might be 3 or 4 links already
    content = re.sub(r'(<link rel="alternate" hreflang="[^"]+" href="[^"]+">\s*)+', hreflang_block + '\n', content)

    # Replace lang selector
    # FR: <li class="lang-sel"><a href="#" class="active">FR</a><span>|</span><a href="/de/index.html">DE</a></li>
    # New: <li class="lang-sel"><a href="{fr_rel}" class="{fr_cls}">FR</a><span>|</span><a href="{de_rel}" class="{de_cls}">DE</a><span>|</span><a href="{en_rel}" class="{en_cls}">EN</a></li>
    
    fr_rel = "/" + fr_equiv if fr_equiv != "index.html" else "/"
    de_rel = "/de/" + {"index.html": "", "tarifs.html": "preise.html", "contact.html": "kontakt.html", "galerie.html": "galerie.html", "itineraires.html": "toerns.html", "avis.html": "bewertungen.html", "permis-bateau-suisse.html": "segelpruefung-schweiz.html", "conditions-generales.html": "agb.html", "mentions-legales.html": "impressum.html"}.get(fr_equiv, fr_equiv)
    en_rel = "/en/" + slugs.get(fr_equiv, fr_equiv)
    if en_rel == "/en/index.html": en_rel = "/en/"

    fr_cls = "active" if lang == "fr" else ""
    de_cls = "active" if lang == "de" else ""
    en_cls = "active" if lang == "en" else ""

    lang_sel_new = f'<li class="lang-sel"><a href="{fr_rel}" class="{fr_cls}">FR</a><span>|</span><a href="{de_rel}" class="{de_cls}">DE</a><span>|</span><a href="{en_rel}" class="{en_cls}">EN</a></li>'
    
    content = re.sub(r'<li class="lang-sel">.*?</li>', lang_sel_new, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Update internal links in EN files
for filepath in en_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace FR links with EN slugs
    for fr_slug, en_slug in slugs.items():
        if fr_slug == "index.html":
            content = content.replace('href="index.html"', 'href="/en/"')
            content = content.replace('href="/"', 'href="/en/"')
        else:
            content = content.replace(f'href="{fr_slug}"', f'href="{en_slug}"')
            content = content.replace(f'href="/{fr_slug}"', f'href="/en/{en_slug}"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Setup completed!")
