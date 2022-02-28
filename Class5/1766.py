import sys
from collections import defaultdict
import heapq

n, m = map(int, sys.stdin.readline().split())

arr = [0 for _ in range(n+1)]
s = defaultdict(list)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    s[a].append(b)
    arr[b] += 1

result = []
q = []
for i, v in enumerate(arr[1:], 1):
    if v == 0:
        heapq.heappush(q, i)
count = 0
while count != n:
    i = heapq.heappop(q)
    print(i, end=" ")
    count +=1
    for j in s[i]:
        arr[j] -=1
        if arr[j]==0:
            heapq.heappush(q, j)