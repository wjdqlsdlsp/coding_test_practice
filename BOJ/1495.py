N, S, M = map(int, input().split())
v = [*map(int, input().split())]
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][S] = 1
for i in range(N):
    for j in range(M+1):
        if dp[i][j] == 1:
            if j+ v[i] <= M:
                dp[i+1][j+v[i]] = 1
            
            if j - v[i] >= 0:
                dp[i+1][j-v[i]] = 1

ansewr = -1
for index, value in enumerate(dp[N]):
    if value == 1:
        ansewr = index

print(ansewr)