import sys
INF = sys.maxsize

n = int(sys.stdin.readline().split()[0])
t = [[*map(int, sys.stdin.readline().split())] for i in range(n)]

dp = [[0] * (1<<n-1) for i in range(n)]

def dfs(now, bit):
    if dp[now][bit] != 0:
        return dp[now][bit]

    if bit == (1 << (n-1)) -1:
        if t[now][0]:
            return t[now][0]
        else:
            return INF

    result = INF

    for j in range(1, n):
        if not t[now][j]:
            continue

        if bit & (1 << j-1):
            continue

        D = t[now][j] + dfs(j, bit | (1<<(j-1)))
        if result > D:
            result = D
    
    dp[now][bit] = result

    return result

print(dfs(0,0))