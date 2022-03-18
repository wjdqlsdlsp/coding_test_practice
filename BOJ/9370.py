import sys
import heapq
T = int(sys.stdin.readline())

def dijkstra(s):
    h = []
    heapq.heappush(h, [0, s])
    dp = [sys.maxsize for i in range(n+1)]
    dp[s] = 0
    while h:
        now_len, c = heapq.heappop(h)
        for pop_b, pop_c in roots[c]:
            length = now_len + pop_c
            if dp[pop_b] > length:
                dp[pop_b] = length
                heapq.heappush(h, [length, pop_b])
    return dp

for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())

    roots = [[] for i in range(n+1)]
    for i in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        roots[a].append([b,c])
        roots[b].append([a,c])

    can = []
    for i in range(t):
        tmp = int(sys.stdin.readline())
        can.append(tmp)

    start = dijkstra(s)
    from_g = dijkstra(g)
    from_h = dijkstra(h)
    answer = []
    for i in can:
        if start[g] + from_g[h] + from_h[i] == start[i] or \
            start[h] + from_h[g] + from_g[i] == start[i]:
            answer.append(i)
    answer.sort()
    for f in answer:
        print(f, end=" ")