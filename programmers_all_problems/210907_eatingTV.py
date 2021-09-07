### https://velog.io/@qweadzs/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%AC%B4%EC%A7%80%EC%9D%98-%EB%A8%B9%EB%B0%A9-%EB%9D%BC%EC%9D%B4%EB%B8%8CPython 블로그참고
### 왜 내가 풀면, 효율성 or 정확성 둘중 하나만 챙겨질까..?

import heapq
def solution(food_times, k):
    answer = 0
    answer_list = []
    q = []
    for index,value in enumerate(food_times):
        heapq.heappush(q, [value, index + 1])

    tmp = 0
    t= 0
    while True:
        if len(q) <=0:
            return -1
        length = len(q)
        t += (q[0][0] - tmp)*length

        if t > k:
            t -= (q[0][0]-tmp) * length
            while q:
                answer_list.append(heapq.heappop(q)[1])
            answer_list.sort()
            answer = answer_list[(k-t)% length]
            break
        else:
            tmp = heapq.heappop(q)[0]
    return answer

print(solution([3,1,2],5))