import glob
import re

contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for file_path in contact_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        old_on_change = """        onChange: function (d) {
          if (!d.length) return;
          var nd = new Date(d[0]); // allow same day
          fpE.set('minDate', nd);
          if (fpE.selectedDates[0] && fpE.selectedDates[0] < d[0]) fpE.clear();
          updateTotal();
        }"""

        new_on_change = """        onChange: function (d) {
          if (!d.length) return;
          var nd = new Date(d[0]);
          var m = nd.getMonth();
          // Enforce 2 days min in July (6) and August (7)
          if (m === 6 || m === 7) {
              nd.setDate(nd.getDate() + 1);
          }
          if (fpE) {
              fpE.set('minDate', nd);
              if (fpE.selectedDates[0] && fpE.selectedDates[0] < nd) {
                  fpE.setDate(nd);
              }
          }
          updateTotal();
        }"""

        html = html.replace(old_on_change, new_on_change)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
