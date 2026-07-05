/**
 * CONFIGURATION DU SITE
 * Modifiez ce fichier pour appliquer les changements sur les versions FR, EN et DE.
 */

window.VOILIER_CONFIG = {
  // Grille des prix (en CHF) selon le nombre de jours

  // Paramètres Google Calendar
  // Remplacez 'VOTRE_CLE_API_ICI' par la clé que vous allez créer
  GOOGLE_CALENDAR_API_KEY: 'AIzaSyB3U9splqxZ5tUG3LnIQA1LU6mquxNvaio',
  GOOGLE_CALENDAR_ID: '352a23f170d4b8a0d40b183303bb12ea40350fc2e420b12dac648695db8a4095@group.calendar.google.com',

  prices_per_days: {
    1: 275,
    2: 510,
    3: 750,
    4: 980,
    5: 1200,
    6: 1410,
    7: 1610,
  },

  // Montant de la caution (en CHF)
  caution: 1000,




  // Modules d'options supplémentaires
  // L'ordre dans lequel vous les placez ici sera l'ordre d'affichage.
  // - name: Nom de l'option (les icônes sont gérées automatiquement ou vous pouvez les inclure)
  // - price: Prix (en CHF)
  // - per: "forfait" (paiement unique) ou "jour" (paiement par jour)
  // - required: true (obligatoire, la case sera cochée et bloquée), false (facultatif)
  options: [
    { name: "Paddle", price: 15, per: "jour", required: false },
    { name: "Gennaker", price: 15, per: "jour", required: false },
    { name: "Nettoyage final (obligatoire)", price: 50, per: "forfait", required: true }
  ],

  // Paramètres Skipper Pass
  pass_price: 800,
  pass_sorties: 5,
  pass_guests: 2
};

window.VOILIER_TRANSLATIONS = {
  'Nettoyage final (obligatoire)': { 'de': 'Endreinigung (obligatorisch)', 'en': 'Final cleaning (mandatory)' },
  'Nettoyage final': { 'de': 'Endreinigung', 'en': 'Final cleaning' },
  'Paddle': { 'de': 'Stand-Up Paddle', 'en': 'Paddleboard' },
  'Gennaker': { 'de': 'Gennaker', 'en': 'Gennaker' }
};

document.addEventListener('DOMContentLoaded', function () {
  const mobFloat = document.querySelector('.mob-float');
  if (mobFloat) {
    const observer = new IntersectionObserver((entries) => {
      let isVisible = false;
      entries.forEach(entry => {
        if (entry.isIntersecting) isVisible = true;
      });
      if (isVisible) {
        mobFloat.style.opacity = '0';
        mobFloat.style.pointerEvents = 'none';
        mobFloat.style.transform = 'translate(-50%, 20px)';
      } else {
        mobFloat.style.opacity = '1';
        mobFloat.style.pointerEvents = 'all';
        mobFloat.style.transform = 'translateX(-50%)';
      }
    }, { threshold: 0.1 });

    document.querySelectorAll('.resa-wrap, footer').forEach(el => observer.observe(el));
  }
});
