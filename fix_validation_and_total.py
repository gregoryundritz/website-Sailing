import re
import glob

# For EN and DE files, replace the total-bar section and add custom validity for required inputs
files = {
    'site/de/kontakt.html': {
        'total_label': 'Gesamtbetrag inkl. MwSt.',
        'validation_msg': 'Bitte füllen Sie dieses Feld aus.'
    },
    'site/en/contact.html': {
        'total_label': 'Total amount VAT incl.',
        'validation_msg': 'Please fill out this field.'
    }
}

for path, texts in files.items():
    try:
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Fix Total Bar
        total_bar_pattern = re.compile(r'<div class="total-bar">.*?</div>', re.DOTALL)
        new_total_bar = f"""<div class="total-bar">
              <span>{texts['total_label']}</span>
              <span class="total-val" id="resa-total">— CHF</span>
            </div>"""
        html = re.sub(total_bar_pattern, new_total_bar, html, count=1)

        # Fix required input validations
        # We need to add oninvalid and oninput to all input and textarea elements that have 'required'
        
        def replace_required(match):
            element = match.group(0)
            if 'oninvalid=' not in element:
                # Add the attributes before the closing bracket
                return element.replace('required>', f'required oninvalid="this.setCustomValidity(\'{texts["validation_msg"]}\')" oninput="this.setCustomValidity(\'\')">')
            return element

        html = re.sub(r'<input[^>]+required[^>]*>', replace_required, html)
        html = re.sub(r'<textarea[^>]+required[^>]*>', replace_required, html)
        html = re.sub(r'<input[^>]+required>', replace_required, html) # some tags end with exactly `required>`

        # Add logic to accept_cg checkbox to clear validation correctly since it's a checkbox, onchange might be better, or oninput works.
        # oninput works for checkboxes in modern browsers to clear custom validity

        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Updated {path}")
    except FileNotFoundError:
        print(f"File not found: {path}")
