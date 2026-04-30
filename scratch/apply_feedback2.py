import re

with open('site/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("if (optsArea) optsArea.style.opacity = '0.4';", "if (optsArea) optsArea.style.display = 'none';")
content = content.replace("if (optsArea) optsArea.style.opacity = '1';", "if (optsArea) optsArea.style.display = 'block';")

with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
