import sys, copy
from collections import deque
input = sys.stdin.readline

r, c= map(int, input().split())

m = []
L_position = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(r):
    tmp = input().split()[0]
    tmp_arr = []
    for index, j in enumerate(list(tmp)):
        if j == '.':
            tmp_arr.append(1)
        elif j == 'L':
            tmp_arr.append(0)
            L_position.append([i, index])
        else:
            tmp_arr.append(0)
    m.append(tmp_arr)

def find_boundary(m):
    arr= set()
    for i in range(r):
        for j in range(c):
            if m[i][j] == 1:
                for k in range(4):
                    x = j + dx[k]
                    y = i + dy[k]
                    if 0 <= x < c and 0<= y <r:
                        if m[y][x] == 0:
                            arr.add((i,j))
    return arr
boundary = find_boundary(m)
def melt(m, boundary):
    new_boundary = set()
    while boundary:
        i, j = boundary.pop()
        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]
            if 0 <= x < c and 0<= y <r:
                if m[y][x] == 0:
                    m[y][x] =1
                    new_boundary.add((y,x))
    return m , new_boundary

time = 0
while True:
    q = deque([])
    q.append([L_position[0][0], L_position[0][1]])
    visited = set()
    while q:
        y, x = q.popleft()

        if y == L_position[1][0] and x == L_position[1][1]:
            print(time)
            exit()
        if (y,x) in visited:
            continue
        visited.add((y,x))

        if m[y][x] == 1:
            for i in range(4):
                next_y, next_x = y+dy[i] , x+dx[i]
                if 0<= next_y < r and 0<= next_x < c:
                    q.append([next_y, next_x])

    time+=1
    m, boundary = melt(m, boundary)