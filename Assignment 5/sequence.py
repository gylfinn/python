n = int(input("Enter the length of the sequence: ")) # Do not change this line

teljari = 0

num1 = 1
num2 = 2
num3 = 3

num2temp = 0
num3temp = 0

while n > teljari:

    print(num1)

    num3temp = num3
    num2temp = num2
    
    num3 = num1 + num2 + num3
    num2 = num3temp
    num1 = num2temp

    teljari += 1

