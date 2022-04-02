import sys
from collections import defaultdict
import copy
N = int(sys.stdin.readline())
costs = [0]+[*map(int, sys.stdin.readline().split())]

discount = defaultdict(list)
for i in range(1, N+1):
    n = int(sys.stdin.readline())
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        discount[i].append([a, b])

result = sys.maxsize
def dfs(i, costs_info, visited, total_cost):
    global result
    if total_cost >= result:
        return
    visited[i] = 1
    if sum(visited) == N:
        result = min(result, total_cost)
        return
    for a, b in discount[i]:
        costs_info[a] -= b

    for j in range(1, N+1):
        if visited[j]:
            continue
        dfs(j, copy.copy(costs_info), copy.copy(visited), total_cost+max(1, costs_info[j]))


for i in range(1,N+1):
    dfs(i, copy.copy(costs), [0]*(N+1), costs[i])
print(result)