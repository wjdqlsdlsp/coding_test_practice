import sys
import bisect
n = int(sys.stdin.readline())
arr = [*map(int, sys.stdin.readline().split())]

q = []
dp = [0]*n
for index, i in enumerate(arr):
    t = bisect.bisect_left(q, i)

    if len(q) == 0:
        q.append(i)
    else:
        if t == len(q):
            q.append(i)
        else:
            q[t] = i

    dp[index] = t
q_len = len(q)

print(q_len)
print_arr = []
for i in range(n-1, -1, -1):
    if dp[i] == q_len-1:
        print_arr.append(arr[i])
        q_len-=1

print(*reversed(print_arr))
