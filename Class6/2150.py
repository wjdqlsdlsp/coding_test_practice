import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
v,e = map(int, sys.stdin.readline().split())
roots = defaultdict(list)
backroots = defaultdict(list)

visited = [0]*(v+1)
s = []
for _ in range(e):
    a, b = map(int, sys.stdin.readline().split())
    roots[a].append(b)
    backroots[b].append(a)

def dfs(now):
    if visited[now]:
        return 
    visited[now] = 1
    for i in roots[now]:
        dfs(i)
    s.append(now)

def backdfs(now):
    global arr
    arr.append(now)
    visited[now] = 1

    for i in backroots[now]:
        if visited[i]:
            continue
        backdfs(i)

for i in range(1, v+1):
    dfs(i)
visited = [0]*(v+1)
result = []
while s:
    tmp = s.pop()
    if visited[tmp] == 0:
        arr = []
        backdfs(tmp)
        arr.sort()
        result.append(arr)

result = sorted(result, key = lambda x : x[0])
print(len(result))
for i in result:
    i.append(-1)
    print(*i)