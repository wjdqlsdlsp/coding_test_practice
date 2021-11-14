from collections import deque
from copy import deepcopy
from collections import defaultdict
def solution(n, start, end, roads, traps):
    our_cost = []
    dp = []
    can_move = defaultdict(list)
    for s,e,c in roads:
        can_move[s].append((e,c))
    
    stack = deque([[start, can_move,0]])
    while stack:
        s, r, c = stack.popleft()
        if s == end:
            our_cost.append(c)
            continue
        if s in traps:
            add_list = []
            for i in range(1,n+1):
                for end_point,cost in r[i]:
                    if end_point == s or i == s:
                        r[i].pop(r[i].index((end_point,cost)))
                        add_list.append((end_point,i,cost))
            for add_s,add_e,add_c in add_list:
                r[add_s].append((add_e,add_c))
                
        if (s, r) in dp:
            continue
        else:
            dp.append((s, deepcopy(r)))
        
        for e,plus_c in r[s]:
            stack.append([e, deepcopy(r), c+plus_c])
        
    return min(our_cost)

print(solution(4,1,4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2,3]))