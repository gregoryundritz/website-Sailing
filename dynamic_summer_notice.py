import glob

files = {
    'site/contact.html': ('* min. 2 jours en juillet et août.', 'min. 2 jours en juillet et août.'),
    'site/de/kontakt.html': ('* Min. 2 Tage im Juli und August.', 'Min. 2 Tage im Juli und August.'),
    'site/en/contact.html': ('* Min. 2 days in July and August.', 'Min. 2 days in July and August.')
}

for file_path, (old_text, new_text) in files.items():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html = f.read()

        # 1. Update text and add ID and hide by default
        html = html.replace(old_text, new_text)
        html = html.replace('<div style="font-size: 13px; color: var(--gold); margin-bottom: 12px; margin-top: -8px;">',
                            '<div id="summer-notice" style="display: none; font-size: 13px; color: var(--gold); margin-bottom: 12px; margin-top: -8px;">')

        # 2. Update fpS onChange
        old_onChange = """          var m = nd.getMonth();
          // Enforce 2 days min in July (6) and August (7)
          if (m === 6 || m === 7) {
              nd.setDate(nd.getDate() + 1);
          }"""
        new_onChange = """          var m = nd.getMonth();
          var sn = document.getElementById('summer-notice');
          // Enforce 2 days min in July (6) and August (7)
          if (m === 6 || m === 7) {
              nd.setDate(nd.getDate() + 1);
              if (sn) sn.style.display = 'block';
          } else {
              if (sn) sn.style.display = 'none';
          }"""
        html = html.replace(old_onChange, new_onChange)

        # 3. Update the init force sync
        old_init_sync = """      if (fpS.selectedDates.length > 0) {
          var nd = new Date(fpS.selectedDates[0]);
          var m = nd.getMonth();
          if (m === 6 || m === 7) nd.setDate(nd.getDate() + 1);"""
        new_init_sync = """      if (fpS.selectedDates.length > 0) {
          var nd = new Date(fpS.selectedDates[0]);
          var m = nd.getMonth();
          var sn = document.getElementById('summer-notice');
          if (m === 6 || m === 7) {
              nd.setDate(nd.getDate() + 1);
              if (sn) sn.style.display = 'block';
          } else {
              if (sn) sn.style.display = 'none';
          }"""
        html = html.replace(old_init_sync, new_init_sync)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
            
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error on {file_path}: {e}")
