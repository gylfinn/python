def celsius_to_fahrenheit(c):
    return c * 1.8 + 32.0


def Func(x):
    total = 0
    for i in range(x):
        total += i * (i-1)
    return total

print(Func(4))


