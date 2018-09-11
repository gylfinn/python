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