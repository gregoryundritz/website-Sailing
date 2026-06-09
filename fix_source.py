import os
import glob

html_files = glob.glob('/home/gregory/Voilier/site/*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix image paths
    content = content.replace('src="img/', 'src="/img/')
    content = content.replace('href="img/', 'href="/img/')

    # Fix language selectors (mob and desktop)
    # Desktop
    if 'href="/en/"' not in content:
        content = content.replace(
            '<a href="/de/" class="">DE</a></li>',
            '<a href="/de/" class="">DE</a><span>|</span><a href="/en/" class="">EN</a></li>'
        )
        content = content.replace(
            '<a href="/de/">DE</a></li>',
            '<a href="/de/">DE</a><span>|</span><a href="/en/">EN</a></li>'
        )
    # Mobile
    if 'href="/en/index.html"' not in content and 'href="/en/"' not in content:
        content = content.replace(
            '<a href="/de/index.html">DE</a></div>',
            '<a href="/de/index.html">DE</a><span>|</span><a href="/en/index.html">EN</a></div>'
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Source files fixed!")
