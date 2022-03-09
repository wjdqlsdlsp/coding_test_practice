import sys
T = sys.stdin.readline()[:-1]
P = sys.stdin.readline()[:-1]

pi = [0 for i in range(len(P))]
j = 0
for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = pi[j-1]
    if P[i] == P[j]:
        j+=1
        pi[i] = j

result = []
c = 0
j=0
for i in range(0, len(T)):
    while j > 0 and T[i] != P[j]:
        j = pi[j-1]
    if T[i] == P[j]:
        if j == len(P) - 1:
            result.append(i - len(P) + 2)
            c +=1
            j = pi[j]
        else:
            j+=1
print(c)
for i in result:
    print(i)