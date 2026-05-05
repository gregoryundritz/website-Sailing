import os

with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Header: From <!DOCTYPE html> down to </nav>
header_end = html.find('</nav>') + len('</nav>')
header = html[:header_end]

# Footer: From <footer> to the end of the file
footer_start = html.rfind('<footer>')
footer = html[footer_start:]

hreflang_tags = """
  <!-- Hreflang Tags pour SEO Multilingue -->
  <link rel="alternate" hreflang="fr" href="https://voilier-neuchatel.ch/" />
  <link rel="alternate" hreflang="x-default" href="https://voilier-neuchatel.ch/" />
"""
header = header.replace('</head>', hreflang_tags + '\n</head>')

# Update Navigation links
header = header.replace('href="#bateau"', 'href="bateau.html"')
header = header.replace('href="#tarifs"', 'href="tarifs.html"')
header = header.replace('href="#infos"', 'href="itineraires.html"')
header = header.replace('href="#avis"', 'href="index.html#avis"')
header = header.replace('href="#localisation"', 'href="index.html#localisation"')
header = header.replace('href="#apropos"', 'href="index.html#apropos"')
header = header.replace('href="#contact"', 'href="contact.html"')
header = header.replace('href="#reservation"', 'href="contact.html#reservation"')

footer = footer.replace('href="#bateau"', 'href="bateau.html"')
footer = footer.replace('href="#tarifs"', 'href="tarifs.html"')
footer = footer.replace('href="#infos"', 'href="itineraires.html"')
footer = footer.replace('href="#avis"', 'href="index.html#avis"')
footer = footer.replace('href="#localisation"', 'href="index.html#localisation"')
footer = footer.replace('href="#apropos"', 'href="index.html#apropos"')
footer = footer.replace('href="#contact"', 'href="contact.html"')
footer = footer.replace('href="#reservation"', 'href="contact.html#reservation"')

def extract_section(start_str, end_str):
    start = html.find(start_str)
    if start == -1: return ""
    end = html.find(end_str, start)
    if end == -1: return ""
    return html[start:end+len(end_str)]

def create_page(filename, title_tag, content):
    new_header = header.replace('<title>Voilier Lac de Neuchâtel — Cheyres, Suisse | Maxus 21</title>', f'<title>{title_tag}</title>')
    page_html = new_header + "\n" + content + "\n" + footer
    with open(f'site/{filename}', 'w', encoding='utf-8') as f:
        f.write(page_html)

# 1. Bateau
bateau_section = extract_section('<section id="bateau">', '</section>')
gal_section = extract_section('<div class="gal">', '<!-- INFOS -->')
if gal_section: gal_section = gal_section.replace('<!-- INFOS -->', '')
create_page("bateau.html", "Le Bateau — Voilier Lac de Neuchâtel", bateau_section + "\n" + gal_section)

# 2. Tarifs
tarifs_section = extract_section('<section id="tarifs" class="tarifs-sec">', '</section>')
pass_skipper_section = extract_section('<section id="pass-skipper"', '</section>')
create_page("tarifs.html", "Tarifs de Location — Voilier Lac de Neuchâtel", tarifs_section + "\n" + pass_skipper_section)

# 3. Contact
contact_section = extract_section('<section id="contact"', '</section>')
create_page("contact.html", "Contact et Réservation — Voilier Lac de Neuchâtel", contact_section)

# 4. Itineraires
itineraires_content = """
<section id="itineraires" style="padding: 100px 24px; background: var(--white); min-height: 60vh; margin-top: 60px;">
  <div class="ct">
    <div class="rv" style="text-align:center;">
      <p class="sec-ey">Découverte</p>
      <h2 class="sec-h">Itinéraires <em>recommandés</em></h2>
      <p class="sec-p">Le lac de Neuchâtel regorge de coins magnifiques. Voici quelques idées pour vos sorties.</p>
    </div>
    <div class="rv" style="margin-top: 40px; display: grid; gap: 40px; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
      <div style="background: var(--sand); padding: 32px; border-radius: var(--r); border: 1px solid var(--sand2);">
        <h3 style="font-family:'Cormorant Garamond',serif;font-size:24px;color:var(--navy);margin-bottom:12px;">1. Cheyres à Estavayer-le-Lac</h3>
        <p style="font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:16px;">Durée : 2 à 3 heures</p>
        <p style="color:var(--text);line-height:1.7;">Une belle navigation le long de la côte sud avec une arrivée pittoresque au pied du château de Chenaux.</p>
      </div>
      <div style="background: var(--sand); padding: 32px; border-radius: var(--r); border: 1px solid var(--sand2);">
        <h3 style="font-family:'Cormorant Garamond',serif;font-size:24px;color:var(--navy);margin-bottom:12px;">2. La Grande Cariçaie</h3>
        <p style="font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:16px;">Durée : 1 journée</p>
        <p style="color:var(--text);line-height:1.7;">Découvrez la plus grande réserve naturelle lacustre de Suisse. Mouillage possible dans des eaux turquoises près des bancs de sable.</p>
      </div>
      <div style="background: var(--sand); padding: 32px; border-radius: var(--r); border: 1px solid var(--sand2);">
        <h3 style="font-family:'Cormorant Garamond',serif;font-size:24px;color:var(--navy);margin-bottom:12px;">3. Cap sur Yverdon-les-Bains</h3>
        <p style="font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:16px;">Durée : Demi-journée</p>
        <p style="color:var(--text);line-height:1.7;">Profitez du vent thermique régulier (la bise ou le sud-ouest) pour descendre confortablement jusqu'au bout du lac.</p>
      </div>
    </div>
  </div>
</section>
"""
create_page("itineraires.html", "Itinéraires et Découvertes — Voilier Lac de Neuchâtel", itineraires_content)

# Clean index.html
new_index = html.replace(bateau_section, '')
if gal_section: new_index = new_index.replace(gal_section, '')
new_index = new_index.replace(tarifs_section, '')
new_index = new_index.replace(pass_skipper_section, '')
new_index = new_index.replace(contact_section, '')

new_index = new_index.replace('</head>', hreflang_tags + '\n</head>')

new_index = new_index.replace('href="#bateau"', 'href="bateau.html"')
new_index = new_index.replace('href="#tarifs"', 'href="tarifs.html"')
new_index = new_index.replace('href="#infos"', 'href="itineraires.html"')
new_index = new_index.replace('href="#contact"', 'href="contact.html"')
new_index = new_index.replace('href="#reservation"', 'href="contact.html#reservation"')

with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(new_index)

print("Split complete!")
