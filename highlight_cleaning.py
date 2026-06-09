import glob
import re

contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for f in contact_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()

        # Fix bad escape `\span` to `<span`
        html = re.sub(r'data-price="60" data-per="forfait"([^>]*)>\s*<span class="oci"><span class="ocn">🧹 Nettoyage final\s*\(obligatoire\)</span><span class="ocp">\+60 CHF</span>',
                      r'data-price="50" data-per="forfait"\1><span class="oci" style="background: rgba(184, 131, 46, 0.15); border: 2px solid var(--gold); opacity: 1;"><span class="ocn">🧹 Nettoyage final (obligatoire)</span><span class="ocp">+50 CHF</span>',
                      html)
        
        html = re.sub(r'data-price="60" data-per="forfait"([^>]*)>\s*<span class="oci"><span class="ocn">🧹 Endreinigung\s*\(obligatorisch\)</span><span class="ocp">\+60 CHF</span>',
                      r'data-price="50" data-per="forfait"\1><span class="oci" style="background: rgba(184, 131, 46, 0.15); border: 2px solid var(--gold); opacity: 1;"><span class="ocn">🧹 Endreinigung (obligatorisch)</span><span class="ocp">+50 CHF</span>',
                      html)
                      
        html = re.sub(r'data-price="60" data-per="forfait"([^>]*)>\s*<span class="oci"><span class="ocn">🧹 Final cleaning\s*\(mandatory\)</span><span class="ocp">\+60 CHF</span>',
                      r'data-price="50" data-per="forfait"\1><span class="oci" style="background: rgba(184, 131, 46, 0.15); border: 2px solid var(--gold); opacity: 1;"><span class="ocn">🧹 Final cleaning (mandatory)</span><span class="ocp">+50 CHF</span>',
                      html)
                      
        html = re.sub(r'data-price="50" data-per="forfait"([^>]*)>\s*<span class="oci"><span class="ocn">🧹 Nettoyage final\s*\(obligatoire\)</span><span class="ocp">\+50 CHF</span>',
                      r'data-price="50" data-per="forfait"\1><span class="oci" style="background: rgba(184, 131, 46, 0.15); border: 2px solid var(--gold); opacity: 1;"><span class="ocn">🧹 Nettoyage final (obligatoire)</span><span class="ocp">+50 CHF</span>',
                      html)

        html = re.sub(r'data-price="50" data-per="forfait"([^>]*)>\s*<span class="oci"><span class="ocn">🧹 Endreinigung\s*\(obligatorisch\)</span><span class="ocp">\+50 CHF</span>',
                      r'data-price="50" data-per="forfait"\1><span class="oci" style="background: rgba(184, 131, 46, 0.15); border: 2px solid var(--gold); opacity: 1;"><span class="ocn">🧹 Endreinigung (obligatorisch)</span><span class="ocp">+50 CHF</span>',
                      html)

        html = re.sub(r'data-price="50" data-per="forfait"([^>]*)>\s*<span class="oci"><span class="ocn">🧹 Final cleaning\s*\(mandatory\)</span><span class="ocp">\+50 CHF</span>',
                      r'data-price="50" data-per="forfait"\1><span class="oci" style="background: rgba(184, 131, 46, 0.15); border: 2px solid var(--gold); opacity: 1;"><span class="ocn">🧹 Final cleaning (mandatory)</span><span class="ocp">+50 CHF</span>',
                      html)

        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)
            
        print(f"Updated {f}")
    except FileNotFoundError:
        pass
