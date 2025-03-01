import os
import urllib.request
import concurrent.futures

# Zuerst: Abfrage der Sprache für die Benutzeroberfläche
interface_choice = input("Bitte wählen Sie die Sprache der Benutzeroberfläche (DE/EN) / Please choose the language of the user interface (DE/EN): ").strip().upper()
if interface_choice == "EN":
    messages = {
        "available_db_languages": "Available DB languages:",
        "input_db_lang": "Please enter the desired languages (e.g., EN,DE,FR) or 'ALL' for all available languages: ",
        "no_valid_languages": "No valid languages selected. Defaulting to 'EN'.",
        "download_db": "DOWNLOAD DB: ",
        "collecting_links": "Collecting links for DISC {} [{}] ({} of {})",
        "error_loading_db": "Error loading DB ",
        "step2_parallel": "Executing downloads in parallel using ThreadPoolExecutor",
        "result": "{}: {} --> {}"
    }
elif interface_choice == "DE":
    messages = {
        "available_db_languages": "Verfügbare DB-Sprachen:",
        "input_db_lang": "Bitte gib die gewünschten Sprachen ein (z.B. EN,DE,FR) oder 'ALL' für alle verfügbaren Sprachen: ",
        "no_valid_languages": "Keine gültigen Sprachen ausgewählt. Standardmäßig wird 'EN' verwendet.",
        "download_db": "DOWNLOAD DB: ",
        "collecting_links": "Sammle Links für DISC {} [{}] ({} von {})",
        "error_loading_db": "Fehler beim Laden der DB ",
        "step2_parallel": "Parallele Downloads mit ThreadPoolExecutor",
        "result": "{}: {} --> {}"
    }
else:
    # Fallback: Standardmäßig Englisch
    messages = {
        "available_db_languages": "Available DB languages:",
        "input_db_lang": "Please enter the desired languages (e.g., EN,DE,FR) or 'ALL' for all available languages: ",
        "no_valid_languages": "No valid languages selected. Defaulting to 'EN'.",
        "download_db": "DOWNLOAD DB: ",
        "collecting_links": "Collecting links for DISC {} [{}] ({} of {})",
        "error_loading_db": "Error loading DB ",
        "step2_parallel": "Executing downloads in parallel using ThreadPoolExecutor",
        "result": "{}: {} --> {}"
    }

# Verfügbare Sprachen, die für die Wii-Datenbank genutzt werden sollen
# Available languages used for the Wii database
available_languages = ["EN", "JA", "FR", "DE", "ES", "IT", "NL", "PT", "RU", "KO", "ZHCN", "ZHTW"]

# WIIDB-URLs werden automatisch anhand der Sprachcodes generiert
# WIIDB URLs are automatically generated based on the language codes
WIIDB = {lang: f'http://www.gametdb.com/wiitdb.txt?LANG={lang}' for lang in available_languages}

COVER = {
    '2D': 'http://art.gametdb.com/wii/cover/',
    '3D': 'http://art.gametdb.com/wii/cover3D/',
    'FULL': 'http://art.gametdb.com/wii/coverfull/',
    '2D2': 'http://art.gametdb.com/wii/cover/',
    '3D2': 'http://art.gametdb.com/wii/cover3D/',
    'FULL2': 'http://art.gametdb.com/wii/coverfull/',
    '2DB': 'http://art.gametdb.com/wii/coverB/',
    '3DB': 'http://art.gametdb.com/wii/cover3DB/',
    'DISC': 'http://art.gametdb.com/wii/disc/',
    'DISCCUSTOM': 'http://art.gametdb.com/wii/disccustom/',
    'DISC2': 'http://art.gametdb.com/wii/disc/',
    'DISCCUSTOM2': 'http://art.gametdb.com/wii/disccustom/',
}

# Basisordner festlegen (hier wird der Ordnername auf "Images" gesetzt)
# Set the base directory (the folder name is set to "Images")
base_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Images')
os.makedirs(base_directory, exist_ok=True)

# Sprachauswahl der Wii-Datenbank durch den Benutzer
# User selects the DB languages
print(messages["available_db_languages"])
for lang in WIIDB.keys():
    print(" -", lang)
choice = input(messages["input_db_lang"]).strip().upper()

if choice == "ALL":
    selected_languages = list(WIIDB.keys())
else:
    # Mehrere Sprachen per Komma getrennt eingeben
    # Enter multiple languages separated by commas
    languages_input = [lang.strip() for lang in choice.split(',')]
    selected_languages = [lang for lang in languages_input if lang in WIIDB]
    if not selected_languages:
        print(messages["no_valid_languages"])
        selected_languages = ['EN']

# Schritt 1: Alle Download-Aufgaben sammeln
# Step 1: Collect all download tasks
download_tasks = []

for lang in selected_languages:
    urldb = WIIDB[lang]
    print(messages["download_db"] + urldb)
    try:
        response = urllib.request.urlopen(urldb)
        data = response.read().decode('utf-8').split('\r\n')[1:]
        lang_dir = os.path.join(base_directory, lang)
        os.makedirs(lang_dir, exist_ok=True)
        for i, item in enumerate(data, start=1):
            disc = item.split(' = ')[0]
            if disc:
                print(messages["collecting_links"].format(disc, lang, i, len(data)))
                for cover, coverurl in COVER.items():
                    cover_dir = os.path.join(lang_dir, cover)
                    os.makedirs(cover_dir, exist_ok=True)
                    url = coverurl + lang + '/' + disc + '.png'
                    file_path = os.path.join(cover_dir, disc + '.png')
                    download_tasks.append((url, file_path, cover))
    except Exception as e:
        print(messages["error_loading_db"] + urldb, e)

# Schritt 2: Parallele Downloads mit ThreadPoolExecutor
# Step 2: Execute downloads in parallel using ThreadPoolExecutor
def download_file(task):
    url, file_path, cover = task
    try:
        urllib.request.urlretrieve(url, file_path)
        return (url, cover, "OK")
    except Exception as e:
        return (url, cover, f"Fehler: {e}")

with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
    results = list(executor.map(download_file, download_tasks))

# Ergebnisse auswerten
# Evaluate results
for url, cover, status in results:
    print(messages["result"].format(cover, url, status))
