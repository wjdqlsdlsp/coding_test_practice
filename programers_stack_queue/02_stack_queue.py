from collections import deque
def solution(priorities, location):
    answer = 0
    Q = deque([[index, priorities[index]] for index in range(len(priorities))])
    while len(Q) > 0:
        max_value  = max(Q, key=(lambda x : x[1]))[1]
        pop = Q.popleft()
        if pop[1] != max_value:
            Q.append(pop)
        else:
            answer +=1
            if pop[0] == location:
                return answer


print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1]	,0))
