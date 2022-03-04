import sys
from collections import defaultdict
N = int(sys.stdin.readline())
for _ in range(N):
    h, w= map(int, sys.stdin.readline().split())
    h_arr, w_arr = h + 2, w + 2
    arr = [["." for j in range(w_arr)] for i in range(h_arr)]
    for i in range(h) :
        arr[i+1][1:-2] = sys.stdin.readline().strip()

    keys = set(input())
    keys.add('.')
    stack = [(0,0)]
    result = 0
    unlock = defaultdict(list)
    while stack:
        r, c = stack.pop()
        candidate = [(r-1,c), (r+1, c),(r, c-1), (r, c+1)]
        item = arr[r][c]
        
        # 달러일때
        if item == "$":
            result +=1
        # 키가 있을 때
        elif item.lower() in keys:
            pass
        # 키일 때
        elif 'a' <= item <= 'z':
            keys.add(item)
            candidate += unlock[item]
            unlock[item] = list()
        # 키가없는 문일 때
        elif item != "*":
            unlock[item.lower()].append((r,c))
            continue
        else:
            continue

        arr[r][c] = "*"

        for r1, c1 in candidate:
            if 0 <= r1 < h_arr and 0 <= c1 < w_arr:
                if arr[r1][c1] !="*":
                    stack.append((r1,c1))
    print(result)