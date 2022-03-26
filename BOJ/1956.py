import sys

v, e = map(int, sys.stdin.readline().split())
INF = sys.maxsize
dp = [[INF]*(v+1) for i in range(v+1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    dp[a][b] = c    

for i in range(1, v+1):
    for j in range(1, v+1):
        for k in range(1, v+1):
            dp[i][j] = min(dp[i][j] ,dp[i][k] + dp[k][j])

min_value = INF
for i in range(1, v+1):
    min_value = min(min_value, dp[i][i])

if min_value == INF:
    print(-1)
else:
    print(min_value)