import glob
import re

files = {
    'site/contact.html': '<div style="font-size: 13px; color: var(--gold); margin-bottom: 12px; margin-top: -8px;">* 2 jours minimum en juillet et août.</div>\n            <div id="resa-duration-display"',
    'site/de/kontakt.html': '<div style="font-size: 13px; color: var(--gold); margin-bottom: 12px; margin-top: -8px;">* Mindestbuchungsdauer von 2 Tagen im Juli und August.</div>\n            <div id="resa-duration-display"',
    'site/en/contact.html': '<div style="font-size: 13px; color: var(--gold); margin-bottom: 12px; margin-top: -8px;">* Minimum 2 days reservation in July and August.</div>\n            <div id="resa-duration-display"'
}

for file_path, injection in files.items():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        html = html.replace('<div id="resa-duration-display"', injection)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
