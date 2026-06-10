import glob

files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

old_fetch = """          fetch('/', {
            method: 'POST',
            body: formData
          })

            .then(() => {"""

new_fetch = """          fetch('/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams(formData).toString()
          })
            .then((response) => {
              if (!response.ok) throw new Error('Erreur réseau ou serveur');
              return response.text();
            })
            .then(() => {"""

# Also need to add a catch block! But wait, where does the `.then()` end?
# Let's just do a regex or replace on the fetch call, and if we want to add a catch, we'll see where the `})` ends.

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if old_fetch in content:
            content = content.replace(old_fetch, new_fetch)
            
            # Now let's find the end of the .then() block to add a .catch()
            # It ends with:
            #               updateTotal();
            #             })
            
            old_end = """              updateTotal();\n            })"""
            new_end = """              updateTotal();\n            })\n            .catch((error) => {\n              btn.disabled = false;\n              btn.textContent = (lang === 'de') ? 'Meine Anfrage senden →' : ((lang === 'en') ? 'Send my request →' : 'Envoyer ma demande →');\n              if (note) {\n                  note.innerHTML = '<span style=\"color:#d9534f;font-weight:600;display:block;padding:12px;background:#fdf2f2;border:1px solid #d9534f;border-radius:6px;margin-bottom:12px;\">⚠️ ' + ((lang === 'de') ? 'Ein Fehler ist aufgetreten. Bitte versuchen Sie es später erneut.' : ((lang === 'en') ? 'An error occurred. Please try again later.' : 'Une erreur est survenue. Veuillez réessayer plus tard.')) + '</span>';\n              }\n              console.error(error);\n            });"""
            
            if old_end in content:
                content = content.replace(old_end, new_end)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated fetch block in {filepath}")
        else:
            print(f"Could not find old_fetch in {filepath}")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
