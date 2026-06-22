
import random


def geheime_zahl_erzeuge():

    return random.randint(1, 100)



def spieler_fragen():
    eingabe = input("Welche zahl rätst du?")
    zahl = int(eingabe)
    return zahl



def tipp_geben(tipp, geheim):
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
    while True :
        tipp = spieler_fragen()
        versuche = versuch + 1
        versuch = versuche
        tipp_geben(tipp, geheim)
        if tipp == geheim:
            break


    print("geschafft! du hast " + str(versuche) + " versuche gebraucht")



    pass



if __name__ == "__main__":
    spiel_starten()
