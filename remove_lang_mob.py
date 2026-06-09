import glob
import re

files = glob.glob('site/de/*.html') + glob.glob('site/en/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove lang-sel-mob
    content = re.sub(r'<div class="lang-sel-mob">.*?</div>', '', content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Removed lang-sel-mob from all DE and EN HTML files.")
