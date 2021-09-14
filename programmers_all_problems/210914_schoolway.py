# 효율성 해결못하고 다른사람 코드 참고;
import copy
my_answer = []
dynamic = {}
def DFS(m, n, column, row,count,root):
    tmp = root.copy()
    tmp.append((column,row))
    global min_answer
    if column > m or row > n:
        return
    if (column, row) in dynamic.keys():
        return
    if column == m and row == n:
        my_answer.append(count)
        for i in root:
            dynamic[i] = count
        return 
    DFS(m, n, column+1, row, count+1,tmp)
    DFS(m, n, column, row+1, count+1,tmp)
    return

def solution(m, n, puddles):
    answer =0
    for puddle in puddles:
        dynamic[(puddle[0],puddle[1])] = -1

    DFS(m, n,1,1, 0,[])
    if len(my_answer) == 0:
        return 0
    min_value = min(my_answer)
    for i in my_answer:
        if i == min_value:
            answer+=1
    return answer%1000000007

# info = dict([((2, 1), 1), ((1, 2), 1)])

# def func(m, n):
#     if m < 1 or n < 1:
#         return 0
#     if (m, n) in info:
#         return info[(m, n)]

# def solution(m, n, puddles):
#     for puddle in puddles:
#         info[tuple(puddle)] = 0

#         return info.setdefault((m, n), func(m - 1, n) + func(m, n - 1))
#     return  func(m, n) % 1000000007