import os
import glob
import re

print("Starting Full Site Audit...")

files = glob.glob('site/*.html') + glob.glob('site/de/*.html') + glob.glob('site/en/*.html')
print(f"Total HTML files found: {len(files)}")

issues = []

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Check for broken internal links
        # Find all href="..."
        links = re.findall(r'href=["\'](.*?)["\']', content)
        for link in links:
            if link.startswith(('http', 'mailto:', 'tel:', '#', 'javascript:')):
                continue
            
            # Resolve the path relative to the file
            dir_path = os.path.dirname(file_path)
            # Remove query params or hash
            clean_link = link.split('#')[0].split('?')[0]
            if not clean_link:
                continue
            
            if clean_link.startswith('/'):
                target_path = os.path.join('site', clean_link.lstrip('/'))
            else:
                target_path = os.path.normpath(os.path.join(dir_path, clean_link))
                
            if not os.path.exists(target_path):
                issues.append(f"[BROKEN LINK] {file_path} -> {link} (Target {target_path} not found)")
                
        # 2. Check for missing form tags
        if '<form' in content and 'data-netlify="true"' not in content:
             issues.append(f"[FORM ISSUE] {file_path} contains a form without data-netlify=\"true\"")
             
        # 3. Check for language switcher links
        if 'lang-sel' in content:
            if 'href="de/' in content or 'href="en/' in content:
                issues.append(f"[LANG SWITCHER] {file_path} contains relative language switcher links. They should be absolute.")
                
    except Exception as e:
        issues.append(f"[ERROR] Could not read {file_path}: {e}")

if not issues:
    print("\nNo major structural issues found during static analysis!")
else:
    print("\nIssues found:")
    for issue in set(issues): # remove duplicates
        print(issue)
