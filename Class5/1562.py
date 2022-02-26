n = int(input())
m = 1000000000
# dp[len][start][bin]
dp = [[[0 for j in range(1<<10)] for i in range(10)]for _ in range(101)]

for i in range(1,10):
    dp[1][i][1 << i] = 1

for i in range(2,n+1):
    for s in range(10):
        for k in range(1<<10):
            if s == 0:
                dp[i][s][k | (1 << s)] += dp[i-1][s+1][k]
            elif s == 9:
                dp[i][s][k | (1 << s)] +=  dp[i-1][s-1][k]
            else:
                dp[i][s][k | (1 << s)] +=  dp[i-1][s-1][k]
                dp[i][s][k | (1 << s)] += dp[i-1][s+1][k]

result = 0
for i in range(10):
    result +=dp[n][i][1023]

print(result%m)