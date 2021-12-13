import sys
sys.setrecursionlimit(300000)

def dfs(x, a, board):
    global visited
    global answer
    global length
    
    now = a[x]
    visited[x] = 1
    
    for i in board[x]:
        if visited[i] == 0:
            now += dfs(i, a, board)
            
    answer += abs(now)
    
    return now
    
def solution(a, edges):
    global visited
    global answer
    global length
    
    answer = 0
    
    if sum(a) != 0:
        return -1
    
    length = len(a)
    board = [[] for _ in range(length)]

    for i, j in edges:
        board[i].append(j)
        board[j].append(i)
    
    visited = [0]*length
    dfs(0, a, board)
    return answer

print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))