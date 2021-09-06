from collections import defaultdict
from collections import deque
import sys
def find_fares(s, d, dict):
    arr = deque([(s,0)])
    dynamic = {s:0}

    while len(arr) >0:
        pop = arr.popleft()
        tmp, price = dict[pop[0]], pop[1]

        for i in tmp:
            if i[0] in dynamic.keys():
                if i[1] + price >= dynamic[i[0]]:
                    continue
                else:
                    dynamic[i[0]] = i[1] + price
            else:
                dynamic[i[0]] = i[1] + price

            arr.append((i[0], price + i[1]))
    if d == 0:
        return dynamic
    else:
        return dynamic[d]

def solution(n, s, a, b, fares):
    dict = defaultdict(list)
    for fare in fares:
        start, end, f = fare
        dict[start].append([end, f])
        dict[end].append([start, f])
    min_cost = sys.maxsize
    mid_poist = find_fares(s,0 , dict)
    a_to_mid = find_fares(a,0 , dict)
    b_to_mid = find_fares(b,0 , dict)
    for i in range(1,n+1):
        if i not in mid_poist.keys():
            continue
        tmp_cost = mid_poist[i] + a_to_mid[i] +b_to_mid[i]

        if tmp_cost < min_cost:
            min_cost = tmp_cost
    return min_cost

print(solution(6,	4,	6,	2,	[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))