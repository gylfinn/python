s = input("Input a string: ")

numberStr = ""

for char in s:
    if char.isdigit():
        numberStr+=char
print(numberStr)