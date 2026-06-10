import os
import glob
import re

PAGES = [
    {'fr': '/', 'de': '/de/', 'en': '/en/'},
    {'fr': '/contact.html', 'de': '/de/kontakt.html', 'en': '/en/contact.html'},
    {'fr': '/a-propos.html', 'de': '/de/ueber-uns.html', 'en': '/en/about.html'},
    {'fr': '/galerie.html', 'de': '/de/galerie.html', 'en': '/en/gallery.html'},
    {'fr': '/tarifs.html', 'de': '/de/preise.html', 'en': '/en/prices.html'},
    {'fr': '/itineraires.html', 'de': '/de/toerns.html', 'en': '/en/itineraries.html'},
    {'fr': '/permis-bateau-suisse.html', 'de': '/de/segelpruefung-schweiz.html', 'en': '/en/sailing-license-switzerland.html'},
    {'fr': '/avis.html', 'de': '/de/bewertungen.html', 'en': '/en/reviews.html'},
    {'fr': '/conditions-generales.html', 'de': '/de/agb.html', 'en': '/en/terms-and-conditions.html'},
    {'fr': '/mentions-legales.html', 'de': '/de/impressum.html', 'en': '/en/legal-notice.html'}
]

all_files = glob.glob('site/*.html') + glob.glob('site/de/*.html') + glob.glob('site/en/*.html')

for file_path in all_files:
    filename = os.path.basename(file_path)
    
    # Determine which page dict applies
    page_dict = None
    if filename == 'index.html':
        page_dict = PAGES[0]
    else:
        for p in PAGES:
            if p['fr'].endswith('/' + filename) or p['de'].endswith('/' + filename) or p['en'].endswith('/' + filename):
                page_dict = p
                break
                
    if not page_dict:
        print(f"Skipping {file_path}, no mapping found.")
        continue
        
    # Determine active language
    lang = 'fr'
    if '/de/' in file_path:
        lang = 'de'
    elif '/en/' in file_path:
        lang = 'en'
        
    # Build new li
    act_fr = ' class="active"' if lang == 'fr' else ' class=""'
    act_de = ' class="active"' if lang == 'de' else ' class=""'
    act_en = ' class="active"' if lang == 'en' else ' class=""'
    
    new_li = f'<li class="lang-sel"><a href="{page_dict["fr"]}"{act_fr}>FR</a><span>|</span><a href="{page_dict["de"]}"{act_de}>DE</a><span>|</span><a href="{page_dict["en"]}"{act_en}>EN</a></li>'
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace the existing lang-sel li
        # Regex to match the entire li tag
        new_content = re.sub(r'<li class="lang-sel">.*?</li>', new_li, content, flags=re.DOTALL)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated language switcher in {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
