import heapq

def solution(operations):
    large_heap = []
    small_heap = []
    count = 0
    for operate in operations:
        if count == 0:
            large_heap = []
            small_heap = []
        split = operate.split(" ")
        if split[0] =='I':
            num = int(split[1])
            heapq.heappush(large_heap, -1* num)
            heapq.heappush(small_heap, num)
            count +=1
        else:
            if count ==0:
                continue
            if split[1] =='1':
                heapq.heappop(large_heap)
                count -=1
            else:
                heapq.heappop(small_heap)
                count -=1
    if count ==0:
        answer = [0,0]
    else:
        answer = [heapq.heappop(large_heap)*-1,heapq.heappop(small_heap)]

    return answer

print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"]))