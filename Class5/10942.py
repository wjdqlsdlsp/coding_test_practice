import sys
T = int(sys.stdin.readline())
arr = [0] + [*map(int, sys.stdin.readline().split())]
n = int(sys.stdin.readline())
dp = set()
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    l, r = s, e
    while l < r:
        if (l, r) in dp:
            l = 1
            r = -1
            break
        if arr[l] == arr[r]:
            l+=1
            r-=1
        else:
            break
    if l>=r:
        dp.add((s,e))
        print(1)

    else:
        print(0)