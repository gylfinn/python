# is_prime function definition goes here

def isPrime(num):
    i = 2
    prime = True
    while i<num:
        if num % i == 0:
            prime = False
        i = i+1
    if not prime:
        return False
    else:
        return True


num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message

prime = isPrime(num)
if not prime:
    print(str(num) + " is not a prime")
else:
    print(str(num) + " is a prime")