import sys
from collections import defaultdict
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

tree = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a].append([b,c])
    # tree[b].append([a,c])

start, end = map(int, sys.stdin.readline().split())

INF = sys.maxsize
dp = [INF] * (n+1)
# dp[start] = 0

h = [[0, start, 0]]
p = [0] * (n+1)
while h:
    distance, x, prev = heapq.heappop(h)
    if distance >= dp[x]:
        continue
    
    p[x] = prev

    dp[x] = distance
    for a,b in tree[x]:
        heapq.heappush(h, [distance+b, a, x])

print(dp[end])
roots = []
def dfs(i):
    if i == 0:
        return
    roots.append(i)
    i = dfs(p[i])

dfs(end)
print(len(roots))
roots.reverse()
print(*roots)