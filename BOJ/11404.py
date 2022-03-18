import sys
v = int(sys.stdin.readline())
e = int(sys.stdin.readline())
INF = sys.maxsize
roots = [[INF]*(v+1) for i in range(v+1)]

for i in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    roots[a][b] = min(c, roots[a][b])

for i in range(1, v+1):
    roots[i][i] = 0

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            roots[i][j] = min(roots[i][j], roots[i][k] + roots[k][j])

for i in roots[1:]:
    for j in i[1:]:
        if j < sys.maxsize:
            print(j, end=" ")
        else:
            print(0, end=" ")
    print()