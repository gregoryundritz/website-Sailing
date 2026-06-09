import glob

# Update DE files
de_files = glob.glob('site/de/*.html')
for f in de_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('<div>Segelboot <span>Genfersee</span></div>', '<div>Segelboot <span>Neuenburgersee</span></div>')
    content = content.replace('<div>Segelboot <span>auf dem Neuenburgersee</span></div>', '<div>Segelboot <span>Neuenburgersee</span></div>')
    content = content.replace('<div class="fl">Segelboot · <span>Genfersee</span></div>', '<div class="fl">Segelboot · <span>Neuenburgersee</span></div>')
    # Extra fallback just in case
    content = content.replace('<div>Segeln <span>Neuenburgersee</span></div>', '<div>Segelboot <span>Neuenburgersee</span></div>')
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

# Update EN files
en_files = glob.glob('site/en/*.html')
for f in en_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('<div>Sailing boat <span>Lake Neuchâtel</span></div>', '<div>Sailing <span>Lake Neuchatel</span></div>')
    content = content.replace('<div>Sailing boat <span>on Lake Neuchâtel</span></div>', '<div>Sailing <span>Lake Neuchatel</span></div>')
    content = content.replace('>Itineraries<', '>Routes<')
    content = content.replace('>ITINERARIES<', '>ROUTES<')
    content = content.replace('<div class="fl">Sailing boat · <span>Lake Neuchâtel</span></div>', '<div class="fl">Sailing · <span>Lake Neuchatel</span></div>')
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Text replacements applied successfully.")
