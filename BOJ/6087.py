import sys
from collections import deque
w,h = map(int, sys.stdin.readline().split())

m = []
c_position = [ ]
for _ in range(h):
    tmp = list(sys.stdin.readline().split()[0])
    for i in range(w):
        if tmp[i] == 'C':
            c_position.append([_, i])
        
        if tmp[i] == '*':
            tmp[i] = False
        else:
            tmp[i] = True
    m.append(tmp)

q = deque()
y, x = c_position[0]
q.append([y,x, -1, -1])
check_map = [[sys.maxsize]*w for _ in range(h)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while q:
    y, x, last_move, c = q.popleft()

    if m[y][x] == False:
        continue

    if c > check_map[y][x]:
        continue

    check_map[y][x] = c

    for k in range(4):
        next_x = x + dx[k]
        next_y = y + dy[k]

        if 0 <= next_x < w and 0<= next_y < h:
            if last_move != k:
                q.append([next_y, next_x, k, c+1])
            else:
                q.append([next_y, next_x, k, c])

y, x = c_position[1]
print(check_map[y][x])