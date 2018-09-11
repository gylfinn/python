s = input("Input a string: ")
s = s.lower()

for count,l in enumerate(s,0):
    if l == 'o':
        print(count)
