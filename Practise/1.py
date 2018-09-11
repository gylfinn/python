while True:
    try:
        tala1 = int(input("Sláðu inn tölu 1: "))
        tala2 = int(input("Sláðu inn tölu 2: "))
    except ValueError:
        print("Þú þarft að slá inn tölu")
        continue
    else:
         sum = tala1+tala2
         print("Summa talnanna er: " + str(sum))
         break
