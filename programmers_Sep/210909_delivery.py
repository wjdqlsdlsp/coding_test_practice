from collections import defaultdict
dynamic = {}
def DFS( root, now_position,value):
    if now_position in dynamic.keys():
        if dynamic[now_position] <= value:
            return
        else:
            dynamic[now_position] = value
    else:
        dynamic[now_position] = value

    if now_position in root.keys():
        for way in root[now_position]:
            DFS(root, way[0],value + way[1])


def solution(N, road, K):
    answer = 0
    root = defaultdict(list)
    for way in road:
        a,b,c = way
        root[a].append((b,c))
        root[b].append((a,c))
    DFS(root,1,0)
    
    for i in range(1,N+1):
        if dynamic[i] <=K:
            answer+=1
    return answer

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))