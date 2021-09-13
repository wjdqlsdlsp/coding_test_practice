# 효율성테스트 시간초과
import copy
result_list = []
def DFS(arr, i):
    if arr[i] == "+":
        arr = arr[:i-1] + [arr[i-1] + arr[i+1]] + arr[i+2:]
    else:
        arr = arr[:i-1] + [arr[i-1] - arr[i+1]] + arr[i+2:]
    if len(arr) == 1:
        result_list.append(int(arr[0]))
        return

    for i in range(1,len(arr),2):
        DFS(arr, i)

def solution(arr):
    arr = [arr[i] if i  % 2 == 1 else int(arr[i]) for i in range(len(arr))]
    for i in range(1,len(arr),2):
        DFS(arr, i)
    return max(result_list)

print(solution(["1", "-", "3", "+", "5", "-", "8"]))