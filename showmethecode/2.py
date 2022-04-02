import sys, copy
from collections import defaultdict

N, Q = map(int, sys.stdin.readline().split())
arr = [''] + [*map(str, sys.stdin.readline().split())]
div_num = 1000000007
roots = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    roots[a].append(b)
    roots[b].append(a)

def dfs(i, visited, string, goal):
    global answer
    string += arr[i]

    visited[i] = 1
    if i == goal:
        answer = int(string) % div_num
        return
    
    for j in roots[i]:
        if visited[j]:
            continue
        dfs(j, copy.copy(visited), string, goal)

for _ in range(Q):
    answer = 0
    start, goal = map(int, sys.stdin.readline().split())
    dfs(start, [0]*(N+1), '', goal)
    print(answer)