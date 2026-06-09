import glob
import re

# 1. Update config.js
config_path = 'site/js/config.js'
with open(config_path, 'r', encoding='utf-8') as f:
    config_js = f.read()

if 'GOOGLE_CALENDAR_API_KEY' not in config_js:
    config_injection = """
  // Paramètres Google Calendar
  // Remplacez 'VOTRE_CLE_API_ICI' par la clé que vous allez créer
  GOOGLE_CALENDAR_API_KEY: 'VOTRE_CLE_API_ICI',
  GOOGLE_CALENDAR_ID: '352a23f170d4b8a0d40b183303bb12ea40350fc2e420b12dac648695db8a4095@group.calendar.google.com',
"""
    config_js = config_js.replace('prices_per_days:', config_injection + '\n  prices_per_days:')
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(config_js)


# 2. Update contact files
contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

# The fetch logic to add before Flatpickr initialization
fetch_logic = """
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
                              // If it's an all-day event (date only), the end date is exclusive in Google Calendar
                              // So we subtract 1 millisecond from end date to make it inclusive for Flatpickr
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
                      // Update Flatpickr instances if they exist
                      if (window.fpS) window.fpS.set('disable', blockedDates);
                      if (window.fpE) window.fpE.set('disable', blockedDates);
                  }
              })
              .catch(err => console.error('Error fetching calendar events:', err));
      }
"""

for f in contact_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
            
        # Remove the iframe div and the appended text "(Vérifiez les dispos ci-dessus)"
        # Regex to find the calendar div
        calendar_div_pattern = r'<div style="width: 100%; overflow: hidden; margin-bottom: 20px; border-radius: var\(--r\); box-shadow: 0 1px 3px rgba\(0,0,0,0\.1\);">\s*<iframe.*?</iframe>\s*</div>\s*'
        html = re.sub(calendar_div_pattern, '', html, flags=re.DOTALL)
        
        # Remove the text in parenthesis in the title
        html = re.sub(r'<span style="font-size:13px; font-weight:400; color:var\(--muted\);">\(.*?\)</span>\s*:', ':', html)

        # Inject the fetch logic right before `var fpS = flatpickr("#fp-start", {`
        if "Fetch Google Calendar Events" not in html:
            html = html.replace('var fpS = flatpickr("#fp-start", {', fetch_logic + '\n      var fpS = flatpickr("#fp-start", {\n        disable: blockedDates,')
            # Also add `disable: blockedDates,` to fpE
            html = html.replace('var fpE = flatpickr("#fp-end", {', 'var fpE = flatpickr("#fp-end", {\n        disable: blockedDates,')

        with open(f, 'w', encoding='utf-8') as file:
            file.write(html)
            
        print(f"Updated {f}")
    except FileNotFoundError:
        pass

print("Google Calendar logic injected.")
