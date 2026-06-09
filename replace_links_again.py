import glob

old_link = "https://www.ocn.ch/de/schiff-fahren/schiffsfuehrerausweis/kategorien"
new_link = "https://www.bav.admin.ch/de/freizeitschifffahrt#FAQ-Freizeitschifffahrt"

# Update DE files
de_files = glob.glob('site/de/*.html')
for f in de_files:
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    if old_link in html:
        html = html.replace(old_link, new_link)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)

# Update EN files
en_files = glob.glob('site/en/*.html')
for f in en_files:
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    if old_link in html:
        html = html.replace(old_link, new_link)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)

print("Links updated successfully.")
