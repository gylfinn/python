sentence = str(input("Enter a sentence: "))

upper_case = 0
lower_case = 0
digits = 0
punctuation = 0

for char in sentence:
    if char.isupper():
        upper_case+=1
    elif char.islower():
        lower_case+=1
    elif char.isdigit():
        digits+=1
    elif char == "," or char == "." or char == '"' or char == "'" or char == "-":
        punctuation+=1




print("Upper case ".rjust(15) + str(upper_case).rjust(5))
print("Lower case ".rjust(15) + str(lower_case).rjust(5))
print("Digits ".rjust(15) + str(digits).rjust(5))
print("Punctuation ".rjust(15) + str(punctuation).rjust(5))