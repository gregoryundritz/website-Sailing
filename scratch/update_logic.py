import os

def update_technical_logic(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add hidden inputs for total/type if missing
    if 'id="resa-total-hidden"' not in content:
        content = content.replace(
            '<div class="fg"><label>Message (optionnel)</label>',
            '<input type="hidden" name="type_reservation" id="resa-type-hidden" value="Location standard">\n        <input type="hidden" name="total" id="resa-total-hidden" value="">\n        <div class="fg"><label>Message (optionnel)</label>'
        )
        # Handle EN/DE message labels
        content = content.replace(
            '<div class="fg"><label>Message (optional)</label>',
            '<input type="hidden" name="type_reservation" id="resa-type-hidden" value="Standard Rental">\n        <input type="hidden" name="total" id="resa-total-hidden" value="">\n        <div class="fg"><label>Message (optional)</label>'
        )

    # Replace handleResaSubmit with AJAX logic
    old_js_start = "// ── Form submission: save to localStorage"
    if old_js_start in content:
        # We find the whole old function and replace it
        # Actually it's easier to replace the loadPrices part
        ajax_js = """
// ── Netlify Form AJAX Handling ──
document.addEventListener('DOMContentLoaded', function() {
  const resaForm = document.querySelector('form[name="reservation"]');
  if (resaForm) {
    resaForm.addEventListener('submit', function(e) {
      e.preventDefault();
      const btn = document.getElementById('resa-submit-btn');
      const note = document.getElementById('resa-note');
      const formData = new FormData(resaForm);
      
      btn.disabled = true;
      btn.textContent = '...';

      fetch('/', {
        method: 'POST',
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams(formData).toString()
      })
      .then(() => {
        btn.style.background = '#28a745';
        btn.textContent = 'OK !';
        note.textContent = 'Enquiry sent!';
        resaForm.reset();
        if(fpS) fpS.clear();
        if(fpE) fpE.clear();
        updateTotal();
      })
      .catch((error) => {
        btn.disabled = false;
        btn.textContent = 'Error';
      });
    });
  }
});
loadPrices();
"""
        # Remove old function logic (rough cut)
        if "function handleResaSubmit" in content:
            import re
            content = re.sub(r'// ── Form submission.*?loadPrices\(\);', ajax_js, content, flags=re.DOTALL)

    # Update updateTotal to fill hidden fields
    if "total.toLocaleString" in content and "resa-total-hidden" not in content:
        content = content.replace(
            "if(tt) tt.textContent=total.toLocaleString('fr-CH')+' CHF';",
            "if(tt) tt.textContent=total.toLocaleString('fr-CH')+' CHF';\n  var hT=document.getElementById('resa-total-hidden'); if(hT) hT.value=total+' CHF';"
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Apply to all
for lang in ['en', 'de']:
    update_technical_logic(f'/home/gregory/Voilier/site/{lang}/index.html')

print("Technical logic propogated to all languages.")
