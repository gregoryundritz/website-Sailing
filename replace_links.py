import glob
import re

ocn_link = "https://www.ocn.ch/de/schiff-fahren/schiffsfuehrerausweis/kategorien"

# Update DE files
de_files = glob.glob('site/de/*.html')
for f in de_files:
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    html = html.replace('href="segelpruefung-schweiz.html"', f'href="{ocn_link}" target="_blank"')
    html = html.replace('href="/segelpruefung-schweiz.html"', f'href="{ocn_link}" target="_blank"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)

# Update EN files
en_files = glob.glob('site/en/*.html')
for f in en_files:
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    html = html.replace('href="sailing-license-switzerland.html"', f'href="{ocn_link}" target="_blank"')
    html = html.replace('href="/sailing-license-switzerland.html"', f'href="{ocn_link}" target="_blank"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)

print("Links replaced successfully.")
