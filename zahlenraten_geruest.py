# =====================================================
#  Zahlenraten-Spiel  -  GERÜST zum selbst Ausfüllen
# =====================================================
#
#  So funktioniert das Spiel:
#  Der Computer denkt sich eine geheime Zahl aus (z.B. zwischen 1 und 100).
#  Du musst raten. Nach jedem Versuch sagt das Programm
#  "zu hoch" oder "zu tief", bis du die Zahl triffst.
#
#  Deine Aufgabe: Fülle die Funktionen unten aus.
#  Über jeder Funktion steht als Kommentar, was sie tun soll.
#  Tipp: Bau eine Funktion nach der anderen und teste zwischendurch!
# =====================================================


# random ist ein "Werkzeugkasten" von Python,
# mit dem man Zufallszahlen erzeugen kann. Den brauchen wir gleich.
import random


# -----------------------------------------------------
# Funktion 1: geheime Zahl erzeugen
# -----------------------------------------------------
# Diese Funktion soll eine zufällige Zahl zwischen 1 und 100
# auswürfeln und zurückgeben.
# Tipp: random.randint(1, 100) gibt dir eine Zufallszahl von 1 bis 100.
def geheime_zahl_erzeugen():
    # TODO: Zufallszahl erzeugen und mit "return" zurückgeben
    pass


# -----------------------------------------------------
# Funktion 2: den Spieler nach einer Zahl fragen
# -----------------------------------------------------
# Diese Funktion soll den Spieler fragen "Welche Zahl rätst du?"
# und die eingegebene Zahl zurückgeben.
# Tipp 1: input("Text") zeigt eine Frage und liest die Eingabe ein.
# Tipp 2: input() gibt immer TEXT zurück. Mit int(...) machst du
#         daraus eine echte Zahl, mit der man rechnen kann.
def spieler_fragen():
    # TODO: Den Spieler fragen, Eingabe in eine Zahl umwandeln und zurückgeben
    pass


# -----------------------------------------------------
# Funktion 3: Tipp geben
# -----------------------------------------------------
# Diese Funktion bekommt zwei Zahlen: den Tipp des Spielers
# und die geheime Zahl. Sie soll auf den Bildschirm schreiben:
#   - "Zu tief!"  wenn der Tipp kleiner als die geheime Zahl ist
#   - "Zu hoch!"  wenn der Tipp größer als die geheime Zahl ist
#   - "Richtig!"  wenn beide gleich sind
# Tipp: Hier brauchst du if / elif / else.
def tipp_geben(tipp, geheim):
    # TODO: Vergleiche tipp und geheim und gib den passenden Text aus (print)
    pass


# -----------------------------------------------------
# Hauptprogramm - hier läuft das Spiel ab
# -----------------------------------------------------
# Ablauf:
#   1. Geheime Zahl erzeugen (Funktion 1 benutzen)
#   2. So lange wiederholen, bis der Spieler richtig geraten hat:
#        - Spieler nach einer Zahl fragen (Funktion 2)
#        - Tipp geben (Funktion 3)
#        - Mitzählen, wie viele Versuche es waren
#   3. Am Ende ausgeben, wie viele Versuche gebraucht wurden
def spiel_starten():
    print("Willkommen beim Zahlenraten!")
    print("Ich denke an eine Zahl zwischen 1 und 100.")

    # TODO 1: geheime Zahl erzeugen und in einer Variablen speichern

    # TODO 2: einen Zähler für die Versuche bei 0 starten

    # TODO 3: Schleife bauen, die wiederholt, bis richtig geraten wurde
    #         (Tipp: while-Schleife)
    #         In der Schleife:
    #           - Spieler fragen
    #           - Versuche-Zähler um 1 erhöhen
    #           - Tipp geben
    #           - prüfen, ob der Tipp gleich der geheimen Zahl ist -> dann aufhören

    # TODO 4: am Ende ausgeben, wie viele Versuche gebraucht wurden
    pass


# Diese Zeile sorgt dafür, dass das Spiel startet,
# wenn man die Datei ausführt. Lass sie einfach so stehen.
if __name__ == "__main__":
    spiel_starten()
