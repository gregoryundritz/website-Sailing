import re
import glob

files = {
    'site/de/kontakt.html': {
        'dates': 'Ihre Reisedaten:',
        'options': 'Zusätzliche Optionen:',
        'type': 'Wählen Sie Ihre Buchungsart:'
    },
    'site/en/contact.html': {
        'dates': 'Your travel dates:',
        'options': 'Additional options:',
        'type': 'Select your booking type:'
    }
}

for path, texts in files.items():
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update Title
    html = re.sub(r'<div style="font-size:14px; font-weight:600; margin-bottom:12px; color:var\(--navy\);">.*?</div>',
                  f'<div class="resa-step-title">{texts["type"]}</div>', html, count=1)
                  
    # Update Dates title
    if 'id="section-standard"' in html and texts["dates"] not in html:
        html = html.replace('<div class="resa-step" id="section-standard">\n            <div class="fr">',
                            f'<div class="resa-step" id="section-standard">\n            <div class="resa-step-title">{texts["dates"]}</div>\n            <div class="fr">')
                            
    # Update Options title
    if 'id="section-options"' in html and texts["options"] not in html:
        html = html.replace('<div class="resa-step" id="section-options">\n\n            <div class="opts-checks" id="resa-options">',
                            f'<div class="resa-step" id="section-options">\n            <div class="resa-step-title">{texts["options"]}</div>\n\n            <div class="opts-checks" id="resa-options">')

    # Update script block for duration
    script_target = r"""      if \(dd\) \{
        var opts = \{ day: 'numeric', month: 'long', year: 'numeric' \};
        dd\.textContent = days \+ ' jour' \+ \(days > 1 \? 's' : ''\) \+ ' · du ' \+ s\.toLocaleDateString\('.*?', opts\) \+ ' au ' \+ e\.toLocaleDateString\('.*?', opts\);
        dd\.style\.display = 'block';
      \}"""
    script_replacement = """      if (dd) {
        var lang = document.documentElement.lang || 'fr';
        var t_jours = (lang === 'de') ? ' Tage' : ((lang === 'en') ? ' days' : ' jours');
        var t_jour = (lang === 'de') ? ' Tag' : ((lang === 'en') ? ' day' : ' jour');
        dd.textContent = days + (days > 1 ? t_jours : t_jour);
        dd.style.display = 'block';
      }"""
    html = re.sub(script_target, script_replacement, html, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated DE and EN contact pages.")
