import sys
print("Starting...")
sys.stdout.flush()

with open('site/index.html', 'r', encoding='utf-8') as f:
    html = f.read()
print(f"Read {len(html)} chars.")
sys.stdout.flush()

# Header
header_end = html.find('</nav>') + 6
header = html[:header_end]

# Footer
footer_start = html.rfind('<footer>')
footer = html[footer_start:]

print("Header/Footer extracted.")
sys.stdout.flush()

# create page
def create_page(name, title, content):
    print(f"Creating {name}...")
    sys.stdout.flush()
    h = header.replace('<title>Voilier Lac de Neuchâtel — Cheyres, Suisse | Maxus 21</title>', f'<title>{title}</title>')
    h = h.replace('href="#bateau"', 'href="bateau.html"')
    f = footer.replace('href="#bateau"', 'href="bateau.html"')
    page = h + '\n<div style="margin-top:100px;"></div>\n' + content + '\n' + f
    with open(f'site/{name}', 'w', encoding='utf-8') as file:
        file.write(page)

# Extract sections manually by string splits
def get_sec(s, e):
    start = html.find(s)
    if start == -1: return ""
    end = html.find(e, start)
    return html[start:end+len(e)]

print("Extracting Bateau...")
sys.stdout.flush()
b = get_sec('<section id="bateau">', '</section>')
print("Extracting Gal...")
sys.stdout.flush()
g = get_sec('<!-- GALERIE -->', '</div>\n  </div>')
create_page('bateau.html', 'Le Bateau — Voilier Lac de Neuchâtel', b + '\n' + g)

print("Extracting Tarifs...")
sys.stdout.flush()
t = get_sec('<section id="tarifs"', '</section>')
ps = get_sec('<section id="pass-skipper"', '</section>')
create_page('tarifs.html', 'Tarifs de Location', t + '\n' + ps)

print("Extracting Contact...")
sys.stdout.flush()
c = get_sec('<section id="contact"', '</form>\n    </div>\n  </section>')
create_page('contact.html', 'Contact', c)

print("Done.")
