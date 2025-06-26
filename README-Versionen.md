# 🏁 Mario Kart Challenge - Version Overview

## 📁 Verfügbare Dateien:

### 🚀 **obs-v4** (EMPFOHLEN)
**Beste Performance + Schönste Animationen**
- ✅ Hardware-Beschleunigung aktiviert
- ✅ Optimierte Partikel-Effekte
- ✅ Intelligente DOM-Updates
- ✅ Performance-Monitoring
- ✅ Adaptive Netzwerk-Abfragerate
- 🎯 **Für:** Moderne PCs mit guter Grafikkarte

### ⚡ **obs-lightweight.html** (Performance)
**Minimale Animationen, maximale Stabilität**
- ✅ Keine Partikel-Effekte
- ✅ Reduzierte Animationen
- ✅ Sehr niedrige CPU-Last
- ✅ Stabil auf schwächeren Systemen
- 🎯 **Für:** Ältere PCs oder bei Performance-Problemen

---

## 🔧 Welche Version wählen?

### 💻 **Moderne Gaming-PCs** (GTX 1060+ / RX 580+)
➜ **obs-v4.html**
- Beste Kombination aus Performance und Optik
- Alle Features verfügbar
- Automatische Optimierungen

### 🖥️ **Mittelklasse-PCs** (GTX 960 / RX 470)
➜ **obs-v4.html** → Bei Problemen: **obs-lightweight.html**
- Teste zuerst die optimierte Version
- Wechsle zu Lightweight bei Rucklern

### 📱 **Schwächere/Ältere PCs**
➜ **obs-lightweight.html**
- Stabile Performance garantiert
- Trotzdem schöne Optik
- Minimale Systemlast

---

## 🎮 OBS Browser Source Setup:

### Für obs-v4.html:
```
URL: http://localhost:8080/obs-v4.html
Breite: 500
Höhe: 700
FPS: 60
Hardware-Beschleunigung: ✅ AN
```

### Für obs-lightweight.html:
```
URL: http://localhost:8080/obs-lightweight.html
Breite: 480
Höhe: 650
FPS: 30
Hardware-Beschleunigung: ✅ AN
```

---

## 🚀 Quick Start:

1. **Server starten:**
   ```
   Doppelklick auf: start-server.bat
   ```

2. **Browser Source in OBS erstellen:**
   - Quelle hinzufügen → Browser
   - URL eingeben (siehe oben)
   - Hardware-Beschleunigung aktivieren

3. **Control Panel öffnen:**
   ```
   http://localhost:8080/control-v3.html
   ```

4. **Testen:**
   - Achievement hinzufügen
   - Joker verwenden
   - Prüfen ob Overlay reagiert

---

## 🔍 Performance Debugging:

### OBS Konsole öffnen:
1. Browser Source → Rechtsklick → "Interagieren"
2. F12 drücken → Console Tab
3. Performance-Werte ablesen

### Erwartete FPS-Werte:
- **obs-v4**: 50-60 FPS
- **obs-lightweight**: 60 FPS (konstant)
- **Unter 30 FPS**: Wechsle zu Lightweight-Version

---

## 📝 Changelog:

### v4 (NEU):
- Hardware-Beschleunigung für alle Elemente
- Intelligente DOM-Updates
- Optimierte Partikel (weniger, aber flüssiger)
- Performance-Monitoring
- Adaptive Netzwerk-Polling
- Memory-Leak Fixes

### v4-mario (Original):
- Vollständige Animationen
- Alle Partikel-Effekte
- Basis-Optimierungen

### Lightweight (NEU):
- Minimale Animationen
- Keine Partikel
- Maximale Kompatibilität

---

## 🆘 Troubleshooting:

### Problem: Overlay ruckelt
**Lösung:**
1. Hardware-Beschleunigung in OBS aktivieren
2. Zu Lightweight-Version wechseln
3. OBS FPS auf 30 reduzieren

### Problem: Hohe CPU-Last
**Lösung:**
1. Lightweight-Version verwenden
2. Hardware-Encoder in OBS aktivieren
3. Browser Source FPS reduzieren

### Problem: Overlay lädt nicht
**Lösung:**
1. Server läuft? `start-server.bat`
2. URL korrekt kopiert?
3. Windows Firewall prüfen

---

## 🎯 Empfohlener Workflow:

1. **Start:** obs-v4.html testen
2. **Performance OK?** → Weiter verwenden ✅
3. **Performance schlecht?** → obs-lightweight.html
4. **Probleme?** → Troubleshooting-Guide folgen

**Ready to Race! 🏁🎮**