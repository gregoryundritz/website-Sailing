import glob
import re

files = {
    'site/contact.html': {
        'old_text': 'Vos dates de séjour :',
        'new_text': 'Vos dates de séjour <span style="font-size:13px; font-weight:400; color:var(--muted);">(Vérifiez les dispos ci-dessus)</span> :'
    },
    'site/de/kontakt.html': {
        'old_text': 'Ihre Reisedaten:',
        'new_text': 'Ihre Reisedaten <span style="font-size:13px; font-weight:400; color:var(--muted);">(Verfügbarkeit oben prüfen)</span>:'
    },
    'site/en/contact.html': {
        'old_text': 'Your travel dates:',
        'new_text': 'Your travel dates <span style="font-size:13px; font-weight:400; color:var(--muted);">(Check availability above)</span>:'
    }
}

for f, texts in files.items():
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
        
        # Current pattern:
        # <div class="resa-step-title">Vos dates de séjour :</div>
        # <div style="width: 100%; overflow: hidden; margin-bottom: 20px; border-radius: var(--r); box-shadow: 0 1px 3px rgba(0,0,0,0.1);">
        #   <iframe ...></iframe>
        # </div>
        
        old_title = f'<div class="resa-step-title">{texts["old_text"]}</div>'
        new_title = f'<div class="resa-step-title">{texts["new_text"]}</div>'
        
        # Regex to capture the calendar div and the title div
        pattern = r'(<div class="resa-step-title">.*?</div>)\s*(<div style="width: 100%; overflow: hidden; margin-bottom: 20px; border-radius: var\(--r\); box-shadow: 0 1px 3px rgba\(0,0,0,0\.1\);">\s*<iframe.*?</iframe>\s*</div>)'
        
        def replace_func(match):
            title = match.group(1)
            calendar = match.group(2)
            # update title text
            title = title.replace(texts["old_text"], texts["new_text"])
            # swap order
            return f'{calendar}\n            {title}'
            
        html = re.sub(pattern, replace_func, html, flags=re.DOTALL)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)
            
        print(f"Updated {f}")
    except FileNotFoundError:
        pass

print("Calendar and title swapped.")
