from collections import defaultdict
from collections import deque
def solution(n, edge):
    root = defaultdict(list)
    for start, des in edge:
        root[start].append(des)
        root[des].append(start)
    is_visit = [False for _ in range(n)]
    is_visit[0] = True
    distance = [0 for _ in range(n)]
    queue =deque([1])

    while queue:
        pop_num = queue.popleft()
        
        while root[pop_num]:
            root_num = root[pop_num].pop()

            if is_visit[root_num-1] == False:
                is_visit[root_num-1] = True
                queue.append(root_num)
                distance[root_num-1] = distance[pop_num-1]+1

    distance.sort(reverse=True)
    return distance.count(distance[0])

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))