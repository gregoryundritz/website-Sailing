import glob

files = {
    'site/contact.html': (
        '<div id="summer-notice" style="display: none; font-size: 13px; color: var(--gold); margin-bottom: 12px; margin-top: -8px;">min. 2 jours en juillet et août.</div>',
        '<div id="summer-notice" style="display: none; font-size: 14px; font-weight: 600; color: #7a5a10; background: #fff8ee; border: 1px solid #f0d898; border-radius: var(--r); padding: 10px 14px; margin-bottom: 16px; margin-top: -4px;">min. 2 jours en juillet et août</div>'
    ),
    'site/de/kontakt.html': (
        '<div id="summer-notice" style="display: none; font-size: 13px; color: var(--gold); margin-bottom: 12px; margin-top: -8px;">Min. 2 Tage im Juli und August.</div>',
        '<div id="summer-notice" style="display: none; font-size: 14px; font-weight: 600; color: #7a5a10; background: #fff8ee; border: 1px solid #f0d898; border-radius: var(--r); padding: 10px 14px; margin-bottom: 16px; margin-top: -4px;">Min. 2 Tage im Juli und August</div>'
    ),
    'site/en/contact.html': (
        '<div id="summer-notice" style="display: none; font-size: 13px; color: var(--gold); margin-bottom: 12px; margin-top: -8px;">Min. 2 days in July and August.</div>',
        '<div id="summer-notice" style="display: none; font-size: 14px; font-weight: 600; color: #7a5a10; background: #fff8ee; border: 1px solid #f0d898; border-radius: var(--r); padding: 10px 14px; margin-bottom: 16px; margin-top: -4px;">Min. 2 days in July and August</div>'
    )
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
