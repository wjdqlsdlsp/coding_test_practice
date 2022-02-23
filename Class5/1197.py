import sys
n,m = map(int, sys.stdin.readline().split())
arr = []

for i in range(m):
    arr.append([*map(int, sys.stdin.readline().split())])
arr = sorted(arr, key=lambda x: x[2])
parent = [i for i in range(0, n+1)]
total_weight = 0
num = 0

def find(x):
    if x==parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x, y = find(x), find(y)
    if x!= y:
        parent[y] = x

for i in arr:
    start, end, weight = i
    if find(start) == find(end):
        continue
    else:
        total_weight += weight
        union(start,end)
        num+=1

    if num == n-1:
        break
print(total_weight)