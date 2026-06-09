import os
import glob

html_files = glob.glob('site/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Revert absolute paths back to relative for FR files
    content = content.replace('src="/img/', 'src="img/')
    content = content.replace('href="/img/', 'href="img/')
    content = content.replace('href="/css/', 'href="css/')
    content = content.replace('src="/js/', 'src="js/')
    
    # Fix mobile menu EN
    if '<a href="/de/index.html">DE</a></div>' in content:
        content = content.replace(
            '<a href="/de/index.html">DE</a></div>',
            '<a href="/de/index.html">DE</a><span>|</span><a href="/en/index.html">EN</a></div>'
        )
    if '<a href="/de/">DE</a></div>' in content:
        content = content.replace(
            '<a href="/de/">DE</a></div>',
            '<a href="/de/">DE</a><span>|</span><a href="/en/">EN</a></div>'
        )
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Source files paths reverted and mobile menu fixed!")
