## Inhaltsverzeichnis
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Erklärung](#erklärung)

## Installation
1. Clone das Repository: `git clone https://github.com/FeuerwehrHackathon2024/water_rescue.git`
2. Wechsle in das Projektverzeichnis: `cd frontend`
3. Installiere die Abhängigkeiten: `npm install` (Sollte das nicht funktionieren muss erst [Node](https://nodejs.org/en/download "Node Download") installiert werden)

## Verwendung
Wenn du das Projekt starten willst kannst du einfach folgenden Befehl ausführen:
```bash
npm start
```

## Erklärung
Um das Tool zu benutzen, muss man zuerst links oben die Möglichkeit aktivieren, einen Startpunkt zu setzen. Hat man 
dies getan und einen Punkt auf der Isar gesetzt, kann man nun mit dem Schieberegler die Minuten verändern, die die 
Person bereits unterwegs ist. Die Isar wird nun dynamisch eingefärbt.

## Weiter Ideen
- Isar soll entsprechend der Wahrscheinlichkeit eingefärbt werden. Das heißt, je höher die Wahrscheinlichkeit ist, dass sich die Person an einer Stelle befindet, desto stärker soll z. B. die Farbe Rot an dieser Stelle sein.
- Es sollte möglich sein, weitere Beobachtungen einzutragen, um die Route anzupassen. 
- Bei Abzweigungen soll das Tool in Zukunft nur eine Hauptader der Isar nehmen.
- Das Tool soll sich dynamisch updaten, sodass man an der Einsatzstelle quasi die 'Live'-Bewegung sieht, auch wenn diese nur interpoliert ist. 
- In Zukunft sollte es möglich sein, den Pegel anzugeben (oder das Tool sollte ihn automatisch aus der API holen), und die Länge sollte dann automatisch angepasst werden.
- Der gesamte Code sowie die Benutzeroberfläche müssen überarbeitet werden, da momentan alles sehr temporär aufgebaut ist.

Wie arbeiten gerne auch noch an dem tool weiter :)
