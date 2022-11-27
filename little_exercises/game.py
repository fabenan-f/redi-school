import random

optionen = ["Schere", "Stein", "Papier"]

# erst wählt der Spieler eine Option
while True:
    spieler = input("Schere, Stein, Papier! Was wählst du? ")
    # hat der Spieler was sinnvolles geschrieben?
    if spieler in optionen:
        break
    else:
        print("Das ist keine Option! Du musst entweder Schere, Stein oder Papier auswählen.")

# nun wählt der Computer zufällig
computer = random.choice(optionen)
print(f"Computer hat {computer} ausgewählt!")
# was ist das Ergebnis?
if spieler == "Stein" and computer == "Schere":
    print("Spieler gewinnt!")
elif spieler == "Papier" and computer == "Stein":
    print("Spieler gewinnt!")
elif spieler == "Schere" and computer == "Papier":
    print("Spieler gewinnt!")
elif computer == "Stein" and spieler == "Schere":
    print("Computer gewinnt!")
elif computer == "Papier" and spieler == "Stein":
    print("Computer gewinnt!")
elif computer == "Schere" and spieler == "Papier":
    print("Computer gewinnt!")
else:
    print("Niemand gewinnt.")

