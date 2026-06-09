import glob
import re

contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for f in contact_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
            
        # We need to add `if (el.type === 'file') return;` before `if (el.type === 'checkbox' || el.type === 'radio') {`
        # Current logic:
        #             if (!el) return;
        #             if (el.type === 'checkbox' || el.type === 'radio') {
        
        target = r"if \(!el\) return;\s*if \(el\.type === 'checkbox'"
        replacement = r"if (!el) return;\n            if (el.type === 'file') return;\n            if (el.type === 'checkbox'"
        
        html = re.sub(target, replacement, html)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)
            
        print(f"Fixed file input bug in {f}")
    except FileNotFoundError:
        pass
