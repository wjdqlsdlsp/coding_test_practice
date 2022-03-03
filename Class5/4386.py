import sys
from itertools import combinations
N = int(sys.stdin.readline())

arr = [[i+1] + [*map(float, sys.stdin.readline().split())] for i in range(N)]
roots = []
for i in [*combinations(arr, 2)]:
    p1, p2 = i
    roots.append([p1[0], p2[0], ((p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)**0.5])

roots = sorted(roots, key=lambda x : x[2])
parent = [i for i in range(N+1)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b= find(b)
    if a< b:
        parent[b] = a
    else:
        parent[a]= b

result = 0
for root in roots:
    a, b, c = root
    if find(a) == find(b):
        continue
    union(a,b)
    result += c

print(round(result, 2))