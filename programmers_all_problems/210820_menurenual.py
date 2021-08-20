from collections import Counter
from itertools import combinations
def solution(orders, course):
    total, answer = [[] for _ in range(len(course))], []
    for order in orders:
        tmp_list = [s for s in order]
        for index, combi in enumerate(course):
            total[index] += list(map(lambda x : "".join(x), list(map(lambda x : sorted(x), list(combinations(tmp_list, combi))))))
            
    for t in total:
        a = Counter(t)
        if len(a) == 0: continue
        max_num = max(a.values())
        if max_num <= 1: continue

        for item in a.items():
            if item[1] == max_num: answer.append(item[0])

    return sorted(answer)

print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))