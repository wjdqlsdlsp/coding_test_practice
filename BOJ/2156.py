import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    input_tmp = int(sys.stdin.readline())
    arr.append(input_tmp)

recur = [0 for _ in range(n)]
recur[0] = arr[0]

if n > 1:
    recur[1] = arr[0] + arr[1]

if n > 2:
    recur[2] = max(recur[0]+arr[2], recur[1], arr[1]+arr[2])

for i in range(3, n):
    recur[i] = max(recur[i-1], recur[i-2]+arr[i], recur[i-3]+arr[i-1]+arr[i])

print(recur[n-1])
