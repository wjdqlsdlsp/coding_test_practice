def solution(rounds):
    answer = 0
    mapping = {'a':0, 'b':1, 'c':2, 'd':3}
    couples = set()
    for case in rounds:

        prev = couples
        couples = set()

        for i, v in enumerate(case):
            point = mapping[case[mapping[v]]]
            if (i, mapping[v]) in prev:
                answer+=1

            if point == i:
                if mapping[v] == i:
                    answer+=1
                else:
                    if (i, mapping[v]) not in prev:
                        couples.add((i, mapping[v]))
                        couples.add((mapping[v], i))

    return answer