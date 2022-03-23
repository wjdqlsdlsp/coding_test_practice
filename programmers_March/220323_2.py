from collections import defaultdict
import sys, copy
sys.setrecursionlimit(10**5)

tree = defaultdict(list)
visited = []
answer = 0

def dfs(now, count, inf):
    global answer
    if inf[now] == 0:
        count[0] +=1
        inf[now] = -1
    elif inf[now] == 1:
        count[1] +=1
        inf[now] = -1
    
    if count[0] <= count[1]:
        answer = max(answer, count[0])
        return
    
    if [now, count, inf] in visited:
        answer = max(answer, count[0])
        return

    visited.append([now, count, inf])

    for i in tree[now]:
        dfs(i, copy.copy(count), copy.copy(inf))

def solution(info, edges):
    for a, b in edges:
        tree[a].append(b)        
        tree[b].append(a)        

    dfs(0, [0, 0], info)

    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))