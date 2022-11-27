wort = input("Welches Wort willst du in die Löffelsprache übersetzt haben? ")

übersetzung = ""

for buchstabe in wort:
    if buchstabe in "aeiouäöü":
        übersetzung += buchstabe + "lew" + buchstabe
    else:
        übersetzung += buchstabe

print("Übersetzung: " + übersetzung)
