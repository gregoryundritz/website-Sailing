import os
import glob
import re

def t(content, fr, en):
    # flexible whitespace replacement
    parts = fr.split()
    fr_regex = r'\s+'.join([re.escape(p) for p in parts])
    return re.sub(fr_regex, en, content, flags=re.IGNORECASE)

def translate_files():
    en_dir = "/home/gregory/Voilier/site/en"
    files = glob.glob(os.path.join(en_dir, "*.html"))
    
    replacements = {
        # Nav & Footer
        """Le bateau""": """The boat""",
        """Emplacement""": """Location""",
        """Tarifs""": """Prices""",
        """Infos""": """Info""",
        """Avis""": """Reviews""",
        """Galerie""": """Gallery""",
        """Itinéraires""": """Itineraries""",
        """Permis Bateau""": """Sailing License""",
        """À propos""": """About""",
        """Contact & Réservation""": """Contact & Booking""",
        """Contact""": """Contact""",
        """Réserver""": """Book""",
        """Conditions Générales""": """Terms and Conditions""",
        """Mentions Légales""": """Legal Notice""",
        """Voilier · <span>Lac de Neuchâtel</span>""": """Sailboat · <span>Lake Neuchâtel</span>""",
        """Lac de Neuchâtel · Port de Cheyres, Suisse""": """Lake Neuchâtel · Cheyres Harbour, Switzerland""",
        """© 2026 · Lac de Neuchâtel Voilier · Tous droits réservés""": """© 2026 · Lake Neuchâtel Sailboat · All rights reserved""",
        """Vers la galerie photos""": """To the photo gallery""",
        
        # Index tags
        """Location de voilier en Suisse : Découvrez le <em>lac de Neuchâtel</em>""": """Sailboat Rental Switzerland: Discover <em>Lake Neuchâtel</em>""",
        """Location de voilier en Suisse : Pourquoi choisir le lac de Neuchâtel ?""": """Sailboat rental in Switzerland: Why choose Lake Neuchâtel?""",
        """Si vous cherchez une <strong>location de voilier en Suisse</strong>, le lac de Neuchâtel offre l'une des meilleures expériences nautiques du pays. Plus sauvage et moins fréquenté que le lac Léman ou le lac de Constance, c'est le plus grand lac entièrement suisse. Avec ses vents thermiques réguliers (la fameuse Joran), ses plages de sable fin, et la magnifique réserve naturelle de la Grande Cariçaie, naviguer à bord d'un voilier habitable comme le Maxus 21 est l'assurance d'une escapade inoubliable au cœur de la Suisse.""": """If you are looking for a <strong>sailboat rental in Switzerland</strong>, Lake Neuchâtel offers one of the best nautical experiences in the country. Wilder and less crowded than Lake Geneva or Lake Constance, it is the largest entirely Swiss lake. With its regular thermal winds (the famous Joran), its fine sandy beaches, and the magnificent Grande Cariçaie nature reserve, sailing aboard a cabin cruiser like the Maxus 21 guarantees an unforgettable getaway in the heart of Switzerland.""",
        """Foire Aux Questions (FAQ)""": """Frequently Asked Questions (FAQ)""",
        """Quel est le meilleur lac pour louer un voilier en Suisse ?""": """Which is the best lake to rent a sailboat in Switzerland?""",
        """Bien que le lac Léman soit le plus connu, le lac de Neuchâtel est souvent considéré comme le plus préservé et le plus agréable pour la voile de plaisance. Ses eaux claires, ses vents constants et son environnement naturel intact en font un choix privilégié pour la location de bateau en Suisse.""": """Although Lake Geneva is the most famous, Lake Neuchâtel is often considered the most preserved and pleasant for leisure sailing. Its clear waters, constant winds, and intact natural environment make it a top choice for boat rental in Switzerland.""",
        """Faut-il un permis pour louer un voilier en Suisse ?""": """Do I need a license to rent a sailboat in Switzerland?""",
        """Oui, pour louer un voilier habitable comme notre Maxus 21, le permis voile (catégorie D) est obligatoire en Suisse (dès 15m² de surface de voile). Les permis étrangers (ICC) sont généralement reconnus pour les touristes. <a href="sailing-license-switzerland.html" style="color: var(--teal); text-decoration: underline;">En savoir plus sur le permis bateau en Suisse</a>.""": """Yes, to rent a cabin sailboat like our Maxus 21, the sailing license (category D) is mandatory in Switzerland (for sails over 15m²). Foreign licenses (ICC) are generally recognized for tourists. <a href="sailing-license-switzerland.html" style="color: var(--teal); text-decoration: underline;">Learn more about the sailing license in Switzerland</a>.""",
        """Combien coûte la location d'un voilier en Suisse ?""": """How much does it cost to rent a sailboat in Switzerland?""",
        """Les prix varient selon la saison et le type de bateau. Sur notre voilier Maxus 21, les tarifs débutent à 275 CHF la journée, offrant l'un des meilleurs rapports qualité-prix pour la location de voilier sur le lac de Neuchâtel. <a href="prices.html" style="color: var(--teal); text-decoration: underline;">Consulter tous nos tarifs</a>.""": """Prices vary depending on the season and the type of boat. On our Maxus 21 sailboat, rates start at 275 CHF per day, offering one of the best value for money for sailboat rentals on Lake Neuchâtel. <a href="prices.html" style="color: var(--teal); text-decoration: underline;">View all our prices</a>.""",
        
        """Location de voilier""": """Sailboat rental""",
        """Port de Cheyres · Lac de Neuchâtel · Suisse""": """Cheyres Harbour · Lake Neuchâtel · Switzerland""",
        """Partez à l'aventure sur les eaux turquoises du lac de Neuchâtel, ses bancs de sable et sa réserve naturelle préservée.""": """Set sail on the turquoise waters of Lake Neuchâtel, exploring its sandy beaches and pristine nature reserve.""",
        """28 avis vérifiés""": """28 verified reviews""",
        """Voir les tarifs""": """View prices""",
        
        # Info block
        """Longueur""": """Length""",
        """Largeur""": """Beam""",
        """Capacité""": """Capacity""",
        """Couchages""": """Berths""",
        """Cabine""": """Cabin""",
        """Toilettes""": """Toilet""",
        """Port""": """Harbour""",
        """Oui (chimique)""": """Yes (chemical)""",
        
        """Le voilier""": """The sailboat""",
        """Le Maxus 21 est un voilier habitable de 6.5 m, conçu par l'architecte naval Jacek Daszkiewicz et produit par le chantier polonais Northman. Gréé en sloop fractionné avec génois sur enrouleur, grand-voile lattée avec lazy-jack et gennaker, il offre un excellent compromis entre performance et facilité de manœuvre. Sa quille relevable (tirant d'eau de 0.35 à 1.45 m) permet d'accéder aux zones peu profondes et aux plages du lac de Neuchâtel. Le cockpit spacieux accueille confortablement 6 personnes, et la cabine équipée — frigo 12V, réchaud gaz, vaisselle, 2 lits doubles — permet de séjourner plusieurs nuits à bord en autonomie complète.""": """The Maxus 21 is a 6.5m cabin cruiser, designed by naval architect Jacek Daszkiewicz and produced by the Polish shipyard Northman. Fractionally rigged sloop with furling genoa, battened mainsail with lazy-jack, and gennaker, it offers an excellent compromise between performance and ease of handling. Its lifting keel (draft from 0.35 to 1.45 m) allows access to shallow areas and the beaches of Lake Neuchâtel. The spacious cockpit comfortably accommodates 6 people, and the equipped cabin — 12V fridge, gas stove, dishes, 2 double beds — allows for stays of several nights on board in complete autonomy.""",
        
        """Matériel sécurité""": """Safety equipment""",
        """Carburant inclus""": """Fuel included""",
        """Foc sur enrouleur""": """Furling jib""",
        
        """Prise en main""": """Handover""",
        """Briefing inclus avant chaque départ.""": """Briefing included before every departure.""",
        """Permis requis""": """License required""",
        """Le permis lac suisse ou international reconnu est obligatoire.""": """Swiss inland sailing license (or recognized international) is mandatory.""",
        """Accès""": """Access""",
        """Port de Cheyres. Parking payant sur place. Gare de Cheyres-Châbles.""": """Cheyres Harbour. Paid parking on site. Cheyres-Châbles train station.""",
        """Météo & annulation""": """Weather & Cancellation""",
        """Possibilité de report en cas de conditions dangereuses.""": """Postponement possible in case of dangerous conditions.""",
        """Nuitées gratuites. Restaurant, douches et plage à proximité.""": """Free overnight stays. Restaurant, showers and beach nearby.""",
        """Départs dès 9h et retours à 18h.""": """Departures from 9 am and returns by 6 pm.""",
        
        """Votre hôte""": """Your host""",
        """Gregory, navigateur passionné""": """Gregory, passionate sailor""",
        """Skipper depuis plus de vingt ans, j'ai navigué sur les lacs suisses comme en mer. La voile n'est pas seulement un loisir pour moi — c'est une façon d'appréhender le monde différemment, de lire le vent, de trouver son cap.""": """Skipper for over twenty years, I have sailed on Swiss lakes as well as at sea. Sailing is not just a hobby for me — it's a way to understand the world differently, to read the wind, to find your course.""",
        """En proposant la location de ce voilier, j'ai envie de partager cet accès au lac et à la voile avec ceux qui n'ont pas encore leur propre bateau. Que vous soyez débutant curieux ou skipper confirmé cherchant un plan d'eau exceptionnel, le lac de Neuchâtel a tout pour vous surprendre.""": """By offering this sailboat for rent, I want to share this access to the lake and sailing with those who do not yet have their own boat. Whether you are a curious beginner or an experienced skipper looking for an exceptional body of water, Lake Neuchâtel has everything to surprise you.""",
        """20+ ans de navigation""": """20+ years of sailing""",
        """Plans d'eau""": """Waters""",
        """Lacs suisses & mer""": """Swiss lakes & sea""",
        """locataires""": """renters""",
        
        # Prices
        """100 CHF de remise sur la 2ème semaine""": """100 CHF discount on the 2nd week""",
        """Obligatoire, réglé au port""": """Mandatory, paid at the harbour""",
        """Sur demande""": """On request""",
        """Caution""": """Deposit""",
        """Franchise assurance""": """Insurance deductible""",
        
        """Sélectionnez une date""": """Select a date""",
        """Un petit mot ? (optionnel)""": """A quick message? (optional)""",
        """Envoyer la demande""": """Send request""",
        """WhatsApp""": """WhatsApp""",
    }

    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for fr, en in replacements.items():
            content = t(content, fr, en)
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print("EN translation basic pass done.")

if __name__ == "__main__":
    translate_files()
