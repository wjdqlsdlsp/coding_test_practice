import heapq
import sys
case = int(sys.stdin.readline())

for _ in range(case):
    answer = 0
    n = int(sys.stdin.readline())
    d = {}
    for u in range(n):
        a, b = map(int, sys.stdin.readline().split())
        d[a] = b
    
    arr =[n+1]
    for i in range(1,n+1):
        if d[i] < arr[0]:
            answer+=1
        heapq.heappush(arr, d[i])
        
    print(answer)