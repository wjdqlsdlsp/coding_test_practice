import sys
from collections import deque

arr = [*map(int, sys.stdin.readline().split())]
# 중앙 0 위 1 왼 2 아래 3 오 4
# 0000 0001 0010 0100 1000
# tmp[depth][l][r]
def score(now, next):
    if now == 0: return 2
    elif now == next: return 1
    elif abs(now - next) == 2: return 4
    else: return 3


dp = [[[-1 for k in range(5)]for j in range(5)] for i in range(len(arr))]
dp[0][0][0] = 0

for depth, goal in enumerate(arr[:-1]):
    for l in range(5):
        for r in range(5):
            if dp[depth][l][r] != -1:
                if dp[depth+1][goal][r] != -1:
                    dp[depth+1][goal][r] = min(dp[depth+1][goal][r], dp[depth][l][r] + score(l,goal))
                else:
                    dp[depth+1][goal][r] = dp[depth][l][r] + score(l,goal)

                if dp[depth+1][l][goal] != -1:
                    dp[depth+1][l][goal] = min(dp[depth+1][l][goal], dp[depth][l][r] + score(r,goal))
                else:
                    dp[depth+1][l][goal] = dp[depth][l][r] + score(r,goal)

result = sys.maxsize
for i in dp[-1]:
    for j in i:
        if j != -1:
            result = min(result, j)

print(result)

# result = sys.maxsize
# q = deque([(0, 0, 0)])

# for goal in arr:
#     if goal == 0:
#         for j in q:
#             result = min(result, j[2])
#         break
#     n = len(q)
#     dp = ()
#     for _ in range(n):
#         l, r, c = q.popleft()
#         q.append((goal, r, c+score(l, goal)))
#         q.append((l, goal, c+score(r, goal)))
