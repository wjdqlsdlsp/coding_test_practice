import sys

N, M = map(int, sys.stdin.readline().split())
m = [*map(int, sys.stdin.readline().split())]
c = [*map(int, sys.stdin.readline().split())]

max_cost = sum(c) + 1
dp = [[0]*max_cost for _ in range(N+1)]
min_cost = max_cost
for i in range(1, N+1):
    for j in range(len(dp[0])):
        if j < c[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
             dp[i][j] = max(dp[i-1][j], dp[i-1][j-c[i-1]] + m[i-1])
        if dp[i][j] >= M and min_cost > j:
            min_cost = j
print(min_cost)