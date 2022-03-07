import sys
from collections import deque
N,M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    tmp = list(sys.stdin.readline().split()[0])
    for i in range(M):
        if tmp[i] == '1':
            tmp[i] = -1
        else:
            tmp[i] = 0
    arr.append(tmp)

result = [[0 for j in range(M)] for i in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
a = {0:1}
group = 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            visited = []
            q = deque([[j,i]])
            while q:
                x,y = q.popleft()
                if arr[y][x] == -1 or [x,y] in visited:
                    continue
                visited.append([x,y])
                for k in range(4):
                    if 0<= y+dy[k] < N and 0<= x+dx[k] < M:
                        q.append([x+dx[k], y+dy[k]])

            a[group] = len(visited)
            for k in visited:
                x, y = k
                arr[y][x] = group
            group+=1

for y in range(N):
    for x in range(M):
        if arr[y][x] == -1:
            s = set([0])
            for k in range(4):
                tmp_y = y + dy[k]
                tmp_x = x + dx[k]
                if 0<=tmp_y <N and 0<= tmp_x < M and arr[tmp_y][tmp_x] > 0:
                    s.add(arr[tmp_y][tmp_x])
            for k in list(s):
                result[y][x] += a[k]


for i in result:
    print(i)
        