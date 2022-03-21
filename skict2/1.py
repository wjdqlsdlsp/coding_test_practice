from collections import defaultdict

def solution(goods):
    answer = []
    shopping = defaultdict(set)

    for good in goods:
        for i in range(1, len(good)+1):
            for j in range(len(good)):
                if j+i > len(good):
                    continue
                shopping[good[j:j+i]].add(good)
    for good in goods:
        tmp_min_size = 101
        tmp = set()
        for i in range(1, len(good)+1):
            for j in range(len(good)):
                if j+i > len(good):
                    continue
                if good in shopping[good[j:j+i]] and len(shopping[good[j:j+i]]) == 1:
                    if i == tmp_min_size:
                        tmp.add(good[j:j+i])
                        tmp_min_size = i
                    elif i < tmp_min_size:
                        tmp = set()
                        tmp.add(good[j:j+i])
                        tmp_min_size = i

        tmp = sorted(list(tmp))
        if len(tmp) == 0:
            answer.append("None")
        else:       
            answer.append(" ".join(tmp))

    return answer

print(solution(["ab","bc", "cd"]))