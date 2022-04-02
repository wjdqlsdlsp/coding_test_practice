import sys
import math
n = int(sys.stdin.readline())
s = list(sys.stdin.readline().split()[0])

h_p = []
e_p = 0
result = 0

def comb(n, t):
    return math.factorial(n) // math.factorial(n-t) //math.factorial(t) 

for i, v in enumerate(s[::-1]):
    if v == 'W':
        for j in h_p:
            for k in range(2, j+1):
                result+=comb(j,k)
        e_p = sum(h_p)

    elif v == 'H':
        h_p.append(e_p)
        e_p=0
    elif v == 'E':
        e_p+=1

result = result % 1000000007
print(result)
