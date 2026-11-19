import random

ord_lista = [
    "äpple", "bil", "dator", "hund", "katt",
    "hus", "skola", "bok", "telefon", "bord",
    "stol", "fönster", "dörr", "cykel", "glass",
    "sol", "måne", "stjärna", "hav", "skog",
    "blomma", "träd", "gräs", "vatten", "eld",
    "snö", "regn", "vind", "moln", "berg",
    "springa", "hoppa", "simma", "skriva", "läsa",
    "spela", "sjunga", "dansa", "tänka", "prata",
    "glad", "ledsen", "snabb", "långsam", "stor",
    "liten", "rolig", "svår", "enkel", "vacker"
]

ordet = random.choice(ord_lista)
rätt = ["*"] * len(ordet)
Gissat = []
Fel_gissningar = []
j = 0

while True:
    gissning = input(f"Säg en bokstav! ({j}/10 fel försök) ---> ").lower()
    print("Fel gissningar:", ", ".join(Fel_gissningar).upper())

    if gissning in Gissat:
        print("Du har redan gissat den bokstaven!")
        continue

    elif gissning not in Gissat:
        Gissat.append(gissning)

    if len(gissning) != 1 or not gissning.isalpha():
        print("Skriv en bokstav!")
        continue
    if gissning in ordet:
        for i in range(len(ordet)):
            if ordet[i] == gissning:
                rätt[i] = gissning

    else:
        j += 1
        Fel_gissningar.append(gissning)
        print("Fel bokstav!")

    print("".join(rätt).upper())

    if "*" not in rätt:
        print("Grattis! Du vann!")
        fråga = input("Vill du spela igen? (j/n) ---> ").lower()

    elif j >= 10:
        print("Du förlorade! Ordet var:", ordet.upper())
        fråga = input("Vill du spela igen? (j/n) ---> ").lower()

    else:
        continue

    if fråga == "j":
        ordet = random.choice(ord_lista)
        rätt = ["*"] * len(ordet)
        j = 0
    else:
        print("Tack för att du spelade!")
        break
