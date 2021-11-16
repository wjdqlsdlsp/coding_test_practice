cost = []
DP = set()
def DFS(arr, x,y, goal_x, goal_y,c):
    # 영역이 아님
    if arr[y][x] == 0:
        return
    # 테두리가아님
    if arr[y-1][x-1] == 1 and arr[y-1][x] == 1 and arr[y-1][x+1] == 1 and \
        arr[y][x-1] == 1 and arr[y][x+1] == 1 and \
        arr[y+1][x-1] == 1 and arr[y+1][x] == 1 and arr[y+1][x+1] == 1:
            return
    # 목표물 도착
    if (x,y) == (goal_x,goal_y):
        cost.append(c)
        return
    # 이미 방문
    if (x,y) in DP:
        return
    else:
        DP.add((x,y))
        
    DFS(arr, x+1,y, goal_x, goal_y,c+1)
    DFS(arr, x,y+1, goal_x, goal_y,c+1)
    DFS(arr, x-1,y, goal_x, goal_y,c+1)
    DFS(arr, x,y-1, goal_x, goal_y,c+1)
    

def solution(rectangle, characterX, characterY, itemX, itemY):
    arr = [[0 for i in range(200)] for j in range(200)]
    
    for x1,y1,x2,y2 in rectangle:
        for i in range(y1*2, (y2)*2+1):
            for j in range(x1 * 2, x2 * 2 + 1):
                arr[i][j] = 1
            
    DFS(arr, characterX*2, characterY*2, itemX*2,itemY*2,0)
    return min(cost)//2

# print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1,3,7,8))
# print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9,7,6,1))
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]],1,4,6,3))
