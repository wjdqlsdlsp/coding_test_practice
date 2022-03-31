import sys
from collections import deque

MAX = 100001
start, goal = map(int, sys.stdin.readline().split())
visited = [0] * MAX
move = [0] * MAX

def path(x):
    arr = []
    temp = x
    for _ in range(visited[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

q = deque([start])
while q:
    x = q.popleft()
    if x == goal:
        print(visited[goal])
        path(x)
        break
    for i in [x-1, x+1, x*2]:
        if 0 <= i < MAX and visited[i] == 0 :
            visited[i] = visited[x] + 1
            q.append(i)
            move[i] = x