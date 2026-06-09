import glob
import re
import html

files = glob.glob('site/de/*.html') + glob.glob('site/en/*.html')

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Decode HTML entities inside <script> blocks
    def unescape_script(match):
        return match.group(1) + html.unescape(match.group(2)) + match.group(3)
        
    content = re.sub(r'(?is)(<script[^>]*>)(.*?)(</script>)', unescape_script, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Unescaped JS in all DE and EN files!")
