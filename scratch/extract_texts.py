import re

def main():
    with open('site/index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove scripts and styles
    html = re.sub(r'<script.*?>.*?</script>', '', html, flags=re.DOTALL)
    html = re.sub(r'<style.*?>.*?</style>', '', html, flags=re.DOTALL)
    
    # Find all texts between tags
    texts = re.findall(r'>([^<]+)<', html)
    
    clean_texts = set()
    for text in texts:
        t = text.strip()
        if len(t) > 1 and not re.match(r'^[0-9\W]+$', t):
            clean_texts.add(t)
            
    for t in sorted(clean_texts):
        print(repr(t))

if __name__ == '__main__':
    main()
