import sys
import copy
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    input_tmp = int(sys.stdin.readline())
    arr.append(input_tmp)


max_count = 0
def DFS(arr, check, i, count):
    if i == len(arr):
        global max_count
        if max_count < count:
            max_count = count
        return

    if i >= 2 and check[i-2] and check[i-1]:
        tmp = copy.copy(check)
        DFS(arr, tmp, i+1, count)

    else:
        tmp1 = copy.copy(check)
        DFS(arr, tmp1, i+1, count)
        tmp2 = copy.copy(check)
        tmp2[i] = True
        DFS(arr, tmp2, i+1, count+ arr[i])


DFS(arr, [False for _ in range(len(arr))], 1, 0)
DFS(arr, [True]+[False for _ in range(len(arr)-1)], 1, arr[0])

print(max_count)