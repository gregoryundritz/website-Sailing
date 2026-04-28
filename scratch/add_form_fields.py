import re

files = [
    'site/index.html',
    'site/en/index.html',
    'site/de/index.html'
]

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add hidden fields
    if 'id="resa-options-hidden"' not in content:
        form_hidden_inject = '''<input type="hidden" name="type_reservation" id="resa-type-hidden" value="Location standard">
        <input type="hidden" name="total" id="resa-total-hidden" value="">
        <input type="hidden" name="options_choisies" id="resa-options-hidden" value="">
        <input type="hidden" name="duree_jours" id="resa-duree-hidden" value="">'''
        
        content = content.replace(
            '''<input type="hidden" name="type_reservation" id="resa-type-hidden" value="Location standard">
        <input type="hidden" name="total" id="resa-total-hidden" value="">''',
            form_hidden_inject
        )

    # 2. Update updateTotal()
    old_update = '''// Optimization: Update hidden fields for Netlify
  var hTotal = document.getElementById('resa-total-hidden');
  var hType = document.getElementById('resa-type-hidden');
  if(hTotal) hTotal.value = total + ' CHF';
  if(hType) {
    var isPass = (typeof currentTab !== 'undefined' && currentTab === 'pass');
    hType.value = isPass ? 'Pass Skipper' : 'Location standard';
  }'''
    
    new_update = '''// Optimization: Update hidden fields for Netlify
  var hTotal = document.getElementById('resa-total-hidden');
  var hType = document.getElementById('resa-type-hidden');
  var hOptions = document.getElementById('resa-options-hidden');
  var hDuree = document.getElementById('resa-duree-hidden');
  
  if(hTotal) hTotal.value = total + ' CHF';
  if(hType) {
    var isPass = (typeof currentTab !== 'undefined' && currentTab === 'pass');
    hType.value = isPass ? 'Pass Skipper' : 'Location standard';
  }
  if(hDuree && typeof days !== 'undefined') {
    hDuree.value = days ? days + ' jours' : '';
  }
  
  var selectedOptions = [];
  document.querySelectorAll('#resa-options input:checked').forEach(function(cb){
    var nameSpan = cb.nextElementSibling.querySelector('.ocn');
    if(nameSpan) {
        // Strip emojis to make it cleaner in email
        var cleanName = nameSpan.textContent.replace(/[^\w\sÀ-ÿ-]/g, '').strip || nameSpan.textContent.trim();
        selectedOptions.push(cleanName.trim());
    }
  });
  if(hOptions) {
    hOptions.value = selectedOptions.length ? selectedOptions.join(', ') : 'Aucune option';
  }'''
  
    content = content.replace(old_update, new_update)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for file in files:
    process_file(file)

print("Updates applied to all 3 files")
