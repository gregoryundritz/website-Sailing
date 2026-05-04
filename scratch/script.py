import re

with open('/home/gregory/Voilier/site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Move tarifs section before contact section
tarifs_regex = re.compile(r'(<!-- TARIFS -->[\s\S]*?<section id="tarifs"[\s\S]*?</section>\s*)')
tarifs_match = tarifs_regex.search(html)

if tarifs_match:
    tarifs_text = tarifs_match.group(1)
    html = html.replace(tarifs_text, '')
    contact_regex = re.compile(r'(<!-- CONTACT -->\s*<section id="contact")')
    html = contact_regex.sub(tarifs_text + r'\1', html)

# 2. Make form inputs lighter
html = html.replace('background: var(--sand);', 'background: var(--white);')

with open('/home/gregory/Voilier/site/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")
