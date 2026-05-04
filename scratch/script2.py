import re

with open('/home/gregory/Voilier/site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Move pass-skipper section after tarifs
pass_regex = re.compile(r'(<!-- PASS SKIPPER -->[\s\S]*?<section id="pass-skipper"[\s\S]*?</section>\s*)')
pass_match = pass_regex.search(html)

if pass_match:
    pass_text = pass_match.group(1)
    html = html.replace(pass_text, '')
    tarifs_regex = re.compile(r'(<!-- TARIFS -->[\s\S]*?<section id="tarifs"[\s\S]*?</section>\s*)')
    tarifs_match = tarifs_regex.search(html)
    if tarifs_match:
        html = html.replace(tarifs_match.group(1), tarifs_match.group(1) + '\n' + pass_text)

# 2. Adjust calendar width
html = html.replace('max-width: 800px; width: 100%; margin-left: auto; margin-right: auto;', 'max-width: 680px; width: 100%; margin-left: auto; margin-right: auto;')

# 3. Flatpickr background to white
html = html.replace('.flatpickr-input {\n      background: var(--sand) !important;', '.flatpickr-input {\n      background: var(--white) !important;')

# 4. Remove Formulaire de demande & Carburant inclus text
html = re.sub(r'<p class="sec-ey">Formulaire de demande</p>\s*', '', html)
html = re.sub(r'<p class="sec-p" style="margin:0 auto">Carburant inclus · Aucun paiement maintenant · Confirmation sous 24h</p>\s*', '', html)

# 5. Remove paiement integral text
html = html.replace('CHF · paiement intégral', 'CHF')

# 6. Remove Autopilote from #resa-options
html = re.sub(r'<label class="opt-check"><input type="checkbox" data-price="20" data-per="jour"\s*onchange="updateTotal\(\)"><span class="oci"><span class="ocn">🤖 Autopilote</span><span class="ocp">\+20\s*CHF/j</span></span></label>\s*', '', html)

# 7. Remove Rencontre personnelle from #resa-options
html = re.sub(r'<label class="opt-check"><input type="checkbox" data-price="50" data-per="forfait"\s*onchange="updateTotal\(\)"><span class="oci"><span class="ocn">🤝 Rencontre personnelle</span><span\s*class="ocp">\+50 CHF</span></span></label>\s*', '', html)

with open('/home/gregory/Voilier/site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")
