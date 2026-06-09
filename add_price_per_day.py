import glob
import re

files = [
    'site/contact.html',
    'site/de/kontakt.html',
    'site/en/contact.html'
]

# We want to replace the `dd.textContent = ...` line in the `updateTotal()` function
# Existing: dd.textContent = days + (days > 1 ? t_jours : t_jour);
# New:      var pricePerDay = Math.round(basePrice / days);
#           dd.textContent = days + (days > 1 ? t_jours : t_jour) + ' (' + pricePerDay + ' CHF / ' + t_jour.trim() + ')';

target = r"dd\.textContent = days \+ \(days > 1 \? t_jours : t_jour\);"
replacement = r"""var pricePerDay = Math.round(basePrice / days);
        dd.textContent = days + (days > 1 ? t_jours : t_jour) + ' (' + pricePerDay + ' CHF / ' + t_jour.trim() + ')';"""

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
            
        html = re.sub(target, replacement, html)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)
        print(f"Updated {f}")
    except FileNotFoundError:
        pass

print("Price per day added to duration summary.")
