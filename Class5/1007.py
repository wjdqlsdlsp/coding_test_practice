import sys
from itertools import combinations

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    arr = [[] for i in range(N)]

    total_x, total_y = 0, 0 
    for i in range(N):
        arr[i] = [*map(int, sys.stdin.readline().split())]
        total_x += arr[i][0]
        total_y += arr[i][1]

    result = sys.maxsize
    for i in [*combinations(arr, N//2)]:

        tmp_x, tmp_y = total_x, total_y
        for j in i:
            tmp_x -= j[0]*2
            tmp_y -= j[1]*2
        if result > (tmp_x**2 + tmp_y**2):
            result = (tmp_x**2 + tmp_y**2)

    print(result**0.5)
