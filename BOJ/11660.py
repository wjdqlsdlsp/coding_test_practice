import sys

n, m = map(int, sys.stdin.readline().split())

arr = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]

sum_arr = [[0]*(n+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        sum_arr[i][j] = sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1] + arr[i-1][j-1]

for _ in range(m):
    a,b,c,d = map(int, sys.stdin.readline().split())
    print(sum_arr[c][d] - sum_arr[c][b-1] - sum_arr[a-1][d] + sum_arr[a-1][b-1])