from collections import deque
# 오른쪽, 아래, 왼쪽, 위
ax = [1,0,-1,0]
ay = [0,1,0,-1]

def solution(board):
    x_len, y_len = len(board[0]), len(board)
    answer = 0
    # x, y, cost,prev_move : if 1 = left or right, if 0 = up or down
    now = deque([[0,0,0,-1]])
    dynamic = {(0,0,-1):0}
    while now:
        pop = now.popleft()
        for i in range(4):
            x,y,cost,pre_direct = pop[0]+ax[i], pop[1]+ay[i], pop[2], pop[3]
            if x < 0 or x >= x_len or y < 0 or y >= y_len or board[y][x] == 1:
                continue
            if pre_direct == -1:
                if i == 0 or i ==2:
                    direct = 1
                else:
                    direct = 0
            # prev -> up or down
            elif pre_direct == 0:
                if i == 0 or i ==2: # now -> right or left
                    direct = 1
                    cost += 500
                else:
                    direct = 0
            else:
                if i == 0 or i ==2: # now -> right or left
                    direct = 1
                else:
                    direct = 0
                    cost += 500
            cost += 100
            if (x,y,direct) in dynamic.keys():
                if cost >= dynamic[(x,y,direct)]:
                    continue

            dynamic[(x,y,direct)] = cost
            now.append([x,y,cost,direct])

    if (x_len-1,y_len-1,0) in dynamic.keys() and (x_len-1,y_len-1,1) in dynamic.keys():
        return min(dynamic[(x_len-1,y_len-1,0)], dynamic[(x_len-1,y_len-1,1)])
    elif (x_len-1,y_len-1,0) in dynamic.keys():
        return dynamic[(x_len-1,y_len-1,0)]
    else:
        return dynamic[(x_len-1,y_len-1,1)]

print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))