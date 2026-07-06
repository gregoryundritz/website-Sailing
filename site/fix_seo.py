import os
import glob

replacements_en = {
    'Location Voilier Suisse | Yacht & Segelschiff mieten Lac de Neuchâtel': 'Sailboat Rental Neuchâtel with/without skipper ► from 235 CHF/day',
    'Location de voilier et yacht sur le lac de Neuchâtel (Suisse). Segelschiff mieten au départ de Cheyres. Voilier habitable Maxus 21 dès 235 CHF avec nuitées gratuites.': 'Rent a sailboat and habitable yacht on Lake Neuchâtel (Switzerland). ✔️ Departure from Cheyres ✔️ Maxus 21 ✔️ Overnights included. Book in 1 click!',
    '"Location Voilier Suisse — Lac de Neuchâtel (Yacht & Segelschiff mieten)"': '"Sailboat Rental Neuchâtel"',
    '"Location de voilier et yacht habitable Northman Maxus 21 (6.5m) au harbour de Cheyres sur le lac de Neuchâtel, Suisse. Segelschiff mieten. Carburant inclus, nuitées au harbour gratuites."': '"Rent a habitable Northman Maxus 21 sailboat on Lake Neuchâtel, Switzerland. Gasoline included, free overnight stays."',
    '"Location de voilier et yacht habitable Northman Maxus 21 (6.5m) au port de Cheyres sur le lac de Neuchâtel, Suisse. Segelschiff mieten. Carburant inclus, nuitées au port gratuites."': '"Rent a habitable Northman Maxus 21 sailboat on Lake Neuchâtel, Switzerland. Gasoline included, free overnight stays."',
    '"Location de voilier et yacht sur le lac de Neuchâtel. Segelschiff mieten."': '"Rent a sailboat on Lake Neuchâtel."'
}

replacements_de = {
    'Location Voilier Suisse | Yacht & Segelschiff mieten Lac de Neuchâtel': 'Segelboot Mieten Neuenburg mit/ohne Skipper ► ab 235 CHF/Tag',
    'Location de voilier et yacht sur le lac de Neuchâtel (Suisse). Segelschiff mieten au départ de Cheyres. Voilier habitable Maxus 21 dès 235 CHF avec nuitées gratuites.': 'Mieten Sie ein Segelboot und Yacht am Neuenburgersee (Schweiz). ✔️ Abfahrt ab Cheyres ✔️ Maxus 21 ✔️ Übernachtungen inklusive. In 1 Klick buchen!',
    '"Location Voilier Suisse — Lac de Neuchâtel (Yacht & Segelschiff mieten)"': '"Segelboot Mieten Neuenburgersee"',
    '"Location de voilier et yacht habitable Northman Maxus 21 (6.5m) au harbour de Cheyres sur le lac de Neuchâtel, Suisse. Segelschiff mieten. Carburant inclus, nuitées au harbour gratuites."': '"Mieten Sie ein Northman Maxus 21 Segelboot am Neuenburgersee, Schweiz. Benzin inklusive, kostenlose Übernachtungen."',
    '"Location de voilier et yacht habitable Northman Maxus 21 (6.5m) au port de Cheyres sur le lac de Neuchâtel, Suisse. Segelschiff mieten. Carburant inclus, nuitées au port gratuites."': '"Mieten Sie ein Northman Maxus 21 Segelboot am Neuenburgersee, Schweiz. Benzin inklusive, kostenlose Übernachtungen."',
    '"Location de voilier et yacht sur le lac de Neuchâtel. Segelschiff mieten."': '"Segelboot mieten am Neuenburgersee."'
}

replacements_fr = {
    'Location Voilier Suisse | Yacht & Segelschiff mieten Lac de Neuchâtel': 'Location Voilier Neuchâtel avec/sans skipper ► dès 235 CHF/j.',
    'Location de voilier et yacht sur le lac de Neuchâtel (Suisse). Segelschiff mieten au départ de Cheyres. Voilier habitable Maxus 21 dès 235 CHF avec nuitées gratuites.': 'Louez un voilier et yacht habitable sur le lac de Neuchâtel (Suisse). ✔️ Départ de Cheyres ✔️ Maxus 21 ✔️ Nuitées incluses. Réservez en 1 clic !',
    '"Location Voilier Suisse — Lac de Neuchâtel (Yacht & Segelschiff mieten)"': '"Location Voilier Neuchâtel"',
    '"Location de voilier et yacht habitable Northman Maxus 21 (6.5m) au harbour de Cheyres sur le lac de Neuchâtel, Suisse. Segelschiff mieten. Carburant inclus, nuitées au harbour gratuites."': '"Location de voilier et yacht habitable Northman Maxus 21 sur le lac de Neuchâtel, Suisse. Carburant inclus, nuitées au port gratuites."',
    '"Location de voilier et yacht habitable Northman Maxus 21 (6.5m) au port de Cheyres sur le lac de Neuchâtel, Suisse. Segelschiff mieten. Carburant inclus, nuitées au port gratuites."': '"Location de voilier et yacht habitable Northman Maxus 21 sur le lac de Neuchâtel, Suisse. Carburant inclus, nuitées au port gratuites."',
    '"Location de voilier et yacht sur le lac de Neuchâtel. Segelschiff mieten."': '"Location de voilier sur le lac de Neuchâtel."'
}

def process_dir(directory, replacements):
    for filepath in glob.glob(os.path.join(directory, '*.html')):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        for k, v in replacements.items():
            content = content.replace(k, v)
            
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filepath}")

base_dir = '/home/gregory/Voilier/site'
process_dir(base_dir, replacements_fr)
process_dir(os.path.join(base_dir, 'en'), replacements_en)
process_dir(os.path.join(base_dir, 'de'), replacements_de)
print("Done")
