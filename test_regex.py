import glob
import re

files = {
    'site/contact.html': 'fr',
    'site/de/kontakt.html': 'de',
    'site/en/contact.html': 'en'
}

for file_path, hardcoded_lang in files.items():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Find the form validation block and replace it entirely
        pattern = r'// ── Form Validation & Session Storage ──\s*document\.addEventListener\(\'DOMContentLoaded\', function\(\) \{\s*const form = document\.querySelector\(\'form\[name="reservation"\]\'\);\s*if \(\!form\) return;\s*(const lang =.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\n.*?\}\);)'
        
        new_val = f"""const lang = '{hardcoded_lang}';
      const msgs = {{
        fr: {{ req: 'Veuillez renseigner ce champ.', email: 'Veuillez entrer une adresse e-mail valide.' }},
        en: {{ req: 'Please fill out this field.', email: 'Please enter a valid email address.' }},
        de: {{ req: 'Bitte füllen Sie dieses Feld aus.', email: 'Bitte geben Sie eine gültige E-Mail-Adresse ein.' }}
      }};

      function getCustomMsg(el) {{
        if (el.validity.valueMissing) return msgs[lang].req;
        if (el.type === 'email' || el.name === 'email') return msgs[lang].email;
        return msgs[lang].req;
      }}

      Array.from(form.elements).forEach(el => {{
        if (!el.willValidate) return;
        el.removeAttribute('oninvalid');
        el.removeAttribute('oninput');
        
        // Set immediately
        el.setCustomValidity('');
        if (!el.validity.valid) el.setCustomValidity(getCustomMsg(el));

        el.addEventListener('input', function(e) {{
          el.setCustomValidity('');
          if (!el.validity.valid) el.setCustomValidity(getCustomMsg(el));
          if (typeof saveFormData === 'function') saveFormData();
        }});
        
        el.addEventListener('invalid', function(e) {{
          el.setCustomValidity('');
          if (!el.validity.valid) el.setCustomValidity(getCustomMsg(el));
        }});
      }});"""
        
        # Replace using regex to match the old block
        # We need to be careful with the regex. Let's just use string replace for the core part if regex is tricky.
        pass
    except Exception as e:
        print(e)
