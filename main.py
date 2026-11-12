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
    "liten", "rolig", "svår", "enkel", "vacker"]
ordet = random.choice(ord_lista)
rätt = ["_"]*len(ordet)

while True:
    gissning = input("Säg en bokstav! ---> ").lower()  
    if gissning in ordet:
        for i in range(len(ordet)):
            if ordet[i].lower() == gissning:
                rätt[i] = ordet[i]
    print("".join(rätt).upper())