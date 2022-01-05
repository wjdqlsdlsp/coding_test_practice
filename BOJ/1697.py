from collections import deque
a,b = map(int, input().split())
dynamic = set()

if a == b:
    print(0)
    exit(0)
arr = deque([[a,0]])

while arr:
    now, t = arr.popleft()
    for v in [now*2, now+1, now-1]:
        if v == b:
            print(t+1)
            arr.clear()
            break

        if v in dynamic or v <0 or v > 100000:
            continue

        dynamic.add(v)
        arr.append([v, t+1])