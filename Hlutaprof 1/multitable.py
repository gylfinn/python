teljari = 1

first_str = ""
second_str = ""
third_str = ""
fourth_str =""
fifth_str =""
sixth_str =""
seventh_str = ""
eight_str =""
ninth_str=""
tenth_str =""



while teljari <= 10:
    first_str += str((1*teljari)).rjust(5)
    second_str += str((2*teljari)).rjust(5)
    third_str += str((3*teljari)).rjust(5)
    fourth_str += str((4*teljari)).rjust(5)
    fifth_str += str((5*teljari)).rjust(5)
    sixth_str += str((6*teljari)).rjust(5)
    seventh_str += str((7*teljari)).rjust(5)
    eight_str += str((8*teljari)).rjust(5)
    ninth_str += str((9*teljari)).rjust(5)
    tenth_str += str((10*teljari)).rjust(5)
    teljari += 1


print(first_str)
print(second_str)
print(third_str)
print(fourth_str)
print(fifth_str)
print(sixth_str)
print(seventh_str)
print(eight_str)
print(ninth_str)
print(tenth_str)