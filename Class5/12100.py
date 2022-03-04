import sys
import copy

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    tmp = [*map(int, sys.stdin.readline().split())]
    tmp = [0] * (n-len(tmp)) + tmp
    arr.append(tmp)

def make_q(arr):
    q = []
    check = 0
    for j in arr:
        if j == 0: continue
        elif len(q) ==0: q.append(j)
        elif q[-1] == j and check == 0:
            q[-1] *=2
            check = 1
        else:
            q.append(j)
            check = 0
    return q

def up(arr):
    tmp_arr = [[] for _ in range(n)]
    for i in range(n):
        tmp = [*map(lambda x : x[i], arr)]
        q = make_q(tmp)
        q = q + [0]*(n - len(q))
        tmp_arr[i] = q
    return_arr = []
    for j in range(n):
        return_arr.append([*map(lambda x: x[j], tmp_arr)])
    return return_arr

def down(arr):
    tmp_arr = [[] for _ in range(n)]
    for i in range(n):
        tmp = [*map(lambda x : x[i], arr)]
        tmp.reverse()
        q = make_q(tmp)
        q.reverse()
        q = [0]*(n - len(q)) + q
        tmp_arr[i] = q
    return_arr = []
    for j in range(n):
        return_arr.append([*map(lambda x: x[j], tmp_arr)])
    return return_arr

def left(arr):
    tmp_arr = [[] for _ in range(n)]
    for i in range(n):
        tmp = arr[i]
        q = make_q(tmp)
        q = q+ [0]*(n - len(q))
        tmp_arr[i] = q
    return tmp_arr

def right(arr):
    tmp_arr = [[] for _ in range(n)]
    for i in range(n):
        tmp = arr[i]
        tmp.reverse()
        q = make_q(tmp)
        q.reverse()
        q = [0]*(n - len(q)) + q
        tmp_arr[i] = q
    return tmp_arr

max_value = 0
def dfs(arr, c):
    global max_value
    for i in arr:
        max_value = max(max_value, max(i))
    if c == 5:
        return


    for func in [up, down, right, left]:
        tmp = copy.deepcopy(arr)
        dfs(func(tmp), c+1)

dfs(arr, 0)

print(max_value)