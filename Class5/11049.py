import sys
T = int(sys.stdin.readline())
arr = [[*map(int, sys.stdin.readline().split())] for _ in range(T)]
min_num = sys.maxsize
  
memo = [[0 for i in range(T)] for j in range(T)]

for i in range(1, T):
    for j in range(T-i):
        x = i + j 
        memo[j][x] = min_num

        for k in range(j, x):
            memo[j][x] = min(memo[j][x], memo[j][k] + memo[k+1][x] + arr[j][0] * arr[k][1] * arr[x][1])

print(memo[0][T-1])