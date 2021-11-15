# 시간초과 코드 DP 필요
import copy
count = []
def DFS(arr, i, c, t):
    if i == len(arr):
        count.append(c)
        return
    for index, tmp in enumerate(t):
        if i in tmp:
            num = index
            break
    if num == 0:
        DFS(arr, i+1, c, t)
    else:
        Y = [*map(lambda x : arr[x],t[num-1])]
        X = [*map(lambda x : arr[x],t[num])]
        if sum(Y) == sum(X):
            tmp = copy.deepcopy(t)
            tmp_pop = tmp.pop(num)
            tmp[num-1] += tmp_pop
            DFS(arr, i, c+[i], tmp)
        DFS(arr, i+1, c, t)
            
def solution(a, s):
    global count
    answer = []
    prev = 0
    for num in s:
        count = []
        DFS(a[prev:prev+num], 0, [], [*map(lambda x : [x], [*range(num)])])
        prev +=num
        answer.append(len(count)%(10**9 + 7))
    return answer

print(solution([1,1,1,1,1,1,2,5,8,2,1,1,4,8,8,8,12,6,6], [4,3,1,5,6]))