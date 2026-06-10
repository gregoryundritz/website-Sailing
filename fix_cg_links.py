import glob
import re
import os

# 1. Fix DE files
de_files = glob.glob('site/de/*.html')
for file_path in de_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace absolute paths to html files with relative paths
        # e.g., href="/agb.html" -> href="agb.html"
        content = re.sub(r'href="/([^"]+\.html)(#[^"]*)?"', r'href="\1\2"', content)
        
        # Fix hardcoded "contact.html" to "kontakt.html" in DE files
        content = content.replace('href="contact.html#reservation"', 'href="kontakt.html#reservation"')
        content = content.replace('href="contact.html"', 'href="kontakt.html"')
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed links in {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# 2. Fix EN files
en_files = glob.glob('site/en/*.html')
for file_path in en_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace absolute paths to html files with relative paths
        content = re.sub(r'href="/([^"]+\.html)(#[^"]*)?"', r'href="\1\2"', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed links in {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
