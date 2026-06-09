import glob
import re

# Fix languages
def fix_language(file_path, lang):
    with open(file_path, 'r', encoding='utf-8') as file:
        html = file.read()

    if lang == 'de':
        html = html.replace('dist/l10n/fr.js', 'dist/l10n/de.js')
        html = html.replace("flatpickr.l10ns.fr) ? 'fr'", "flatpickr.l10ns.de) ? 'de'")
    elif lang == 'en':
        # Remove the localization script
        html = re.sub(r'<script src="https://cdn.jsdelivr.net/npm/flatpickr/dist/l10n/.*?.js"></script>', '', html)
        html = re.sub(r"var loc = .*?;", "var loc = 'default';", html)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html)

for f in glob.glob('site/de/*.html'):
    fix_language(f, 'de')
for f in glob.glob('site/en/*.html'):
    fix_language(f, 'en')

print("Languages fixed.")

# Fix calendar race condition in contact.html files
contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for f in contact_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
            
        # We replace the fetch logic
        # Find the old fetch logic block
        pattern_fetch = r'let blockedDates = \[\];.*?catch\(err => console\.error\(\'Error fetching calendar events:\', err\)\);\s*}'
        
        new_fetch = """
    window.VOILIER_BLOCKED_DATES = window.VOILIER_BLOCKED_DATES || [];
    window.updateFpDates = function() {
        if (typeof fpS !== 'undefined' && fpS) { (Array.isArray(fpS) ? fpS[0] : fpS).set('disable', window.VOILIER_BLOCKED_DATES); }
        if (typeof fpE !== 'undefined' && fpE) { (Array.isArray(fpE) ? fpE[0] : fpE).set('disable', window.VOILIER_BLOCKED_DATES); }
    };
    
    if (window.VOILIER_CONFIG && window.VOILIER_CONFIG.GOOGLE_CALENDAR_API_KEY && window.VOILIER_CONFIG.GOOGLE_CALENDAR_API_KEY !== 'VOTRE_CLE_API_ICI') {
        const calId = encodeURIComponent(window.VOILIER_CONFIG.GOOGLE_CALENDAR_ID);
        const apiKey = window.VOILIER_CONFIG.GOOGLE_CALENDAR_API_KEY;
        const timeMin = new Date().toISOString();
        const url = `https://www.googleapis.com/calendar/v3/calendars/${calId}/events?key=${apiKey}&timeMin=${timeMin}&singleEvents=true&orderBy=startTime`;
        
        fetch(url)
            .then(r => r.json())
            .then(data => {
                if (data.items) {
                    let dates = [];
                    data.items.forEach(event => {
                        let start = event.start.date || event.start.dateTime;
                        let end = event.end.date || event.end.dateTime;
                        if (start && end) {
                            let endDate = new Date(end);
                            if (event.end.date) {
                                endDate.setDate(endDate.getDate() - 1);
                            }
                            dates.push({
                                from: new Date(start).toISOString().split('T')[0],
                                to: endDate.toISOString().split('T')[0]
                            });
                        }
                    });
                    window.VOILIER_BLOCKED_DATES = dates;
                    window.updateFpDates();
                }
            })
            .catch(err => console.error('Error fetching calendar events:', err));
    }
"""
        html = re.sub(pattern_fetch, new_fetch, html, flags=re.DOTALL)
        
        # Now update the initFp to also set disable
        # `locale: loc, dateFormat: 'j F Y', minDate: minD, disableMobile: true, allowInput: false,`
        # We append `disable: window.VOILIER_BLOCKED_DATES,`
        
        html = html.replace("locale: loc, dateFormat: 'j F Y', minDate: minD, disableMobile: true, allowInput: false,",
                            "disable: window.VOILIER_BLOCKED_DATES, locale: loc, dateFormat: 'j F Y', minDate: minD, disableMobile: true, allowInput: false,")
                            
        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)
            
        print(f"Fixed race condition in {f}")
    except FileNotFoundError:
        pass
