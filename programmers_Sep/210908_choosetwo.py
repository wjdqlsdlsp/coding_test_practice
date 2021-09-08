from itertools import combinations
def solution(numbers):
    a = list(combinations(numbers,2))
    tmp = list(set(map(lambda x : sum(x),a)))
    tmp.sort()
    return tmp

print(solution([2,1,3,4,1]))