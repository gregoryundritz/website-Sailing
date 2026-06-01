import os
import re

def t(fr, de, text):
    # Replace normal spaces and newlines with a flexible whitespace regex
    # We split by whitespace and join with \s+
    parts = fr.split()
    fr_regex = r'\s+'.join([re.escape(p) for p in parts])
    # Add a little buffer for HTML tags maybe? No, let's keep it to text.
    return re.sub(fr_regex, de, text, flags=re.IGNORECASE)

def translate_files():
    files = ['de/index.html', 'de/preise.html', 'de/toerns.html', 'de/galerie.html', 'de/bewertungen.html', 'de/kontakt.html']
    
    replacements = {
        # Strip
        "Länge": "Länge", # already translated
        "Largeur": "Breite",
        "Capacité": "Kapazität",
        "Couchages": "Schlafplätze",
        "Cabine": "Kabine",
        "Toilettes": "Toiletten",
        "Port": "Hafen",
        "Cheyres, Neuchâtel": "Cheyres, Neuenburg",
        "Oui (chimique)": "Ja (Chemie)",
        
        # Bateau paragraph
        "Le voilier": "Das Segelboot",
        "Le Maxus 21 est un voilier habitable de 6.5 m, conçu par l'architecte naval Jacek Daszkiewicz et produit par le chantier polonais Northman. Gréé en sloop fractionné avec génois sur enrouleur, grand-voile lattée avec lazy-jack et gennaker, il offre un excellent compromis entre performance et facilité de manœuvre. Sa quille relevable (tirant d'eau de 0.35 à 1.45 m) permet d'accéder aux zones peu profondes et aux plages du Neuenburgersee. Le cockpit spacieux accueille confortablement 6 personnes, et la cabine équipée — frigo 12V, réchaud gaz, vaisselle, 2 lits doubles — permet de séjourner plusieurs nuits à bord en autonomie complète.": "Die Maxus 21 ist ein 6,5 m langes bewohnbares Segelboot, entworfen vom Schiffsarchitekten Jacek Daszkiewicz und produziert von der polnischen Werft Northman. Als fraktioniertes Sloop getakelt mit Rollgenua, durchgelattetem Großsegel mit Lazy-Jack und Gennaker bietet sie einen hervorragenden Kompromiss zwischen Leistung und einfacher Handhabung. Der Hubkiel (Tiefgang von 0,35 bis 1,45 m) ermöglicht den Zugang zu flachen Zonen und den Stränden des Neuenburgersees. Das geräumige Cockpit bietet bequem Platz für 6 Personen, und die ausgestattete Kabine — 12V-Kühlschrank, Gaskocher, Geschirr, 2 Doppelbetten — ermöglicht mehrtägige Aufenthalte an Bord in völliger Autonomie.",
        
        # Tags
        "Matériel sécurité": "Sicherheitsausrüstung",
        "Carburant inclus": "Treibstoff inklusive",
        "Foc sur enrouleur": "Rollfock",
        
        # Infos
        "Prise en main": "Einweisung",
        "Briefing inclus avant chaque départ.": "Briefing vor jeder Abfahrt inbegriffen.",
        "Permis requis": "Führerschein erforderlich",
        "Le permis lac Schweiz ou international reconnu est obligatoire.": "Der Schweizer Binnensegelschein (oder international anerkannt) ist obligatorisch.",
        "Le permis lac suisse ou international reconnu est obligatoire.": "Der Schweizer Binnensegelschein (oder international anerkannt) ist obligatorisch.",
        "Accès": "Anfahrt",
        "Port de Cheyres. Parking payant sur place. Gare de Cheyres-Châbles.": "Hafen von Cheyres. Kostenpflichtige Parkplätze vor Ort. Bahnhof Cheyres-Châbles.",
        "Météo & annulation": "Wetter & Stornierung",
        "Possibilité de report en cas de conditions dangereuses.": "Verschiebung bei gefährlichen Wetterbedingungen möglich.",
        "Nuitées gratuites. Restaurant, douches et plage à proximité.": "Kostenlose Übernachtungen. Restaurant, Duschen und Strand in der Nähe.",
        "Départs dès 9h et retours à 18h.": "Abfahrt ab 9 Uhr und Rückkehr bis 18 Uhr.",
        
        # Apropos
        "Votre hôte": "Ihr Gastgeber",
        "Gregory, navigateur passionné": "Gregory, leidenschaftlicher Segler",
        "Skipper depuis plus de vingt ans, j'ai navigué sur les lacs suisses comme en mer. La voile n'est pas seulement un loisir pour moi — c'est une façon d'appréhender le monde différemment, de lire le vent, de trouver son cap.": "Als Skipper mit über zwanzig Jahren Erfahrung bin ich sowohl auf Schweizer Seen als auch auf dem Meer gesegelt. Segeln ist für mich nicht nur ein Hobby — es ist eine Art, die Welt anders wahrzunehmen, den Wind zu lesen und seinen Kurs zu finden.",
        "En proposant la location de ce voilier, j'ai envie de partager cet accès au lac et à la voile avec ceux qui n'ont pas encore leur propre bateau. Que vous soyez débutant curieux ou skipper confirmé cherchant un plan d'eau exceptionnel, le Neuenburgersee a tout pour vous surprendre.": "Mit der Vermietung dieses Segelbootes möchte ich den Zugang zum See und zum Segeln mit denen teilen, die noch kein eigenes Boot haben. Ob Sie ein neugieriger Anfänger oder ein erfahrener Skipper sind, der ein außergewöhnliches Gewässer sucht, der Neuenburgersee wird Sie überraschen.",
        "20+ ans de navigation": "20+ Jahre Segelerfahrung",
        "Plans d'eau": "Reviere",
        "Lacs suisses & mer": "Schweizer Seen & Meer",
        "locataires": "Gäste",
        
        # Footer
        "© 2026 · Neuenburgersee Voilier · Alle Rechte vorbehalten": "© 2026 · Segelboot Neuenburgersee · Alle Rechte vorbehalten",
        
        # Other loose texts (tarifs)
        "100 CHF de remise sur la 2ème semaine": "100 CHF Rabatt auf die 2. Woche",
        "Obligatoire, réglé au port": "Obligatorisch, am Hafen zu zahlen",
        "Sur demande": "Auf Anfrage",
        "Caution": "Kaution",
        "Franchise assurance": "Versicherungsselbstbehalt",
        
        # Itineraires
        "Départ et Retour": "Abfahrt und Rückkehr",
        "Points forts": "Highlights",
        "Réserve de la Grande Cariçaie": "Naturschutzgebiet Grande Cariçaie",
        "Château d'Estavayer": "Schloss Estavayer",
        "Baignade au large": "Baden im offenen See",
        "Vignobles de Gorgier": "Weinberge von Gorgier",
        "Ville de Neuchâtel": "Stadt Neuenburg",
        "Château de Grandson": "Schloss Grandson",
        
        # Form / Contact
        "Sélectionnez une date": "Wählen Sie ein Datum",
        "Un petit mot ? (optionnel)": "Eine kurze Nachricht? (optional)",
        "Envoyer la demande": "Anfrage senden",
        
        # Mobile app bar
        "Buchen": "Buchen",
        "WhatsApp": "WhatsApp",
        
        # Navigation
        "Contact": "Kontakt"
    }

    for filename in files:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for fr, de in replacements.items():
                content = t(fr, de, content)
                
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Processed {filename}")

if __name__ == "__main__":
    translate_files()
