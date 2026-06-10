import glob
import re

# 1. Update style.css
with open('site/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.resa-sec {\n      background: var(--sand);\n      padding: 80px 0;\n    }', '.resa-sec {\n      background: var(--sand);\n      padding: 40px 0 80px;\n    }')
with open('site/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update HTML files
contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for file_path in contact_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        html = html.replace('<section id="contact" style="padding: 120px 0 80px; background:var(--white);">',
                            '<section id="contact" style="padding: 120px 0 0px; background:var(--white);">')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
