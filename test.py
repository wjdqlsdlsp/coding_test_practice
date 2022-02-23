import heapq

arr = []

tmp = [(1,2,3),
        (3,2,1),
        (5,1,2),
        (2,1,3),
        (4,2,3),
        (6,2,1)]
for i in range(len(tmp)):

    heapq.heappush(arr, tmp[i])

print(arr)