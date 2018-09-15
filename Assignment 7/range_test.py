# The function definition goes here
def range(num):
    if num > 1 and num < 555:
        return True
    else:
        return False




num = int(input("Enter a number: "))

# You call the function here
number_check = range(num)

if number_check:
    print(str(num) + " is in range!")
else:
    print(str(num) + " is outside the range!")