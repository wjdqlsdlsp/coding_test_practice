import sys
n, b = map(int, sys.stdin.readline().split())
max_size = 1000
arr = [[*map(int, sys.stdin.readline().split())] for i in range(n)]
def mul(U, V):
    n = len(U)
    Z = [[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % max_size
    return Z

def square(A, B):
    if B == 1:
        for x in range(n):
            for y in range(n):
                A[x][y] %= max_size
        return A
    tmp = square(A, B//2)
    if B % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)

arr = square(arr,b)
    
for i in arr:
    for j in i:
        print(j%max_size, end=" ")
    print("")