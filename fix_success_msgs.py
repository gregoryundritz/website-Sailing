import glob
import re

files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        old_btn_text = "btn.textContent = 'Demande envoyée !';"
        new_btn_text = "btn.textContent = (lang === 'de') ? 'Anfrage gesendet!' : ((lang === 'en') ? 'Request sent!' : 'Demande envoyée !');"
        
        old_note_text = "note.innerHTML = '✓ Votre demande est enregistrée. <strong>Vous recevrez un email de confirmation et votre lien de paiement sous 24h.</strong>';"
        new_note_text = "note.innerHTML = (lang === 'de') ? '✓ Ihre Anfrage wurde gespeichert. <strong>Sie erhalten innerhalb von 24 Stunden eine Bestätigungs-E-Mail und Ihren Zahlungslink.</strong>' : ((lang === 'en') ? '✓ Your request has been saved. <strong>You will receive a confirmation email and your payment link within 24 hours.</strong>' : '✓ Votre demande est enregistrée. <strong>Vous recevrez un email de confirmation et votre lien de paiement sous 24h.</strong>');"
        
        content = content.replace(old_btn_text, new_btn_text)
        content = content.replace(old_note_text, new_note_text)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Fixed translations in {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
