import glob
import re

all_files = glob.glob('site/*.html') + glob.glob('site/de/*.html') + glob.glob('site/en/*.html')

targets = [
    'conditions-generales.html', '/conditions-generales.html',
    'mentions-legales.html', '/mentions-legales.html',
    'agb.html', '/de/agb.html',
    'impressum.html', '/de/impressum.html',
    'terms-and-conditions.html', '/en/terms-and-conditions.html',
    'legal-notice.html', '/en/legal-notice.html'
]

for file_path in all_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # We find all <a href="..."> and if the href matches one of the targets, we ensure it has target="_blank"
        # We can use a regex to match the <a> tag
        
        def replace_a_tag(match):
            a_tag = match.group(0)
            href = match.group(2)
            if href in targets:
                if 'target="_blank"' not in a_tag:
                    return a_tag.replace('<a ', '<a target="_blank" ')
            return a_tag
            
        content = re.sub(r'<a\s+([^>]*)href="([^"]+)"([^>]*)>', replace_a_tag, content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file_path}")
            
    except Exception as e:
        print(f"Error on {file_path}: {e}")
