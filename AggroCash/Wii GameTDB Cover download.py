import os
import urllib.request
import concurrent.futures

# URLs und Verzeichnisse definieren
WIIDB = {
    'DE': 'http://www.gametdb.com/wiitdb.txt?LANG=DE',
    'EN': 'http://www.gametdb.com/wiitdb.txt?LANG=EN',
    'RU': 'http://www.gametdb.com/wiitdb.txt?LANG=RU',
    'JA': 'http://www.gametdb.com/wiitdb.txt?LANG=JA',
}

COVER = {
    'COVER': 'http://art.gametdb.com/wii/cover/',
    'COVER3D': 'http://art.gametdb.com/wii/cover3D/',
    'COVERFULL': 'http://art.gametdb.com/wii/coverfull/',
    'COVER2': 'http://art.gametdb.com/wii/cover/',
    'COVER3D2': 'http://art.gametdb.com/wii/cover3D/',
    'COVERFULL2': 'http://art.gametdb.com/wii/coverfull/',
    'COVERB': 'http://art.gametdb.com/wii/coverB/',
    'COVER3DB': 'http://art.gametdb.com/wii/cover3DB/',
    'DISC': 'http://art.gametdb.com/wii/disc/',
    'DISCCUSTOM': 'http://art.gametdb.com/wii/disccustom/',
    'DISC2': 'http://art.gametdb.com/wii/disc/',
    'DISCCUSTOM2': 'http://art.gametdb.com/wii/disccustom/',
}

base_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DATA')
os.makedirs(base_directory, exist_ok=True)

# Schritt 1: Sammle alle Download-Aufgaben
download_tasks = []

for lang, urldb in WIIDB.items():
    print('DOWNLOAD DB: ' + urldb)
    try:
        response = urllib.request.urlopen(urldb)
        data = response.read().decode('utf-8').split('\r\n')[1:]
        lang_dir = os.path.join(base_directory, lang)
        os.makedirs(lang_dir, exist_ok=True)
        for i, item in enumerate(data, start=1):
            disc = item.split(' = ')[0]
            if disc:
                print(f'  Sammle Links für DISC {disc} [{lang}] ({i} von {len(data)})')
                for cover, coverurl in COVER.items():
                    cover_dir = os.path.join(lang_dir, cover)
                    os.makedirs(cover_dir, exist_ok=True)
                    url = coverurl + lang + '/' + disc + '.png'
                    file_path = os.path.join(cover_dir, disc + '.png')
                    download_tasks.append((url, file_path, cover))
    except Exception as e:
        print('Fehler beim Laden der DB ' + urldb, e)

# Schritt 2: Parallele Downloads mit ThreadPoolExecutor
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
for url, cover, status in results:
    print(f'{cover}: {url} --> {status}')
