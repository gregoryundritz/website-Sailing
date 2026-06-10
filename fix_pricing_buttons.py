import glob
import re

# 1. Update the pricing pages
pricing_files = {
    'site/tarifs.html': 'contact.html',
    'site/de/preise.html': 'kontakt.html',
    'site/en/prices.html': 'contact.html'
}

for file_path, contact_file in pricing_files.items():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace(
            'href="#resa-form" onclick="selectStandard()"',
            f'href="{contact_file}#reservation"'
        )
        content = content.replace(
            'href="#resa-form" onclick="selectPassSkipper()"',
            f'href="{contact_file}?pass=1#reservation"'
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated links in {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")

# 2. Update the contact pages to handle ?pass=1
contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

js_snippet = """
    // Handle ?pass=1 from pricing page
    document.addEventListener('DOMContentLoaded', function() {
      if (window.location.search.includes('pass=1') && typeof selectTab === 'function') {
        selectTab('pass');
        var el = document.getElementById('resa-form');
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }
    });
"""

for file_path in contact_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "window.location.search.includes('pass=1')" not in content:
            # Inject right before the closing </script> tag at the end of the main script block
            # Actually, let's inject it before initFp(); or just before </script>
            content = content.replace("initFp();\n", f"initFp();\n{js_snippet}\n")
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Injected JS in {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
