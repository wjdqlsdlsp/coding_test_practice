import sys
from collections import defaultdict
from collections import deque

total_game = int(sys.stdin.readline())

for _ in range(total_game):
    con_n, rule = [*map(int, sys.stdin.readline().split())]
    arr = [0] + [*map(int, sys.stdin.readline().split())]
    how_many = [0] * (con_n+1)
    r = defaultdict(list)
    for i in range(rule):
        a, b = [*map(int, sys.stdin.readline().split())]
        how_many[b] += 1
        r[a].append(b)
    victory = int(sys.stdin.readline())

    dp = [0] * (con_n + 1)
    q = deque([])

    for i in range(1, con_n + 1):
        if how_many[i] == 0:
            q.append(i)
            dp[i] += arr[i]
    
    while q:
        now = q.popleft()
        for i in r[now]:
            how_many[i] -= 1
            dp[i] = max(dp[i], dp[now] + arr[i])

            if how_many[i] == 0:
                q.append(i) 

    print(dp[victory])   