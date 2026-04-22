import os

def translate_file(filepath, mapping):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for fr, target in mapping.items():
        content = content.replace(fr, target)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# EN MAPPING
en_map = {
    'lang="fr"': 'lang="en"',
    'Location Voilier Lac de Neuchâtel — Cheyres, Suisse | Maxus 21': 'Sailboat Rental Lake Neuchâtel — Cheyres, Switzerland | Maxus 21',
    'Louez un voilier habitable Maxus 21 sur le lac de Neuchâtel au départ du port de Cheyres, Suisse. Carburant inclus, nuitées gratuites au port. Réservez en ligne dès 280 CHF.': 'Rent a liveaboard sailboat Maxus 21 on Lake Neuchâtel departing from Cheyres harbour, Switzerland. Fuel included, free nights at the harbour. Book online from 280 CHF.',
    'Location Voilier Lac de Neuchâtel — Cheyres, Suisse': 'Sailboat Rental Lake Neuchâtel — Cheyres, Switzerland',
    'Louez un voilier habitable Maxus 21 sur le lac de Neuchâtel. Carburant inclus, nuitées gratuites. Dès 280 CHF.': 'Rent a liveaboard sailboat Maxus 21 on Lake Neuchâtel. Fuel included, free nights. From 280 CHF.',
    'Le voilier': 'The sailboat',
    'Location de voilier': 'Sailboat rental',
    'Port de Cheyres · Lac de Neuchâtel · Suisse': 'Cheyres Harbour · Lake Neuchâtel · Switzerland',
    'Votre voilier sur le <em>lac de Neuchâtel</em>': 'Your sailboat on <em>Lake Neuchâtel</em>',
    'Partez à l’aventure sur les eaux turquoises du lac de Neuchâtel, ses bancs de sable et sa réserve naturelle préservée.': 'Set sail on the turquoise waters of Lake Neuchâtel, its sandbanks and its pristine nature reserve.',
    '4.9 · 5 avis vérifiés': '4.9 · 5 verified reviews',
    'Propriétaire vérifié': 'Verified owner',
    'Réserver maintenant': 'Book now',
    'Découvrir le bateau': 'Discover the boat',
    'Longueur': 'Length',
    'Personnes max': 'Max persons',
    'Lits doubles': 'Double berths',
    'Note · 5 avis': 'Rating · 5 reviews',
    'Nuitées port Cheyres': 'Nights at Cheyres harbour',
    'Le Maxus 21 est un voilier habitable': 'The Maxus 21 is a liveaboard sailboat',
    'Tarifs & Forfaits': 'Rates & Packages',
    'Des prix simples et transparents': 'Simple and transparent prices',
    'Tous les prix en CHF · Carburant inclus · Assurance comprise': 'All prices in CHF · Fuel included · Insurance included',
    'Journée': 'Full Day',
    'Idéal pour une escapade': 'Ideal for a day escape',
    '2 Jours (1 nuit)': 'Two Days (1 night)',
    'Vivez l\'expérience à bord': 'Experience the life aboard',
    'Semaine': 'Week',
    'Total liberté': 'Total freedom',
    'Les options disponibles': 'Optional Extras',
    'Pass Skipper': 'Skipper Pass',
    'Pas de permis ? Pas de soucis': 'No license? No problem',
    'Le <em>Pass Skipper</em>': 'The <em>Skipper Pass</em>',
    'Sorties découverte 2h - 4h': '2h - 4h Discoveries',
    'Cours de voile possible': 'Sailing lessons available',
    'Sessions partagées ou privées': 'Shared or private sessions',
    'Se renseigner sur le Pass': 'Enquire about Skipper Pass',
    'Populaire': 'Popular',
    'Réservez & <em>payez en ligne</em>': 'Reserve & <em>pay online</em>',
    'Carburant inclus · Nuitées au port de Cheyres gratuites': 'Fuel included · Free nights at Cheyres harbour',
    'Demande de réservation': 'Booking enquiry',
    'Caution par empreinte bancaire': 'Security deposit via credit card',
    'Date de départ': 'Departure Date',
    'Date de retour': 'Return Date',
    'Choisir la date de départ': 'Choose departure date',
    'Choisir la date de retour': 'Choose return date',
    'Prénom & Nom': 'First & Last Name',
    'Type de réservation': 'Booking Type',
    'Location standard': 'Standard Rental',
    'Options (extras)': 'Optional Extras',
    'Estimation totale': 'Total estimate',
    'Envoyer ma demande': 'Send Enquiry',
    'No payment now': 'No payment now',
    'Le bateau': 'The Boat',
    'Tarifs': 'Rates',
    'Infos': 'Info',
    'Avis': 'Reviews',
    'Carte': 'Map',
    'À propos': 'About',
    'Réserver': 'Book Now',
    'AU PORT DE CHEYRES': 'AT CHEYRES HARBOUR',
    'Informations pratiques': 'Practical Information',
    'Accès & Localisation': 'Access & Location',
    'Contact & Réservation': 'Contact & Booking'
}

# DE MAPPING (Basic translations)
de_map = {
    'lang="fr"': 'lang="de"',
    'Location Voilier Lac de Neuchâtel': 'Segelbootvermietung Neuenburgersee',
    'Louez un voilier habitable': 'Mieten Sie ein bewohnbares Segelboot',
    'Votre voilier sur le': 'Ihr Segelboot auf dem',
    'Tarifs & Forfaits': 'Preise & Pakete',
    'Réserver maintenant': 'Jetzt buchen',
    'Le bateau': 'Das Boot',
    'Tarifs': 'Preise',
    'Infos': 'Infos',
    'Avis': 'Bewertungen',
    'Carte': 'Karte',
    'À propos': 'Über uns',
    'Réserver': 'Buchen',
    'Journée': 'Tag',
    'Semaine': 'Woche',
}

translate_file('/home/gregory/Voilier/site/en/index.html', en_map)
translate_file('/home/gregory/Voilier/site/de/index.html', de_map)

print("Translation completed successfully.")
