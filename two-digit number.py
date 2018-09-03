n = 11
i = 0
while n <= 31:
    i = n**2
    if str(n) in str(i):
        print(n)
    n = n+1