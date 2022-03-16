import sys
from collections import defaultdict
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())

forward =defaultdict(list)
back =defaultdict(list)


for i in range(m):
    a, b = map(int, input().split())
    forward[-a].append(b)
    forward[-b].append(a)

    back[b].append(-a)
    back[a].append(-b)


def dfs(cur):
    visited.add(cur)
    for next in forward[cur]:
        if next not in visited:
            dfs(next)
    stack.append(cur)

def reverseDfs(cur, scc):
    visited.add(cur)
    scc.append(cur)
    for next in back[cur]:
        if next not in visited:
            scc = reverseDfs(next, scc)
    return scc

def kosaraju():
    global visited
    answer = []
    for i in range(-n, n+1):
        if i not in visited:
            dfs(i)
    visited = set()
    while stack:
        scc = []
        cur = stack.pop()
        if cur in visited:
            continue
        answer.append(sorted(reverseDfs(cur, scc)))
    return answer

stack = []
visited = set()
answer = kosaraju()

result = [0]*(n*2+1)
print_result = [0] *n

for index, i in enumerate(answer):
    for j in i:
        result[j] = index

for i in range(1,n+1):
    if result[i] == result[-i]:
        print(0)
        break
    if result[i] > result[-i]:
        print_result[i-1] = 1

else:
    print(1)
    print(*print_result)