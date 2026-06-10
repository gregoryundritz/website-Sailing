import glob

contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for file_path in contact_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        old_init_fp_end = """      fpE = flatpickr('#fp-end', {
        disable: window.VOILIER_BLOCKED_DATES, locale: loc, dateFormat: 'j F Y', minDate: minD, disableMobile: true, allowInput: false,
        onChange: function () { updateTotal(); }
      });
    }"""

        new_init_fp_end = """      fpE = flatpickr('#fp-end', {
        disable: window.VOILIER_BLOCKED_DATES, locale: loc, dateFormat: 'j F Y', minDate: minD, disableMobile: true, allowInput: false,
        onChange: function () { updateTotal(); }
      });

      // Force sync constraints if dates were pre-filled (e.g. from draft)
      if (fpS.selectedDates.length > 0) {
          var nd = new Date(fpS.selectedDates[0]);
          var m = nd.getMonth();
          if (m === 6 || m === 7) nd.setDate(nd.getDate() + 1);
          fpE.set('minDate', nd);
          if (fpE.selectedDates.length > 0 && fpE.selectedDates[0] < nd) {
              fpE.setDate(nd, true);
          }
      }
      updateTotal();
    }"""

        html = html.replace(old_init_fp_end, new_init_fp_end)
        
        # Also fix loadFormData to trigger onChange just in case it runs AFTER initFp
        html = html.replace('window.fpS.setDate(data.date_depart);', 'window.fpS.setDate(data.date_depart, true);')
        html = html.replace('window.fpE.setDate(data.date_retour);', 'window.fpE.setDate(data.date_retour, true);')

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
