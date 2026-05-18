# Audit complet — voilier-neuchatel.ch
**Date :** mai 2026 · **Périmètre :** site web, SEO, UX, positionnement, concurrence, évolutions business

---

## 1. Synthèse exécutive

### Ce qui marche déjà très bien
- **Positionnement clair** : voilier habitable, Cheyres, lac de Neuchâtel, dès 275 CHF.
- **Social proof solide** : 28 avis Google, 4.9/5 affichés haut sur la page.
- **Conversion design** : single-page bien rythmée, CTA visibles, WhatsApp en pied de page collant, formulaire de réservation intégré.
- **Offre différenciante** : le *Skipper Pass* (5 sorties à 800 CHF, semaine, valable l'année) est un excellent produit qui te protège des plateformes et fidélise.
- **Meta de base correctes** : title, meta description, OG tags, Twitter cards, canonical, viewport, robots `index, follow`, Google Search Console vérifié.
- **Mentions légales et CGL** : pages dédiées propres et conformes RGPD/LPD.

### Les 5 priorités absolues (impact / effort)
1. **Aligner les prix entre ton site et Click&Boat/SamBoat** — tu te tires une balle dans le pied.
2. **Ajouter JSON-LD (`LocalBusiness` + `Product` + `Review` + `FAQPage`)** — gain SEO immédiat, rich snippets.
3. **Créer 4–6 pages de contenu (mouillages, itinéraires, FAQ permis, météo)** — c'est ce qui fait que Google te trouve sur les requêtes longue traîne.
4. **Version allemande (de-CH)** — tu déclares `og:locale:alternate de_CH` mais la page n'existe pas. La Suisse alémanique = ~60 % du marché touristique suisse.
5. **Pivoter une partie de l'offre vers les expériences à plus haute marge** (apéro coucher de soleil avec skipper, anniversaire, demande en mariage, teambuilding) — détaillé en section 7.

---

## 2. Audit SEO & référencement Google

### 2.1 On-page : ce qui est en place
| Élément | État | Commentaire |
|---|---|---|
| `<title>` | ✅ Bon | « Location Voilier Lac de Neuchâtel — Cheyres, Suisse \| Maxus 21 » — 70 caractères, mots-clés primaires bien placés |
| `meta description` | ✅ Bon | 160 caractères, incluant CTA et prix |
| Canonical | ✅ | `https://voilier-neuchatel.ch/` |
| OG/Twitter | ✅ | OK |
| Robots | ✅ | `index, follow` |
| Google Site Verification | ✅ | Search Console actif |
| HTTPS | ✅ | Netlify gère bien |
| H1 unique | ✅ | « Votre voilier sur le lac de Neuchâtel » |

### 2.2 Ce qui manque (à corriger en priorité)

**Données structurées JSON-LD — absentes.** C'est le manque le plus rentable à combler. Ajoute dans le `<head>` :

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://voilier-neuchatel.ch/#business",
  "name": "Voilier Lac de Neuchâtel",
  "image": "https://voilier-neuchatel.ch/img/og-preview.jpg",
  "telephone": "+41793867381",
  "email": "welcome@voilier-neuchatel.ch",
  "priceRange": "CHF 180–275",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Cheyres",
    "postalCode": "1468",
    "addressCountry": "CH"
  },
  "geo": { "@type": "GeoCoordinates", "latitude": 46.815, "longitude": 6.786 },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.9",
    "reviewCount": "28"
  }
}
```

Ajoute aussi un schema `Product` (avec offre, prix, disponibilité) et un `FAQPage` (voir section 3.4).

**Multilangue déclaré mais inexistant.** Le HTML déclare `og:locale:alternate: de_CH`. Soit tu crées vraiment une version DE, soit tu retires la déclaration (Google déteste les fausses promesses hreflang). Idem pour l'anglais — 3 de tes 9 avis affichés sont en anglais (Rupert, Martijn, Brian), preuve qu'il y a une clientèle internationale.

**Pas de sitemap.xml et robots.txt visible.** À vérifier : `https://voilier-neuchatel.ch/sitemap.xml` et `/robots.txt` doivent exister et lister les pages.

**Structure mono-page = SEO plafonné.** Tu te bats sur une seule URL pour toutes les requêtes. Tu devrais créer :
- `/voilier-maxus-21` (page produit dédiée)
- `/itineraires-lac-neuchatel` (guide des mouillages)
- `/permis-bateau-suisse` (FAQ permis)
- `/skipper-pass` (page dédiée à l'offre signature)
- `/cheyres-port` (page locale)
- `/blog` (pour la longue traîne saisonnière)

**Alt text à vérifier.** Tu as au moins une image `logo.jpg` utilisée pour montrer le bateau au port — probablement un mauvais asset. À auditer image par image.

### 2.3 Mots-clés à viser (avec stratégie)

Classement attendu et difficulté estimés :

| Requête | Volume estimé/mois (CH-FR) | Difficulté | Action |
|---|---|---|---|
| location voilier lac neuchâtel | 200–500 | Moyenne | **Page d'accueil** (déjà bien partie) |
| louer bateau cheyres | 50–100 | Faible | Page locale dédiée |
| voilier habitable suisse romande | 100–300 | Moyenne | Page produit + blog |
| weekend voilier suisse | 50–200 | Moyenne | Article blog « weekend romantique en voilier » |
| skipper pass lac neuchâtel | <50 | Très faible | Page dédiée (tu serais #1) |
| cours voile lac neuchâtel | 100–300 | Forte | Articles, pas frontal contre Alpha Voile / Les Vikings |
| Segelboot mieten Neuenburgersee | 50–200 (DE-CH) | Faible | **Version allemande = océan bleu** |

**Stratégie longue traîne** : crée des articles ciblant les requêtes informationnelles qui amèneront des locataires : « peut-on dormir sur un voilier au port de Cheyres », « météo et joran lac de Neuchâtel », « 10 plus belles plages accessibles en voilier sur le lac », « obtenir le permis voile suisse en 2026 ».

### 2.4 Local SEO

- **Google Business Profile** : à vérifier impérativement (revendiquer la fiche, photos pro, posts hebdo, liens vers site, FAQ activée). Les avis vérifiés Google que tu as déjà → c'est exactement ce qui te fait monter dans Google Maps. Continue d'en demander à chaque locataire (template d'email post-location).
- **Citations locales** : assure-toi d'être listé sur Local.ch, Search.ch, TripAdvisor (catégorie « activité »), Yelp Suisse, j3l.ch (tourisme Jura & 3 Lacs — c'est là qu'apparaît la concurrence « Découverte du lac à la voile » depuis Hauterive, exemple à copier).
- **Office du tourisme** : Estavayer-le-Lac Tourisme et Cheyres-Châbles devraient avoir un lien vers toi. À demander.

### 2.5 Backlinks / autorité

Probable que ton domaine est jeune et peu lié. Quelques actions :
- Inscription aux annuaires tourisme suisses (j3l.ch, myswitzerland.com).
- Article invité sur les blogs nautiques romands (bateau24.ch, lakeboat.ch ont des sections édito).
- Partenariat de contenu avec un B&B / camping à Cheyres (« notre partenaire voilier »).
- Le forum Hisse-et-Oh / scanvoile (mentions naturelles dans des fils de discussion sur le lac de Neuchâtel).

---

## 3. Audit UX (desktop, tablette, mobile)

### 3.1 Architecture
Site single-page avec ancres : `#bateau`, `#emplacement`, `#tarifs`, `#infos`, `#avis`, `#apropos`, `#contact`, `#reservation`. C'est efficace pour la conversion d'un visiteur déjà chaud, mais limite la profondeur informationnelle.

### 3.2 Mobile (priorité absolue — probablement 60–75 % du trafic)
À vérifier sur ton site, par expérience avec ce type de page :
- **Boutons CTA WhatsApp / Réserver flottants** : déjà présents en footer (bien), s'assurer qu'ils ne masquent pas de contenu critique.
- **Tableau de tarifs en colonnes** : sur smartphone, un tableau 7 colonnes (1j → 7j) est ingérable. À tester ; si scroll horizontal nécessaire, repenser en cartes empilées ou en sélecteur de durée.
- **Carte Google Maps embed** : lourde en JS, à charger en lazy (`loading="lazy"` sur l'iframe) pour ne pas pénaliser le LCP.
- **Formulaire de réservation** : champs nombreux (nb équipage, niveau, upload permis, options, CGL). Sur mobile, c'est un point de friction massif. **Recommandation** : passer en formulaire en 3 étapes (Dates → Équipage & options → Contact & permis) avec barre de progression. Pas de upload obligatoire à ce stade.
- **Touch targets** : boutons ≥ 48×48 px, espacement entre liens du nav.

### 3.3 Desktop & tablette
- **Hero** : titre, sous-titre, étoiles, CTA — classique et efficace. Garder.
- **Galerie photos** : seulement 3 images visibles dans le HTML extrait, avec une image suspecte (`logo.jpg`). Une location de voilier se vend avec les images. **Action** : 15–25 photos pro (extérieur sous voiles, intérieur cabine, vue du cockpit, plage de sable, lever de soleil au port, scène repas à bord, paddle accroché à la poupe). Investis dans un shooting pro 1 journée (1 200–2 000 CHF) — c'est rentabilisé en 4 locations.
- **Vidéo** : 0 vidéo. Une vidéo de 30 sec en hero (loop muet) double souvent les conversions. Drone + GoPro embarquée + cockpit. Tu peux la faire toi-même.

### 3.4 Contenu manquant (à ajouter)
- **FAQ visible** (et balisée en JSON-LD `FAQPage` — double bénéfice SEO + conversion) :
  - Faut-il un permis ? (lien vers article dédié)
  - Annulation météo ? Combien de jours avant ?
  - Peut-on naviguer sans expérience ? (réponse : oui sur le lac avec permis, ou Skipper Pass + briefing renforcé)
  - Caution comment fonctionne-t-elle ?
  - Que se passe-t-il s'il n'y a pas de vent ?
  - Y a-t-il vraiment 6 couchages confortables ?
  - Toilettes chimiques : pour quel usage exactement ?
  - Quel est le tirant d'eau pour s'échouer sur les plages ?
- **Itinéraires types** : « Journée à La Sauge », « Weekend Yverdon → Cudrefin », « 3 jours Trois-Lacs (Neuchâtel-Morat-Bienne par les canaux) ».
- **Sécurité et confort** : matériel embarqué détaillé, gilets aux tailles dispo, gestion enfants, accessibilité.

### 3.5 Performance technique
À tester avec PageSpeed Insights et WebPageTest (les recommandations habituelles s'appliquent) :
- Images en WebP/AVIF, compressées, dimensionnées (pas d'image 4 000 px affichée en 800 px).
- `<img loading="lazy">` partout sauf hero.
- Google Maps en lazy iframe (charger sur clic sur poster image).
- Polices Google chargées en `font-display: swap`.
- Pas de JS bloquant.

### 3.6 Trust & conversion
Manques notables :
- **Pas de mention de l'assurance** sur la page d'accueil (alors que tu as une casco complète — c'est un argument fort, à mettre en hero ou dans le bandeau Infos).
- **Aucune mention de l'expérience pratique** : depuis combien d'années tu loues ce bateau ? Combien de locataires servis ?
- **Pas de badge ou logo de paiement** sécurisé (Stripe, Twint, etc.) — même symbolique, ça rassure.
- **Pas d'« annulation flexible »** mise en avant : ton CGL dit annulation 50 % si <7 jours. C'est en fait plus généreux que beaucoup d'AirBnB → en faire un argument commercial.

---

## 4. Audit concurrence

### 4.1 Concurrents directs sur le lac de Neuchâtel

| Acteur | Localisation | Offre | Force | Comment se différencier |
|---|---|---|---|---|
| **Alpha Voile** | Estavayer | Voilier + bateau moteur + permis | École reconnue, formation | Toi = location autonome, expérience plaisir, pas école |
| **Les Vikings SA** | Yvonand | Bateaux sans permis, planche, paddle, voile | Très grand public, plage | Toi = expérience premium, habitable, plusieurs jours |
| **Chantier Scholl** | Cheyres (!) | Location bateau, sorties teambuilding | Voisin direct, ancien | Toi = positionnement web et marque plus moderne |
| **Begni Boat** | Neuchâtel (Nid-du-Crô) | Quicksilver moteur | Bateau moteur, urbain | Toi = voile, sud du lac, plus authentique |
| **Marine Services Loisirs** | Neuchâtel | Pédalos, bateaux moteur | Touristique de masse | Toi = expérience exclusive |
| **« Découverte du lac à la voile »** (Hauterive, Maxi 77) | Hauterive | Sortie skipper Maxi 77 | Listé j3l.ch tourisme | Toi = sans skipper possible, multi-jours, habitable |

**Lecture stratégique** : tu es seul à proposer un voilier **habitable + nuitées + autonomie** sur le sud du lac (Cheyres). C'est ton océan bleu. Le Skipper Pass renforce cette position.

### 4.2 Concurrents indirects (plateformes)

| Plateforme | Inventaire CH | Modèle |
|---|---|---|
| **Click&Boat** | Ton bateau y est listé à 212 €/j | Commission 15–20 % |
| **SamBoat** | 4 bateaux Neuchâtel | Commission ~15 % |
| **Nautal** | Présent | Commission |
| **Océans Evasion** | Présent (Great Dane 28 à 42 €/j !) | Commission |

**Le sujet brûlant : alignement de prix.** Ton site direct affiche 275 CHF/jour. Click&Boat affiche 212 €/jour ≈ 200 CHF. Cas de figure et solutions :

- **Si tu factures vraiment 200 CHF en passant par Click&Boat** : Click&Boat prend sa commission par-dessus (donc le client paie ~240 CHF). Mais tu reçois 200 CHF. Sur ton site, tu touches les 275 CHF complets. → **Solution : abaisse ton tarif direct à 250 CHF/j**, qui te donne 250 CHF net vs 200 CHF via Click&Boat. Tu restes plus compétitif que via plateforme **et** tu gagnes plus.
- **Si Click&Boat affiche un prix client de 212 € (le client paie ça TTC)** : alors tu touches ~170–180 CHF après commission, et ton tarif direct à 275 CHF est complètement déconnecté. Cas catastrophique. → **Solution : monte le prix sur Click&Boat à 290 € minimum**, et **garde 275 CHF en direct**, en intégrant un argumentaire « réservez en direct, économisez ».

Action concrète : ajoute sur ton site, près du formulaire, un encart : *« Réservez en direct : -10 % vs plateformes, contact direct avec le skipper, pas de frais cachés. »*

### 4.3 Concurrents touristiques (substituts)
- LNM (bateaux de ligne et croisières) — pas vraiment un concurrent : eux = passifs, toi = actif.
- Restos / bars au bord du lac, plages, randonnée, vélo — concurrence du portefeuille loisir.
- Locations AirBnB lacustres — tu pourrais te positionner comme « AirBnB flottant ».

---

## 5. Positionnement & tarifs

### 5.1 Grille actuelle (rappel)

| Durée | Prix total | Prix/jour |
|---|---|---|
| 1 j | 275 CHF | 275 |
| 2 j | 490 CHF | 245 |
| 3 j | 720 CHF | 240 |
| 4 j | 840 CHF | 210 |
| 7 j | 1 260 CHF | 180 |
| Skipper Pass (5 sorties) | 800 CHF | 160 |

+ Nettoyage 60 CHF · Gennaker 15 CHF/j · Paddle 15 CHF/j · Caution 1 000 CHF

### 5.2 Analyse

**Forces de la grille**
- Dégressivité bien construite (-35 % du jour à la semaine).
- Skipper Pass à 160 CHF/j = excellent produit d'appel pour clients récurrents en semaine.
- Carburant inclus + nuitée port gratuite = différenciation forte (les concurrents font payer le carburant).

**Faiblesses**
- **Le prix 1 jour à 275 CHF** est élevé pour une journée sans expérience. Le client B2C lambda compare à « louer un Quicksilver 1 journée à 250 CHF chez Begni » et choisit le moteur car plus facile.
- **Pas de demi-journée** (4h) — gros manque pour le segment « apéro coucher de soleil » qui pourrait te rapporter 180 CHF en 4h × plusieurs créneaux/semaine.
- **Pas de tarif weekend (vendredi soir → dimanche soir)** différencié → tu loues comme un 3 jours à 720 CHF, alors qu'un forfait « weekend romantique » à 650 CHF avec bouteille de blanc Cheyres inclus serait plus vendeur.
- **Nettoyage obligatoire 60 CHF** présenté comme une corvée. À reformuler : « Pack accueil (nettoyage + préparation bateau prêt à embarquer) ».
- **Caution 1 000 CHF** : élevée pour le ticket d'entrée 275 CHF. Considère un produit d'assurance « rachat de caution » (~30 CHF/jour) qui réduit la friction et te rapporte une marge.

### 5.3 Grille recommandée (proposition)

| Produit | Durée | Prix | Logique |
|---|---|---|---|
| Apéro Sunset (avec skipper) | 17h-21h | 280 CHF/groupe (4 pers max) | Nouveau, high margin |
| Demi-journée | 9h-13h ou 14h-18h | 195 CHF | Capter clients hésitants |
| Journée | 9h-18h | 275 CHF | Inchangé |
| Weekend Romance | Ven 17h → Dim 18h | 650 CHF (au lieu de 720) + bouteille incluse | Forfait packagé |
| Semaine | 7 j | 1 260 CHF | Inchangé |
| Skipper Pass | 5 sorties / an | 800 CHF | Inchangé, c'est ta pépite |
| **NOUVEAU** Pass annuel illimité | Saison mai-oct, semaine | 2 800 CHF | Pour passionnés sans bateau |

Le « Pass annuel illimité » est inspiré du *Liberty Pass* de Loca-Boat sur le Léman et peut te rapporter 3–5 abonnements/an = 8 000 à 14 000 CHF de revenu garanti, et fidélise des évangélistes pour ta marque.

---

## 6. Plan d'action priorisé

### Sprint 1 — Cette semaine (gains rapides, 0–5 h de travail)
1. ✅ Vérifier et **uniformiser les tarifs** entre site, Click&Boat, SamBoat (voir § 4.2). Décision stratégique : continuer multi-canal ou passer 100 % direct.
2. ✅ Ajouter un encart « Réservez en direct, économisez 10 % » près du CTA.
3. ✅ Demander 5 avis Google supplémentaires à tes derniers locataires (objectif : passer de 28 à 35 avis cette saison).
4. ✅ Revendiquer / optimiser la fiche **Google Business Profile** (photos, horaires, FAQ).
5. ✅ Retirer la déclaration `og:locale:alternate de_CH` si la version DE n'existe pas (ou la créer — voir Sprint 3).

### Sprint 2 — 2 prochaines semaines (5–15 h)
6. ✅ **JSON-LD** : LocalBusiness + Product + AggregateRating + FAQPage (gain SEO majeur, fait une fois pour toutes).
7. ✅ **FAQ visible** sur la page (8–10 questions) — bénéfice double : moins d'emails de Q&R, plus de SEO.
8. ✅ **Photos pro** : briefer un photographe pour 1 shooting (jour de beau temps avec voile, plus jour avec cabine intérieure éclairée, plus drone).
9. ✅ Optimiser les images existantes (WebP, alt text descriptifs, dimensions correctes).
10. ✅ Sitemap.xml et robots.txt vérifiés et soumis à Search Console.

### Sprint 3 — Le mois prochain (15–40 h)
11. ✅ Créer 4 pages SEO : `/skipper-pass`, `/itineraires`, `/voilier-maxus-21`, `/permis-bateau-suisse`.
12. ✅ Version **allemande** du site (priorité 1 sur l'anglais — la Suisse alémanique est ton plus gros marché potentiel non exploité).
13. ✅ Ajouter une vidéo hero (30–60 sec, drone + cockpit + intérieur).
14. ✅ Repenser le formulaire de réservation en 3 étapes mobile-first.
15. ✅ Newsletter / capture email (lead magnet : « Guide PDF des 10 plus beaux mouillages du lac de Neuchâtel »).

### Sprint 4 — Avant la haute saison 2026 (40 h+)
16. ✅ Lancer un blog avec 6–8 articles de fond (mouillages, météo joran, permis, recettes à bord, weekend Trois-Lacs).
17. ✅ Tester le produit « Apéro Sunset » sur 4–6 dates pilotes mai–juin.
18. ✅ Lancer le « Pass annuel illimité » comme produit phare 2026.
19. ✅ Mettre en place un email post-location automatisé (demande d'avis + parrainage 50 CHF crédité).
20. ✅ Partenariats : Estavayer Tourisme, j3l.ch, 2 B&B de Cheyres/Châbles (commission croisée).

---

## 7. Évolutions business : où amener le projet

Je classe par ordre de réalisme/effort/revenu attendu pour un opérateur solo avec 1 bateau.

### Niveau 1 — Optimiser l'existant (0–6 mois, +30 à +50 % de CA, faible risque)

**1.1 Apéro Sunset avec skipper (toi à bord)**
- Format : 17h–21h, 4 personnes max, prosecco/bières/petit plateau apéro inclus.
- Prix : 280 CHF/sortie (70 CHF/pers).
- Marge : ~220 CHF nette/sortie après consommables et carburant.
- Demande : très forte, demande latente énorme sur le sud du lac. Une partie du trafic Booking/Airbnb cherche des activités du soir.
- Distribution : ton site + GetYourGuide + Airbnb Experiences (très puissant pour ce format) + offices du tourisme.
- Calcul : 30 sorties sur mai–septembre = 8 400 CHF supplémentaires.

**1.2 Demande en mariage / anniversaire / cadeau d'entreprise**
- Format : sortie privative + déco + bouteille + photographe partenaire (option).
- Prix : 450–750 CHF selon options.
- Très haute marge, marketing via Pinterest + Instagram + partenaires (wedding planners, fleuristes).

**1.3 Bons cadeaux**
- Stripe ou plateforme type Tipsi.ch / Smartbox CH.
- Marge bonus : 15–20 % des bons ne sont jamais utilisés.

**1.4 Pass annuel illimité (voir § 5.3)**
- 2 800 CHF/an, semaine uniquement, mai–oct.
- Objectif : 3 à 5 abonnés Année 1.

### Niveau 2 — Diversifier la prestation (6–18 mois, doubler le CA, risque modéré)

**2.1 Skipper-on-demand sur les bateaux des autres**
- Tu es skipper 20+ ans. Beaucoup de propriétaires de voiliers sur le lac n'osent pas naviguer ou veulent un accompagnement pour une journée.
- Tarif : 250–350 CHF/journée comme skipper indépendant.
- Aucun investissement, valorise ta compétence, lisse les revenus.
- Marché : retraités propriétaires de bateaux qui ont peur, familles inexpérimentées qui louent ailleurs, événements d'entreprise sur grands bateaux.

**2.2 Teambuilding entreprises**
- Format : journée pour 4–8 personnes (split sur le voilier + bateau partenaire moteur), avec briefing voile, mini-régate, repas livré à bord ou au port.
- Prix : 1 500–3 000 CHF/journée pour un groupe.
- Très haute marge, ticket moyen élevé.
- Distribution : LinkedIn, agence MICE Romande, partenariats hôtels d'affaires Yverdon/Neuchâtel.
- Plafond raisonnable : 10–15 journées/an = 25 000–40 000 CHF.

**2.3 Gestion-conciergerie pour propriétaires**
- Tu gères le bateau d'un propriétaire absent (entretien, hivernage, mise à l'eau, sorties pour le rouler), il te laisse louer X jours/an pour amortir.
- Marge : commission gestion (~3 000–6 000 CHF/an par bateau) + revenus locations.
- Modèle scalable : 3–5 bateaux gérés = vrai business.

**2.4 Stages d'initiation / perfectionnement (sans concurrencer frontalement Alpha Voile)**
- Niche : « stage de remise en confiance après le permis ». Cible : gens qui ont leur permis depuis longtemps mais n'osent plus naviguer.
- Format : 2 demi-journées personnalisées.
- Prix : 450 CHF.
- C'est ce que ton Skipper Pass cible déjà — pousser plus loin.

### Niveau 3 — Devenir une flotte (18 mois +, x3–5 le CA, investissement)

**3.1 Acheter un 2e voilier (occasion, type Beneteau First 27, Dehler 25, Maxus 26)**
- Investissement : 25 000–60 000 CHF d'occasion.
- Place de port à Cheyres ou Estavayer : ~2 000–3 500 CHF/an.
- ROI : si tu atteins ~50 % d'occupation comme sur le bateau actuel, retour en 3–5 ans.
- Réduit le risque de saisonnalité et permet les départs simultanés (couples d'amis).

**3.2 Devenir base nautique « Sailing Club Cheyres »**
- 3 bateaux + 1 skipper salarié saisonnier + offre type « club » à 3 500 CHF/an = 30 jours de bateau.
- Modèle : ~30 membres × 3 500 CHF = 105 000 CHF/an récurrents + locations à la journée du « surplus ».
- Comparable inspirant : *Loca-Boat* sur le Léman avec son « Liberty Pass ».

**3.3 Charter sur d'autres lacs**
- Étendre à Léman ou Lac de Bienne via un autre bateau.
- Plus risqué (concurrence Léman très forte).

### Niveau 4 — Vertical adjacents (long terme, optionnel)

- **Vente de produits dérivés** : casquettes/t-shirts marque « Voilier Lac de Neuchâtel », faible CA mais haute marge et marketing gratuit.
- **Cours d'initiation au permis voile suisse** : nécessite agrément moniteur fédéral. Marché stable mais saturé sur le lac.
- **Plateforme** : créer ton propre annuaire « location bateaux Lac de Neuchâtel » et capter les recherches en collectant un % sur les autres acteurs. Très ambitieux.
- **Bed & Sail** : combiner location voilier + nuitée en B&B partenaire (cross-selling).

### Évolution recommandée (synthèse)

> **Année 2026** : maximise l'existant. Apéro Sunset, Pass annuel, version DE, SEO. Objectif : +40 % CA.
>
> **Année 2027** : ajoute le service skipper sur d'autres bateaux + 5–10 teambuildings. Cherche un 2e bateau d'occasion à la fin de saison.
>
> **Année 2028** : 2 bateaux, transition vers le modèle « club » avec abonnement annuel.
>
> **Horizon 2030** : flotte de 3 bateaux, base nautique du sud-ouest du lac, 1 employé saisonnier.

---

## 8. Indicateurs à suivre

Mets en place dès maintenant un suivi mensuel de :
- Trafic Google Analytics (sessions, source, taux de rebond mobile vs desktop).
- Positions Search Console sur les requêtes prioritaires (§ 2.3).
- Taux de conversion formulaire (visites / demandes envoyées).
- CA par canal : direct vs Click&Boat vs SamBoat (pour décider si tu sors d'une plateforme).
- Note moyenne et nombre d'avis Google.
- Taux d'occupation hebdo (objectif sain : 60 % mai–sept).
- NPS post-location (« recommanderiez-vous ? »).

---

## 9. Trois choses à ne pas faire

1. **Ne pas baisser tes prix en panique.** Tu es positionné premium-accessible, c'est cohérent avec une expérience. Si les réservations sont basses, c'est un problème de visibilité, pas de prix.
2. **Ne pas tenter de concurrencer Alpha Voile sur la formation permis.** Eux ont 15 ans d'avance, agrément officiel et flotte. Reste sur le créneau « plaisir et liberté », pas « formation ».
3. **Ne pas multiplier les plateformes (Samboat, Nautal, Click&Boat, Filovent, Océans Evasion).** Chaque plateforme = -15/-20 % de marge + cannibalisation du direct. Choisis-en **une** (la plus performante) comme canal d'acquisition, et investis le reste dans le SEO de ton site.

---

*Audit réalisé en mai 2026. Les volumes de recherche sont estimés à partir de signaux observables ; pour des chiffres précis, brancher Search Console + Ahrefs/SEMrush ou demander un audit SEO ponctuel à un freelance romand (compter 500–1 500 CHF).*
