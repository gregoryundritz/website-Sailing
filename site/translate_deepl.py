import os
import glob
import re
import deepl
from dotenv import load_dotenv

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(env_path)
API_KEY = os.getenv("DEEPL_API_KEY")

if not API_KEY:
    print("Error: DEEPL_API_KEY not found in .env")
    exit(1)

translator = deepl.Translator(API_KEY)

ROUTE_MAP = {
    'index.html': {'de': 'index.html', 'en': 'index.html'},
    'tarifs.html': {'de': 'preise.html', 'en': 'prices.html'},
    'contact.html': {'de': 'kontakt.html', 'en': 'contact.html'},
    'galerie.html': {'de': 'galerie.html', 'en': 'gallery.html'},
    'itineraires.html': {'de': 'toerns.html', 'en': 'itineraries.html'},
    'avis.html': {'de': 'bewertungen.html', 'en': 'reviews.html'},
    'permis-bateau-suisse.html': {'de': 'segelpruefung-schweiz.html', 'en': 'sailing-license-switzerland.html'},
    'conditions-generales.html': {'de': 'agb.html', 'en': 'terms-and-conditions.html'},
    'mentions-legales.html': {'de': 'impressum.html', 'en': 'legal-notice.html'},
    'a-propos.html': {'de': 'ueber-uns.html', 'en': 'about.html'}
}

def translate_html_file(filepath, source_lang="FR", target_lang="DE"):
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    basename = os.path.basename(filepath)
    short_lang = target_lang.split('-')[0].lower()

    # Pre-process: Protect links so DeepL doesn't translate them into unpredictable strings
    for fr_page in ROUTE_MAP.keys():
        # Match href="page.html" or href="/page.html"
        html_content = html_content.replace(f'href="{fr_page}"', f'href="LINK_PROTECT_{fr_page}"')
        html_content = html_content.replace(f'href="/{fr_page}"', f'href="/LINK_PROTECT_{fr_page}"')
        
        # Also protect the language switcher paths
        html_content = html_content.replace(f'href="/de/{fr_page}"', f'href="/de/LINK_PROTECT_{fr_page}"')
        html_content = html_content.replace(f'href="/en/{fr_page}"', f'href="/en/LINK_PROTECT_{fr_page}"')

    print(f"Translating {filepath} to {target_lang}...")
    
    # Translate the HTML content
    result = translator.translate_text(
        html_content,
        source_lang=source_lang,
        target_lang=target_lang,
        tag_handling="html"
    )
    
    translated_html = result.text
    
    if target_lang == "DE":
        # --- Swiss German specificities ---
        translated_html = translated_html.replace('ß', 'ss')
        translated_html = translated_html.replace('ẞ', 'SS')
        translated_html = translated_html.replace('Verleih', 'Vermietung')
        translated_html = translated_html.replace('verleih', 'vermietung')
        translated_html = translated_html.replace('Bootsführerschein', 'Segelschein')
        translated_html = translated_html.replace('bootsführerschein', 'segelschein')
        
    elif target_lang == "EN-GB":
        translated_html = re.sub(r'\bport\b', 'harbour', translated_html)
        translated_html = re.sub(r'\bPort\b', 'Harbour', translated_html)
        translated_html = re.sub(r'\bhire\b', 'rental', translated_html, flags=re.IGNORECASE)
    
    # Map relative paths back to parent directory for translated subdirectories
    translated_html = translated_html.replace('src="img/', 'src="../img/')
    translated_html = translated_html.replace('href="img/', 'href="../img/')
    translated_html = translated_html.replace('href="css/', 'href="../css/')
    translated_html = translated_html.replace('src="js/', 'src="../js/')
    
    # Post-process: Restore links mapped to localized names
    for fr_page, translations in ROUTE_MAP.items():
        localized_name = translations.get(short_lang, fr_page)
        translated_html = translated_html.replace(f'href="LINK_PROTECT_{fr_page}"', f'href="{localized_name}"')
        translated_html = translated_html.replace(f'href="/LINK_PROTECT_{fr_page}"', f'href="/{localized_name}"')
        
        # Restore the language switcher paths.
        translated_html = translated_html.replace(f'href="/de/LINK_PROTECT_{fr_page}"', f'href="/de/{translations.get("de", fr_page)}"')
        translated_html = translated_html.replace(f'href="/en/LINK_PROTECT_{fr_page}"', f'href="/en/{translations.get("en", fr_page)}"')
    
    # Update the lang attribute manually to avoid breaking formatting
    translated_html = translated_html.replace('lang="fr"', f'lang="{short_lang}"')
    translated_html = translated_html.replace("lang='fr'", f"lang='{short_lang}'")
    
    # Fix active state in language selector
    translated_html = translated_html.replace('class="active">FR', 'class="">FR')
    
    if short_lang == "de":
        translated_html = translated_html.replace('href="/de/" class=""', 'href="/de/" class="active"')
        translated_html = translated_html.replace('href="/de/index.html" class=""', 'href="/de/index.html" class="active"')
    elif short_lang == "en":
        translated_html = translated_html.replace('href="/en/" class=""', 'href="/en/" class="active"')
        translated_html = translated_html.replace('href="/en/index.html" class=""', 'href="/en/index.html" class="active"')
    
    # Inject CSS to fix badge-pill overflow for long translated words
    css_fix = """
    <style>
      .badge-pill { white-space: normal !important; height: auto !important; max-width: 100%; box-sizing: border-box; }
      .badge-pill span { word-break: break-word; hyphens: auto; letter-spacing: 0.05em !important; line-height: 1.4; display: block; }
    </style>
    </head>
    """
    translated_html = translated_html.replace('</head>', css_fix)

    # Determine output path with localized name
    target_basename = ROUTE_MAP.get(basename, {}).get(short_lang, basename)
    output_dir = os.path.join(os.path.dirname(__file__), short_lang)
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, target_basename)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(translated_html)
        
    print(f"Saved translated file to {output_path}")

if __name__ == "__main__":
    # Translate all HTML files in the directory
    source_dir = os.path.dirname(__file__)
    html_files = glob.glob(os.path.join(source_dir, '*.html'))
    
    target_languages = ["DE", "EN-GB"]
    
    for source_file in html_files:
        for lang in target_languages:
            translate_html_file(source_file, source_lang="FR", target_lang=lang)
    
    print("\nAll translations completed!")
