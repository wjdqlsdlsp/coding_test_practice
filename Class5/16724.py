import sys
input =sys.stdin.readline
N,M = map(int,input().split())
field = [list(input().strip()) for _ in range(N)]
parents = list(range(N*M))

d =dict()
d['D'] = (0, 1)
d['L'] = (-1, 0)
d['R'] = (1, 0)
d['U'] = (0, -1)

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    a,b = find(a), find(b)
    if a==b:
        return
    if a<b:
        parents[b] = a
    else:
        parents[a] = b


for num in range(N*M):
    x = num%M
    y = num//M
    cur = field[y][x]
    nx = x+ d[cur][0]
    ny = y+ d[cur][1]
    next_num = ny*M + nx
    if next_num < 0 or next_num >= M*N:
        continue
    union(num, next_num)

answer = 0 
visited = dict() 
for i in range(N*M): 
    if find(parents[i]) not in visited: 
        answer+=1 
        visited[parents[i]]=True 
print(answer)
