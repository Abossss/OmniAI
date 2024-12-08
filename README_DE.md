<div align="center">  

# 🌟 <span style="color: #3498db;">OmniAI</span>  

[简体中文](README_CN.md) / [繁体中文](README_TC.md) / [English](README.md)  / Deutsch / [日本語](README_JP.md)


</div>  

---

## 🌐 <span style="color: #2ecc71;">Projektübersicht</span>  

Dieses Projekt basiert auf Large-Model-Technologie (wie ❤️ <span style="color: #e74c3c;">Ollama-Framework</span>) und allgemeiner künstlicher Intelligenz (AGI) und zielt darauf ab, einen intelligenten Assistenten zu entwickeln.  

Dieser intelligente Assistent bietet eine Vielzahl von Funktionen, darunter:  
- 🧠 **Kurzzeit- und Langzeitgedächtnis**  
- 🔧 **Werkzeugintegration**  
- 📋 **Planung und Ausführung**  

Das Ziel ist es, die Effizienz von Frontline-Mitarbeitern zu steigern und sie mit dem Fachwissen eines Branchenexperten auszustatten. Durch die Integration modernster Technologien für die Verarbeitung natürlicher Sprache kann der Assistent präzise Anleitungen, Geschäftsentscheidungen und branchenspezifische Lösungen bieten. Das Design ist auf verschiedene Anwendungsfälle in der Industrie ausgerichtet, um Arbeitsabläufe zu vereinfachen und die operative Komplexität zu reduzieren.  

> 💡 <span style="color: #f1c40f;">**Hinweis**</span>: Dieses Produkt befindet sich derzeit in der Testphase. Der bereitgestellte Inhalt der Wissensdatenbank dient nur zu Testzwecken. Bei der Implementierung in realen Umgebungen müssen Nutzer branchenspezifisches Wissen integrieren.  

---

## 🚀 <span style="color: #9b59b6;">Kernfunktionen</span>  

- 🏭 **<span style="color: #1abc9c;">Branchenexpertise</span>**  
  Der intelligente Assistent verfügt über branchenspezifisches Fachwissen und kann auf branchenspezifische Fragen antworten.  

- 📚 **<span style="color: #3498db;">Kurzzeit- und Langzeitgedächtnis</span>**  
  Kann sich an die Eingaben des Nutzers (z. B. bestimmte Fragen) sowie an langfristige Informationen (z. B. häufige Aktionen oder Anforderungen des Nutzers) erinnern, um die Effizienz und Intelligenz der Interaktionen zu verbessern.  

- ⚙️ **<span style="color: #e67e22;">Werkzeugintegration</span>**  
  Unterstützt den Einsatz externer Tools (z. B. Websuche und Dateiverarbeitung), um die Reichweite und Genauigkeit der Antworten zu erhöhen.  

- 🗓️ **<span style="color: #95a5a6;">Planung und Ausführung</span>**  
  Bietet grundlegende Aufgabenverwaltung und Ausführungsfunktionen, um den Nutzern bei der effizienten Planung und Durchführung ihrer Aufgaben zu helfen.  

- 🤖 **<span style="color: #f39c12;">Automatisierte Entscheidungen</span>**  
  Nutzt Large-Model-Technologien, um Lösungen basierend auf den Anforderungen der Nutzer zu generieren und auszuführen.  

- 📂 **<span style="color: #2c3e50;">Datei- und Wissensmanagement</span>**  
  Unterstützt die Verarbeitung und Extraktion von Informationen aus lokalen Dateien (z. B. `.docx` und `.pdf`) und aktualisiert die Wissensdatenbank automatisch, um das Fachwissen kontinuierlich zu erweitern.  

---

## 🛠️ <span style="color: #8e44ad;">Systemarchitektur</span>  

Das System basiert auf Large-Model-Technologien und AGI und verwendet eine modulare Architektur mit folgenden Modulen:  

- 💬 **<span style="color: #16a085;">Interaktionsmodul</span>**  
  Verarbeitet Benutzerinteraktionen und -eingaben und gleicht diese mit lokalen Wissensdatenbanken und Dateiinhalten ab. Wenn keine lokale Antwort möglich ist, wird eine Websuche gestartet und externe Large-Model-Quellen werden genutzt.  

- 🧠 **<span style="color: #34495e;">Gedächtnismodul</span>**  
  Verwalten von Kurzzeit- und Langzeitgedächtnis. Das Kurzzeitgedächtnis speichert die letzten Eingaben des Nutzers, während das Langzeitgedächtnis dauerhafte Informationen behält, um die Intelligenz der Interaktionen zu verbessern.  

- 📖 **<span style="color: #e74c3c;">Wissensmodul</span>**  
  Unterstützt die dynamische Lade-, Aktualisierungs- und Speichermanagement sowie die Abfrage von lokalen Wissensdatenbanken.  

- 🌐 **<span style="color: #f1c40f;">Websuchmodul</span>**  
  Ermöglicht die Integration von Websuchfunktionen und die Verwendung externer Large-Model-Systeme (z. B. qwen2), um externe Daten für präzise Antworten zu sammeln.  

- 🔗 **<span style="color: #d35400;">Werkzeugmodul</span>**  
  Unterstützt die Integration externer APIs und Tools zur Erweiterung der Funktionen, wie z. B. Wetterberichte und Lieferkettenanalysen.  

---

## ⚙️ <span style="color: #2c3e50;">Installation und Konfiguration</span>  

### 🌍 <span style="color: #95a5a6;">Systemanforderungen</span>  

- 💻 **<span style="color: #1abc9c;">Betriebssystem</span>**: Kompatibel mit Windows, macOS, Linux  
- 🐍 **<span style="color: #3498db;">Python-Version</span>**: 3.6 oder höher  
- 📦 **<span style="color: #e67e22;">Abhängigkeiten</span>**:  

```bash
pip install ollama~=0.4.0
pip install docx~=0.2.4
pip install python-docx~=1.1.2
pip install pdfplumber~=0.11.2
```  

✨ Jetzt ist alles bereit! Beginnen Sie Ihre intelligente Entdeckungsreise! 🎉  
