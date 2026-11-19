import random

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
rätt = ["*"] * len(ordet)
Gissat = []
Fel_gissningar = []
j = 0

while True:
    print("Fel gissningar:", ", ".join(Fel_gissningar).upper())
    gissning = input(f"Säg en bokstav! ({j}/10 fel försök) ---> ").lower().replace(" ", "")

    if len(gissning) != 1 or not gissning.isalpha():
        print("Skriv en bokstav!")
        continue
    if gissning in ordet:
        for i in range(len(ordet)):
            if ordet[i] == gissning:
                rätt[i] = gissning
    if gissning in Gissat:
        print("Du har redan gissat den bokstaven!")
        print("".join(rätt).upper())
    
        continue
        
    if gissning not in Gissat:
        Gissat.append(gissning)

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
        rätt = ["*"] * len(ordet)
        j = 0
        Gissat = []
        Fel_gissningar = []
    else:
        print("Tack för att du spelade!")
        break
