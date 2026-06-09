import glob
import re

# 1. Remove "of Charter" from English pages
en_files = glob.glob('site/en/*.html')
for f in en_files:
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    html = re.sub(r'(?i)of charter\b', '', html)
    # Also clean up "General Terms and Conditions "
    html = html.replace('General Terms and Conditions ', 'General Terms and Conditions')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)

# 2. Add validation script and session storage to contact.html files
contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

validation_script = """
    // ── Form Validation & Session Storage ──
    document.addEventListener('DOMContentLoaded', function() {
      const form = document.querySelector('form[name="reservation"]');
      if (!form) return;
      
      const lang = document.documentElement.lang || 'fr';
      const msgs = {
        fr: { req: 'Veuillez renseigner ce champ.', email: 'Veuillez entrer une adresse e-mail valide.' },
        en: { req: 'Please fill out this field.', email: 'Please enter a valid email address.' },
        de: { req: 'Bitte füllen Sie dieses Feld aus.', email: 'Bitte geben Sie eine gültige E-Mail-Adresse ein.' }
      };

      // Custom validation messages
      Array.from(form.elements).forEach(el => {
        // Remove inline handlers if they exist
        el.removeAttribute('oninvalid');
        el.removeAttribute('oninput');
        
        el.addEventListener('invalid', function(e) {
          if (el.validity.valueMissing) el.setCustomValidity(msgs[lang].req);
          else if (el.validity.typeMismatch) el.setCustomValidity(msgs[lang].email);
        });
        el.addEventListener('input', function(e) {
          el.setCustomValidity('');
          saveFormData();
        });
      });

      // Session storage logic
      function saveFormData() {
        const formData = new FormData(form);
        const data = {};
        for (let [k, v] of formData.entries()) {
          data[k] = v;
        }
        sessionStorage.setItem('resa_draft', JSON.stringify(data));
      }

      function loadFormData() {
        const saved = sessionStorage.getItem('resa_draft');
        if (!saved) return;
        try {
          const data = JSON.parse(saved);
          Object.keys(data).forEach(k => {
            const el = form.elements[k];
            if (!el) return;
            if (el.type === 'checkbox' || el.type === 'radio') {
              if (el instanceof RadioNodeList) {
                el.value = data[k];
              } else {
                el.checked = (data[k] === el.value || data[k] === 'on');
              }
            } else {
              el.value = data[k];
            }
          });
          if (data.date_depart && window.fpS) window.fpS.setDate(data.date_depart);
          if (data.date_retour && window.fpE) window.fpE.setDate(data.date_retour);
          if (typeof updateTotal === 'function') updateTotal();
        } catch (e) {
          console.error('Failed to parse form draft', e);
        }
      }
      
      // Load form data immediately
      loadFormData();
      
      // Also save data on flatpickr changes
      if (window.fpS) window.fpS.config.onChange.push(saveFormData);
      if (window.fpE) window.fpE.config.onChange.push(saveFormData);
    });
"""

for f in contact_files:
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    # Remove old inline oninvalid
    html = re.sub(r'oninvalid="[^"]*"', '', html)
    html = re.sub(r'oninput="this.setCustomValidity\(\'\'\)"', '', html)
    
    # Inject script if not present
    if "Form Validation & Session Storage" not in html:
        html = html.replace('// ── Total ──', validation_script + '\n    // ── Total ──')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)

print("Applied form fixes.")
