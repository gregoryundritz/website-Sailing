import re
import glob

# 1. Update config.js to add translations
with open('site/js/config.js', 'r', encoding='utf-8') as f:
    config_js = f.read()

if 'VOILIER_TRANSLATIONS' not in config_js:
    translations = """
window.VOILIER_TRANSLATIONS = {
  'Nettoyage final (obligatoire)': { 'de': 'Endreinigung (obligatorisch)', 'en': 'Final cleaning (mandatory)' },
  'Nettoyage final': { 'de': 'Endreinigung', 'en': 'Final cleaning' },
  'Paddle': { 'de': 'Stand-Up Paddle', 'en': 'Paddleboard' },
  'Gennaker': { 'de': 'Gennaker', 'en': 'Gennaker' }
};
"""
    config_js += translations
    with open('site/js/config.js', 'w', encoding='utf-8') as f:
        f.write(config_js)

# 2. Update contact files to move the section and add translations
contact_files = {
    'site/contact.html': ('fr', 'Sélectionnez votre type de réservation :'),
    'site/de/kontakt.html': ('de', 'Wählen Sie Ihre Buchungsart :'),
    'site/en/contact.html': ('en', 'Select your booking type :')
}

for path, (lang, text) in contact_files.items():
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Move the standard/pass section
    # First, extract it
    match = re.search(r'(<div class="resa-step" style="margin-bottom:24px;">\s*<div id="resa-type-tabs".*?</div>\s*</div>)', html, flags=re.DOTALL)
    if match:
        section = match.group(1)
        # Remove it from its current position
        html = html.replace(section, '')
        
        # Add the mini-text inside the section
        new_section = section.replace('<div id="resa-type-tabs"', f'<div style="font-size:14px; font-weight:600; margin-bottom:12px; color:var(--navy);">{text}</div>\n            <div id="resa-type-tabs"')
        
        # Insert it right before <!-- TOTAL VISIBLE ICI -->
        html = html.replace('<!-- TOTAL VISIBLE ICI -->', new_section + '\n\n          <!-- TOTAL VISIBLE ICI -->')

    # Update JS for options translation
    js_update = """        var lang = document.documentElement.lang || 'fr';
        function t(str) {
           if (lang === 'fr') return str;
           if (!window.VOILIER_TRANSLATIONS) return str;
           for (var k in window.VOILIER_TRANSLATIONS) {
               if (str.toLowerCase().includes(k.toLowerCase())) {
                   var trans = window.VOILIER_TRANSLATIONS[k][lang];
                   if(trans) return str.replace(new RegExp(k, 'i'), trans);
               }
           }
           return str;
        }"""
    
    if 'function t(str)' not in html:
        html = html.replace('if (c.options && c.options.length) {', 'if (c.options && c.options.length) {\n' + js_update)

    # Replace /j string logic
    html = re.sub(r"var pl = o\.per === 'jour' \? '/j' : o\.per === 'forfait' \? '' : '/' \+ o\.per;", 
                  r"var pl = o.per === 'jour' ? (lang==='de'? '/Tag' : lang==='en'? '/day' : '/j') : o.per === 'forfait' ? '' : '/' + o.per;", html)

    # Replace o.name with t(o.name) in the HTML generation for options
    html = html.replace('${gi(o.name)} ${o.name}', '${gi(o.name)} ${t(o.name)}')
    
    # Remove OF CHARTER properly
    html = re.sub(r'(?i)\s*of charter', '', html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

# 3. Also update tarifs.html for options translation!
tarifs_files = {
    'site/tarifs.html': 'fr',
    'site/de/preise.html': 'de',
    'site/en/prices.html': 'en'
}

for path, lang in tarifs_files.items():
    try:
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
            
        if 'function t(str)' not in html:
            html = html.replace('if (c.options && c.options.length) {', 'if (c.options && c.options.length) {\n' + js_update)
        
        html = re.sub(r"var pl = o\.per === 'jour' \? '/j' : o\.per === 'forfait' \? '' : '/' \+ o\.per;", 
                      r"var pl = o.per === 'jour' ? (lang==='de'? '/Tag' : lang==='en'? '/day' : '/j') : o.per === 'forfait' ? '' : '/' + o.per;", html)
        
        html = html.replace('${gi(o.name)} ${o.name}', '${gi(o.name)} ${t(o.name)}')
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
    except FileNotFoundError:
        pass

print("Fixed border thickness, moved resa-tabs, added mini-text, and implemented JS options translations!")
