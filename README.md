# 🎮 Wii Cover Downloader  

## 📌 Beschreibung (Deutsch)  

Dieses Skript lädt eine **Wii-Datenbank** von [GameTDB.com](https://www.gametdb.com) herunter, die Informationen zu Wii-Spielen in verschiedenen Sprachen enthält. Für jeden Eintrag in der Datenbank werden mehrere **Cover-Bilder** (*2D, 3D, FULL usw.*) von definierten URLs heruntergeladen.  

### ✨ Funktionen  

- **🌍 Multilinguale Benutzeroberfläche**  
  - Beim Start fragt das Skript, in welcher Sprache (*DE/EN*) die Eingabeaufforderungen angezeigt werden sollen.  
- **📂 Mehrsprachige DB-Auswahl**  
  - Der Benutzer kann eine oder mehrere **Datenbank-Sprachen** angeben (*z. B. "EN,DE,FR"*) oder `"ALL"` eingeben, um alle verfügbaren Sprachen zu verarbeiten.  
- **⚡ Parallelisierte Downloads**  
  - Alle Download-Aufgaben werden mithilfe von `concurrent.futures.ThreadPoolExecutor` parallel abgearbeitet, wodurch der Gesamtprozess **beschleunigt** wird.  
- **🗂 Strukturierte Speicherung**  
  - Die heruntergeladenen Cover-Bilder werden in einem **Basisordner** namens `Images` gespeichert.  
  - Unterordner werden nach **Sprache** und anschließend nach **Cover-Typ** angelegt.  


### 📌 Voraussetzungen  

- ✅ **Python 3.x**  

### ▶️ Verwendung  

1. Stelle sicher, dass **Python 3.x** installiert ist.  
2. Speichere das Skript in einem beliebigen Verzeichnis.  
3. Führe das Skript über die Kommandozeile aus:  

   ```bash
   python Wii-GameTDB-Cover-download.py

  Wähle die gewünschte Sprache der Benutzeroberfläche (DE/EN).
  Gib die Datenbank-Sprachen ein (z. B. "EN,DE,FR" oder "ALL" für alle Sprachen).
  Nach Abschluss der Downloads findest du die Cover-Bilder im Ordner Images, organisiert nach Sprache und Cover-Typ.

## 📌 Description (English)  

This script downloads a **Wii database** from [GameTDB.com](https://www.gametdb.com), which contains information about Wii games in various languages. For each entry in the database, multiple **cover images** (*2D, 3D, FULL, etc.*) are downloaded from predefined URLs.  

### ✨ Features  

- **🌍 Multilingual User Interface**  
  - At startup, the script asks in which language (*DE/EN*) the prompts should be displayed.  
- **📂 Multi-language DB Selection**  
  - The user can specify one or more **database languages** (*e.g., "EN,DE,FR"*) or enter `"ALL"` to process all available languages.  
- **⚡ Parallelized Downloads**  
  - All download tasks are processed in parallel using `concurrent.futures.ThreadPoolExecutor`, which **speeds up** the overall process.  
- **🗂 Structured Storage**  
  - The downloaded cover images are stored in a **base folder** named `Images`.  
  - Subfolders are created based on **language**, followed by **cover type**.  

### 📌 Requirements  

- ✅ **Python 3.x**  

### ▶️ Usage  

1. Ensure that **Python 3.x** is installed.  
2. Save the script in any directory.  
3. Run the script via the command line:  

   ```bash
   python Wii-GameTDB-Cover-download.py

Choose the desired user interface language (DE/EN).
Enter the database languages (e.g., "EN,DE,FR" or "ALL" for all languages).
After the downloads are complete, you will find the cover images in the Images folder, organized by language and cover type.
