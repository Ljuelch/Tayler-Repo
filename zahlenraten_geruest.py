
import random


def geheime_zahl_erzeuge():
    # TODO: Zufallszahl erzeugen und mit "return" zurückgeben
    return random.randint(1, 100)



def spieler_fragen():
    eingabe = input("Welche zahl rätst du?")
    zahl = int(eingabe)
    return zahl



def tipp_geben(tipp, geheim):
    # TODO: Vergleiche tipp und geheim und gib den passenden Text aus (print)
    if tipp < geheim:
        print("die zahl ist größer")
    elif tipp > geheim:
        print("die zahl ist kleiner")
    else:
        print("die zahl ist Richtig")

def spiel_starten():
    print("Willkommen beim Zahlenraten!")
    print("Ich denke an eine Zahl zwischen 1 und 100.")
    geheim = geheime_zahl_erzeuge()
    versuch = 0

    # TODO 1: geheime Zahl erzeugen und in einer Variablen speichern

    # TODO 2: einen Zähler für die Versuche bei 0 starten
    while True :

        tipp = spieler_fragen()
        versuche = versuch + 1
        versuch = versuche
        tipp_geben(tipp, geheim)
        if tipp == geheim:
            break


    print("geschafft! du hast " + str(versuche) + " versuche gebraucht")


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
