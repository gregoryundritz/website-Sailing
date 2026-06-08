import os
import glob
import re

def t(content, fr, en):
    parts = fr.split()
    fr_regex = r'\s+'.join([re.escape(p) for p in parts])
    return re.sub(fr_regex, en, content, flags=re.IGNORECASE)

def translate_files():
    en_dir = "/home/gregory/Voilier/site/en"
    files = glob.glob(os.path.join(en_dir, "*.html"))
    
    replacements = {
        # Prices (tarifs)
        """Tarifs Location Voilier Neuchâtel""": """Sailboat Rental Prices Neuchâtel""",
        """Location de voilier sur le lac de Neuchâtel. Découvrez nos tarifs de location pour une journée, un week-end ou une semaine. Options avec ou sans skipper.""": """Sailboat rental on Lake Neuchâtel. Discover our rental prices for a day, a weekend or a week. Options with or without skipper.""",
        """Tarifs de location""": """Rental prices""",
        """Des tarifs transparents et dégressifs. Carburant et nuitées au port d'attache inclus.""": """Transparent and decreasing prices. Fuel and overnight stays at the home port included.""",
        """Basse Saison""": """Low Season""",
        """Avril, Mai, Septembre, Octobre""": """April, May, September, October""",
        """Haute Saison""": """High Season""",
        """Juin, Juillet, Août""": """June, July, August""",
        """1 jour""": """1 day""",
        """2 jours""": """2 days""",
        """3 jours""": """3 days""",
        """1 semaine""": """1 week""",
        """Dès CHF""": """From CHF""",
        """100 CHF de remise sur la 2ème semaine""": """100 CHF discount on the 2nd week""",
        """Le tarif inclut :""": """The price includes:""",
        """Voilier préparé et prêt à naviguer""": """Sailboat prepared and ready to sail""",
        """Carburant (moteur hors-bord 5cv)""": """Fuel (5hp outboard engine)""",
        """Nuitées gratuites au port de Cheyres""": """Free overnight stays at Cheyres harbour""",
        """Briefing de départ complet""": """Comprehensive departure briefing""",
        """Ce qui n'est pas inclus :""": """What is not included:""",
        """Taxes visiteurs pour nuitées hors de Cheyres""": """Visitor taxes for overnight stays outside Cheyres""",
        """Assurance annulation""": """Cancellation insurance""",
        """Frais de nettoyage final (optionnel)""": """Final cleaning fee (optional)""",
        """Nouveau: Skipper Pass""": """New: Skipper Pass""",
        """Le forfait illimité pour les passionnés""": """The unlimited package for enthusiasts""",
        """Un forfait saison unique de 800 CHF vous permettant de naviguer de manière illimitée toute la saison, incluant l'assurance Plus.""": """A unique seasonal package of 800 CHF allowing you to sail unlimitedly throughout the season, including Plus insurance.""",
        """Forfait illimité toute la saison""": """Unlimited package all season""",
        """Assurance "Plus" incluse""": """'Plus' insurance included""",
        """Réservation simplifiée (dernière minute possible)""": """Simplified booking (last minute possible)""",
        """Limité à 5 membres maximum""": """Limited to 5 members maximum""",
        """Voir le Skipper Pass""": """View Skipper Pass""",
        
        """Options & Suppléments""": """Options & Supplements""",
        """Assurance base""": """Basic insurance""",
        """Caution : CHF 1000.-""": """Deposit: CHF 1000.-""",
        """Franchise en cas de sinistre : CHF 1000.-""": """Deductible in case of claim: CHF 1000.-""",
        """Inclus""": """Included""",
        """Assurance Plus""": """Plus insurance""",
        """Réduction de la caution et franchise à CHF 300.-""": """Reduction of deposit and deductible to CHF 300.-""",
        """Skipper""": """Skipper""",
        """Demi-journée""": """Half day""",
        """Journée""": """Full day""",
        """Nettoyage final""": """Final cleaning""",
        """Intérieur et extérieur. Vous pouvez aussi le faire vous-même gratuitement.""": """Interior and exterior. You can also do it yourself for free.""",
        """Literie""": """Bedding""",
        """Sac de couchage et oreiller par personne""": """Sleeping bag and pillow per person""",
        """Chien à bord""": """Dog on board""",
        """Nettoyage approfondi requis""": """Deep cleaning required""",
        
        # Itineraries
        """Itinéraires de navigation sur le lac de Neuchâtel""": """Sailing itineraries on Lake Neuchâtel""",
        """Découvrez les plus beaux itinéraires et destinations pour votre location de voilier sur le lac de Neuchâtel. Plages, réserves naturelles et ports pittoresques.""": """Discover the most beautiful itineraries and destinations for your sailboat rental on Lake Neuchâtel. Beaches, nature reserves and picturesque harbours.""",
        """Idées d'itinéraires""": """Itinerary ideas""",
        """De la balade d'une journée à la croisière d'une semaine, découvrez les plus beaux recoins des Trois-Lacs.""": """From a day trip to a week-long cruise, discover the most beautiful corners of the Three Lakes.""",
        """La Rive Sud & Estavayer""": """The South Shore & Estavayer""",
        """Une navigation paisible le long de la Grande Cariçaie, la plus grande réserve naturelle lacustre de Suisse. Idéal pour une sortie à la demi-journée ou une journée complète avec halte à Estavayer-le-Lac pour visiter son château.""": """A peaceful sail along the Grande Cariçaie, the largest lakeside nature reserve in Switzerland. Ideal for a half-day or full-day trip with a stop at Estavayer-le-Lac to visit its castle.""",
        """Durée : Demi-journée à 1 jour""": """Duration: Half-day to 1 day""",
        """Difficulté : Facile""": """Difficulty: Easy""",
        """À voir : Réserve naturelle, port d'Estavayer""": """To see: Nature reserve, Estavayer harbour""",
        """Grand Tour du Lac""": """Grand Tour of the Lake""",
        """Partez pour 2 à 3 jours de navigation autour du lac. Traversez vers Gorgier, remontez jusqu'à Neuchâtel, puis longez la rive nord avant de redescendre vers Cheyres.""": """Set off for 2 to 3 days of sailing around the lake. Cross towards Gorgier, head up to Neuchâtel, then sail along the north shore before heading back down to Cheyres.""",
        """Durée : 2 à 3 jours (week-end)""": """Duration: 2 to 3 days (weekend)""",
        """Difficulté : Modérée""": """Difficulty: Moderate""",
        """À voir : Neuchâtel, Yverdon, vues sur les Alpes""": """To see: Neuchâtel, Yverdon, views of the Alps""",
        
        # Contact
        """Contact & Réservation - Location de voilier""": """Contact & Booking - Sailboat Rental""",
        """Demande de réservation""": """Booking request""",
        """Prêt à larguer les amarres ? Remplissez le formulaire ci-dessous pour vérifier les disponibilités.""": """Ready to cast off? Fill out the form below to check availability.""",
        """Demande de Réservation""": """Booking Request""",
        """Location standard""": """Standard Rental""",
        """1. Choisissez vos dates""": """1. Choose your dates""",
        """Du:""": """From:""",
        """Au:""": """To:""",
        """Nb jours:""": """Nb days:""",
        """2. Sélectionnez vos options""": """2. Select your options""",
        """Nom complet *""": """Full name *""",
        """Adresse email *""": """Email address *""",
        """N° de téléphone *""": """Phone number *""",
        """Pays de résidence""": """Country of residence""",
        """Votre message""": """Your message""",
        """Je souhaite souscrire au Skipper Pass pour 800 CHF""": """I wish to subscribe to the Skipper Pass for 800 CHF""",
        """Comment fonctionne le Pass ?""": """How does the Pass work?""",
        """Le Skipper Pass vous permet de naviguer de manière illimitée sur la saison en réservant le bateau quand il est disponible, même à la dernière minute. <a href="prices.html" target="_blank" style="color:var(--teal);text-decoration:underline">Voir les conditions détaillées</a>.""": """The Skipper Pass allows you to sail unlimitedly during the season by booking the boat when it's available, even at the last minute. <a href="prices.html" target="_blank" style="color:var(--teal);text-decoration:underline">See detailed conditions</a>.""",
        """J'ai lu et j'accepte les <a href="/conditions-generales.html" target="_blank" style="color: var(--teal); text-decoration: underline; font-weight: 500;">AGB de Location</a> *""": """I have read and accept the <a href="/en/terms-and-conditions.html" target="_blank" style="color: var(--teal); text-decoration: underline; font-weight: 500;">Rental Terms and Conditions</a> *""",
        """Envoyer la demande""": """Send request""",
        """Des questions ?""": """Questions?""",
        """Écrivez-nous par email""": """Write to us by email""",
        
        # Sailing License
        """Permis bateau Suisse | Voile catégorie D | Voilier Neuchâtel""": """Swiss sailing license | Category D | Sailboat Neuchâtel""",
        """Tout savoir sur le permis voile (catégorie D) en Suisse. Conditions, reconnaissance des permis étrangers et cours de voile sur le lac de Neuchâtel.""": """Everything you need to know about the sailing license (category D) in Switzerland. Conditions, recognition of foreign licenses and sailing courses on Lake Neuchâtel.""",
        """Le Permis Voile en Suisse""": """The Sailing License in Switzerland""",
        """Pour naviguer sur le Maxus 21, un permis est requis. Voici tout ce qu'il faut savoir.""": """To sail the Maxus 21, a license is required. Here is everything you need to know.""",
        """Réglementation Suisse (Catégorie D)""": """Swiss Regulations (Category D)""",
        """En Suisse, le permis de voile (permis de navigation de la catégorie D) est obligatoire pour conduire un voilier dont la surface vélique est supérieure à 15 m².""": """In Switzerland, the sailing license (category D navigation license) is mandatory to steer a sailboat with a sail area of more than 15 m².""",
        """Notre voilier Maxus 21 dispose d'une surface de voile de 21 m² (Grand-voile + Foc). Le permis est donc <strong>strictement obligatoire</strong> pour le louer sans skipper.""": """Our Maxus 21 sailboat has a sail area of 21 m² (Mainsail + Jib). The license is therefore <strong>strictly mandatory</strong> to rent it without a skipper.""",
        """Reconnaissance des permis étrangers""": """Recognition of foreign licenses""",
        """Visiteurs et touristes""": """Visitors and tourists""",
        """Si vous êtes de passage en Suisse pour des vacances, les autorités cantonales reconnaissent généralement les permis étrangers équivalents, notamment l'<strong>ICC (International Certificate of Competence)</strong> voilier.""": """If you are visiting Switzerland for holidays, cantonal authorities generally recognize equivalent foreign licenses, particularly the <strong>ICC (International Certificate of Competence)</strong> for sailing.""",
        """Résidents étrangers en Suisse""": """Foreign residents in Switzerland""",
        """Si vous avez élu domicile en Suisse, vous disposez d'un délai de <strong>12 mois</strong> pour faire transcrire votre permis de voile étranger en permis suisse.""": """If you have taken up residence in Switzerland, you have a period of <strong>12 months</strong> to transcribe your foreign sailing license into a Swiss license.""",
        """Obtenir son permis (Canton de Fribourg / Neuchâtel)""": """Obtaining your license (Canton of Fribourg / Neuchâtel)""",
        """Le port de Cheyres étant situé dans le canton de Fribourg, vous pouvez passer votre examen théorique et pratique auprès de l'Office de la Circulation et de la Navigation (OCN).""": """As Cheyres harbour is located in the canton of Fribourg, you can take your theoretical and practical exam at the Office of Circulation and Navigation (OCN).""",
        """Théorie : Un examen de type QCM sur les règles de navigation (signaux, priorités, météo).""": """Theory: A multiple-choice exam on navigation rules (signals, right of way, weather).""",
        """Pratique : Un examen sur l'eau avec un expert pour valider les manœuvres de base (homme à la mer, accostage, nœuds).""": """Practice: A practical exam on the water with an expert to validate basic maneuvers (man overboard, docking, knots).""",
        """Sources officielles et informations""": """Official sources and information""",
        """Pour plus d'informations sur les lois, la reconnaissance de votre permis ou pour vous inscrire aux examens :""": """For more information on laws, recognition of your license or to register for exams:""",
        """Visiter le site de l'OCN Fribourg →""": """Visit the OCN Fribourg website →""",
        """FAQ Office fédéral des transports →""": """FAQ Federal Office of Transport →""",
        
        # Reviews
        """Avis & Témoignages | Location Voilier Lac de Neuchâtel""": """Reviews & Testimonials | Sailboat Rental Lake Neuchâtel""",
        """Découvrez les avis et témoignages des navigateurs qui ont loué notre voilier Maxus 21 sur le lac de Neuchâtel.""": """Discover the reviews and testimonials of sailors who have rented our Maxus 21 sailboat on Lake Neuchâtel.""",
        """Avis des navigateurs""": """Sailors' reviews""",
        """Découvrez les retours d'expérience de ceux qui ont navigué avec nous.""": """Discover the feedback from those who have sailed with us.""",
        """Note globale""": """Overall rating""",
        """Avis vérifiés""": """Verified reviews""",
        """Tous les avis proviennent de locataires réels ayant navigué sur notre voilier.""": """All reviews come from real renters who have sailed on our sailboat.""",
        
        # Gallery
        """Galerie Photos | Voilier Maxus 21 | Lac de Neuchâtel""": """Photo Gallery | Sailboat Maxus 21 | Lake Neuchâtel""",
        """Photos de notre voilier Maxus 21 à louer sur le lac de Neuchâtel. Découvrez l'intérieur, le cockpit et des paysages de navigation.""": """Photos of our Maxus 21 sailboat for rent on Lake Neuchâtel. Discover the interior, the cockpit and sailing landscapes.""",
        """Galerie Photos""": """Photo Gallery""",
        """Explorez le Maxus 21 en images, de l'intérieur confortable aux magnifiques paysages du lac de Neuchâtel.""": """Explore the Maxus 21 in pictures, from the comfortable interior to the magnificent landscapes of Lake Neuchâtel.""",
        
        # Terms & Conditions (CG)
        """Conditions Générales de Location | Voilier Neuchâtel""": """Rental Terms and Conditions | Sailboat Neuchâtel""",
        """Lisez les conditions générales de location de notre voilier Maxus 21 au port de Cheyres sur le lac de Neuchâtel.""": """Read the general rental conditions of our Maxus 21 sailboat at Cheyres harbour on Lake Neuchâtel.""",
        """Conditions Générales de Location""": """General Rental Conditions""",
        """1. Objet""": """1. Purpose""",
        """Les présentes conditions générales régissent la location du voilier de type Northman Maxus 21 (ci-après « le bateau ») par Grégory Undritz (ci-après « le loueur ») à toute personne physique ou morale (ci-après « le locataire »).""": """These general conditions govern the rental of the Northman Maxus 21 type sailboat (hereinafter "the boat") by Grégory Undritz (hereinafter "the owner") to any natural or legal person (hereinafter "the renter").""",
        """2. Conditions préalables""": """2. Prerequisites""",
        """Le locataire (ou le skipper désigné) doit être âgé d'au moins 18 ans et être titulaire d'un permis de conduire pour bateaux à voiles (Catégorie D) valable en Suisse ou d'un titre jugé équivalent par les autorités suisses.""": """The renter (or the designated skipper) must be at least 18 years old and hold a valid sailing boat driving license (Category D) in Switzerland or a title deemed equivalent by the Swiss authorities.""",
        """Le locataire s'engage à présenter l'original de son permis ainsi qu'une pièce d'identité valide le jour de la prise en charge.""": """The renter agrees to present the original of their license as well as a valid ID on the day of handover.""",
        """3. Réservation et Paiement""": """3. Booking and Payment""",
        """La réservation ne devient ferme et définitive qu'après réception de la confirmation par email de la part du loueur et paiement du montant de la location ou de l'acompte demandé.""": """The booking becomes firm and final only after receipt of the email confirmation from the owner and payment of the rental amount or requested deposit.""",
        """Le paiement s'effectue selon les modalités indiquées sur la facture ou la plateforme de réservation.""": """Payment is made according to the terms indicated on the invoice or the booking platform.""",
        """4. Caution""": """4. Deposit""",
        """Une caution de CHF 1'000.- (ou CHF 300.- si l'assurance « Plus » est souscrite) est exigée avant la prise en charge du bateau.""": """A deposit of CHF 1,000.- (or CHF 300.- if "Plus" insurance is subscribed) is required before taking charge of the boat.""",
        """Elle peut être versée en espèces, par virement bancaire ou bloquée sur une carte de crédit (selon accord).""": """It can be paid in cash, by bank transfer or blocked on a credit card (by agreement).""",
        """La caution est restituée intégralement à la fin de la location si aucun dommage ou perte n'est constaté et si le bateau est rendu dans un état de propreté conforme.""": """The deposit is fully refunded at the end of the rental if no damage or loss is noted and if the boat is returned in a compliant state of cleanliness.""",
        """5. Annulation""": """5. Cancellation""",
        """Par le locataire :""": """By the renter:""",
        """Annulation plus de 30 jours avant le départ : remboursement intégral (hors éventuels frais de dossier).""": """Cancellation more than 30 days before departure: full refund (excluding possible administrative fees).""",
        """Annulation entre 30 et 14 jours avant le départ : 50% du montant est retenu.""": """Cancellation between 30 and 14 days before departure: 50% of the amount is retained.""",
        """Annulation à moins de 14 jours : la totalité du montant est due.""": """Cancellation less than 14 days: the total amount is due.""",
        """Par le loueur :""": """By the owner:""",
        """Le loueur se réserve le droit d'annuler la location pour des raisons de sécurité (ex: avis de tempête, avarie technique). Dans ce cas, un report est proposé ou le locataire est intégralement remboursé.""": """The owner reserves the right to cancel the rental for safety reasons (e.g. storm warning, technical breakdown). In this case, a postponement is offered or the renter is fully refunded.""",
        """6. Prise en charge et Restitution""": """6. Handover and Return""",
        """Le bateau est mis à disposition au port de Cheyres avec le plein de carburant, propre et en parfait état de fonctionnement.""": """The boat is made available at Cheyres harbour with a full tank of fuel, clean and in perfect working order.""",
        """Un état des lieux (check-in) est effectué au départ. Le locataire s'engage à signaler toute anomalie avant de quitter le port.""": """An inventory (check-in) is carried out at departure. The renter agrees to report any anomaly before leaving the port.""",
        """Le bateau doit être restitué à l'heure convenue, propre, rangé et dans le même état qu'au départ. Tout retard non excusé peut entraîner une pénalité financière.""": """The boat must be returned at the agreed time, clean, tidy and in the same condition as at departure. Any unexcused delay may result in a financial penalty.""",
        """7. Utilisation du bateau""": """7. Use of the boat""",
        """Le bateau doit être utilisé exclusivement à des fins de plaisance. La sous-location est interdite.""": """The boat must be used exclusively for pleasure purposes. Subletting is prohibited.""",
        """La navigation est autorisée sur les lacs de Neuchâtel, Bienne et Morat, dans les limites des zones autorisées par la loi.""": """Navigation is authorized on lakes Neuchâtel, Biel and Morat, within the limits of the zones authorized by law.""",
        """Le nombre maximum de personnes à bord (6 personnes) ne doit jamais être dépassé.""": """The maximum number of people on board (6 people) must never be exceeded.""",
        """Le locataire est tenu de respecter les lois sur la navigation intérieure (LNI/ONI), les règles de priorité et les avis de tempête.""": """The renter is required to comply with inland navigation laws (LNI/ONI), priority rules and storm warnings.""",
        """8. Responsabilité et Assurances""": """8. Liability and Insurance""",
        """Le bateau est assuré en responsabilité civile (RC) et casco (dégâts au bateau).""": """The boat is insured for third-party liability (RC) and comprehensive (damage to the boat).""",
        """En cas de sinistre responsable, la franchise (CHF 1'000.- ou CHF 300.-) reste à la charge exclusive du locataire.""": """In the event of a responsible claim, the deductible (CHF 1,000.- or CHF 300.-) remains the exclusive responsibility of the renter.""",
        """Le locataire est seul responsable des amendes et contraventions encourues durant la période de location.""": """The renter is solely responsible for fines and penalties incurred during the rental period.""",
        """L'assurance ne couvre pas les effets personnels du locataire et de ses passagers. Une assurance individuelle accident est recommandée.""": """Insurance does not cover the personal effects of the renter and their passengers. Individual accident insurance is recommended.""",
        """9. Avaries et Sinistres""": """9. Breakdowns and Claims""",
        """En cas d'accident, de vol ou de dommage grave, le locataire doit immédiatement contacter les autorités compétentes (police du lac) et informer le loueur.""": """In case of accident, theft or serious damage, the renter must immediately contact the competent authorities (lake police) and inform the owner.""",
        """Le locataire ne doit procéder à aucune réparation lourde sans l'accord préalable du loueur.""": """The renter must not carry out any heavy repairs without the prior agreement of the owner.""",
        """10. For juridique""": """10. Jurisdiction""",
        """Le présent contrat est soumis au droit suisse. Le for juridique exclusif est situé dans le canton de Fribourg, sous réserve des voies de recours au Tribunal fédéral.""": """This contract is subject to Swiss law. The exclusive jurisdiction is located in the canton of Fribourg, subject to appeals to the Federal Supreme Court.""",
        
        # Skipper pass section inside prices
        """Skipper Pass Saison""": """Seasonal Skipper Pass""",
        """Navigation illimitée toute la saison""": """Unlimited sailing all season""",
        """800 CHF""": """800 CHF""",
        """Saison complète (Avril - Octobre)""": """Full season (April - October)""",
        """Réservations via agenda en ligne""": """Bookings via online calendar""",
        """Assurance "Plus" incluse (Franchise 300.-)""": """'Plus' insurance included (Deductible 300.-)""",
        """Nettoyage final à la charge du locataire""": """Final cleaning is the responsibility of the renter""",
        """Devenir Membre""": """Become a Member""",
        
        """En Savoir Plus""": """Learn More"""
    }

    for filename in files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for fr, en in replacements.items():
            content = t(content, fr, en)
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print("EN translation deep pass done.")

if __name__ == "__main__":
    translate_files()
