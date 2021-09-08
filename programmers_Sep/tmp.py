import heapq

a = []

heapq.heappush(a, (2,(3,2)))
heapq.heappush(a, (3,(1,3)))
heapq.heappush(a, (1,(2,3)))


print(a)