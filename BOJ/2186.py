import sys

n, m, k = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline().split()[0]) for _ in range(n)]
goal = list(sys.stdin.readline().split()[0])
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
c = [[[-1] * len(goal) for _ in range(m)] for _ in range(n)]

start_position = []
for y in range(n):
    for x in range(m):
        if arr[y][x] == goal[0]:
            start_position.append([y,x])
def dfs(y, x, char_n):
    global answer
    if char_n == len(goal):
        return 1
    
    if c[y][x][char_n] != -1:
        return c[y][x][char_n]

    c[y][x][char_n] = 0

    for i in range(1, k+1):
        for j in range(4):
            next_x = x + i*dx[j]
            next_y = y + i*dy[j]
            if 0<= next_x < m and 0 <= next_y < n:
                if arr[next_y][next_x] == goal[char_n]:
                    c[y][x][char_n] += dfs(next_y, next_x, char_n+1)
    return c[y][x][char_n]
                    
answer = 0
for i in start_position:
    y, x = i
    answer += dfs(y, x, 1)

print(answer)