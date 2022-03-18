import sys
T = int(sys.stdin.readline())

for _ in range(T):
    n,m,k = map(int, sys.stdin.readline().split())
    roots = [[] for i in range(n+1)]
    dp = [[sys.maxsize]*(n+1) for i in range(m+1)]
    dp[0][1] = 0

    for i in range(k):
        u,v,c,d = map(int, sys.stdin.readline().split())
        roots[u].append([v,c,d])

    for c in range(m+1):
        for d in range(1, n+1):
            if dp[c][d] == sys.maxsize:
                continue
            t = dp[c][d]

            for dv, dc, dd in roots[d]:
                if dc+c > m:
                    continue
                dp[dc+c][dv] = min(dp[dc+c][dv], t+dd)

    result = []
    for i in range(m+1):
        if dp[i][n] != sys.maxsize:
            result.append(dp[i][n])

    if len(result) > 0:
        print(min(result))

    else:
        print("Poor KCM")