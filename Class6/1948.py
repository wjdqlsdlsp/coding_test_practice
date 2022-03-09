import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
tree =defaultdict(list)
back =defaultdict(list)
indegree = [0]*(n+1)

for _ in range(m):
    s,e,c = [*map(int, sys.stdin.readline().split())]
    tree[s].append((e,c))
    back[e].append((s,c))

    indegree[e] += 1

start, end = map(int, sys.stdin.readline().split())
q = deque([start])
result = [0]*(n+1)

while q:
    cur = q.popleft()
    for i,t in tree[cur]:
        indegree[i] -=1
        result[i] = max(result[i], result[cur]+t)
        if indegree[i] == 0:
            q.append(i)

check = [0]*(n+1)
cnt = 0
q.append(end)
while q:
    cur = q.popleft()
    for i, t in back[cur]:
        if result[cur] - result[i] == t:
            cnt+=1
            if check[i] == 0:
                q.append(i)
                check[i] = 1

print(result[end])
print(cnt)