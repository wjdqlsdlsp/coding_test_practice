import sys
from collections import Counter

T = int(sys.stdin.readline().split()[0])

a_len = int(sys.stdin.readline().split()[0])
a = [*map(int, sys.stdin.readline().split())]
b_len = int(sys.stdin.readline().split()[0])
b = [*map(int, sys.stdin.readline().split())]

a_sum = []
for i in range(1, a_len+1):
    for j in range(0, a_len-i+1):
        a_sum.append(sum(a[j:j+i]))

b_sum = []
for i in range(1, b_len+1):
    for j in range(0, b_len-i+1):
        b_sum.append(sum(b[j:j+i]))


a_counter = Counter(a_sum).items()
b_counter = Counter(b_sum).items()

a_counter = sorted(a_counter, key= lambda x: x[0])
b_counter = sorted(b_counter, key= lambda x: x[0], reverse=True)


result = 0
l, r = 0, 0
while l < len(a_counter) and r < len(b_counter):
    if a_counter[l][0] + b_counter[r][0] == T:
        result += a_counter[l][1] * b_counter[r][1]
        l+=1
        r+=1
    elif a_counter[l][0] + b_counter[r][0] < T:
        l+=1

    else:
        r+=1

print(result)