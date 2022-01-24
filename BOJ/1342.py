from collections import Counter
import copy, math
a = input()
count = Counter(a)
answer = 0
def DFS(prev, count, str_len):
    global answer

    if str_len == len(a):
        answer+=1
        return
    
    for i in count.keys():
        if prev != i and count[i] >=1:
            tmp = copy.deepcopy(count)
            tmp[i] -= 1
            if tmp[i] == 0:
                del tmp[i]
            if i not in tmp.keys() and len(tmp.keys()) == sum(tmp.values()):
                answer+= math.perm(len(tmp.keys()))
            else:
                DFS(i, tmp, str_len+1)

for i in count.keys():
    tmp = copy.deepcopy(count)
    tmp[i] -= 1
    if tmp[i] == 0:
        del tmp[i]
    DFS(i, tmp, 1)
print(answer)