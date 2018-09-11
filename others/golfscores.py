number_of_hole = 1
score = 0



while number_of_hole <= 18:
    par_of_hole = int(input("Par of hole " + str(number_of_hole) + ": "))
    score_on_hole = int(input("Score on hole " + str(number_of_hole) + ": "))

    score = score_on_hole - par_of_hole
    if score == 1:
        print("bogey")
    elif score == 2:
        print("double bogey")
    elif score == 3:
        print("triple bogey")
    elif score >= 4:
        print("bad hole")
    elif score == -1:
        print("birdie")
    elif score == -2:
        print("eagle")
    elif score == -3:
        print("albatross")
    elif score <= -4:
        print("invalid score")
    else:
        print("par")

    number_of_hole += 1




