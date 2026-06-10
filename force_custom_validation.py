import glob

files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # 1. Remove the old custom validation loop (lines starting from `Array.from(form.elements).forEach` up to `// Session storage logic`)
        start_marker = "Array.from(form.elements).forEach(el => {"
        end_marker = "// Session storage logic"
        
        start_idx = html.find(start_marker)
        end_idx = html.find(end_marker, start_idx)
        
        if start_idx != -1 and end_idx != -1:
            # We remove it completely
            html = html[:start_idx] + html[end_idx:]

        # 2. Modify the Netlify Form AJAX Handling block
        # We look for:
        #           const formData = new FormData(resaForm);
        #
        #           btn.disabled = true;
        
        ajax_start = "          const btn = document.getElementById('resa-submit-btn');"
        
        if ajax_start in html:
            custom_validation_code = """          const btn = document.getElementById('resa-submit-btn');
          const note = document.getElementById('resa-note');
          
          // Manual Custom Validation
          let isFormValid = true;
          let firstInvalid = null;
          
          for (let el of resaForm.elements) {
            if (el.willValidate && !el.validity.valid) {
              isFormValid = false;
              if (!firstInvalid) firstInvalid = el;
            }
          }
          
          if (!isFormValid) {
             const docLang = document.documentElement.lang || 'fr';
             const errMsgs = {
               fr: { req: 'Veuillez renseigner ce champ.', email: 'Veuillez entrer une adresse e-mail valide.' },
               en: { req: 'Please fill out this field.', email: 'Please enter a valid email address.' },
               de: { req: 'Bitte füllen Sie dieses Feld aus.', email: 'Bitte geben Sie eine gültige E-Mail-Adresse ein.' }
             };
             let msg = errMsgs[docLang] ? errMsgs[docLang].req : errMsgs.fr.req;
             if (firstInvalid.type === 'email' || firstInvalid.name === 'email') {
                 msg = firstInvalid.validity.valueMissing ? (errMsgs[docLang] ? errMsgs[docLang].req : errMsgs.fr.req) : (errMsgs[docLang] ? errMsgs[docLang].email : errMsgs.fr.email);
             }
             if (note) {
                 note.innerHTML = '<span style="color:#d9534f;font-weight:600;display:block;padding:12px;background:#fdf2f2;border:1px solid #d9534f;border-radius:6px;margin-bottom:12px;">⚠️ ' + msg + '</span>';
             }
             firstInvalid.style.borderColor = '#d9534f';
             // Scroll to the invalid element
             firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
             firstInvalid.focus({ preventScroll: true });
             
             firstInvalid.addEventListener('input', function() {
                 firstInvalid.style.borderColor = '';
                 if (note) note.innerHTML = '';
             }, {once: true});
             return;
          }"""
            
            html = html.replace("          const btn = document.getElementById('resa-submit-btn');", custom_validation_code)
            
            # Add novalidate
            html = html.replace("resaForm.addEventListener('submit'", "resaForm.setAttribute('novalidate', 'true');\n        resaForm.addEventListener('submit'")
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"Updated {file_path}")
        else:
            print(f"Could not find AJAX handler in {file_path}")
            
    except Exception as e:
        print(f"Error on {file_path}: {e}")
