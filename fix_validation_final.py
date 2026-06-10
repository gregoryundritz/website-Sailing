import glob

files = {
    'site/contact.html': 'fr',
    'site/de/kontakt.html': 'de',
    'site/en/contact.html': 'en'
}

for file_path, hardcoded_lang in files.items():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Find the specific block to replace
        start_marker = "const lang = document.documentElement.lang || 'fr';"
        end_marker = "});\n\n      // Session storage logic"
        
        start_idx = html.find(start_marker)
        end_idx = html.find(end_marker, start_idx)
        
        if start_idx != -1 and end_idx != -1:
            old_block = html[start_idx:end_idx]
            
            new_block = f"""const lang = '{hardcoded_lang}';
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
        
        // Initial setup
        el.setCustomValidity('');
        if (!el.validity.valid) el.setCustomValidity(getCustomMsg(el));
        
        // Re-evaluate on input
        el.addEventListener('input', function(e) {{
          el.setCustomValidity('');
          if (!el.validity.valid) el.setCustomValidity(getCustomMsg(el));
          if (typeof saveFormData === 'function') saveFormData();
        }});
        
        // Ensure it's set on invalid
        el.addEventListener('invalid', function(e) {{
          el.setCustomValidity('');
          if (!el.validity.valid) el.setCustomValidity(getCustomMsg(el));
        }});
      """
            html = html.replace(old_block, new_block)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Updated {file_path}")
        else:
            print(f"Block not found in {file_path}")
    except Exception as e:
        print(e)
