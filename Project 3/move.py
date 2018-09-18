Keep_Playing = True
def check_pos(pos):
    VALUES = [1,2,3,4,5,6,7,8,9,10]
    
    pos = int(pos)
    for i in VALUES:
        if i == pos:
            return True
    else:
        return False


pos = input("Input a position between 1 and 10: ")
while Keep_Playing:
    is_pos = check_pos(pos)
    if is_pos:
        pos = int(pos)
        print("l - for moving left")
        print("r - for moving right")
        print("Any other letter for quitting")
        choice = input("Input your choice: ")
        if choice == "l":
            pos -= 1
            if pos == 0:
                pos = 1
            print("New position is: " + str(pos))
        elif choice == "r":
            pos += 1
            if pos == 11:
                pos = 10
            print("New position is: " + str(pos))
        else:
            print("New position is: " + str(pos))
            Keep_Playing = False

    else:
        print("ERROR in INPUT")
        Keep_Playing = False


#def moving_char(pos, choice):
#print("l - for moving left")
#print("r - for moving right")
#print("Any other letter for quitting")
#choice = input("Input your choice: ")

