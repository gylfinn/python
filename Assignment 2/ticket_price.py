age = int(input("Input age: ")) # Do not change this line
# Fill in the missing code below


ticketprice = float(30)
senior = False
children = False

if age >= 65:
    senior = True
elif age <= 5:
    children = True

if senior:
    ticketprice = ticketprice / 2
elif children:
    ticketprice = ticketprice * 0

print(ticketprice)
