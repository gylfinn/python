# Your function definition goes here
def isFibo(n):
    a,b = 0,1
    fibo_str = ""
    for i in range(n):
        fibo_str += str(b) + " "
        a,b = b,a+b
    return fibo_str
n = int(input("Input the length of Fibonacci sequence (n>=1): "))

FiboSeq = isFibo(n)
print(FiboSeq) 
