import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 9)
n = int(sys.stdin.readline())
tree = defaultdict(list)
for a, b in range(n-1):
    a,b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0]*2 for i in range(n+1)]
visited = [0 for i in range(n+1)]

def dfs(r):
    visited[r] = 1
    dp[r][0] = 1
    for i in tree[r]:
        if not visited[i]:
            dfs(i)
            dp[r][0] += min(dp[i][0], dp[i][1])
            dp[r][1] += dp[i][0]

dfs(1)
print(min(dp[1][0], dp[1][1]))