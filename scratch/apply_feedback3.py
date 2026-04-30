import re

with open('site/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'Possibilité de report en cas de conditions dangereuses (vent violent/tempête). Aucun report pour absence de vent.',
    'Possibilité de report en cas de conditions dangereuses'
)

with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
