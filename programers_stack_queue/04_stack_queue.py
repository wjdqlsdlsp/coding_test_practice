# 에러뜨고 결과가 안나옴
from collections import deque
def solution(prices):
    Q = deque(prices)
    answer = []
    for _ in range(len(Q)):
        price = Q.popleft()
        count=0
        for i in range(len(Q)-1):
            if price < Q[count]:
                break
        answer.append(len(Q) - i)
    return answer

print(solution([1, 2, 3, 2, 3]))