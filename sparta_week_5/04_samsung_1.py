k = 4  # 말의 개수
chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    turn_count = 0
    map_stack = [[[] for i in range(n)] for j in range(n)]
    for i in range(len(horse_location_and_directions)):
        x,y,d = horse_location_and_directions[i]
        map_stack[x][y].append(i)

    print(map_stack)
    while turn_count <=1000:
        for i in range(len(horse_location_and_directions)):
            x,y,d = horse_location_and_directions[i]
            stack_index = map_stack[x][y].index(i)
            new_x = x + dx[d]
            new_y = y + dy[d]

            if new_x < 0 or new_x >=n or new_y < 0 or new_y >=n or game_map[new_x][new_y] == 2 :
                if d == 0: d = 1
                elif d == 1: d= 0
                elif d ==2: d = 3
                else: d =2
                new_x = x + dx[d]
                new_y = y + dy[d]
                horse_location_and_directions[i] = new_x, new_y, d
                while len(map_stack[x][y]) > stack_index:
                    horse_num = map_stack[x][y].pop(stack_index)
                    horse_location_and_directions[horse_num] = new_x, new_y, horse_location_and_directions[horse_num][2]
                    map_stack[new_x][new_y].append(horse_num)
                    if len(map_stack[new_x][new_y]) >=4:
                        return turn_count+1

            if game_map[new_x][new_y] == 0:
                horse_location_and_directions[i]  = new_x, new_y, d
                while len(map_stack[x][y]) > stack_index:
                    horse_num = map_stack[x][y].pop(stack_index)
                    horse_location_and_directions[horse_num] = new_x, new_y, horse_location_and_directions[horse_num][2]
                    map_stack[new_x][new_y].append(horse_num)
                    if len(map_stack[new_x][new_y]) >=4:
                        return turn_count+1
            else:
                return
        turn_count +=1
        print(map_stack)

    return -1

print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다

start_horse_location_and_directions = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# print("정답 = 9 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))

# start_horse_location_and_directions = [
#     [0, 1, 0],
#     [0, 1, 1],
#     [0, 1, 0],
#     [2, 1, 2]
# ]
# print("정답 = 3 / 현재 풀이 값 = ", get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))