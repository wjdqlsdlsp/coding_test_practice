import sys
from collections import deque

a, b, c = map(int, sys.stdin.readline().split())

q = deque([[a,b]])
sum_stone = sum([a,b,c])
if sum_stone % 3 == 0:

    visited = set()
    while q:
        a, b = q.popleft()
        c = sum_stone - a - b
        if a==b==c:
            print(1)
            exit()
        for x,y in ((a,b), (b,c), (a,c)):
            if x == y:
                continue
            x, y = min(x,y), max(x,y)
            x, y = x+x, y-x
            if (x,y) not in visited:
                visited.add((x,y))
                q.append([x,y])

    print(0)
else:
    print(0)