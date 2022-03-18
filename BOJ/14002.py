import sys
import bisect
n = int(sys.stdin.readline())

arr = [*map(int, sys.stdin.readline().split())]

dp = [0 for i in range(n)]
s = []

for index, value in enumerate(arr):
    t = bisect.bisect_left(s, value)

    if len(s) == 0:
        s.append(value)
    else:
        if t == len(s):
            s.append(value)
        else:
            s[t] = value
    dp[index] = t + 1

max_count = max(dp)
print(max_count)

result = []
for i in range(n-1, -1, -1):
    if dp[i] == max_count:
        result.append(arr[i])
        max_count-=1

result = result[::-1]
print(*result)