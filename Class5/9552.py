import sys

s1 = sys.stdin.readline().split()[0]
s2 = sys.stdin.readline().split()[0]

arr = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1 
        else:
            arr[i][j] = max(arr[i][j-1], arr[i-1][j])

print(arr[len(s1)][len(s2)])
if arr[len(s1)][len(s2)] ==0:
    pass

answer = []
x = len(s1)
y = len(s2)
while 1:
    now = arr[x][y]
    if now == 0:
        break
    if arr[x-1][y-1] == (now - 1) and arr[x][y-1] == (now - 1) and arr[x-1][y] == (now-1):
        x -= 1
        y -= 1
        answer.append(s2[y])
    else:
        if now == arr[x-1][y]:
            x -= 1
        else:
            y -= 1


print("".join(answer)[::-1])