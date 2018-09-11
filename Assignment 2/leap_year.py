year = int(input("Input a year: ")) # Do not change this line

# Fill in the missing code below

is_leap_year = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
    else:
        is_leap_year = True
print(is_leap_year)
