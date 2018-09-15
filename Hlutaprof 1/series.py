initial_gildi = int(input("Initial value: "))
mismunur = int(input("Step: "))

summa = 0
summu_str = ""
while summa <= 100:
    summu_str += str(initial_gildi) + " "
    summa += initial_gildi
    initial_gildi += mismunur
print(summu_str)
print("Sum of series: " + str(summa))
    