from collections import defaultdict
from collections import deque
def solution(n, path, order):
    tree = defaultdict(list)
    for p in path:
        tree[p[0]].append(p[1])
        tree[p[1]].append(p[0])
    orders =[0 for i in range(n)]
    for pre, post in order:
        orders[post] = pre
    check = [False for i in range(n)]
    queue = deque([0])
    after = {}
    answer = 0
    while queue:
        now = queue.popleft()
        if orders[now] and not check[orders[now]]:
            after[orders[now]] = now
            continue
        check[now] = True
        answer+=1

        for t in tree[now]:
            if not check[t]:
                queue.append(t)

        if now in after:
            queue.append(after[now])
    return answer == n
    
print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))


# 시간초과
# from collections import defaultdict
# import copy
# dp = []
# answer = False

# def DFS(tree, can_go, check, now, n, order_list):
#     if sum(can_go) == n:
#         global answer
#         answer = True
#         return
#     if [check,now] in dp:
#         return
#     dp.append([check, now])    
#     check[now] = True
#     if now in order_list.keys():
#         can_go[order_list[now]]=True
#     for way in tree[now]:
#         if can_go[way] == True:
#             DFS(tree, copy.copy(can_go), copy.copy(check), way, n, order_list)

# def solution(n, path, order):
#     check = [False for i in range(n)]
#     can_go = [True for i in range(n)]
#     tree = defaultdict(list)
#     order_list = dict()
#     for p in path:
#         tree[p[0]].append(p[1])
#         tree[p[1]].append(p[0])
#     for o in order:
#         order_list[o[0]] = o[1]
#         can_go[o[1]] = False
#     DFS(tree, can_go, check, 0, n, order_list)
#     return answer
