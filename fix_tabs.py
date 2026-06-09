import re

files_to_update = {
    'site/contact.html': ('Sélectionnez votre type de réservation :', 'Location standard', '⭐ Skipper Pass'),
    'site/de/kontakt.html': ('Wählen Sie Ihre Buchungsart :', 'Standardmiete', '⭐ Skipper Pass'),
    'site/en/contact.html': ('Select your booking type :', 'Standard rental', '⭐ Skipper Pass')
}

for path, (text, standard_text, pass_text) in files_to_update.items():
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the block wherever it is
    # It starts with <div class="resa-step" style="margin-bottom:24px;">
    # then has the minitext
    # then the resa-type-tabs div
    # then the buttons
    # ends with </div></div>
    
    match = re.search(r'(<div class="resa-step" style="margin-bottom:24px;">\s*<div style="font-size:14px; font-weight:600; margin-bottom:12px; color:var\(--navy\);">.*?</div>\s*<div id="resa-type-tabs".*?</div>\s*</div>)', html, flags=re.DOTALL)
    
    if match:
        block = match.group(1)
        html = html.replace(block, '') # Remove it from the bottom
    else:
        print(f"Could not find the block in {path}")
        continue
        
    radio_block = f'''<div class="resa-step" style="margin-bottom:24px;" id="section-type">
            <div style="font-size:14px; font-weight:600; margin-bottom:12px; color:var(--navy);">{text}</div>
            <div id="resa-type-tabs" style="display:flex; gap:8px; flex-wrap: wrap;">
              <label class="opt-check" style="flex:1; min-width:200px; margin:0;">
                <input type="radio" name="resa_type" value="standard" checked onchange="selectTab('standard')">
                <span class="oci" style="height:100%;"><span style="display:flex; align-items:center;"><span class="oc-radio"></span><span class="ocn" style="font-weight:600;" id="tab-label-standard">{standard_text}</span></span></span>
              </label>
              <label class="opt-check" style="flex:1; min-width:200px; margin:0;">
                <input type="radio" name="resa_type" value="pass" onchange="selectTab('pass')">
                <span class="oci" style="height:100%;"><span style="display:flex; align-items:center;"><span class="oc-radio"></span><span class="ocn" style="font-weight:600;" id="tab-label-pass">{pass_text}</span></span></span>
              </label>
            </div>
          </div>'''
          
    # Insert it right after <!-- ÉTAPE 1 : Type de séjour -->
    html = html.replace('<!-- ÉTAPE 1 : Type de séjour -->', f'<!-- ÉTAPE 1 : Type de séjour -->\n          {radio_block}')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Moved block back to step 1 and converted to radio buttons!")
