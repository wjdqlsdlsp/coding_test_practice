# 실패 ( 왜 DFS가 for 문에서 반복이 안될까...? )

import copy
from collections import defaultdict
dp = []
our_cost = []

def DFS(n, now, goal, can_move, traps,cost,where):
    if now == goal:
        our_cost.append(cost)
        return
    
    if now in traps:
        add_list = []
        for s in range(1,n+1):
            for e,c in can_move[s]:
                if e == now or s == now:
                    can_move[s].pop(can_move[s].index((e,c)))
                    add_list.append((e,s,c))
            
        for s,e,c in add_list:
            can_move[s].append((e,c))
            
    if [now, where, can_move.items()] in dp:
        return
    else:
        dp.append([now, where, can_move.items()])
            
    for e,c in can_move[now]:
        DFS(n, e, goal, copy.copy(can_move), traps, cost+c,now)

def solution(n, start, end, roads, traps):
    can_move = defaultdict(list)
    for s,e,c in roads:
        can_move[s].append((e,c))
    DFS(n, start, end, can_move, traps,0,0)
    return min(our_cost)

print(solution(4,1,4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2,3]))