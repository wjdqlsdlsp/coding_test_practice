from collections import deque
# up, down, left, right
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def solution(maps):
    n,m = len(maps), len(maps[0])
    dynamic = set((0,0))
    arr = deque([[0,0,0]])
    while len(arr) > 0:
        cur = arr.popleft()
        count = cur[2] + 1
        for i in range(4):
            x, y = cur[0] + dy[i], cur[1] + dx[i]
            if [x,y] == [n-1,m-1]:
                return count + 1
            if (x,y) in dynamic:
                continue
            else:
                if x<0 or y<0 or x > n-1 or y> m-1 or maps[x][y] ==0:
                    continue
                else:
                    arr.append([x,y,count])
                    dynamic.add((x,y))
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))