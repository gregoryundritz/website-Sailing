import glob
import re

mappings = [
    ('/cgv.html', '/de/agb.html', '/en/terms-and-conditions.html'),
    ('/mentions-legales.html', '/de/impressum.html', '/en/legal-notice.html'),
]

def update_lang_sel(lang, file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Find matching mapping based on file_path ending
    match = None
    for m in mappings:
        if lang == 'de' and file_path.endswith(m[1].split('/')[-1]):
            match = m
            break
        if lang == 'en' and file_path.endswith(m[2].split('/')[-1]):
            match = m
            break
            
    if not match:
        return

    # Build correct lang_sel string
    fr_rel, de_rel, en_rel = match
    fr_cls = "active" if lang == 'fr' else ""
    de_cls = "active" if lang == 'de' else ""
    en_cls = "active" if lang == 'en' else ""
    
    correct_lang_sel = f'<li class="lang-sel"><a href="{fr_rel}" class="{fr_cls}">FR</a><span>|</span><a href="{de_rel}" class="{de_cls}">DE</a><span>|</span><a href="{en_rel}" class="{en_cls}">EN</a></li>'
    
    # Replace in file
    new_html = re.sub(r'<li class="lang-sel">.*?</li>', correct_lang_sel, html, flags=re.DOTALL)
    
    if new_html != html:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Fixed {file_path}")

de_files = glob.glob('site/de/*.html')
en_files = glob.glob('site/en/*.html')

for f in de_files:
    update_lang_sel('de', f)

for f in en_files:
    update_lang_sel('en', f)
