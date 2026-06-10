import os

files = {
    'site/contact.html': 'Une question ? <em>Parlons-en</em>',
    'site/de/kontakt.html': 'Haben Sie eine Frage? <em>Sprechen wir darüber</em>',
    'site/en/contact.html': 'Any questions? <em>Let’s talk</em>'
}

for filepath, old_text in files.items():
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove the emphasis part
        new_text = old_text.split(' <em>')[0]
        if '?' not in new_text and 'question' in old_text:
            new_text = 'Une question ?' # fallback just in case
            
        # Replace the full block to harmonize spacing
        old_block = f"""      <div class="rv" style="text-align:center;margin-bottom:48px;">\n\n        <h2 class="sec-h" style="max-width:520px;margin:0 auto 16px;">{old_text}</h2>\n\n      </div>"""
        
        new_block = f"""      <div class="rv" style="text-align:center;margin-bottom:40px;">\n        <h2 class="sec-h" style="max-width:520px;margin:0 auto;">{new_text}</h2>\n      </div>"""
        
        if old_block in content:
            content = content.replace(old_block, new_block)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filepath} (exact block match)")
        else:
            # Fallback if exact block match fails
            print(f"Exact block match failed for {filepath}. Attempting regex.")
            import re
            content = re.sub(
                r'<div class="rv" style="text-align:center;margin-bottom:48px;">\s*<h2 class="sec-h" style="max-width:520px;margin:0 auto 16px;">.*?</h2>\s*</div>',
                new_block,
                content
            )
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filepath} via regex")

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
