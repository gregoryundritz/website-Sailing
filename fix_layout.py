import glob
import re

# 1. Update style.css
with open('site/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('.resa-sec {\n      background: var(--sand)\n    }', '.resa-sec {\n      background: var(--sand);\n      padding: 80px 0;\n    }')
with open('site/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update HTML files
contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for file_path in contact_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Fix 1: Checkbox alignment
        html = html.replace('align-items: flex-start; gap: 10px; cursor: pointer; font-size: 14px; color: var(--muted); line-height: 1.5;',
                            'align-items: center; gap: 10px; cursor: pointer; font-size: 14px; color: var(--muted); line-height: 1.5;')
        html = html.replace('style="width: 18px; height: 18px; margin-top: 1px; cursor: pointer; flex-shrink: 0;"',
                            'style="width: 18px; height: 18px; cursor: pointer; flex-shrink: 0; margin: 0;"')

        # Fix typo in EN file
        html = html.replace('General Terms and Conditionsof', 'General Terms and Conditions of')

        # Fix 2: Message field gap
        html = html.replace('<div class="resa-step" style="margin-top:8px;">',
                            '<div class="resa-step" style="margin-top:-16px;">')

        # Fix 3: Space between Contact and Reservation
        html = html.replace('<section id="contact" style="padding-top: 120px; background:var(--white);">',
                            '<section id="contact" style="padding: 120px 0 80px; background:var(--white);">')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
