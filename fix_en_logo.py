import glob
import re

en_files = glob.glob('site/en/*.html')

target_logo = '<div>Sailing <span>Lake Neuchatel</span></div></a>'

for f in en_files:
    with open(f, 'r', encoding='utf-8') as file:
        html = file.read()
    
    # We want to replace whatever is inside <a href="index.html" class="logo">...</a> with the consistent text
    # But only the text part, the image should stay.
    # Pattern: <a href="index.html" class="logo"><img ...><div>.*?</div></a>
    html = re.sub(
        r'(<a href="index\.html" class="logo">\s*<img[^>]*>\s*)<div>.*?</div>\s*</a>',
        r'\1<div>Sailing <span>Lake Neuchatel</span></div></a>',
        html,
        flags=re.DOTALL
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(html)

print("Unified EN logo text.")
