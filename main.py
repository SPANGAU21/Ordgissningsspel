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
rätt = ["*"]*len(ordet)
j = 0

<<<<<<< HEAD
while j <= 10:
    gissning = input(f"Säg en bokstav! ({j}/10 försök kvar) ---> ").lower()  
=======
while True:
    gissning = input(f"Säg en bokstav! ({j}/10 fel försök kvar) ---> ").lower()  
    if len(gissning) != 1 or not gissning.isalpha():
        continue
>>>>>>> c13668b20eedfed18dc80fd2bee5b575d35dfff2
    if gissning in ordet:
        for i in range(len(ordet)):
            if ordet[i].lower() == gissning:
                rätt[i] = ordet[i]
    else:
        j += 1
        if j == 10:
            print(f"Du har förlorat! Ordet var: {ordet.upper()}")
            fråga = input("Vill du spela igen? (j/n) ---> ").lower()
            if fråga == "j":
                ordet = random.choice(ord_lista)
                rätt = ["*"]*len(ordet)
                j = 0
            else:
                print("Tack för att du spelade!")
                break
    print("".join(rätt).upper())
<<<<<<< HEAD
    j += 1
print("Du förlorade!")
=======
>>>>>>> c13668b20eedfed18dc80fd2bee5b575d35dfff2
