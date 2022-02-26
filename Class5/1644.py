from collections import deque
n = int(input())

arr = [True for i in range(n+1)]

for i in range(2, n):
    if arr[i]:
        for j in range(i*2, n+1,i):
            arr[j] = False

prime_num = []
for i in range(2, n+1):
    if arr[i]:
        prime_num.append(i)

result = 0 
total_sum = 0
q = deque([])
for i in prime_num:
    
    q.append(i)
    total_sum+=i

    if total_sum == n:
        result +=1

    while total_sum >= n:
        a = q.popleft()
        total_sum-=a

        if total_sum == n:
            result+=1

print(result)