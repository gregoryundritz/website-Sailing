import glob
import re

files = {
    'site/contact.html': ('<div id="summer-notice" style="display: none; font-size: 14px; font-weight: 600; color: #7a5a10; background: #fff8ee; border: 1px solid #f0d898; border-radius: var(--r); padding: 10px 14px; margin-bottom: 16px; margin-top: -4px;">min. 2 jours en juillet et août</div>', 'min. 2 jours en juillet et août'),
    'site/de/kontakt.html': ('<div id="summer-notice" style="display: none; font-size: 14px; font-weight: 600; color: #7a5a10; background: #fff8ee; border: 1px solid #f0d898; border-radius: var(--r); padding: 10px 14px; margin-bottom: 16px; margin-top: -4px;">Min. 2 Tage im Juli und August</div>', 'Min. 2 Tage im Juli und August'),
    'site/en/contact.html': ('<div id="summer-notice" style="display: none; font-size: 14px; font-weight: 600; color: #7a5a10; background: #fff8ee; border: 1px solid #f0d898; border-radius: var(--r); padding: 10px 14px; margin-bottom: 16px; margin-top: -4px;">Min. 2 days in July and August</div>', 'Min. 2 days in July and August')
}

for file_path, (old_html_notice, localized_text) in files.items():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # Remove the HTML notice
        html = html.replace(old_html_notice, '')

        # Replace initFp block
        pattern = r'function initFp\(\) \{.*?\n    \}'
        
        new_init = f"""function initFp() {{
      if (typeof flatpickr === 'undefined') {{ setTimeout(initFp, 80); return; }}
      var loc = (typeof flatpickr.l10ns !== 'undefined' && flatpickr.l10ns.fr) ? 'fr' : 'default';
      
      var summerNoticeText = "{localized_text}";
      function toggleNotice(inst) {{
          var m = inst.currentMonth;
          if (inst.summerNote) {{
              inst.summerNote.style.display = (m === 6 || m === 7) ? 'block' : 'none';
          }}
      }}
      function onReadyHandler(s, d, inst) {{
          var note = document.createElement("div");
          note.innerHTML = summerNoticeText;
          note.style.padding = "10px";
          note.style.textAlign = "center";
          note.style.fontSize = "13px";
          note.style.fontWeight = "600";
          note.style.color = "#7a5a10";
          note.style.background = "#fff8ee";
          note.style.borderTop = "1px solid #f0d898";
          note.style.display = "none";
          inst.calendarContainer.appendChild(note);
          inst.summerNote = note;
          toggleNotice(inst);
      }}

      fpS = flatpickr('#fp-start', {{
        disable: window.VOILIER_BLOCKED_DATES, locale: loc, dateFormat: 'j F Y', minDate: minD, disableMobile: true, allowInput: false,
        onReady: onReadyHandler,
        onMonthChange: function(s, d, inst) {{ toggleNotice(inst); }},
        onYearChange: function(s, d, inst) {{ toggleNotice(inst); }},
        onOpen: function(s, d, inst) {{ toggleNotice(inst); }},
        onChange: function (d) {{
          if (!d.length) return;
          var nd = new Date(d[0]);
          var m = nd.getMonth();
          if (m === 6 || m === 7) {{
              nd.setDate(nd.getDate() + 1);
          }}
          if (fpE) {{
              fpE.set('minDate', nd);
              if (fpE.selectedDates[0] && fpE.selectedDates[0] < nd) {{
                  fpE.setDate(nd);
              }}
          }}
          updateTotal();
        }}
      }});
      fpE = flatpickr('#fp-end', {{
        disable: window.VOILIER_BLOCKED_DATES, locale: loc, dateFormat: 'j F Y', minDate: minD, disableMobile: true, allowInput: false,
        onReady: onReadyHandler,
        onMonthChange: function(s, d, inst) {{ toggleNotice(inst); }},
        onYearChange: function(s, d, inst) {{ toggleNotice(inst); }},
        onOpen: function(s, d, inst) {{ toggleNotice(inst); }},
        onChange: function () {{ updateTotal(); }}
      }});

      // Force sync constraints if dates were pre-filled (e.g. from draft)
      if (fpS.selectedDates.length > 0) {{
          var nd = new Date(fpS.selectedDates[0]);
          var m = nd.getMonth();
          if (m === 6 || m === 7) nd.setDate(nd.getDate() + 1);
          fpE.set('minDate', nd);
          if (fpE.selectedDates.length > 0 && fpE.selectedDates[0] < nd) {{
              fpE.setDate(nd, true);
          }}
      }}
      updateTotal();
    }}"""
        
        html = re.sub(pattern, new_init, html, flags=re.DOTALL)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
