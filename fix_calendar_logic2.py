import glob
import re

contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

new_fetch_logic = """
    var fpS, fpE;
    // Fetch Google Calendar Events
    let blockedDates = [];
    if (window.VOILIER_CONFIG && window.VOILIER_CONFIG.GOOGLE_CALENDAR_API_KEY && window.VOILIER_CONFIG.GOOGLE_CALENDAR_API_KEY !== 'VOTRE_CLE_API_ICI') {
        const calId = encodeURIComponent(window.VOILIER_CONFIG.GOOGLE_CALENDAR_ID);
        const apiKey = window.VOILIER_CONFIG.GOOGLE_CALENDAR_API_KEY;
        const timeMin = new Date().toISOString();
        const url = `https://www.googleapis.com/calendar/v3/calendars/${calId}/events?key=${apiKey}&timeMin=${timeMin}&singleEvents=true&orderBy=startTime`;
        
        fetch(url)
            .then(response => {
                if (!response.ok) {
                    console.error('Google API Error:', response.status);
                }
                return response.json();
            })
            .then(data => {
                if (data.error) {
                    console.error('Google API Error:', data.error);
                }
                if (data.items) {
                    data.items.forEach(event => {
                        let start = event.start.date || event.start.dateTime;
                        let end = event.end.date || event.end.dateTime;
                        if (start && end) {
                            let endDate = new Date(end);
                            if (event.end.date) {
                                endDate.setDate(endDate.getDate() - 1);
                            }
                            blockedDates.push({
                                from: new Date(start).toISOString().split('T')[0],
                                to: endDate.toISOString().split('T')[0]
                            });
                        }
                    });
                    console.log('Successfully fetched and blocked dates:', blockedDates);
                    // Update Flatpickr safely
                    const safelySetDisable = (fpInstance) => {
                        if (!fpInstance) return;
                        const instance = Array.isArray(fpInstance) ? fpInstance[0] : fpInstance;
                        if (instance && typeof instance.set === 'function') {
                            instance.set('disable', blockedDates);
                        }
                    };
                    safelySetDisable(fpS);
                    safelySetDisable(fpE);
                }
            })
            .catch(err => console.error('Error fetching calendar events:', err));
    }
"""

for f in contact_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
            
        # Replace old fetch logic with new robust logic
        # We need to extract from `var fpS, fpE;` down to the end of the `if (window.VOILIER_CONFIG ... }` block
        # I'll use regex to match it.
        pattern = r'\s*var fpS, fpE;\s*// Fetch Google Calendar Events.*?catch\(err => console\.error\(\'Error fetching calendar events:\', err\)\);\s*}'
        html = re.sub(pattern, new_fetch_logic, html, flags=re.DOTALL)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)
            
        print(f"Updated {f}")
    except FileNotFoundError:
        pass

print("Calendar fetch logic made more robust.")
