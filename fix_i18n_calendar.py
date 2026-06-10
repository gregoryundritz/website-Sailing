import glob

files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # 1. Fix flatpickr language
        old_loc = "var loc = (typeof flatpickr.l10ns !== 'undefined' && flatpickr.l10ns.fr) ? 'fr' : 'default';"
        new_loc = """var docLang = document.documentElement.lang || 'fr';
      var loc = (typeof flatpickr.l10ns !== 'undefined' && flatpickr.l10ns[docLang]) ? docLang : 'default';"""
        html = html.replace(old_loc, new_loc)

        # 2. Fix email validation logic
        old_val = """        if (!el.validity.valid) {
          if (el.validity.valueMissing) el.setCustomValidity(msgs[lang].req);
          else if (el.validity.typeMismatch) el.setCustomValidity(msgs[lang].email);
        }"""
        new_val = """        if (!el.validity.valid) {
          if (el.validity.valueMissing) el.setCustomValidity(msgs[lang].req);
          else if (el.type === 'email') el.setCustomValidity(msgs[lang].email);
          else el.setCustomValidity(msgs[lang].req);
        }"""
        html = html.replace(old_val, new_val)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
