x = [0, 0, 1, -1]
y = [1, -1, 0, 0]

def solution(dirs):
    answer = 0
    position = [0,0]
    com = {'U':0, 'D':1, 'R':2, 'L':3}
    my_root = set() # (start_x, start_y, next_x, next_y)
    for command in dirs:
        act = com[command]
        next_x, next_y = position[0] + x[act], position[1]+ y[act]
        if next_x > 5: next_x = 5
        elif next_x < -5: next_x = -5

        if next_y > 5: next_y = 5
        elif next_y < -5: next_y = -5

        next_position = [next_x, next_y]
        if next_position == position:
            continue

        my_root.add((position[0], position[1], next_position[0], next_position[1]))
        my_root.add((next_position[0], next_position[1], position[0], position[1]))

        position = next_position
    return len(my_root)//2

print(solution("LULLLLLLU"))