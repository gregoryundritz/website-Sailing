import os

def run():
    files = [f for f in os.listdir('de') if f.endswith('.html')]
    for filename in files:
        filepath = os.path.join('de', filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            c = f.read()
            
        # First fix the specific bug in segelpruefung-schweiz.html
        if filename == 'segelpruefung-schweiz.html':
            c = c.replace('<li><a href="segelpruefung-schweiz.html">Törns</a></li>', 
                          '<li><a href="toerns.html">Routen</a></li>\n      <li><a href="segelpruefung-schweiz.html">Segelprüfung</a></li>')
        
        # Then replace any remaining "Törns" in the menu
        c = c.replace('<li><a href="toerns.html">Törns</a></li>', '<li><a href="toerns.html">Routen</a></li>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(c)

if __name__ == "__main__":
    run()
