import sys
import heapq

n, k = map(int, sys.stdin.readline().split())

jewel = []
bag = []
can = []
total = 0

for _ in range(n):
    weight,price = map(int, sys.stdin.readline().split())
    heapq.heappush(jewel, [weight, price])

for _ in range(k):
    tmp = int(sys.stdin.readline())
    bag.append(tmp)
bag.sort()

for b in bag:
    while jewel and b >= jewel[0][0]:
        weight, price = heapq.heappop(jewel)
        heapq.heappush(can, price*-1)
    
    if can:
        total -= heapq.heappop(can)

print(total)