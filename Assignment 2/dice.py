d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line
dice_sum = 0
# Fill in the missing code below
dice_sum = d1 + d2

if d1 > 6 or d1 < 1 or d2 > 6 or d2 < 1:
    print("Invalid input")
elif dice_sum == 7 or dice_sum == 11:
    print("Winner")
elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
    print("Loser")
else:
    print(dice_sum)
    
