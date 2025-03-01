# 🎮 Wii Cover Downloader

## 📌 Beschreibung (Deutsch)

Dieses Skript lädt eine **Wii-Datenbank** von [GameTDB.com](https://www.gametdb.com) herunter, die Informationen zu Wii-Spielen in verschiedenen Sprachen enthält. Für jeden Eintrag in der Datenbank werden mehrere **Cover-Bilder** (*2D, 3D, FULL usw.*) von definierten URLs heruntergeladen.

### ✨ Funktionen

- **🌍 Multilinguale Benutzeroberfläche**
  - Beim Start fragt das Skript, in welcher Sprache (*DE/EN*) die Eingabeaufforderungen angezeigt werden sollen.
- **📂 Mehrsprachige DB-Auswahl**
  - Der Benutzer kann eine oder mehrere **Datenbank-Sprachen** angeben (*z. B. "EN,DE,FR"*) oder `"ALL"` eingeben, um alle verfügbaren Sprachen zu verarbeiten.
- **🎨 Covertypen-Auswahl**
  - Es können spezifische **Covertypen** ausgewählt werden (*z. B. "2D,3D,FULL"*) oder `"ALL"` für alle verfügbaren Cover.
- **🔎 Cover-ID-Suche**
  - Zusätzlich kann der Benutzer wählen, ob alle Cover oder nur bestimmte Cover anhand ihrer ID heruntergeladen werden sollen. Bei Auswahl der Option **ID** können ein oder mehrere Cover-IDs (getrennt durch Kommas) eingegeben werden. Wird keine ID eingegeben, werden standardmäßig alle Cover heruntergeladen.
- **⚡ Parallelisierte Downloads**
  - Alle Download-Aufgaben werden mithilfe von `concurrent.futures.ThreadPoolExecutor` parallel abgearbeitet, wodurch der Gesamtprozess **beschleunigt** wird.
- **🗂 Strukturierte Speicherung**
  - Die heruntergeladenen Cover-Bilder werden in einem **Basisordner** namens `Images` gespeichert.
  - Unterordner werden nach **Sprache** und anschließend nach **Cover-Typ** angelegt.
- **📊 Download-Zusammenfassung**
  - Nach Abschluss der Downloads wird eine Zusammenfassung angezeigt, die für jede Cover-Kategorie und Sprache angibt, wie viele Cover erfolgreich heruntergeladen und wie viele nicht gefunden wurden.
- **📜 Fehlerprotokollierung**
  - Falls Fehler auftreten, wird der Benutzer gefragt, ob ein detailliertes Fehlerprotokoll (`error.log`) erstellt werden soll. Dieses Protokoll listet die fehlgeschlagenen Downloads gruppiert nach Sprache und Cover-Typ auf.

### 📌 Voraussetzungen

- ✅ **Python 3.x**

### ▶️ Verwendung

1. **Python-Installation prüfen**  
   - Stelle sicher, dass **Python 3.x** auf deinem System installiert ist.

2. **Skript speichern**  
   - Lade das Skript herunter und speichere es in einem gewünschten Verzeichnis.

3. **Skript starten**  
   - Öffne die Kommandozeile (*cmd, PowerShell oder Terminal*) und navigiere zu dem Verzeichnis, in dem das Skript gespeichert ist.
   - Starte das Skript mit folgendem Befehl:

   ```bash
   python Wii-GameTDB-Cover-download.py
   ```

4. UI-Sprache wählen  
   - Das Skript fragt zu Beginn:  
     "Bitte wählen Sie die Sprache der Benutzeroberfläche (DE/EN):"
   - Wähle **DE** für Deutsch oder **EN** für Englisch.

5. DB-Sprachen auswählen  
   - Alle verfügbaren Wii-Datenbank-Sprachen werden angezeigt.
   - Gib eine oder mehrere **Sprachcodes** ein (*z. B. "EN,DE,FR"*) oder "ALL", um alle Sprachen herunterzuladen.

6. Covertypen auswählen  
   - Die verfügbaren **Covertypen** werden angezeigt.
   - Gib die gewünschten Covertypen ein (*z. B. "2D,3D,FULL"*) oder "ALL" für alle Cover.
   - Falls **keine Eingabe** erfolgt, werden automatisch **alle Covertypen** heruntergeladen.

7. Cover-ID-Suche oder Alle Cover herunterladen  
   - Anschließend wird abgefragt, ob alle Cover oder nur nach Cover-ID heruntergeladen werden sollen.
   - Wählt man **ID**, kann man eine oder mehrere Cover-IDs (getrennt durch Kommas) eingeben. Wird keine ID eingegeben, werden standardmäßig alle Cover heruntergeladen.

8. Download starten  
   - Das Skript lädt nun die **Datenbanken** und die entsprechenden **Coverbilder** parallel herunter.

9. Zusammenfassung und Fehlerprotokoll  
   - Nach Abschluss der Downloads wird eine Übersicht angezeigt, wie viele Cover pro Kategorie und Sprache gefunden bzw. nicht gefunden wurden.
   - Falls Fehler aufgetreten sind, wird der Benutzer gefragt, ob ein `error.log` erstellt werden soll, in dem die fehlgeschlagenen Downloads gruppiert nach Sprache und Cover-Typ aufgeführt werden.

10. Speicherung der Cover  
   - Nach Abschluss der Downloads findest du die Bilder im Ordner `Images`, organisiert nach **Sprache** und **Cover-Typ**.



---

## 📌 Description (English)

This script downloads a **Wii database** from [GameTDB.com](https://www.gametdb.com), which contains information about Wii games in various languages. For each entry in the database, multiple **cover images** (*2D, 3D, FULL, etc.*) are downloaded from predefined URLs.

### ✨ Features

- **🌍 Multilingual User Interface**
  - At startup, the script asks in which language (*DE/EN*) the prompts should be displayed.
- **📂 Multi-language DB Selection**
  - The user can specify one or more **database languages** (*e.g., "EN,DE,FR"*) or enter `"ALL"` to process all available languages.
- **🎨 Cover Type Selection**
  - Specific **cover types** can be selected (*e.g., "2D,3D,FULL"*) or `"ALL"` for all available cover types.
- **🔎 Cover ID Search**
  - The user can choose to download all covers or only specific covers by entering their IDs. If the **ID** option is selected, one or more cover IDs (comma-separated) can be entered. If no ID is provided, all covers will be downloaded by default.
- **⚡ Parallelized Downloads**
  - All download tasks are processed in parallel using `concurrent.futures.ThreadPoolExecutor`, which **speeds up** the overall process.
- **🗂 Structured Storage**
  - The downloaded cover images are stored in a **base folder** named `Images`.
  - Subfolders are created based on **language**, followed by **cover type**.
- **📊 Download Summary**
  - After the downloads are complete, a summary is displayed, showing the number of covers successfully downloaded and those not found, grouped by category and language.
- **📜 Error Logging**
  - If errors occur, the user is asked whether to create a detailed error log (`error.log`), listing failed downloads grouped by language and cover type.

### 📌 Requirements

- ✅ **Python 3.x**

### ▶️ Usage

1. **Check Python Installation**  
   - Ensure that **Python 3.x** is installed on your system.

2. **Save the Script**  
   - Download the script and save it in your desired directory.

3. **Run the Script**  
   - Open the command line (*cmd, PowerShell, or Terminal*) and navigate to the script directory.
   - Run the following command:

   ```bash
   python Wii-GameTDB-Cover-download.py
   ```

4. Select UI Language  
   - The script prompts:  
     "Please choose the language of the user interface (DE/EN):"
   - Choose **DE** for German or **EN** for English.

5. Select DB Languages  
   - All available Wii database languages are displayed.
   - Enter one or more **language codes** (*e.g., "EN,DE,FR"*) or "ALL" to download all available languages.

6. Select Cover Types  
   - The available **cover types** are displayed.
   - Enter the desired **cover types** (*e.g., "2D,3D,FULL"*) or "ALL" for all covers.
   - If **no input** is provided, all **cover types** will be downloaded by default.

7. Cover ID Search or Download All Covers  
   - The script asks whether to download all covers or only specific ones based on their ID.
   - If **ID** is selected, enter one or more cover IDs (comma-separated). If no ID is provided, all covers will be downloaded by default.

8. Start Download  
   - The script now downloads the **databases** and the corresponding **cover images** in parallel.

9. Download Summary and Error Log  
   - After the downloads are complete, a summary displays how many covers were found and downloaded per category and language.
   - If errors occurred, the user is asked whether to generate an `error.log` file, listing failed downloads grouped by language and cover type.

10. Storing the Covers  
   - Once the downloads are complete, you will find the images in the `Images` folder, organized by **language** and **cover type**.
