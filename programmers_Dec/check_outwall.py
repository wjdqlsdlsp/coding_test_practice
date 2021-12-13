from itertools import permutations
def solution(n, weak, dist):
    arr = [weak[i:] + [*map(lambda x : x + n, weak[:i])] for i in range(len(weak))]
    for i in range(1,len(dist)+1):
        can_permutations = [*permutations(dist,i)]
        for j in arr:
            for t in can_permutations:
                now_value = j[0]
                for co in t:
                    for tmp in j[1:]:
                        if now_value + co < tmp:
                            break
                    else:
                        return i
                    now_value = tmp
    return -1

print(solution(12, [1, 5, 6, 10], [1,2,3,4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))