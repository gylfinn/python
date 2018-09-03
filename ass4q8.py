stars = int(input("Max number of stars: ")) # Do not change this line


string1=""
for num in range(1,stars+1):
    for i in str(num):
        string1 += "*"
        print(string1)
for num in range(stars-1, 0, -1):
    for i in range(num-1, 0, -1):
        print("*", end="")
    print("*")