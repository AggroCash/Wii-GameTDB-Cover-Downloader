Wii Cover Downloader

Deutsch
Beschreibung

Dieses Skript lädt eine Wii-Spieldatenbank von gametdb.com herunter, welche Informationen zu Wii-Spielen enthält. Anschließend werden für jeden Eintrag in der Datenbank mehrere Cover-Bilder (z. B. COVER, COVER3D, COVERFULL usw.) von definierten URLs heruntergeladen. Die Bilder werden in einem strukturierten Verzeichnisbaum unter dem Ordner Images gespeichert – sortiert nach Sprache und Cover-Typ.
Funktionsweise

    Datenbank-Download:
    Das Skript lädt die Datenbank-Datei herunter und verarbeitet diese zeilenweise, wobei der jeweilige Disc-Name extrahiert wird.

    Aufgabensammlung:
    Für jeden ermittelten Disc-Eintrag wird eine Liste von Download-Aufgaben erstellt. Jede Aufgabe enthält den Download-Link sowie den Zielpfad für das jeweilige Cover-Bild.

    Parallele Downloads:
    Anstatt jeden Download sequenziell auszuführen, werden alle gesammelten Aufgaben mithilfe von concurrent.futures.ThreadPoolExecutor parallel abgearbeitet. Dadurch wird der Gesamtprozess deutlich beschleunigt.

    Speicherung:
    Die heruntergeladenen Bilder werden in einem Verzeichnisbaum abgelegt, der zuerst nach Sprache und dann nach Cover-Typ strukturiert ist.

Voraussetzungen

    Python 3.x

Verwendung

    Stelle sicher, dass Python 3.x installiert ist und du eine stabile Internetverbindung hast.
    Speichere das Skript in einem Verzeichnis deiner Wahl.
    Starte das Skript über die Kommandozeile, z. B.:

    python Wii-GameTDB-Cover-download.py

    Nach erfolgreichem Download findest du die Dateien im Unterordner Images.

English
Description

This script downloads a Wii game database from gametdb.com which contains information about Wii games. For each entry in the database, it downloads multiple cover images (e.g., COVER, COVER3D, COVERFULL, etc.) from specified URLs. The images are saved in a structured directory tree under the Images folder, organized by language and cover type.
How It Works

    Database Download:
    The script downloads the database file and processes it line by line, extracting the game disc identifier.

    Task Collection:
    For each disc entry, a list of download tasks is created. Each task consists of the download URL and the target file path for the cover image.

    Parallel Downloads:
    Instead of downloading files sequentially, all collected tasks are executed in parallel using Python’s concurrent.futures.ThreadPoolExecutor. This greatly reduces the overall download time.

    Storage:
    The downloaded images are saved in a directory tree that is first organized by language and then by cover type.

Requirements

    Python 3.x

Usage

    Ensure that Python 3.x is installed and that you have a stable internet connection.
    Save the script in a directory of your choice.
    Run the script from the command line, for example:

python Wii-GameTDB-Cover-download.py

Once the downloads complete, you can find the images in the Images folder.
