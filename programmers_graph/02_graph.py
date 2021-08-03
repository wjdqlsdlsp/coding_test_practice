from collections import defaultdict
from collections import deque
def solution(n, results):
    answer = 0
    win_lose = defaultdict(list)
    lose_win = defaultdict(list)

    for winner, loser in results:
        win_lose[winner].append(loser)
        lose_win[loser].append(winner)

    for i in range(1,n+1):
        fight_list =  [0 for _ in range(n+1)]
        is_fight1 = [False for _ in range(n+1)]
        is_fight2 = [False for _ in range(n+1)]
        queue = deque([i])
        while len(queue) > 0:
            pop_num = queue.popleft()
            for num in win_lose[pop_num]:
                if is_fight1[num] == False:
                    is_fight1[num] = True
                    fight_list[num] = 1
                    queue.append(num)

        queue = deque([i])
        while len(queue) > 0:
            pop_num = queue.popleft()
            for num in lose_win[pop_num]:
                if is_fight2[num] == False:
                    is_fight2[num] = True
                    fight_list[num] = 1
                    queue.append(num)

        if sum(fight_list) == n-1:
            answer +=1
    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))