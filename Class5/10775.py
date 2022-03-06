import sys

G = int(sys.stdin.readline())
P = int(sys.stdin.readline())

gate = [False]+ [True for i in range(G)]
parent = [i for i in range(G+1)]
result = 0

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[a] = b


for i in range(P):
    p = int(sys.stdin.readline())
    par = find(p)
    if par == 0:
        break
    
    else:
        result +=1
        union(par, par-1)

print(result)