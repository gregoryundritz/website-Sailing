import glob
import re

contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

fetch_logic = """
    var fpS, fpE;
    // Fetch Google Calendar Events
    let blockedDates = [];
    if (window.VOILIER_CONFIG && window.VOILIER_CONFIG.GOOGLE_CALENDAR_API_KEY && window.VOILIER_CONFIG.GOOGLE_CALENDAR_API_KEY !== 'VOTRE_CLE_API_ICI') {
        const calId = encodeURIComponent(window.VOILIER_CONFIG.GOOGLE_CALENDAR_ID);
        const apiKey = window.VOILIER_CONFIG.GOOGLE_CALENDAR_API_KEY;
        const timeMin = new Date().toISOString();
        const url = `https://www.googleapis.com/calendar/v3/calendars/${calId}/events?key=${apiKey}&timeMin=${timeMin}&singleEvents=true&orderBy=startTime`;
        
        fetch(url)
            .then(response => response.json())
            .then(data => {
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
                    if (fpS) fpS.set('disable', blockedDates);
                    if (fpE) fpE.set('disable', blockedDates);
                }
            })
            .catch(err => console.error('Error fetching calendar events:', err));
    }
"""

for f in contact_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
            
        # If we didn't inject correctly, replace `var fpS, fpE;`
        if "Fetch Google Calendar Events" not in html:
            html = html.replace('var fpS, fpE;', fetch_logic)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)
            
        print(f"Updated {f}")
    except FileNotFoundError:
        pass

print("Calendar fetch logic fixed.")
