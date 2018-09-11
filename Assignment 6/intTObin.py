my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code
bstr= ""

if my_int < 0:
    print("Number should be 0 or higher. Try again")
    my_int = int(input('Give me an int >= 0: '))
else:
    numb = my_int
    while numb > 0:
    #bstr = '{0:b}'.format(my_int)
        n = numb % 2
        bstr += str(n)
        numb //= 2
    if bstr == "":
        bstr = "0"


    print("The binary of", my_int, "is", bstr[::-1])



