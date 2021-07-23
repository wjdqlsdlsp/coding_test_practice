from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]

# 위 오 아 왼
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(game_map,Rx, Ry,Bx,By, i):
    while game_map[Rx][Ry] !='#' and game_map[Rx][Ry] !='O':
        Rx = Rx + dx[i]
        Ry = Ry + dy[i]

    if game_map[Rx][Ry] =='#':
        Rx = Rx - dx[i]
        Ry = Ry - dy[i]

    while game_map[Bx][By] !='#' and game_map[Bx][By] !='O':
        Bx = Bx + dx[i]
        By = By + dy[i]

    if game_map[Bx][By] =='#':
        Bx = Bx - dx[i]
        By = By - dy[i]

    return game_map, Rx, Ry, Bx, By

def is_available_to_take_out_only_red_marble(game_map):
    n = len(game_map)
    m = len(game_map[0])
    for i in range(n):
        if "R" in game_map[i]:
            R_x, R_y = i, game_map[i].index("R")
        if "B" in game_map[i]:
            B_x, B_y = i, game_map[i].index("B")
        if "O" in game_map[i]:
            O_x, O_y = i, game_map[i].index("O")
    visited = [[(R_x, R_y),(B_x,B_y)]]
    queue = deque([[(R_x,R_y),(B_x,B_y)]])
    while len(queue) > 0:
        print(queue)
        (R_x, R_y), (B_x, B_y) = queue.popleft()
        for i in range(4):
            game_map,new_R_x, new_R_y, new_B_x, new_B_y= move(game_map, R_x, R_y,B_x,B_y, i)
            if new_B_x == O_x and new_B_y ==O_y:
                continue 
            elif new_R_x == O_x and new_R_y == O_y:
                return True
            elif [(new_R_x, new_R_y), (new_B_x, new_B_y)] in visited:
                continue
            else:
                visited.append([(new_R_x,new_R_y),(new_B_x,new_B_y)])
                queue.append([(new_R_x,new_R_y),(new_B_x,new_B_y)])

    return False

print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다

game_map = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", "O", ".", ".", ".", ".", "R", "B", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = False / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))


game_map = [
["#", "#", "#", "#", "#", "#", "#"],
["#", ".", ".", "R", "#", "B", "#"],
["#", ".", "#", "#", "#", "#", "#"],
["#", ".", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", ".", "#"],
["#", "O", ".", ".", ".", ".", "#"],
["#", "#", "#", "#", "#", "#", "#"]
]
print("정답 = True / 현재 풀이 값 = ", is_available_to_take_out_only_red_marble(game_map))