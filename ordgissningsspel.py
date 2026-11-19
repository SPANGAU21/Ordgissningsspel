import random

# Skapar två listor med ord, en för lätta ord och en för svåra ord
lätta_ord = [
    "bil", "hus", "hund", "katt", "sol", "bok", "mat", "glass",
    "stol", "bord", "sko", "boll", "fisk", "träd", "blomma",
    "skola", "dator", "mobil", "cykel", "fönster", "dörr",
    "måne", "stjärna", "hav", "skog", "regn", "snö", "vind",
    "klocka", "penna", "papper", "nyckel", "väska", "jacka",
    "mössa", "handske", "lampa", "spegel", "tavla", "soffa",
    "säng", "kudde", "tårta", "pizza", "banan", "äpple",
    "päron", "orange", "tomat", "potatis", "morot", "gurka"
]
svåra_ord = [
    "elektricitet", "astronomi", "arkitektur", "programmering",
    "laboratorium", "demokrati", "civilisation", "experiment",
    "psykologi", "filosofi", "teknologi", "geografi",
    "meteorologi", "konstellation", "gravitation", "infrastruktur",
    "kommunikation", "innovation", "perspektiv", "imagination",
    "komplikation", "observation", "hypotes", "parallell",
    "symmetri", "karaktär", "strategi", "analys",
    "konstruktion", "organisation", "administration",
    "entreprenör", "ekosystem", "biologisk", "kristallisation",
    "universum", "atmosfär", "kontinent", "demonstration",
    "kategorisering", "individualism", "revolution",
    "mysterium", "labyrint", "schackmästare", "självständighet",
    "överenskommelse", "förutsättning", "tillväxt",
    "samhällsutveckling", "frekvens"
]
while True:
    try:
        # Fråga användaren om svårighetsgrad och välj ett ord baserat på det
        svårighetsgrad = input("Välj svårighetsgrad (lätt/svår): ").lower().replace(" ", "")
        # Ger användaren ett ord från den lätta listan
        if svårighetsgrad == "lätt":
            ordet = random.choice(lätta_ord)
            print("Du har valt lätt svårighetsgrad!")
            break
        # Ger användaren ett ord från den svåra listan
        elif svårighetsgrad == "svår":
            ordet = random.choice(svåra_ord)
            print("Du har valt svår svårighetsgrad!")
            break
        # Om användaren inte väljer en giltig svårighetsgrad, skriv ut ett felmeddelande och detta loopar tills användaren väljer en giltig svårighetsgrad
        else:
            print("Välj en giltig svårighetsgrad (lätt/svår)!")
    # Om ett fel uppstår, skriv ut ett felmeddelande och detta loopar tills användaren väljer en giltig svårighetsgrad
    except Exception as e:
        print("Ett fel uppstod, försök igen!")
# Skapar en lista med "*" lika lång som ordet som ska gissas, samt listor för gissade bokstäver och felaktiga gissningar
rätt = ["*"] * len(ordet)
Gissat = []
Fel_gissningar = []
j = 0

# Loop som kör spelet tills användaren vinner eller förlorar
while True:
    # Skriv ut felaktiga gissningar och ber användaren att gissa en bokstav
    print("Fel gissningar:", ", ".join(Fel_gissningar).upper())
    gissning = input(f"Säg en bokstav! ({j}/10 fel försök) ---> ").lower().replace(" ", "")

    # Kontrollera om användaren redan har gissat bokstaven, om inte lägg till den i listan över gissade bokstäver
    if gissning in Gissat:
        print("Du har redan gissat den bokstaven!")
        print("".join(rätt).upper())
        continue

    # Ifall användaren inte har gissat bokstaven tidigare, lägg till den i listan över gissade bokstäver
    elif gissning not in Gissat:
        Gissat.append(gissning)

    # Kontrollera om användaren har gissat en giltig bokstav, om inte skriv ut ett felmeddelande och fortsätt loopen
    if len(gissning) != 1 or not gissning.isalpha():
        print("Skriv en bokstav!")
        continue

    # Kontrollera om gissningen finns i ordet, om ja, uppdatera listan med rätt gissningar, annars öka antalet felaktiga gissningar och lägg till bokstaven i listan över felaktiga gissningar
    if gissning in ordet:
        for i in range(len(ordet)):
            if ordet[i] == gissning:
                rätt[i] = gissning

    # Om gissningen inte finns i ordet, öka antalet felaktiga gissningar och lägg till bokstaven i listan över felaktiga gissningar
    else:
        j += 1
        Fel_gissningar.append(gissning)
        print("Fel bokstav!")

    # Skriv ut listan med rätt gissningar
    print("".join(rätt).upper())

    # Kontrollera om användaren har vunnit eller förlorat, och fråga om de vill spela igen
    if "*" not in rätt:
        print("Grattis! Du vann!")
        fråga = input("Vill du spela igen? (j/n) ---> ").lower()

    # Om användaren har gjort 10 felaktiga gissningar, skriv ut att de förlorade och visa det korrekta ordet, samt fråga om de vill spela igen
    elif j >= 10:
        print("Du förlorade! Ordet var:", ordet.upper())
        while True:
            fråga = input("Vill du spela igen? (j/n) ---> ").lower().replace(" ", "")
            if fråga in ["j", "n"]:
                break
            else:
                print("Välj ett giltigt alternativ (j/n)!")

    else:
        continue

    # Om användaren vill spela igen, fråga om de vill ändra svårighetsgrad och starta om spelet med det nya ordet och nollställda variabler
    if fråga == "j":
        ändra_svårighetsgrad = input("Vill du ändra svårighetsgrad? (j/n) ---> ").lower().replace(" ", "")
        if ändra_svårighetsgrad == "j":
            while True:
                try:
                    svårighetsgrad = input("Välj svårighetsgrad (lätt/svår): ").lower().replace(" ", "")

                    if svårighetsgrad == "lätt":
                        ordet = random.choice(lätta_ord)
                        print("Du har valt lätt svårighetsgrad!")
                        break

                    elif svårighetsgrad == "svår":
                        ordet = random.choice(svåra_ord)
                        print("Du har valt svår svårighetsgrad!")
                        break

                    else:
                        print("Välj en giltig svårighetsgrad (lätt/svår)!")

                except Exception as e:
                    print("Ett fel uppstod, försök igen!")
        elif ändra_svårighetsgrad == "n":
            if svårighetsgrad == "lätt":
                ordet = random.choice(lätta_ord)
            elif svårighetsgrad == "svår":
                ordet = random.choice(svåra_ord)
        rätt = ["*"] * len(ordet)
        j = 0
        Gissat = []
        Fel_gissningar = []
    else:
        print("Tack för att du spelade!")
        break
