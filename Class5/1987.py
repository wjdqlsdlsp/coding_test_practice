import sys

R,C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().split()[0]) for _ in range(R)]
check = [0] * 26
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 0
def dfs(x, y, count):
    global result
    result = max(result, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<= nx < C) and (0<= ny < R) and check[ord(arr[ny][nx])-65] == 0:
            check[ord(arr[ny][nx])-65] = 1
            dfs(nx, ny, count+1)
            check[ord(arr[ny][nx])-65] = 0

check[ord(arr[0][0]) - 65] = 1
dfs(0, 0, 1)
print(result)