import re

with open('site/css/style.css', 'r', encoding='utf-8') as f: css = f.read()
if '.oc-radio' not in css:
    css += """
    .oc-radio {
      display: inline-block;
      width: 18px;
      height: 18px;
      min-width: 18px;
      border: 1.5px solid var(--sand2);
      border-radius: 50%;
      margin-right: 12px;
      transition: 0.2s;
      vertical-align: middle;
    }
    .opt-check input:checked + .oci .oc-radio {
      border-color: var(--gold);
      border-width: 5px;
    }
    input[type="checkbox"]:not(.opt-check input) {
      appearance: none;
      -webkit-appearance: none;
      width: 20px;
      height: 20px;
      min-width: 20px;
      border: 1.5px solid var(--sand2);
      border-radius: 50%;
      background: var(--white);
      cursor: pointer;
      position: relative;
      margin: 0;
      transition: 0.2s;
      vertical-align: middle;
    }
    input[type="checkbox"]:not(.opt-check input):checked {
      border-color: var(--gold);
      border-width: 6px;
    }
"""
    with open('site/css/style.css', 'w', encoding='utf-8') as f: f.write(css)

files_to_update = {
    'site/contact.html': 'fr',
    'site/de/kontakt.html': 'de',
    'site/en/contact.html': 'en'
}

for path, lang in files_to_update.items():
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # TABS
    html = re.sub(r'<div style="display:\s*flex;\s*gap:\s*8px;\s*margin-bottom:\s*24px;">\s*<button type="button" id="tab-standard".*?>(.*?)</button>\s*<button type="button" id="tab-pass".*?>(.*?)</button>\s*</div>',
                  r'''<div style="display:flex; gap:8px; margin-bottom:24px; flex-wrap: wrap;">
              <label class="opt-check" style="flex:1; min-width:200px;">
                <input type="radio" name="resa_type" value="standard" checked onchange="selectTab('standard')">
                <span class="oci"><span style="display:flex; align-items:center;"><span class="oc-radio"></span><span class="ocn" style="font-weight:600;">\1</span></span></span>
              </label>
              <label class="opt-check" style="flex:1; min-width:200px;">
                <input type="radio" name="resa_type" value="pass" onchange="selectTab('pass')">
                <span class="oci"><span style="display:flex; align-items:center;"><span class="oc-radio"></span><span class="ocn" style="font-weight:600;">\2</span></span></span>
              </label>
            </div>''', html, flags=re.DOTALL)

    # JS HTML Update
    html = html.replace('ro.innerHTML += `<label class="opt-check ${disabledClass}"><input type="checkbox" data-price="${o.price}" data-per="${o.per}" ${inputAttrs}><span class="oci"><span class="ocn">${gi(o.name)} ${o.name}</span><span class="ocp">+${o.price} CHF${pl}</span></span></label>`;',
                        'ro.innerHTML += `<label class="opt-check ${disabledClass}"><input type="checkbox" data-price="${o.price}" data-per="${o.per}" ${inputAttrs}><span class="oci"><span style="display:flex; align-items:center;"><span class="oc-radio"></span><span class="ocn">${gi(o.name)} ${o.name}</span></span><span class="ocp">+${o.price} CHF${pl}</span></span></label>`;')

    # JS selectTab update
    html = re.sub(r"btnP\.style\.background = 'var\(--gold\)';.*?if \(secP\) secP\.style\.display = 'block';", 
                  r"if (secP) secP.style.display = 'block';", html, flags=re.DOTALL)
    html = re.sub(r"if \(wrap\) wrap\.style\.display = 'block';\s*\} else \{", 
                  r"if (wrap) wrap.style.display = 'block';\n        var rad = document.querySelector('input[value=\"pass\"]');\n        if(rad) rad.checked = true;\n      } else {", html)
    html = re.sub(r"btnS\.style\.background = 'var\(--navy\)';.*?if \(secP\) secP\.style\.display = 'none';", 
                  r"if (secP) secP.style.display = 'none';\n        var rad = document.querySelector('input[value=\"standard\"]');\n        if(rad) rad.checked = true;", html, flags=re.DOTALL)

    # Placeholders
    if lang == 'de':
        html = html.replace('placeholder="Date de départ"', 'placeholder="Abreisedatum"')
        html = html.replace('placeholder="Date de retour"', 'placeholder="Rückgabedatum"')
        html = html.replace('placeholder="Prénom & Nom *"', 'placeholder="Vorname & Name *"')
        html = html.replace('placeholder="Email *"', 'placeholder="E-Mail *"')
        html = html.replace('placeholder="Rue, numéro"', 'placeholder="Strasse, Hausnummer"')
        html = html.replace('placeholder="NPA"', 'placeholder="PLZ"')
        html = html.replace('placeholder="Localité"', 'placeholder="Ort"')
        html = html.replace('placeholder="Téléphone"', 'placeholder="Telefon"')
        html = html.replace('placeholder="Votre message"', 'placeholder="Ihre Nachricht"')
    elif lang == 'en':
        html = html.replace('placeholder="Date de départ"', 'placeholder="Departure date"')
        html = html.replace('placeholder="Date de retour"', 'placeholder="Return date"')
        html = html.replace('placeholder="Prénom & Nom *"', 'placeholder="First & Last Name *"')
        html = html.replace('placeholder="Email *"', 'placeholder="Email *"')
        html = html.replace('placeholder="Rue, numéro"', 'placeholder="Street, Number"')
        html = html.replace('placeholder="NPA"', 'placeholder="ZIP code"')
        html = html.replace('placeholder="Localité"', 'placeholder="City"')
        html = html.replace('placeholder="Téléphone"', 'placeholder="Phone"')
        html = html.replace('placeholder="Votre message"', 'placeholder="Your message"')
        
        html = html.replace('OF CHARTER', '')
        html = html.replace('of charter', '')
        html = html.replace('of Charter', '')

    # Underline conditions & remove link underline
    html = re.sub(r'(text-decoration:\s*underline;\s*text-underline-offset:\s*3px;\s*color:\s*var\(--navy\);)', r'color: var(--navy);', html)
    html = re.sub(r'<span style="text-transform:\s*uppercase;\s*font-size:\s*12px;\s*font-weight:\s*500;\s*color:\s*var\(--muted\);\s*letter-spacing:\s*0.05em;?">', 
                  r'<span style="text-transform:uppercase; font-size:12px; font-weight:500; color:var(--muted); letter-spacing:0.05em; text-decoration:underline; text-underline-offset:3px;">', html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
