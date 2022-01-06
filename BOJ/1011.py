from collections import deque
n = int(input())


for _ in range(n):
    start, end = map(int, input().split())
    distance = end - start
    count = 0
    while distance > 0:
        t = int(distance**0.5)
        distance = distance - t**2
        count = count + 2*t -1
    print(count)
    # arr = deque([(start+1, 1, 1)])
    # visited = set()

    # while arr:
    #     location, move, count = arr.popleft()
        
    #     if location in visited:
    #         continue

    #     visited.add(location)
        
    #     for i in [move-1, move, move+1]:
    #         if (location + i == end-1 and 0 <= i <= 2) \
    #             or (location + i == end+1 and -1 <= i <= 0):
    #             print(count+2)
    #             arr.clear()
    #             break
                
    #         arr.append((location+i, i, count+1))
