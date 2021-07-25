import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >=2:
        a, b = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        answer +=1
        if scoville[0] >=K:
            return answer
    return -1

print(solution([1,2,3,9,10,12], 7))