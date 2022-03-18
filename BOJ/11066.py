import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    arr = [*map(int, sys.stdin.readline().split())]
    dp = [[0] * (n) for i in range(n)]

    for i in range(n-1):
        dp[i][i+1] = arr[i] + arr[i+1]
        for j in range(i+2, n):
            dp[i][j] = dp[i][j-1] + arr[j]



    for v in range(2, n):
        for i in range(n-v):
            j = i+v
            dp[i][j] += min([dp[i][k] + dp[k+1][j] for k in range(i, j)])
    
    for i in dp:
        print(i)

    print(dp[0][n-1])