/**
 * CONFIGURATION DU SITE
 * Modifiez ce fichier pour appliquer les changements sur les versions FR, EN et DE.
 */

window.VOILIER_CONFIG = {
  // Grille des prix (en CHF) selon le nombre de jours
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
    { name: "Nettoyage final", price: 60, per: "forfait", required: true },
    { name: "Briefing navigation", price: 50, per: "forfait", required: false },
    { name: "Gennaker", price: 30, per: "jour", required: false },
    { name: "Paddle", price: 20, per: "jour", required: false }
  ]
};
