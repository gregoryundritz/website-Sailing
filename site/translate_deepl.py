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

def translate_html_file(filepath, source_lang="FR", target_lang="DE"):
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()

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
        # In Switzerland, the "ß" (Eszett) is not used. It is replaced by "ss".
        translated_html = translated_html.replace('ß', 'ss')
        translated_html = translated_html.replace('ẞ', 'SS')
        
        # Custom Swiss vocabulary replacements
        translated_html = translated_html.replace('Verleih', 'Vermietung')
        translated_html = translated_html.replace('verleih', 'vermietung')
        translated_html = translated_html.replace('Bootsführerschein', 'Segelschein')
        translated_html = translated_html.replace('bootsführerschein', 'segelschein')
        
    elif target_lang == "EN-GB":
        # Custom English vocabulary replacements
        # Use regex \b to match whole words and avoid replacing inside 'viewport' or 'important'
        translated_html = re.sub(r'\bport\b', 'harbour', translated_html)
        translated_html = re.sub(r'\bPort\b', 'Harbour', translated_html)
    
    # For languages like EN-GB, use 'en' for folder and lang attribute
    short_lang = target_lang.split('-')[0].lower()
    
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
      .badge-pill { white-space: normal !important; height: auto !important; padding: 6px 12px !important; text-align: center; line-height: 1.2; }
    </style>
    </head>
    """
    translated_html = translated_html.replace('</head>', css_fix)

    # Determine output path
    basename = os.path.basename(filepath)
    output_dir = os.path.join(os.path.dirname(__file__), short_lang)
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, basename)
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
