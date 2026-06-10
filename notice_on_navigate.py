import glob
import re

contact_files = ['site/contact.html', 'site/de/kontakt.html', 'site/en/contact.html']

for file_path in contact_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Extract the entire function initFp() block up to its closing brace
        pattern = r'function initFp\(\) \{.*?\n    \}'
        
        new_init = """function initFp() {
      if (typeof flatpickr === 'undefined') { setTimeout(initFp, 80); return; }
      var loc = (typeof flatpickr.l10ns !== 'undefined' && flatpickr.l10ns.fr) ? 'fr' : 'default';
      
      function toggleNotice(inst) {
          var m = inst.currentMonth;
          var sn = document.getElementById('summer-notice');
          if (sn) sn.style.display = (m === 6 || m === 7) ? 'block' : 'none';
      }
      function checkNotice() {
          var sn = document.getElementById('summer-notice');
          if (!sn) return;
          var m = (fpS && fpS.selectedDates[0]) ? fpS.selectedDates[0].getMonth() : -1;
          sn.style.display = (m === 6 || m === 7) ? 'block' : 'none';
      }

      fpS = flatpickr('#fp-start', {
        disable: window.VOILIER_BLOCKED_DATES, locale: loc, dateFormat: 'j F Y', minDate: minD, disableMobile: true, allowInput: false,
        onMonthChange: function(s, d, inst) { toggleNotice(inst); },
        onYearChange: function(s, d, inst) { toggleNotice(inst); },
        onOpen: function(s, d, inst) { toggleNotice(inst); },
        onClose: function() { checkNotice(); },
        onChange: function (d) {
          if (!d.length) return;
          var nd = new Date(d[0]);
          var m = nd.getMonth();
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
        }
      });
      fpE = flatpickr('#fp-end', {
        disable: window.VOILIER_BLOCKED_DATES, locale: loc, dateFormat: 'j F Y', minDate: minD, disableMobile: true, allowInput: false,
        onMonthChange: function(s, d, inst) { toggleNotice(inst); },
        onYearChange: function(s, d, inst) { toggleNotice(inst); },
        onOpen: function(s, d, inst) { toggleNotice(inst); },
        onClose: function() { checkNotice(); },
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
      checkNotice();
      updateTotal();
    }"""
        
        html = re.sub(pattern, new_init, html, flags=re.DOTALL)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
