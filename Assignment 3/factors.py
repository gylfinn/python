n = int(input("Input an int: ")) # Do not change this line
# Fill in the missing code below
factor_int = 1

while factor_int <= n:
    if n % factor_int == 0:
        print(factor_int)
    factor_int += 1