import sys
import copy
n = int(sys.stdin.readline())

arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = [*map(int, sys.stdin.readline().split()[0])]

who_take = [[True]*n for _ in range(n)]
who_take[0][0] = False
max_num = 0

def DFS(price, owner, who_take, arr, num):

    for index, p in enumerate(arr[owner]):
        if who_take[owner][index] and price <= p:
            tmp = copy.copy(who_take)
            tmp[owner] = [False] * n
            DFS(p, index, tmp, arr, num+1)
        else:
            who_take[owner][index] = False
        
    else:
        global max_num
        if max_num < num:
            max_num = num

DFS(0, 0, who_take, arr, 1)

print(max_num)