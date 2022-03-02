import sys
from collections import defaultdict


N, M = map(int, sys.stdin.readline().split())

arr = [0 for i in range(N+1)]

d = defaultdict(list)
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    d[a].append(b)
    arr[b] += 1

i = 1
# result = []

while i <= N:
    if arr[i] == 0:
        print(i, end=" ")
        # result.append(i)
        arr[i] = -1
        for j in d[i]:
            arr[j] -=1
        i = 0
    i+=1

# print(result)