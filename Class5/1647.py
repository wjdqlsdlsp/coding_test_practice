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
now = n

def find(num):
    if roots[num] == num:
        return num
    roots[num] = find(roots[num])
    global now
    now-=1
    return roots[num]


def union(a,b):
    p_a = find(a)
    p_b = find(b)

    if p_a > p_b:
        roots[p_a] = p_b
    else:
        roots[p_b] = p_a



for a,b,cost in arr:
    if n == 2:
        break
    if find(a) == find(b):
        continue
    else:
        union(a,b)
        now-=1
        result += cost

print(result)
