import sys
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]
n = int(sys.stdin.readline())

def bfs():
    q = deque()
    c = [[0]*n for _ in range(n)]
    q.append([0, 0])
    c[0][0] = 1
    while q:
        x, y = q.popleft()
        if x == n-1 and y == n-1:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if left <= a[nx][ny] <= right and not c[nx][ny]:
                    c[nx][ny] = 1
                    q.append([nx, ny])
    return 0

a, r_max, l_min = [], 0, sys.maxsize
for i in range(n):
    tmp = [*map(int, sys.stdin.readline().split())]
    a.append(tmp)
    l_min = min(l_min, min(tmp))
    r_max = max(r_max, max(tmp))

l_max = min(a[0][0], a[n-1][n-1])
r_min = max(a[0][0], a[n-1][n-1])

left, right = l_min, r_min
ans = sys.maxsize

while l_min <= left <= l_max and r_min <= right <= r_max:
    if bfs():
        ans = min(ans, right-left)
        left+=1
    else:
        right+=1
print(ans)