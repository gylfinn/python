top_num = int(input("Upper number for the range: ")) # Do not change this line

for i in range(1, top_num-1):
    isperf = 0
    for p in range(1 ,i-1):
        if i % p == 0:
            isperf += p
    if(isperf==i):
        print(isperf)