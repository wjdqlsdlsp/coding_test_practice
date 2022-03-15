import sys
import heapq
import copy
input = sys.stdin.readline

n = int(input())
max_heap = []
min_heap = []

for i in range(n):
    num = int(input())
    if i == 0:
        heapq.heappush(max_heap, -num)
        print(max_heap[0]*-1)
        continue
    else:
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, num)
        else:
            heapq.heappush(max_heap, -num)
    
    if -max_heap[0] > min_heap[0]:
        max_heap_pop = heapq.heappop(max_heap) * -1
        min_heap_pop = heapq.heappop(min_heap)

        heapq.heappush(max_heap, -min_heap_pop)
        heapq.heappush(min_heap, max_heap_pop)

    print(max_heap[0]*-1)