import random
import string

print("### WILLKOMMEN BEI DEINEM PERSÖNLICHEN PASSWORT GENERATOR ###")

anzahlDerKleinbuchstaben = int(input("Wie viele Kleinbuchstaben soll dein Passwort beinhalten? "))
anzahlDerGroßbuchstaben = int(input("Wie viele Großbuchtstaben soll dein Passwort beinhalten? "))
anzahlDerZahlen = int(input("Wie viele Zahlen soll dein Passwort beinhalten? "))
sonderzeichen = input("Welche Sonderzeichen soll dein Passwort enthalten? ")

passwort = [] + list(sonderzeichen)
passwort += random.choices(string.ascii_lowercase, k=anzahlDerKleinbuchstaben)
passwort += random.choices(string.ascii_uppercase, k=anzahlDerGroßbuchstaben)
passwort += random.choices(string.digits, k=anzahlDerZahlen)

random.shuffle(passwort)
print("Hier ist dein Passwort: " + "".join(passwort))
