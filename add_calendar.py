import glob

files = {
    'site/contact.html': 'fr',
    'site/de/kontakt.html': 'de',
    'site/en/contact.html': 'en'
}

for f, lang in files.items():
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
        
        # Calendar snippet with responsive width and correct language
        calendar_snippet = f'''
            <div style="width: 100%; overflow: hidden; margin-bottom: 20px; border-radius: var(--r); box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
              <iframe src="https://calendar.google.com/calendar/embed?height=400&wkst=2&ctz=Europe%2FZurich&showPrint=0&showTitle=0&showTabs=0&showCalendars=0&showTz=0&hl={lang}&src=MzUyYTIzZjE3MGQ0YjhhMGQ0MGIxODMzMDNiYjEyZWE0MDM1MGZjMmU0MjBiMTJkYWM2NDg2OTVkYjhhNDA5NUBncm91cC5jYWxlbmRhci5nb29nbGUuY29t&color=%234285f4" style="border-width:0; width: 100%; height: 400px;" frameborder="0" scrolling="no"></iframe>
            </div>
            <div class="fr">'''

        # We inject it right before the `<div class="fr">` inside `#section-standard`
        # But we need to make sure we don't duplicate it if run multiple times
        if "calendar.google.com/calendar/embed" not in html:
            # The search string has a newline and spaces to match the formatting exactly
            search_str = '''<div class="resa-step" id="section-standard">\n            <div class="resa-step-title">'''
            
            # Since the title differs per language, we split by the title div.
            # Instead of matching the exact title string, we can regex replace:
            import re
            html = re.sub(
                r'(<div class="resa-step" id="section-standard">\s*<div class="resa-step-title">.*?</div>\s*)<div class="fr">',
                r'\1' + calendar_snippet,
                html
            )
            
            with open(f, 'w', encoding='utf-8') as file:
                file.write(html)
            print(f"Added calendar to {f}")
    except FileNotFoundError:
        pass

print("Calendar injection complete.")
