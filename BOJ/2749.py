import sys

n = int(sys.stdin.readline())
mod = 1000000
p = mod // 10*15
dp = [0]*(p+1)
dp[0] = 0
dp[1] = 1
for i in range(2,p):
    dp[i] = (dp[i-1] + dp[i-2]) % mod

print(dp[n%p]%mod)