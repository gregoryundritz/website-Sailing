import glob
import re

contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for file_path in contact_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # 1. Update form validation
        old_val = """      // Custom validation messages
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
      });"""
        new_val = """      // Custom validation messages
      function updateValidity(el) {
        el.setCustomValidity('');
        if (!el.validity.valid) {
          if (el.validity.valueMissing) el.setCustomValidity(msgs[lang].req);
          else if (el.validity.typeMismatch) el.setCustomValidity(msgs[lang].email);
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
        html = html.replace(old_val, new_val)

        # 2. Update Max 14 jours
        old_max = "days > 14 ? 'Max 14 jours' : '— CHF'"
        new_max = "days > 14 ? ((lang === 'de') ? 'Max 14 Tage' : ((lang === 'en') ? 'Max 14 days' : 'Max 14 jours')) : '— CHF'"
        html = html.replace(old_max, new_max)

        # 3. Update Envoi en cours
        old_sending = "btn.textContent = 'Envoi en cours...';"
        new_sending = "btn.textContent = (lang === 'de') ? 'Wird gesendet...' : ((lang === 'en') ? 'Sending...' : 'Envoi en cours...');"
        html = html.replace(old_sending, new_sending)

        # 4. Update Erreur and Réessayer
        old_err1 = "btn.textContent = 'Réessayer';"
        new_err1 = "btn.textContent = (lang === 'de') ? 'Erneut versuchen' : ((lang === 'en') ? 'Retry' : 'Réessayer');"
        html = html.replace(old_err1, new_err1)
        
        old_err2 = "alert('Erreur lors de l\\'envoi. Veuillez réessayer.');"
        new_err2 = "alert((lang === 'de') ? 'Fehler beim Senden. Bitte versuchen Sie es erneut.' : ((lang === 'en') ? 'Error sending. Please try again.' : 'Erreur lors de l\\'envoi. Veuillez réessayer.'));"
        html = html.replace(old_err2, new_err2)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
