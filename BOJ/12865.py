import sys
input = sys.stdin.readline
n, k = map(int, input().split())

arr = [[*map(int, input().split())] for i in range(n)]
dp = [[0] * (k+1) for i in range(n+1)]

for i in range(n):
    w,v = arr[i]
    for j in range(k):
        dp[i][j] = max(dp[i-1][j], dp[i][j])

        if j + w <= k:
            dp[i][j+w] = max(dp[i][j+w], dp[i-1][j] + v)
    
result = 0
for j in dp:
    result = max(result, max(j))

print(result)