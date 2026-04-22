import re
import os

files = ['site/index.html', 'site/en/index.html', 'site/de/index.html']

js_target = r"""const DP_DEF = \{.*?\};
function getCfg\(\)\{ try\{return JSON\.parse\(localStorage\.getItem\('voilier_config'\)\|\|'\{\}'\)\}catch\(e\)\{return \{\}\} \}
function getPrice\(d\)\{ const c=getCfg\(\),k='pd_'\+d; return\(c\[k\]!==undefined&&c\[k\]>0\)\?parseInt\(c\[k\]\):\(DP_DEF\[d\]\|\|DP_DEF\[14\]\); \}"""

js_replace = r"""function getCfg(){ return window.VOILIER_CONFIG || { prices_per_days: {}, options: [], blocked_dates: [] }; }
function getPrice(d){ const c=getCfg(); return c.prices_per_days && c.prices_per_days[d] ? c.prices_per_days[d] : (c.prices_per_days[14] || 1400); }"""

for f in files:
    path = f"/home/gregory/Voilier/{f}"
    if not os.path.exists(path): continue
    with open(path, 'r') as file:
        content = file.read()
    
    # 1. Inject config.js
    if '<script src="/js/config.js"></script>' not in content:
        content = content.replace('<script src="https://cdn.jsdelivr.net/npm/flatpickr/dist/l10n/fr.js"></script>',
                                  '<script src="https://cdn.jsdelivr.net/npm/flatpickr/dist/l10n/fr.js"></script>\n<script src="/js/config.js"></script>')
        content = content.replace('<script src="https://cdn.jsdelivr.net/npm/flatpickr/dist/l10n/de.js"></script>',
                                  '<script src="https://cdn.jsdelivr.net/npm/flatpickr/dist/l10n/de.js"></script>\n<script src="/js/config.js"></script>')
        # For EN, there's no localization script for flatpickr natively loaded, let's inject before the main <script>
        if '<script src="https://cdn.jsdelivr.net/npm/flatpickr"></script>' in content:
            content = content.replace('<script>\n// ── Reveal ──', '<script src="/js/config.js"></script>\n<script>\n// ── Reveal ──')

    # 2. Update getCfg and getPrice logic
    content = re.sub(js_target, js_replace, content)
    
    # 3. Update the c.opts usage in loadPrices to c.options
    content = content.replace('c.opts&&c.opts.length', 'c.options&&c.options.length')
    content = content.replace('c.opts.forEach', 'c.options.forEach')
    content = content.replace('c.opts.filter', 'c.options.filter')

    with open(path, 'w') as file:
        file.write(content)

print("Updated HTML logic")
