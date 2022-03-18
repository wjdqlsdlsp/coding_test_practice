from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(wasted,robot):
    visited = [[[0]*(1<<10) for i in range(w)] for i in range(h)]
    queue = deque([])
    queue.append((robot[0],robot[1],0))
    while queue:
        x,y,clean_bit = queue.popleft()
        if clean_bit == (1 << len(wasted)) -1:
            return visited[x][y][clean_bit]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= h or ny >= w or arr[nx][ny] == 'x': continue
            if arr[nx][ny] == '*':
                next_bit = clean_bit | (1<<wasted.index((nx,ny)))
                if not visited[nx][ny][next_bit]:
                    queue.append((nx,ny,next_bit))
                    visited[nx][ny][next_bit] = visited[x][y][clean_bit] + 1
            else:
                if not visited[nx][ny][clean_bit]:
                    queue.append((nx,ny,clean_bit))
                    visited[nx][ny][clean_bit] = visited[x][y][clean_bit] + 1
    return -1
while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    arr = []
    for i in range(h):
        arr.append(list(input()))
    wasted = []
    for i in range(h):
        for j in range(w):
            if arr[i][j] == '*':
                wasted.append((i,j))
            elif arr[i][j] == 'o':
                robot = [i,j]
    print(bfs(wasted,robot))
