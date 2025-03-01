Wii Cover Downloader

Deutsch

Beschreibung

Dieses Skript lädt eine Wii-Datenbank von gametdb.com herunter, die Informationen zu Wii-Spielen in verschiedenen Sprachen enthält. Für jeden Eintrag in der Datenbank werden mehrere Cover-Bilder (wie 2D, 3D, FULL usw.) von definierten URLs heruntergeladen. Dabei bietet das Skript folgende Funktionen:

    Multilinguale Benutzeroberfläche:
    Beim Start fragt das Skript, in welcher Sprache (DE/EN) die Eingabeaufforderungen angezeigt werden sollen.
    Mehrsprachige DB-Auswahl:
    Der Benutzer kann eine oder mehrere Datenbank-Sprachen angeben (z. B. "EN,DE,FR") oder "ALL" eingeben, um alle verfügbaren Sprachen zu verarbeiten.
    Parallelisierte Downloads:
    Alle Download-Aufgaben werden mithilfe von concurrent.futures.ThreadPoolExecutor parallel abgearbeitet, wodurch der Gesamtprozess beschleunigt wird.
    Strukturierte Speicherung:
    Die heruntergeladenen Cover-Bilder werden in einem Basisordner namens Images gespeichert. Unterordner werden nach Sprache und dann nach Cover-Typen angelegt.

Funktionsweise

    UI-Sprache wählen:
    Der Benutzer wählt zu Beginn, ob die Eingabeaufforderungen in Deutsch oder Englisch angezeigt werden sollen.
    DB-Sprachen auswählen:
    Anschließend werden alle verfügbaren Wii-Datenbank-Sprachen angezeigt. Der Benutzer gibt entweder einzelne Sprachcodes (kommagetrennt) oder "ALL" ein.
    Datenbank laden & Links sammeln:
    Für jede ausgewählte Sprache wird die entsprechende Wii-Datenbank heruntergeladen. Aus jedem Datensatz wird die Disc-ID extrahiert und für jeden Cover-Typ ein Download-Link erstellt.
    Paralleler Download:
    Mithilfe eines Thread-Pools werden die Bilder parallel heruntergeladen.
    Speicherung:
    Die Bilder werden in einem Verzeichnisbaum unter dem Ordner Images abgelegt, strukturiert nach Sprache und Cover-Typ.

Voraussetzungen

    Python 3.x

Verwendung

    Stelle sicher, dass Python 3.x installiert ist.
    Speichere das Skript in einem beliebigen Verzeichnis.
    Führe das Skript über die Kommandozeile aus:

        python dein_skript_name.py

    Wähle die gewünschte Sprache der Benutzeroberfläche (DE/EN) aus – die Eingabeaufforderung zeigt beide Optionen an.
    Gib dann die gewünschten Datenbank-Sprachen ein (z. B. "EN,DE,FR") oder "ALL" für alle Sprachen.
    Nach Abschluss der Downloads findest du die Cover-Bilder im Ordner Images, organisiert nach Sprache und Cover-Typ.



English

Description

This script downloads a Wii game database from gametdb.com, which contains information about Wii games in various languages. For each entry in the database, multiple cover images (such as 2D, 3D, FULL, etc.) are downloaded from specified URLs. The script offers the following features:

    Multilingual User Interface:
    At startup, the script asks the user to choose whether the prompts should be displayed in German (DE) or English (EN).
    Multilingual DB Selection:
    The user can enter one or more database languages (e.g., "EN,DE,FR") or type "ALL" to process all available languages.
    Parallel Downloads:
    All download tasks are executed in parallel using Python’s concurrent.futures.ThreadPoolExecutor, which significantly speeds up the process.
    Structured Storage:
    The downloaded cover images are saved in a base folder named Images, with subfolders organized by language and cover type.

How It Works

    Select UI Language:
    The user is prompted at the beginning to choose the language of the interface (DE/EN).
    Select DB Languages:
    All available Wii database languages are displayed. The user can enter individual language codes (comma-separated) or "ALL" for all languages.
    Load Database & Collect Links:
    For each selected language, the corresponding Wii database is downloaded. The disc identifier is extracted from each record, and a download link is created for each cover type.
    Parallel Download:
    A thread pool is used to download the images in parallel.
    Storage:
    The images are stored in a directory tree under the Images folder, organized by language and cover type.

Requirements

    Python 3.x

Usage

    Make sure Python 3.x is installed.
    Save the script in your desired directory.
    Run the script from the command line:

        python your_script_name.py

    First, choose the UI language (DE/EN) from the prompt, which displays both options.
    Then, enter the desired database languages (e.g., "EN,DE,FR") or type "ALL" to download all available languages.
    Once the downloads are complete, you will find the cover images in the Images folder, organized by language and cover type.