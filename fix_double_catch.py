import glob

files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the double catch syntax error:
        #             });
        #             .catch((error) => {
        #               btn.disabled = false;
        #               btn.textContent = (lang === 'de') ? 'Erneut versuchen' : ((lang === 'en') ? 'Retry' : 'Réessayer');
        #               alert((lang === 'de') ? 'Fehler beim Senden. Bitte versuchen Sie es erneut.' : ((lang === 'en') ? 'Error sending. Please try again.' : 'Erreur lors de l\\'envoi. Veuillez réessayer.'));
        #             });
        
        # We can just remove the old catch block entirely, OR remove the `;` from our new catch block.
        # But having two catch blocks makes no sense. Let's remove the second one.
        
        # We can locate the string using a regex or simple split.
        import re
        
        # Match pattern:
        #             });
        #             .catch((error) => { ... });
        pattern = r'\n            }\);\n            \.catch\(\(error\) => \{\n.*?\}\);'
        
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, '\n            });', content, flags=re.DOTALL)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed syntax error in {filepath}")
        else:
            print(f"No syntax error found in {filepath} (or pattern didn't match)")
            
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
