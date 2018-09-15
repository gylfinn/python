#number = 0x9b
#isOdd = number & 0x01
#if isOdd:
#    print(str(number) + " is odd number")
#else:
#    print(str(number) + " is even number")


number = 0x7d9a
print(number)
# 0x7d9a == 0111 1101 1001 1010
#                    qqq q
#                aa

#qqqq = 1100
#aa = 11


#   0111 1101 1001 1010
#   0000-0001-1000-0000
#   0000 0000 0000 1100
#0x0180

#   0111 1101 1001 1010
#   0000 1100 0000 0000
#0x0C00

#0x7d9a = 
0x0C00 >> 10