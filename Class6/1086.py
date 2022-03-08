import sys, math
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
size = [len(str(i)) for i in arr]
k = int(sys.stdin.readline())
arr = [*map(lambda x: x%k, arr)]

dp = [[0]*k for i in range(1<<n)]
octal = [0]*51
octal[0] = 1
for i in range(1, 51):
    octal[i] = (octal[i-1]*10) % k
dp[0][0] = 1

for i in range(0, 1<<n):
    for j in range(0, k):
        for t in range(0, n):
            if i&(1<<t)==0:
                dp[i | (1 << t)][(j*(octal[size[t]]) + arr[t]) % k] += dp[i][j]

def gcd(x,y):
    while y:
        x,y = y, x%y
    return x

p = dp[(1<<n)-1][0]
q = math.factorial(n)
t = gcd(p,q)
p,q = p//t, q//t
print(f"{p}/{q}")