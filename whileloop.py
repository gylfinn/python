#1
num = int(input("Input an int: ")) # Do not change this line
counter = 1

while counter < num:
    print(counter)
    counter += 1





#2
num = int(input("Input an int: ")) # Do not change this line
counter = 0
oddatala = 1
while counter < num:
    print(oddatala)
    oddatala += 2
    counter += 1




#3 
samtalstala = 0
num = 0
while num != 10:
    samtalstala += num
    num = int(input("Input an int: ")) # Do not change this line
   
else:
    print(samtalstala)



#4
n = int(input("Input an int: ")) # Do not change this line
# Fill in the missing code below
factor_int = 1

while factor_int <= n:
    if n % factor_int == 0:
        print(factor_int)
    factor_int += 1


#5
n = int(input("Input a natural number: ")) # Do not change this line
prime = True
# Fill in the missing code below
i = 2
while i<n:
    if n % i == 0:
        prime = False
    i = i+1
# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("!Prime")




