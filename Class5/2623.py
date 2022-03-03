import sys
from collections import defaultdict
N, M = map(int, sys.stdin.readline().split())

arr = [0 for i in range(N+1)]

d = defaultdict(list)
for i in range(M):
    tmp = [*map(int, sys.stdin.readline().split())]
    for j in range(tmp[0]-1):
        now, next = tmp[j+1], tmp[j+2]
        d[now].append(next)
        arr[next]+=1

i = 1
result = []
tmp = []
while i < N+1:
    if arr[i] == 0:
        result.append(i)
        arr[i] = -1
        for j in d[i]:
            arr[j] -= 1
        i = 0
    i+=1
if len(result) == N:
    for i in result:
        print(i)
else:
    print(0)