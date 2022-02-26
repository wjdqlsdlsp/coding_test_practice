s = input()
l = len(s)
dp = [[0 for j in range(l+1)] for i in range(l+1)]

for i in range(1, l+1):
    dp[i][i] = 1

for i in range(1, l):
    if s[i-1] == s[i]:
        dp[i][i+1] = 1

for i in range(2, l):
    for j in range(1, l+1-i):
        if s[j-1] == s[j+i-1] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] =1

result = [float('inf')] *(l+1)
result[0] = 0
for i in range(1, l+1):
    result[i] = min(result[i], result[i-1]+1)

    for j in range(i+1, l+1):
        if dp[i][j] != 0:
            result[j] = min(result[j], result[i-1]+1)

print(result[l])