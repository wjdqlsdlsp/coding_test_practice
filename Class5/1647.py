import sys
from collections import Counter
n, m = map(int, sys.stdin.readline().split())

roots = [i for i in range(0, n+1)]

arr = []
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    arr.append([a,b,cost])

arr = sorted(arr, key = lambda x : x[2])
result = 0

def find(num):
    if roots[num] == num:
        return num
    roots[num] = find(roots[num])
    return roots[num]


def union(a,b):
    a = find(a)
    b = find(b)

    if a > b:
        roots[a] = b
    else:
        roots[b] = a

last = 0

for a,b,cost in arr:
    if n == 2:
        break
    if find(a) == find(b):
        continue
    else:
        union(a,b)
        result += cost
        last = cost
print(result - last)
