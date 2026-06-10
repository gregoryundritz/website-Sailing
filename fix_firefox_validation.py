import glob
import re

files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        old_val = """      // Custom validation messages
      function updateValidity(el) {
        el.setCustomValidity('');
        if (!el.validity.valid) {
          if (el.validity.valueMissing) el.setCustomValidity(msgs[lang].req);
          else if (el.type === 'email') el.setCustomValidity(msgs[lang].email);
          else el.setCustomValidity(msgs[lang].req);
        }
      }
      Array.from(form.elements).forEach(el => {
        el.removeAttribute('oninvalid');
        el.removeAttribute('oninput');
        updateValidity(el);
        el.addEventListener('input', function(e) {
          updateValidity(el);
          saveFormData();
        });
        el.addEventListener('invalid', function(e) {
          updateValidity(el);
        });
      });"""
        
        new_val = """      // Custom validation messages
      function updateValidity(el) {
        if (!el.setCustomValidity) return;
        el.setCustomValidity(''); // Clear to check native validity
        if (!el.validity.valid) {
          if (el.validity.valueMissing) el.setCustomValidity(msgs[lang].req);
          else if (el.type === 'email') el.setCustomValidity(msgs[lang].email);
          else el.setCustomValidity(msgs[lang].req);
        }
      }
      Array.from(form.elements).forEach(el => {
        el.removeAttribute('oninvalid');
        el.removeAttribute('oninput');
        
        // Initial setup
        updateValidity(el);
        
        // Re-evaluate on input
        el.addEventListener('input', function(e) {
          updateValidity(el);
          if (typeof saveFormData === 'function') saveFormData();
        });
        
        // DO NOT clear on invalid event, Firefox will grab the native string!
        // Just let the browser display the custom message we already set.
      });"""
        html = html.replace(old_val, new_val)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
