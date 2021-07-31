from collections import deque
def solution(n, computers):
    queue = deque(computers)
    arr = []
    first = queue.popleft()
    while queue:
        for i in range(len(queue)):
            tmp = list(map(lambda x,y : x+y, first,queue[i]))
            if max(tmp) > 1:

                tmp = list(map(lambda x: 1 if x >= 1 else 0,tmp))
                queue[i] = tmp
                first = queue.popleft()
                break
        else:
            arr.append(first)
            first = queue.popleft()
    return len(arr) + 1



# print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(6,[[1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1]]))
