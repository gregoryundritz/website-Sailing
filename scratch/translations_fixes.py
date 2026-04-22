import re

def fix_file(path, lang):
    with open(path, 'r') as f:
        content = f.read()
    
    # 1. Responsive CSS
    css_target = r"@media\(max-width:900px\)\s*\{\s*\.price-grid\s*\{\s*grid-template-columns:\s*repeat\(4,\s*1fr\)\s*\}\s*"
    
    new_css = """@media(max-width:900px) {
      .tarifs-sec .ct, .tarifs-sec .rv { overflow-x: auto; padding-bottom: 20px; }
      .price-grid { min-width: 600px; }
"""
    if re.search(css_target, content):
        content = re.sub(css_target, new_css, content)
    else:
        # Check alternative minified version
        css_min_target = r"@media\(max-width:900px\)\{.price-grid\{grid-template-columns:repeat\(4,1fr\)\}"
        new_css_min = "@media(max-width:900px){.tarifs-sec .ct{overflow-x:auto;padding-bottom:10px}.price-grid{min-width:600px;grid-template-columns:repeat(7,1fr)}"
        content = re.sub(css_min_target, new_css_min, content)

    # 2. Add hidden subject if missing
    if 'name="subject"' not in content:
        subj = "Demande de réservation - Voilier Neuchâtel"
        if lang == 'en': subj = "New Reservation Request - Sailboat Neuchâtel"
        if lang == 'de': subj = "Neue Buchungsanfrage - Segelboot Neuenburgersee"
        
        content = content.replace('<input type="hidden" name="form-name" value="reservation">',
                                  f'<input type="hidden" name="form-name" value="reservation">\n      <input type="hidden" name="subject" value="{subj}">')

    # 3. Lang switcher class
    if lang == 'de':
        content = content.replace('<a href="/" class="lang-active">FR</a>', '<a href="/">FR</a>')
        content = content.replace('<a href="/de/">DE</a>', '<a href="/de/" class="lang-active">DE</a>')
    
    # 4. Enforce exact translations
    if lang == 'en':
        content = content.replace('Lac de Neuchâtel', 'Lake of Neuchâtel')
        content = content.replace('lac de Neuchâtel', 'Lake of Neuchâtel')
        content = content.replace('Lake Neuchâtel', 'Lake of Neuchâtel')
        # Translate the title of DE if it is wrong
    if lang == 'de':
        content = content.replace('Lac de Neuchâtel', 'Neuenburgersee')
        content = content.replace('lac de Neuchâtel', 'Neuenburgersee')
        content = content.replace('Lake of Neuchâtel', 'Neuenburgersee')

    with open(path, 'w') as f:
        f.write(content)

fix_file('/home/gregory/Voilier/site/index.html', 'fr')
fix_file('/home/gregory/Voilier/site/en/index.html', 'en')
fix_file('/home/gregory/Voilier/site/de/index.html', 'de')
print("Fixes applied successfully")
