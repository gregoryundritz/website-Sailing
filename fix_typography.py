import glob
import re

contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for f in contact_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()

        # Update FR
        html = re.sub(r'<span class="oci" style="[^"]*"><span class="ocn">🧹 Nettoyage final \(obligatoire\)</span>',
                      r'<span class="oci" style="background: #fff8ee; border: 2px solid var(--gold);"><span class="ocn" style="color: var(--navy); font-weight: 700; font-size: 14px;">🧹 Nettoyage final (obligatoire)</span>',
                      html)
        
        # Update DE
        html = re.sub(r'<span class="oci" style="[^"]*"><span class="ocn">🧹 Endreinigung \(obligatorisch\)</span>',
                      r'<span class="oci" style="background: #fff8ee; border: 2px solid var(--gold);"><span class="ocn" style="color: var(--navy); font-weight: 700; font-size: 14px;">🧹 Endreinigung (obligatorisch)</span>',
                      html)
                      
        # Update EN
        html = re.sub(r'<span class="oci" style="[^"]*"><span class="ocn">🧹 Final cleaning \(mandatory\)</span>',
                      r'<span class="oci" style="background: #fff8ee; border: 2px solid var(--gold);"><span class="ocn" style="color: var(--navy); font-weight: 700; font-size: 14px;">🧹 Final cleaning (mandatory)</span>',
                      html)
                      
        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)
            
        print(f"Updated typography in {f}")
    except FileNotFoundError:
        pass
