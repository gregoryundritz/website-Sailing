import glob
import re

# 1. Update the BAV links at the bottom of the "permis" pages
bav_fr = "https://www.bav.admin.ch/fr/navigation-de-plaisance#FAQ-Navigation-de-plaisance"
bav_de = "https://www.bav.admin.ch/de/freizeitschifffahrt#FAQ-Freizeitschifffahrt"

permis_files = [
    'site/de/segelpruefung-schweiz.html',
    'site/en/sailing-license-switzerland.html'
]

for p in permis_files:
    try:
        with open(p, 'r', encoding='utf-8') as f:
            html = f.read()
        if bav_fr in html:
            html = html.replace(bav_fr, bav_de)
            with open(p, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Updated BAV link in {p}")
    except FileNotFoundError:
        pass

# 2. Fix the t(str) translation bug in all HTML files
t_str_target = """        function t(str) {
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

t_str_replacement = """        function t(str) {
           if (lang === 'fr') return str;
           if (!window.VOILIER_TRANSLATIONS) return str;
           var keys = Object.keys(window.VOILIER_TRANSLATIONS).sort(function(a, b) { return b.length - a.length; });
           for (var i = 0; i < keys.length; i++) {
               var k = keys[i];
               if (str.toLowerCase().includes(k.toLowerCase())) {
                   var trans = window.VOILIER_TRANSLATIONS[k][lang];
                   var escapedK = k.replace(/[-\\/\\\\^$*+?.()|[\\]{}]/g, '\\\\$&');
                   if(trans) return str.replace(new RegExp(escapedK, 'i'), trans);
               }
           }
           return str;
        }"""

all_html_files = glob.glob('site/*.html') + glob.glob('site/de/*.html') + glob.glob('site/en/*.html')

for p in all_html_files:
    try:
        with open(p, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # Some files might have slightly different spacing, so a direct replace might fail if spaces mismatch.
        # But `apply_step2.py` inserted this exact block, so it should match.
        if "function t(str) {" in html:
            if t_str_target in html:
                html = html.replace(t_str_target, t_str_replacement)
            else:
                # Fallback to regex replace if exact string doesn't match due to line endings
                html = re.sub(r'function t\(str\) \{.*?return str;\s*\}', t_str_replacement, html, flags=re.DOTALL)
            
            with open(p, 'w', encoding='utf-8') as f:
                f.write(html)
    except FileNotFoundError:
        pass

print("Fixed translation script in all HTML files.")
