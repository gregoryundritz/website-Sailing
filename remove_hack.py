import glob
import re

files = glob.glob('site/de/*.html') + glob.glob('site/en/*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove the injected CSS
    content = re.sub(r'<style>\s*\.badge-pill \{ white-space: normal.*?</style>', '', content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Removed badge-pill hack from all translated HTML files.")
