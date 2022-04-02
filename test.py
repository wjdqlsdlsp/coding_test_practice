import math

def comb(n, t):
    return math.factorial(n) // math.factorial(n-t) //math.factorial(t)

print(comb(5,3))  