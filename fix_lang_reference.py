import glob

files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        target = "          const formData = new FormData(resaForm);"
        replacement = "          const lang = document.documentElement.lang || 'fr';\n          const formData = new FormData(resaForm);"
        
        if target in html:
            html = html.replace(target, replacement)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Updated {file_path}")
        else:
            print(f"Target not found in {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
