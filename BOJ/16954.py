import sys, copy
from collections import deque
input = sys.stdin.readline

m = []
for _ in range(8):
    tmp = list(input().split()[0])  
    for i, v in enumerate(tmp):
        if v == '.':
            tmp[i] = 1
        else:
            tmp[i] = 0
    m.append(tmp)

q = deque()
q.append([7, 0])

dx = [1, 0, -1, 0, 1, -1, 1, -1,0]
dy = [0, 1, 0, -1, 1, -1, -1, 1,0]

visited = []
while q:
    y, x = q.popleft()

    if m[y][x] == 0:
        continue

    if y == 0:
        print(1)
        exit()

    if [y, x] in visited:
        continue

    visited.append([y, x])

    for k in range(9):
        next_x = x + dx[k]
        next_y = y + dy[k]
        if 0<= next_x < 8 and 0<= next_y < 8:
            if m[next_y][next_x]:
                q.append([next_y-1, next_x])


print(0)