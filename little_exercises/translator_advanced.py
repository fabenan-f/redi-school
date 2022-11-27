wort = input("Welches Wort willst du in die Löffelsprache übersetzt haben? ")

übersetzung = ""

for i in range(len(wort)):
    
    if wort[i] in "aei" and (i + 1) < len(wort):
        if wort[i] == "a" and wort[i + 1] == "u":
            übersetzung += "aulewau"
        elif wort[i] == "e" and wort[i + 1] == "i":
            übersetzung += "eilewei"
        elif wort[i] == "i" and wort[i + 1] == "e":
            übersetzung += "ielewie"
        else:
            übersetzung += wort[i] + "lew" + wort[i]
    elif wort[i] in "uie":
        if wort[i] == "u" and wort[i - 1] == "a":
            continue
        elif wort[i] == "i" and wort[i - 1] == "e":
            continue
        elif wort[i] == "e" and wort[i - 1] == "i":
            continue
        else:
            übersetzung += wort[i] + "lew" + wort[i]
    elif wort[i] in "aeiouäöü":
        übersetzung += wort[i] + "lew" + wort[i]
    else:
        übersetzung += wort[i]


print("Übersetzung: " + übersetzung)
