import sys
n = int(sys.stdin.readline())
arr = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]

arr = sorted(arr, key= lambda x : x[0])
start, end = arr[0][0], arr[0][1]
result = 0
for s, e in arr[1:]:
    if e <=end:
        continue
    elif s <= end <= e:
        end = e
    elif end < s:
        result += end-start
        start, end = s, e

result += end - start
print(result)