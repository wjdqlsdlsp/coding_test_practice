from collections import deque

def solution(progresses, speeds):
    queue = deque()
    answer = []
    day = 0

    for work,speeds in zip(progresses,speeds):
        for i in range(1, 100):
            if work + speeds * i >=100:
                queue.append(i)
                break
            
    while len(queue) > 0:
        pop = queue.popleft()
        if pop <= day:
            answer[-1] += 1
        else:
            answer.append(1)
            day = pop

    return answer

print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
