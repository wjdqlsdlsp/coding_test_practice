import sys
n, k = map(int, sys.stdin.readline().split())
n = str(n)
s_arr = set([n])
for _ in range(k):
    can_change = set()
    for s in list(s_arr):
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                a = s
                a = a[:i] + a[j] + a[i+1: j] + a[i] + a[j+1:]
                if a[0] == '0':
                    continue
                can_change.add(a)
    s_arr = can_change

arr = [*map(int, list(s_arr))]
if len(arr) > 0:
    print(max(arr))
else:
    print(-1)