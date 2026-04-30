import re

with open('site/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Options (Screenshot 1)
# 2a. Add "(obligatoire)" to static Nettoyage final
content = content.replace(
    '<div class="opt-card-name">🧹 Nettoyage final</div>',
    '<div class="opt-card-name">🧹 Nettoyage final (obligatoire)</div>'
)
# 2b. Remove static Caution block
caution_block = '''          <div class="opt-card">
            <div class="opt-card-name">��️ Caution</div>
            <div class="opt-card-price"><span id="caution-display">500</span> CHF</div>
          </div>'''
content = content.replace(caution_block, '')

# 2c. Remove dynamic Caution block in JS
dynamic_caution = '''          // Add caution card
          tg.innerHTML += `<div class="opt-card"><div class="opt-card-name">🛡️ Caution</div><div class="opt-card-price">${c.caution || 500} CHF</div></div>`;'''
content = content.replace(dynamic_caution, '')

# 3. Météo & annulation (Screenshot 2)
content = content.replace(
    'Remboursement intégral si météo défavorable.',
    'Possibilité de report en cas de conditions dangereuses (vent violent/tempête). Aucun report pour absence de vent.'
)

# 4. Avis Google link
avis_block = '''          <div>
            <div style="color:var(--gold2);font-size:16px;letter-spacing:2px">★★★★★</div>
            <div style="font-size:12px;color:var(--muted);margin-top:4px">5 avis vérifiés</div>
          </div>
        </div>'''
avis_new = '''          <div>
            <div style="color:var(--gold2);font-size:16px;letter-spacing:2px">★★★★★</div>
            <div style="font-size:12px;color:var(--muted);margin-top:4px">5 avis vérifiés</div>
          </div>
        </div>
        <a href="https://share.google/afqyXacNFCUYGWM0j" target="_blank" style="margin-left:auto; display:inline-block; padding: 10px 20px; border-radius: 4px; background: var(--teal); color: var(--white); font-weight: 500; font-size: 13px; text-decoration: none; margin-bottom: 16px;">✏️ Laisser un avis sur Google</a>'''
content = content.replace(avis_block, avis_new)

# 5. Visuel "Comment ça fonctionne"
ccf_old = '''          <div
            style="background:#f0f9ff;border:1px solid #bae6fd;border-radius:var(--r);padding:14px 18px;margin-bottom:14px;">
            <div style="display:flex;align-items:flex-start;gap:10px;">
              <div style="font-size:18px;flex-shrink:0;">ℹ️</div>
              <div style="font-size:13px;color:#0c4a6e;line-height:1.65;">'''
ccf_new = '''          <div
            style="background:#faf8f5;border:1px solid #eaddce;border-radius:var(--r);padding:14px 18px;margin-bottom:14px;">
            <div style="display:flex;align-items:flex-start;gap:10px;">
              <div style="font-size:13px;color:var(--muted);line-height:1.65;">'''
content = content.replace(ccf_old, ccf_new)

# 6. Flatpickr 1 day logic
fp_old_logic = '''          if (!d.length) return;
          var nd = new Date(d[0]); nd.setDate(nd.getDate() + 1);
          fpE.set('minDate', nd);
          if (fpE.selectedDates[0] && fpE.selectedDates[0] <= d[0]) fpE.clear();'''
fp_new_logic = '''          if (!d.length) return;
          var nd = new Date(d[0]); // allow same day
          fpE.set('minDate', nd);
          if (fpE.selectedDates[0] && fpE.selectedDates[0] < d[0]) fpE.clear();'''
content = content.replace(fp_old_logic, fp_new_logic)

# update total days calculation
calc_old = 'var days = Math.round((e - s) / 86400000);'
calc_new = 'var days = Math.round((e - s) / 86400000) + 1;'
content = content.replace(calc_old, calc_new)

# 7. Hide options for Pass Skipper
selectTab_old = '''      if (tabId === 'pass') {
        bS.style.background = 'var(--white)'; bS.style.color = 'var(--muted)'; bS.style.borderColor = 'var(--sand2)';
        bP.style.background = 'var(--navy)'; bP.style.color = 'var(--white)'; bP.style.borderColor = 'var(--navy)';
        currentTab = 'pass';
      } else {
        bP.style.background = 'var(--white)'; bP.style.color = 'var(--muted)'; bP.style.borderColor = 'var(--sand2)';
        bS.style.background = 'var(--navy)'; bS.style.color = 'var(--white)'; bS.style.borderColor = 'var(--navy)';
        currentTab = 'standard';
      }'''
selectTab_new = '''      var optsArea = document.getElementById('resa-options');
      if (tabId === 'pass') {
        bS.style.background = 'var(--white)'; bS.style.color = 'var(--muted)'; bS.style.borderColor = 'var(--sand2)';
        bP.style.background = 'var(--navy)'; bP.style.color = 'var(--white)'; bP.style.borderColor = 'var(--navy)';
        currentTab = 'pass';
        if (optsArea) optsArea.style.display = 'none';
      } else {
        bP.style.background = 'var(--white)'; bP.style.color = 'var(--muted)'; bP.style.borderColor = 'var(--sand2)';
        bS.style.background = 'var(--navy)'; bS.style.color = 'var(--white)'; bS.style.borderColor = 'var(--navy)';
        currentTab = 'standard';
        if (optsArea) optsArea.style.display = 'block';
      }'''
content = content.replace(selectTab_old, selectTab_new)

# 8. Reorder hidden inputs for email
hidden_old = '''    <form name="reservation" method="POST" data-netlify="true" class="resa-wrap rv">
      <input type="hidden" name="form-name" value="reservation">
      <input type="hidden" name="subject" value="Demande de réservation - Voilier Neuchâtel">
      <input type="hidden" name="type_reservation" id="resa-type-hidden" value="Location standard">
      <input type="hidden" name="total" id="resa-total-hidden" value="">
      <input type="hidden" name="options_choisies" id="resa-options-hidden" value="">
      <input type="hidden" name="duree_jours" id="resa-duree-hidden" value="">'''
hidden_new = '''    <form name="reservation" method="POST" data-netlify="true" class="resa-wrap rv">
      <input type="hidden" name="form-name" value="reservation">
      <input type="hidden" name="subject" value="Demande de réservation - Voilier Neuchâtel">
      <input type="hidden" name="type_reservation" id="resa-type-hidden" value="Location standard">
      <input type="hidden" name="duree_jours" id="resa-duree-hidden" value="">
      <input type="hidden" name="options_choisies" id="resa-options-hidden" value="">
      <input type="hidden" name="total" id="resa-total-hidden" value="">'''
content = content.replace(hidden_old, hidden_new)

# Update options chosen string to include prices
options_js_old = '''          var cleanName = nameSpan.textContent.replace(/[^\w\sÀ-ÿ-]/g, '').trim();
          selectedOptions.push(cleanName);'''
options_js_new = '''          var cleanName = nameSpan.textContent.replace(/[^\w\sÀ-ÿ-()]/g, '').trim();
          var p = parseInt(cb.dataset.price) || 0;
          var pl = cb.dataset.per === 'jour' ? ' (+' + p + ' CHF/jour)' : ' (+' + p + ' CHF)';
          selectedOptions.push(cleanName + pl);'''
content = content.replace(options_js_old, options_js_new)

# Also, if tab is 'pass', we shouldn't charge options
update_total_opts_old = '''      document.querySelectorAll('#resa-options input:checked').forEach(function (cb) {
        var p = parseInt(cb.dataset.price) || 0;
        total += (cb.dataset.per === 'jour') ? p * days : p;
      });'''
update_total_opts_new = '''      var isPass = (typeof currentTab !== 'undefined' && currentTab === 'pass');
      if (!isPass) {
        document.querySelectorAll('#resa-options input:checked').forEach(function (cb) {
          var p = parseInt(cb.dataset.price) || 0;
          total += (cb.dataset.per === 'jour') ? p * days : p;
        });
      }'''
content = content.replace(update_total_opts_old, update_total_opts_new)

# Same for selectedOptions string logic
selected_opts_loop_old = '''      document.querySelectorAll('#resa-options input:checked').forEach(function (cb) {
        var nameSpan = cb.nextElementSibling.querySelector('.ocn');
        if (nameSpan) {
          var cleanName = nameSpan.textContent.replace(/[^\w\sÀ-ÿ-()]/g, '').trim();
          var p = parseInt(cb.dataset.price) || 0;
          var pl = cb.dataset.per === 'jour' ? ' (+' + p + ' CHF/jour)' : ' (+' + p + ' CHF)';
          selectedOptions.push(cleanName + pl);
        }
      });'''
selected_opts_loop_new = '''      if (!isPass) {
        document.querySelectorAll('#resa-options input:checked').forEach(function (cb) {
          var nameSpan = cb.nextElementSibling.querySelector('.ocn');
          if (nameSpan) {
            var cleanName = nameSpan.textContent.replace(/[^\w\sÀ-ÿ-()]/g, '').trim();
            var p = parseInt(cb.dataset.price) || 0;
            var pl = cb.dataset.per === 'jour' ? ' (+' + p + ' CHF/jour)' : ' (+' + p + ' CHF)';
            selectedOptions.push(cleanName + pl);
          }
        });
      }'''
content = content.replace(selected_opts_loop_old, selected_opts_loop_new)

with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
