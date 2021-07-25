import heapq

def solution(jobs):
    heap = []
    length = len(jobs)
    answer = 0
    time =0
    heapq.heapify(jobs)
    while len(jobs) + len(heap) > 0:
        while len(jobs)>0 and jobs[0][0] <=time:
            pop_jobs = heapq.heappop(jobs)
            heapq.heappush(heap, [pop_jobs[1], pop_jobs[0]])
            
        if heap:
            pop_heap = heapq.heappop(heap)
            time += pop_heap[0]
            answer += (time - pop_heap[1])
        else:
            time +=1
    return answer//length


print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))