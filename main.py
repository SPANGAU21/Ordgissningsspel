ordet = "banan"

rätt = ["_"]*len(ordet)

while True:
    gissning = input("Säg en bokstav! ---> ").lower()  
    if gissning in ordet:
        for i in range(len(ordet)):
            if ordet[i].lower() == gissning:
                rätt[i] = ordet[i]
    print("".join(rätt).upper())