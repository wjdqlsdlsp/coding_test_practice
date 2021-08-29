# 효율성 못통과..
from collections import defaultdict

def solution(info, query):
    people_len = len(info)
    answer = []
    people_list = defaultdict(set)
    people_time = {}
    for i in range(len(info)):
        inf = info[i].split(" ")
        for j in range(4):
            people_list[inf[j]].add(i)
        people_time[i] = int(inf[4])

    people_time = sorted(people_time.items(), key=lambda x : x[1])

    people_list['-'] = set(range(0,people_len))
    for que in query:
        count = 0
        t = que.split(" and ")
        a = t[-1].split(" ")
        t[-1], time = a[0], int(a[1])
        tmp = [people_list[i] for i in t]

        set_tmp = tmp[0] & tmp[1] & tmp[2] & tmp[3]
        print(people_time[[0,1]])
        answer.append(count)
            
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
