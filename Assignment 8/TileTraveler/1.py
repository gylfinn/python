#Forritið keyrir á meðan hún er True. Starting position er 1.1, forritið athugar hvar þú getur farið,
#ef þú ferð vitlaust þá lætur forritið þig vita, ef þú ferð á reit sem þú mátt fara þá færist þú. 
#Ef þú lendir á 3.1 þá sigraru og forritið hættur keyrslu


x = 1
y = 1
Keep_Playing = True

print("You can travel: (N)orth.")
while Keep_Playing:
    if x == 3 and y == 1:
        print("Victory!")
        Keep_Playing = False

    elif x == 1 and y == 1:
        move = input("Direction: ")
        move = move.lower()
        if move == "n":
            x = 1
            y = 2
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        else:
            print("Not a valid direction!")
    elif x == 1 and y == 2:
        move = input("Direction: ")
        move = move.lower()
        if move == "n":
            x = 1
            y = 3
            print("You can travel: (E)ast or (S)outh.")
        elif move == "e":
            x = 2
            y = 2
            print("You can travel: (W)est or (S)outh.")
        elif move == "s":
            x = 1
            y = 1
            print("You can travel: (N)orth.")
        else:
            print("Not a valid direction!")
            move = input("Direction: ")
            move = move.lower()
    elif x == 1 and y == 3:
        move = input("Direction: ")
        move = move.lower()
        if move == "e":
            x = 2
            y = 3
        elif move == "s":
            x = 1
            y = 2
            
        else:
            print("Not a valid direction!")
            move = input("Direction: ")
            move = move.lower()
    elif x == 2 and y == 1:
        print("You can travel: (N)orth.")
        move = input("Direction: ")
        move = move.lower()
        if move == "n":
            x = 2
            y = 2
            print("You can travel: (W)est or (S)outh.")
        else:
            print("Not a valid direction!")
    elif x == 2 and y == 2:
        move = input("Direction: ")
        move = move.lower()
        if move == "w":
            x = 1
            y = 2
        elif move == "s":
            x = 2
            y = 1
        else:
            print("Not a valid direction!")
            move = input("Direction: ")
            move = move.lower()
    elif x == 2 and y == 3:
        print("You can travel: (E)ast or (W)est.")
        move = input("Direction: ")
        move = move.lower()
        if move == "w":
            x = 1
            y = 3
        elif move == "e":
            x = 3
            y = 3
        else:
            print("Not a valid direction!")
            move = input("Direction: ")
            move = move.lower()
    elif x == 3 and y == 3:
        print("You can travel: (S)outh or (W)est.")
        move = input("Direction: ")
        move = move.lower()
        if move == "w":
            x = 2
            y = 3
        elif move == "s":
            x = 3
            y = 2
            print("You can travel: (N)orth or (S)outh.")
        else:
            print("Not a valid direction!")
            move = input("Direction: ")
            move = move.lower()
    elif x == 3 and y == 2:
        move = input("Direction: ")
        move = move.lower()
        if move == "n":
            x = 3
            y = 3
        elif move == "s":
            x = 3
            y = 1
        else:
            print("Not a valid direction!")
            move = input("Direction: ")
            move = move.lower()