/**
 * CONFIGURATION DU SITE
 * Modifiez ce fichier pour appliquer les changements sur les versions FR, EN et DE.
 */

window.VOILIER_CONFIG = {
  // Grille des prix (en CHF) selon le nombre de jours
  prices_per_days: {
    1: 190,
    2: 360,
    3: 510,
    4: 640,
    5: 750,
    6: 840,
    7: 910,
    14: 1400
  },

  // Montant de la caution (en CHF)
  caution: 1000,

  // Dates bloquées dans le calendrier (format "YYYY-MM-DD")
  // Exemple: ["2026-05-01", "2026-05-02"]
  blocked_dates: [

  ],

  // Modules d'options supplémentaires
  // L'ordre dans lequel vous les placez ici sera l'ordre d'affichage.
  // - name: Nom de l'option (les icônes sont gérées automatiquement ou vous pouvez les inclure)
  // - price: Prix (en CHF)
  // - per: "forfait" (paiement unique) ou "jour" (paiement par jour)
  // - required: true (obligatoire, la case sera cochée et bloquée), false (facultatif)
  options: [
    { name: "Briefing navigation", price: 50, per: "forfait", required: false },
    { name: "Nettoyage final", price: 60, per: "forfait", required: true },
    { name: "Gennaker", price: 30, per: "jour", required: false },
    { name: "Paddle", price: 20, per: "jour", required: false }
  ]
};
