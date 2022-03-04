import sys
from collections import deque
n = int(sys.stdin.readline())
q = deque()
q.append((n,[n]))
visited = [0]*(n+1)

while q:
    num, result = q.popleft()
    if num == 1:
        print(len(result)-1)
        print(*result)
        break
    if not visited[num]:
        visited[num] = 1
        if num % 3 == 0:
            q.append((num//3, result+[num//3]))
        if num % 2 == 0:
            q.append((num//2, result+[num//2]))
    q.append((num-1, result+[num-1]))
