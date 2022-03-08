import sys
n, s, e, t = map(int, sys.stdin.readline().split())
mxw = 5
a = [[0] * (n * mxw) for __ in range(n * mxw)]

for r in range(n):
    for i in range(1, mxw):
        a[r * mxw + i][r * mxw + i - 1] = 1

for r in range(n):
    for c, v in enumerate(map(int, input())):
        if v: a[r * mxw][c * mxw + v - 1] = 1

def mm(a, b):
    sz = n * mxw
    c = [[0] * sz for __ in range(sz)]
    for i in range(sz):
        for j in range(sz):
            for k in range(sz):
                c[i][j] += a[i][k] * b[k][j]
    for i in range(sz):
        for j in range(sz):
            c[i][j] %= 1000003
    return c

r = a
for d in map(int, bin(t)[3:]):
    r = mm(r, r)
    if d: r = mm(r, a)

ans = r[(s - 1) * mxw][(e - 1) * mxw]
print(ans)