import sys

n = int(sys.stdin.readline())

rgb = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]
dp = [[0 for j in range(3)] for i in range(n)]
result = sys.maxsize

for k in range(3):
    dp[0][0] = sys.maxsize
    dp[0][1] = sys.maxsize
    dp[0][2] = sys.maxsize
    dp[0][k] = rgb[0][k]

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
        dp[i][1] = min(dp[i-1][2], dp[i-1][0]) + rgb[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]

    for i in range(3):
        if i != k:
            result = min(result, dp[n-1][i])

print(result)