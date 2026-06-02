import os
import glob

directory = "/home/gregory/Voilier/site/de/"
html_files = glob.glob(os.path.join(directory, "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generic replacements for AGB and Impressum links
    content = content.replace('<a href="/conditions-generales.html">AGB</a>', '<a href="/de/agb.html">AGB</a>')
    content = content.replace('<a href="/mentions-legales.html">Impressum</a>', '<a href="/de/impressum.html">Impressum</a>')

    if filepath.endswith('kontakt.html'):
        content = content.replace(
            '''<span>J'ai lu et j'accepte les <a href="/conditions-generales.html" target="_blank"
                style="color: var(--teal); text-decoration: underline; font-weight: 500;">AGB de
                Location</a> *</span>''',
            '''<span>Ich habe die <a href="/de/agb.html" target="_blank"
                style="color: var(--teal); text-decoration: underline; font-weight: 500;">Allgemeinen Mietbedingungen</a> gelesen und akzeptiere sie *</span>'''
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Links fixed in all DE files.")
