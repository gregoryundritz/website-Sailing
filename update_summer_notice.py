import glob

files = {
    'site/contact.html': ('* 2 jours minimum en juillet et août.', '* min. 2 jours en juillet et août.'),
    'site/de/kontakt.html': ('* Mindestbuchungsdauer von 2 Tagen im Juli und August.', '* Min. 2 Tage im Juli und August.'),
    'site/en/contact.html': ('* Minimum 2 days reservation in July and August.', '* Min. 2 days in July and August.')
}

for file_path, (old_text, new_text) in files.items():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        html = html.replace(old_text, new_text)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
