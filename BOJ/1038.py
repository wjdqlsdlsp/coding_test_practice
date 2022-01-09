from itertools import combinations
a = int(input())

result = []
for i in range(1,11):
    for tmp in combinations(range(0,10), i):
        tmp = list(tmp)
        tmp.sort(reverse=True)
        result.append(int("".join(map(str, tmp))))

result.sort()

if len(result) < a:
    print(-1)
else:
    print(result[a])