top_num = int(input("Input a number between 0 and 999: "))


for num in range(0, top_num):
    if num >= 100:
        tala1 = num // 100
        tala2 = (num % 100) // 10
        tala3 = (num % 100) % 10
        if ((tala1**3)+(tala2**3)+(tala3**3)) == num:
            print(num)

    elif num < 10:
        num**1==num
        print(num)
    else:
        tala1 = num // 10
        tala2 = num % 10
        if ((tala1**2)+(tala2**2)) == num:
            print(num)

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
""" order = len(str(num))
    
 
   sum = 0

 
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
"""