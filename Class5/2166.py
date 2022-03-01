import sys, math

N = int(sys.stdin.readline())
arr = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]
arr.append(arr[0])
p, m = 0, 0 
start_x, start_y = arr[0][0], arr[0][1]
for i in range(len(arr) -1):
    p += arr[i][0] * arr[i+1][1]
    m += arr[i][1] * arr[i+1][0]

result = math.fabs(0.5 *(p - m))
print(round(result,1))
