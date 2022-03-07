import sys

n, m = map(int, sys.stdin.readline().split())

parents = [i for i in range(n)]

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a, b = find(a), find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


for i in range(1, m+1):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) == find(b):
        print(i)
        break

    union(a,b)
else:
    print(0)