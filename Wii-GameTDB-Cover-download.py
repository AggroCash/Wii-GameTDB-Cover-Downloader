import os
import urllib.request
import concurrent.futures
from collections import defaultdict

# --- Benutzeroberfläche: Sprache wählen ---
interface_choice = input("Bitte wählen Sie die Sprache der Benutzeroberfläche (DE/EN) / Please choose the language of the user interface (DE/EN): ").strip().upper()
if interface_choice == "EN":
    messages = {
        "available_db_languages": "Available DB languages:",
        "input_db_lang": "Please enter the desired languages (e.g., EN,DE,FR) or 'ALL' for all available languages: ",
        "no_valid_languages": "No valid languages selected. Defaulting to 'EN'.",
        "available_cover_types": "Available cover types:",
        "input_cover_types": "Please enter the desired cover types (e.g., 2D,3D,FULL) or 'ALL' for all cover types (Default: ALL if nothing is entered): ",
        "no_valid_cover_types": "No valid cover types selected. Defaulting to all cover types.",
        "cover_download_choice": "Do you want to download all covers or search by ID? (ALL/ID): ",
        "input_cover_ids": "Enter one or more cover IDs separated by commas: ",
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
        "cover_download_choice": "Möchtest du alle Cover herunterladen oder nach ID suchen? (ALL/ID): ",
        "input_cover_ids": "Bitte gib eine oder mehrere Cover-IDs ein, getrennt durch Kommas: ",
        "download_db": "DOWNLOAD DB: ",
        "collecting_links": "Sammle Links für DISC {} [{}] ({} von {})",
        "error_loading_db": "Fehler beim Laden der DB ",
        "step2_parallel": "Parallele Downloads mit ThreadPoolExecutor",
        "result": "{}: {} --> {}"
    }
else:
    messages = {
        "available_db_languages": "Available DB languages:",
        "input_db_lang": "Please enter the desired languages (e.g., EN,DE,FR) or 'ALL' for all available languages: ",
        "no_valid_languages": "No valid languages selected. Defaulting to 'EN'.",
        "available_cover_types": "Available cover types:",
        "input_cover_types": "Please enter the desired cover types (e.g., 2D,3D,FULL) or 'ALL' for all cover types (Default: ALL if nothing is entered): ",
        "no_valid_cover_types": "No valid cover types selected. Defaulting to all cover types.",
        "cover_download_choice": "Do you want to download all covers or search by ID? (ALL/ID): ",
        "input_cover_ids": "Enter one or more cover IDs separated by commas: ",
        "download_db": "DOWNLOAD DB: ",
        "collecting_links": "Collecting links for DISC {} [{}] ({} of {})",
        "error_loading_db": "Error loading DB ",
        "step2_parallel": "Executing downloads in parallel using ThreadPoolExecutor",
        "result": "{}: {} --> {}"
    }

# --- Verfügbare Wii-DB-Sprachen ---
available_languages = ["EN", "JA", "FR", "DE", "ES", "IT", "NL", "PT", "RU", "KO", "ZHCN", "ZHTW"]
WIIDB = {lang: f'http://www.gametdb.com/wiitdb.txt?LANG={lang}' for lang in available_languages}

# --- Verfügbare Covertypen ---
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
base_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Images')
os.makedirs(base_directory, exist_ok=True)

# --- Sprachauswahl der Wii-Datenbank ---
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

# --- Auswahl: Alle Cover oder nach ID suchen ---
download_choice = input(messages["cover_download_choice"]).strip().upper()
if download_choice == "ID":
    cover_ids_input = input(messages["input_cover_ids"]).strip()
    if cover_ids_input:
        selected_ids = [cid.strip() for cid in cover_ids_input.split(',') if cid.strip()]
    else:
        print("Keine IDs eingegeben. Es werden alle Cover heruntergeladen.")
        selected_ids = None
else:
    selected_ids = None

# --- Schritt 1: Alle Download-Aufgaben sammeln ---
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
            # Falls Cover-IDs ausgewählt wurden, nur diese verarbeiten
            if selected_ids and disc not in selected_ids:
                continue
            if disc:
                print(messages["collecting_links"].format(disc, lang, i, len(data)))
                for cover, coverurl in COVER.items():
                    if cover not in selected_cover_types:
                        continue
                    cover_dir = os.path.join(lang_dir, cover)
                    os.makedirs(cover_dir, exist_ok=True)
                    url = coverurl + lang + '/' + disc + '.png'
                    file_path = os.path.join(cover_dir, disc + '.png')
                    # Speichere zusätzlich die Cover-ID (disc)
                    download_tasks.append((url, file_path, cover, lang, disc))
    except Exception as e:
        print(messages["error_loading_db"] + urldb, e)

# --- Schritt 2: Parallele Downloads ---
def download_file(task):
    url, file_path, cover, lang, disc = task
    try:
        urllib.request.urlretrieve(url, file_path)
        return (url, cover, lang, disc, "OK")
    except Exception as e:
        return (url, cover, lang, disc, f"Fehler: {e}")

with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
    results = list(executor.map(download_file, download_tasks))

# --- Ergebnisse aggregieren ---
found_counts = defaultdict(lambda: defaultdict(int))
error_counts = defaultdict(lambda: defaultdict(int))
error_details = defaultdict(lambda: defaultdict(list))

for url, cover, lang, disc, status in results:
    if status == "OK":
        found_counts[cover][lang] += 1
    else:
        error_counts[cover][lang] += 1
        error_details[cover][lang].append(f"{disc}: {status}")

# --- Zusammenfassung ausgeben ---
print("\nZusammenfassung der gefundenen Cover:")
all_covers = set(list(found_counts.keys()) + list(error_counts.keys()))
for cover in all_covers:
    summary_found = ", ".join(f"{lang}: {found_counts[cover][lang]}" for lang in found_counts[cover])
    summary_errors = ", ".join(f"{lang}: {error_counts[cover][lang]}" for lang in error_counts[cover])
    print(f"{cover} - Gefunden: {summary_found if summary_found else '0'}; Nicht gefunden: {summary_errors if summary_errors else '0'}")

# --- Fehlerprotokoll erstellen falls Fehler vorhanden ---
total_errors = sum(error_counts[cover][lang] for cover in error_counts for lang in error_counts[cover])
if total_errors > 0:
    create_log = input("\nEs gab Fehler. Möchtest du eine error.log erstellen? (Y/N): ").strip().upper()
    if create_log == "Y":
        log_path = os.path.join(base_directory, "error.log")
        with open(log_path, "w", encoding="utf-8") as f:
            # Gruppierung der Fehler nach Sprache
            languages_with_errors = sorted({lang for cover in error_details for lang in error_details[cover]})
            for lang in languages_with_errors:
                f.write(f"Sprache: {lang}\n")
                for cover in error_details:
                    if lang in error_details[cover]:
                        for detail in error_details[cover][lang]:
                            f.write(f"  {cover}: {detail}\n")
                f.write("\n")
        print(f"Fehlerprotokoll wurde erstellt: {log_path}")
