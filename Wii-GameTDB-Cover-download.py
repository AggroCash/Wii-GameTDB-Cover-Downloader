import os
import urllib.request
import concurrent.futures

# --- Benutzeroberfläche: Sprache wählen ---
# Choose UI language
interface_choice = input("Bitte wählen Sie die Sprache der Benutzeroberfläche (DE/EN) / Please choose the language of the user interface (DE/EN): ").strip().upper()
if interface_choice == "EN":
    messages = {
        "available_db_languages": "Available DB languages:",
        "input_db_lang": "Please enter the desired languages (e.g., EN,DE,FR) or 'ALL' for all available languages: ",
        "no_valid_languages": "No valid languages selected. Defaulting to 'EN'.",
        "available_cover_types": "Available cover types:",
        "input_cover_types": "Please enter the desired cover types (e.g., 2D,3D,FULL) or 'ALL' for all cover types (Default: ALL if nothing is entered): ",
        "no_valid_cover_types": "No valid cover types selected. Defaulting to all cover types.",
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
        "available_cover_types": "Verfügbare Covertypen:",
        "input_cover_types": "Bitte gib die gewünschten Covertypen ein (z.B. 2D,3D,FULL) oder 'ALL' für alle Covertypen (Standard: ALL, falls nichts eingegeben wird): ",
        "no_valid_cover_types": "Keine gültigen Covertypen ausgewählt. Standardmäßig werden alle Covertypen verwendet.",
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
        "available_cover_types": "Available cover types:",
        "input_cover_types": "Please enter the desired cover types (e.g., 2D,3D,FULL) or 'ALL' for all cover types (Default: ALL if nothing is entered): ",
        "no_valid_cover_types": "No valid cover types selected. Defaulting to all cover types.",
        "download_db": "DOWNLOAD DB: ",
        "collecting_links": "Collecting links for DISC {} [{}] ({} of {})",
        "error_loading_db": "Error loading DB ",
        "step2_parallel": "Executing downloads in parallel using ThreadPoolExecutor",
        "result": "{}: {} --> {}"
    }

# --- Verfügbare Wii-DB-Sprachen ---
# Available languages used for the Wii database
available_languages = ["EN", "JA", "FR", "DE", "ES", "IT", "NL", "PT", "RU", "KO", "ZHCN", "ZHTW"]

# WIIDB-URLs werden automatisch anhand der Sprachcodes generiert
# WIIDB URLs are automatically generated based on the language codes
WIIDB = {lang: f'http://www.gametdb.com/wiitdb.txt?LANG={lang}' for lang in available_languages}

# --- Verfügbare Covertypen ---
# Available cover types with corresponding base URLs
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

# --- Basisordner festlegen ---
# Set the base directory (the folder name is set to "Images")
base_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Images')
os.makedirs(base_directory, exist_ok=True)

# --- Sprachauswahl der Wii-Datenbank ---
# User selects the DB languages
print(messages["available_db_languages"])
for lang in WIIDB.keys():
    print(" -", lang)
db_choice = input(messages["input_db_lang"]).strip().upper()

if db_choice == "ALL":
    selected_languages = list(WIIDB.keys())
else:
    languages_input = [lang.strip() for lang in db_choice.split(',')]
    selected_languages = [lang for lang in languages_input if lang in WIIDB]
    if not selected_languages:
        print(messages["no_valid_languages"])
        selected_languages = ['EN']

# --- Covertypen-Auswahl ---
# User selects the cover types
print(messages["available_cover_types"])
for cover in COVER.keys():
    print(" -", cover)
cover_choice = input(messages["input_cover_types"]).strip().upper()

if cover_choice == "" or cover_choice == "ALL":
    selected_cover_types = list(COVER.keys())
else:
    covers_input = [c.strip() for c in cover_choice.split(',')]
    selected_cover_types = [c for c in covers_input if c in COVER]
    if not selected_cover_types:
        print(messages["no_valid_cover_types"])
        selected_cover_types = list(COVER.keys())

# --- Schritt 1: Alle Download-Aufgaben sammeln ---
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
                # Nur die ausgewählten Covertypen werden verarbeitet
                for cover, coverurl in COVER.items():
                    if cover not in selected_cover_types:
                        continue
                    cover_dir = os.path.join(lang_dir, cover)
                    os.makedirs(cover_dir, exist_ok=True)
                    url = coverurl + lang + '/' + disc + '.png'
                    file_path = os.path.join(cover_dir, disc + '.png')
                    download_tasks.append((url, file_path, cover))
    except Exception as e:
        print(messages["error_loading_db"] + urldb, e)

# --- Schritt 2: Parallele Downloads ---
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

# --- Ergebnisse auswerten ---
# Evaluate results
for url, cover, status in results:
    print(messages["result"].format(cover, url, status))
