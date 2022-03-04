import sys
sys.setrecursionlimit(111111)
T =int(sys.stdin.readline())

def dfs(x):
    global result
    check[x] = True
    cycle.append(x)
    now = d[x]

    if check[now]:
        if now in cycle:
            result += cycle[cycle.index(now):]
        return
    else:
        dfs(now)


for _ in range(T):
    n = int(sys.stdin.readline())
    d = [0] + [*map(int, sys.stdin.readline().split())]
    check = [True] + [False]*n
    result = []
    for i in range(1, n+1):
        if not check[i]:
            cycle = []
            dfs(i)

    print(n - len(result))