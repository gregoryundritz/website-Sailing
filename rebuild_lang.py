import os
import glob
import re

ROUTE_MAP = {
    'index.html': {'de': 'index.html', 'EN-GB': 'index.html'},
    'tarifs.html': {'de': 'preise.html', 'EN-GB': 'prices.html'},
    'galerie.html': {'de': 'galerie.html', 'EN-GB': 'gallery.html'},
    'contact.html': {'de': 'kontakt.html', 'EN-GB': 'contact.html'},
    'a-propos.html': {'de': 'ueber-uns.html', 'EN-GB': 'about.html'},
    'itineraires.html': {'de': 'toerns.html', 'EN-GB': 'itineraries.html'},
    'avis.html': {'de': 'bewertungen.html', 'EN-GB': 'reviews.html'},
    'conditions-generales.html': {'de': 'agb.html', 'EN-GB': 'terms-and-conditions.html'},
    'mentions-legales.html': {'de': 'impressum.html', 'EN-GB': 'legal-notice.html'},
    'permis-bateau-suisse.html': {'de': 'segelpruefung-schweiz.html', 'EN-GB': 'sailing-license-switzerland.html'}
}

html_files = glob.glob('site/*.html')

for filepath in html_files:
    basename = os.path.basename(filepath)
    if basename not in ROUTE_MAP: continue
    
    de_page = ROUTE_MAP[basename]['de']
    en_page = ROUTE_MAP[basename]['EN-GB']
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    fr_url = "/" if basename == "index.html" else f"/{basename}"
    de_url = "/de/" if de_page == "index.html" else f"/de/{de_page}"
    en_url = "/en/" if en_page == "index.html" else f"/en/{en_page}"
    
    new_mob = f'<div class="lang-sel-mob"><a href="#" class="active">FR</a><span>|</span><a href="{de_url}" class="">DE</a><span>|</span><a href="{en_url}" class="">EN</a></div>'
    content = re.sub(r'<div class="lang-sel-mob">.*?</div>', new_mob, content)
    
    new_desk = f'<li class="lang-sel"><a href="{fr_url}" class="active">FR</a><span>|</span><a href="{de_url}" class="">DE</a><span>|</span><a href="{en_url}" class="">EN</a></li>'
    content = re.sub(r'<li class="lang-sel">.*?</li>', new_desk, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Language menus rebuilt for all FR source files.")
