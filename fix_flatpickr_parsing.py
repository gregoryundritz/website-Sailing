import glob
import re

# 1. Update style.css to hide outside days
with open('site/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.flatpickr-day.prevMonthDay' not in css:
    css += "\n\n/* Hide previous and next month days in Flatpickr */\n.flatpickr-day.prevMonthDay, .flatpickr-day.nextMonthDay {\n    visibility: hidden;\n}\n"

with open('site/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update HTML files to use Date objects for Flatpickr disable
contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for file_path in contact_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # The old push logic
        old_push_logic = """
                            dates.push({
                                from: new Date(start).toISOString().split('T')[0],
                                to: endDate.toISOString().split('T')[0]
                            });"""
        
        # We need to replace the loop logic
        # Let's replace the whole inner body of `if (start && end)`
        # Actually it's safer to use regex to replace the entire `if (start && end) { ... }` block
        
        pattern = r'if \(start && end\) \{.*?dates\.push\(\{.*?\}\);\s*\}'
        
        new_logic = """if (start && end) {
                            let startStr = start.split('T')[0];
                            let endStr = end.split('T')[0];
                            
                            let startDateObj = new Date(startStr + 'T00:00:00');
                            let endDateObj = new Date(endStr + 'T00:00:00');
                            
                            if (event.end.date) {
                                endDateObj.setDate(endDateObj.getDate() - 1);
                            }
                            
                            dates.push({
                                from: startDateObj,
                                to: endDateObj
                            });
                        }"""
        
        html = re.sub(pattern, new_logic, html, flags=re.DOTALL)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
