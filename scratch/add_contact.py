with open('site/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update navbar: "Réserver" -> "Nous contacter"
content = content.replace(
    '<li><a href="#reservation" class="nav-btn">Réserver</a></li>',
    '<li><a href="#contact" class="nav-btn">Nous contacter</a></li>'
)

# 2. Update hero buttons: "Réserver maintenant" -> "Nous contacter"
content = content.replace(
    '<a href="#reservation" class="btn-p">Réserver maintenant</a>',
    '<a href="#contact" class="btn-p">Nous contacter</a>'
)

# 3. Soften the reservation section header
content = content.replace(
    '''      <div class="rv" style="text-align:center">
        <p class="sec-ey">Réservation directe</p>
        <h2 class="sec-h" style="max-width:500px;margin:0 auto 16px">Réservez & <em>payez en ligne</em></h2>
        <p class="sec-p" style="margin:0 auto">Carburant inclus · Nuitées au port de Cheyres gratuites</p>
      </div>''',
    '''      <div class="rv" style="text-align:center">
        <p class="sec-ey">Formulaire de demande</p>
        <h2 class="sec-h" style="max-width:500px;margin:0 auto 16px">Une date <em>en tête ?</em></h2>
        <p class="sec-p" style="margin:0 auto">Carburant inclus · Aucun paiement maintenant · Confirmation sous 24h</p>
      </div>'''
)

# 4. Insert contact section before reservation section
contact_section = '''  <!-- CONTACT -->
  <section id="contact" style="background:var(--white);padding:80px 24px;">
    <div class="ct">
      <div class="rv" style="text-align:center;margin-bottom:48px;">
        <p class="sec-ey">Contact</p>
        <h2 class="sec-h" style="max-width:520px;margin:0 auto 16px;">Une question ? <em>Parlons-en</em></h2>
        <p class="sec-p" style="margin:0 auto;">Réservation ou simple question — je réponds personnellement sous 24h. N'hésitez pas à me contacter avant de remplir le formulaire.</p>
      </div>
      <div class="rv" style="display:flex;gap:24px;justify-content:center;flex-wrap:wrap;max-width:700px;margin:0 auto 40px;">
        <a href="mailto:welcome@voilier-neuchatel.ch" style="flex:1;min-width:260px;display:flex;align-items:center;gap:18px;padding:28px 32px;border-radius:var(--r);border:1.5px solid var(--sand2);background:var(--sand);text-decoration:none;transition:box-shadow .2s;" onmouseover="this.style.boxShadow='0 4px 24px rgba(0,0,0,0.08)'" onmouseout="this.style.boxShadow='none'">
          <div style="width:48px;height:48px;border-radius:50%;background:var(--navy);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:20px;">✉️</div>
          <div>
            <div style="font-size:11px;font-weight:600;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);margin-bottom:4px;">Email</div>
            <div style="font-family:'Cormorant Garamond',serif;font-size:17px;color:var(--navy);font-weight:500;">welcome@voilier-neuchatel.ch</div>
          </div>
        </a>
        <a href="tel:+41793867381" style="flex:1;min-width:260px;display:flex;align-items:center;gap:18px;padding:28px 32px;border-radius:var(--r);border:1.5px solid var(--sand2);background:var(--sand);text-decoration:none;transition:box-shadow .2s;" onmouseover="this.style.boxShadow='0 4px 24px rgba(0,0,0,0.08)'" onmouseout="this.style.boxShadow='none'">
          <div style="width:48px;height:48px;border-radius:50%;background:var(--teal);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-size:20px;">📞</div>
          <div>
            <div style="font-size:11px;font-weight:600;letter-spacing:.15em;text-transform:uppercase;color:var(--muted);margin-bottom:4px;">Téléphone</div>
            <div style="font-family:'Cormorant Garamond',serif;font-size:17px;color:var(--navy);font-weight:500;">+41 79 386 73 81</div>
          </div>
        </a>
      </div>
      <div class="rv" style="text-align:center;">
        <p style="font-size:14px;color:var(--muted);margin-bottom:20px;">Vous avez déjà une date en tête ? Utilisez directement notre formulaire de demande.</p>
        <a href="#reservation" style="display:inline-block;padding:12px 28px;border-radius:var(--r);border:1.5px solid var(--navy);color:var(--navy);font-size:13px;font-weight:500;text-decoration:none;font-family:'DM Sans',sans-serif;transition:background .2s,color .2s;" onmouseover="this.style.background='var(--navy)';this.style.color='var(--white)'" onmouseout="this.style.background='transparent';this.style.color='var(--navy)'">Accéder au formulaire →</a>
      </div>
    </div>
  </section>

  <!-- RÉSERVATION -->'''

content = content.replace('  <!-- RÉSERVATION -->', contact_section)

with open('site/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("done")
