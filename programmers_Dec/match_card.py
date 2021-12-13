# 미완성
from collections import defaultdict
import copy
def DFS(x1,y1,x2,y2,count,visited, board):
    global a
    if x1 <0 or x1>3 or y1 <0 or y1>3:
        return
    if x1 == x2 and y1 == y2:
        a.append(count)
        return
    if (x1, y1) in visited or count >= min(a):
        return
    visited.add((x1,y1))

    min_x, max_x =max(x1-1,0), min(x1+1,3)
    min_y, max_y =max(y1-1,0), min(y1+1,3)
    while board[y1][max_x]==0 and max_x < 3:
        max_x +=1
    while board[y1][min_x]==0 and min_x > 0:
        min_x -=1
    while [*map(lambda x: x[x1], board)][max_y]==0 and max_y < 3:
        max_y +=1
    while [*map(lambda x: x[x1], board)][min_y]==0 and min_y > 0:
        min_y -=1        

    
    DFS(x1+1,y1,x2,y2,count+1,visited, board)
    DFS(x1-1,y1,x2,y2,count+1,visited, board)
    DFS(x1,y1+1,x2,y2,count+1,visited, board)
    DFS(x1,y1-1,x2,y2,count+1,visited, board)
    DFS(min_x,y1,x2,y2,count+1,visited, board)
    DFS(max_x,y1,x2,y2,count+1,visited, board)
    DFS(x1,min_y,x2,y2,count+1,visited, board)
    DFS(x1,max_y,x2,y2,count+1,visited, board)

def calcul_distance(x1,y1, x2,y2, board):
    if x1 == x2 and y1 == y2:
        return 0
    global a
    a = [100]
    min_x, max_x =max(x1-1,0), min(x1+1,3)
    min_y, max_y =max(y1-1,0), min(y1+1,3)
    while board[y1][max_x]==0 and max_x < 3:
        max_x +=1
    while board[y1][min_x]==0 and min_x > 0:
        min_x -=1
    while [*map(lambda x: x[x1], board)][max_y]==0 and max_y < 3:
        max_y +=1
    while [*map(lambda x: x[x1], board)][min_y]==0 and min_y > 0:
        min_y -=1        

    
    DFS(x1+1,y1,x2,y2,1,set(), board)
    DFS(x1-1,y1,x2,y2,1,set(), board)
    DFS(x1,y1+1,x2,y2,1,set(), board)
    DFS(x1,y1-1,x2,y2,1,set(), board)
    
    DFS(min_x,y1,x2,y2,1,set(), board)
    DFS(max_x,y1,x2,y2,1,set(), board)
    DFS(x1,min_y,x2,y2,1,set(), board)
    DFS(x1,max_y,x2,y2,1,set(), board)
    return min(a)

def DFS_root(x1,y1, x2,y2, a, i, num, visited, should_visit,count, board):
    global result
    count += calcul_distance(x1,y1, x2,y2, board)
    count += calcul_distance(a[i][0][0], a[i][0][1], a[i][1][0], a[i][1][1], board)+2
    tmp_board = copy.deepcopy(board)
    tmp_board[a[i][0][1]][a[i][0][0]] = 0
    tmp_board[a[i][1][1]][a[i][1][0]] = 0

    if i in visited:
        return
    
    visited.add(i)

    if len(visited) == len(should_visit):
        result.append(count)
        return
    
    if num == 0:    
        r = a[i][1][0]
        c = a[i][1][1]
    else:
        r = a[i][0][0]
        c = a[i][0][1]

    for i in a.keys():
        tmp = copy.deepcopy(visited)
        DFS_root(r,c, a[i][0][0], a[i][0][1],a, i, 0, tmp, a.keys(), count, tmp_board)
        tmp2 = copy.deepcopy(visited)
        DFS_root(r,c, a[i][1][0], a[i][1][1],a, i, 1, tmp2, a. keys(), count, tmp_board)

def solution(board, r, c):

    global result
    result =[]
    a = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[j][i] != 0:
                a[board[j][i]].append([i,j])

    for i in a.keys():
        DFS_root(c,r, a[i][0][0], a[i][0][1],a, i, 0, set(), a.keys(),0, board)
        DFS_root(c,r, a[i][1][0], a[i][1][1],a, i, 1, set() ,a.keys(),0, board)

    return min(result)

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1,0))


print(solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0,1))

