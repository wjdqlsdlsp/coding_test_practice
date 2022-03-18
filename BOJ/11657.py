import sys
n, m = map(int, sys.stdin.readline().split())
INF = sys.maxsize
edges = [[*map(int, sys.stdin.readline().split())] for _ in range(m)]
dist = [INF] * (n+1)
def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            node, next_node, cost = edges[j]
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost

                if i == n-1:
                    return 1
    return 0

if bf(1):
    print(-1)
else:
    for i in range(2, n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])