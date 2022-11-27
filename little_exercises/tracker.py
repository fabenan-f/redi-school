
anzahlDerLäufeAlsText = input("Wie häufig warst du laufen? ")
anzahlDerLäufeAlsZahl = int(anzahlDerLäufeAlsText)

zeitInsgesamt= 0

for i in range(anzahlDerLäufeAlsZahl):
    zeitAlsText = input("Was war deine Zeit in Minuten beim " + str(i + 1) + ". Lauf? ")
    zeitAlsZahl = int(zeitAlsText)

    zeitInsgesamt = zeitInsgesamt + zeitAlsZahl


durchschnitt = zeitInsgesamt / anzahlDerLäufeAlsZahl
print("Du hast durchschnittlich " + str(durchschnitt) + " min gebraucht")
