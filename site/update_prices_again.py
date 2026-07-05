import os
import glob

directory = '/home/gregory/Voilier/site'
files = glob.glob(os.path.join(directory, '**/*.html'), recursive=True)

replacements = {
    '"priceRange": "275-1610 CHF"': '"priceRange": "235-1330 CHF"',
    '"lowPrice": "275"': '"lowPrice": "235"',
    '"highPrice": "1610"': '"highPrice": "1330"',
    '275 CHF': '235 CHF',
    'CHF 275': 'CHF 235',
    'data-day="1">275<': 'data-day="1">235<',
    'data-day="2">510<': 'data-day="2">430<',
    'data-day="3">750<': 'data-day="3">630<',
    'data-day="4">980<': 'data-day="4">820<',
    'data-day="5">1200<': 'data-day="5">1000<',
    'data-day="6">1410<': 'data-day="6">1170<',
    'data-day="7">1610<': 'data-day="7">1330<',
    'data-day-ppd="1">275': 'data-day-ppd="1">235',
    'data-day-ppd="2">255': 'data-day-ppd="2">215',
    'data-day-ppd="3">250': 'data-day-ppd="3">210',
    'data-day-ppd="4">245': 'data-day-ppd="4">205',
    'data-day-ppd="5">240': 'data-day-ppd="5">200',
    'data-day-ppd="6">235': 'data-day-ppd="6">195',
    'data-day-ppd="7">230': 'data-day-ppd="7">190',
}

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
        
    if content != new_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

print("Done")
