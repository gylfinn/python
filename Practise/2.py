while True:
    try:
        tala1 = int(input("Sláðu inn tölu 1: "))
        tala2 = int(input("Sláðu inn tölu 2: "))
        tala3 = int(input("Sláðu inn tölu 3: "))
    except ValueError:
        print("Þú þarft að slá inn tölu\n Byrjum aftur")
        continue
    else:
         sum = tala1+tala2+tala3
         print("Summa talnanna er: " + str(sum))
         break
