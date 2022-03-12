def move_right(goal, arr, x, y, num, clockwise):
    dx = 0
    while dx < goal:
        arr[y][x+dx] = num
        num+=1
        dx+=1
    if clockwise == True:
        return arr, x+dx-1, y+1, num
    else:
        return arr, x+dx-1, y-1, num

def move_left(goal, arr, x, y, num, clockwise):
    dx = 0
    while dx < goal:
        arr[y][x-dx] = num
        num+=1
        dx +=1

    if clockwise == True:
        return arr, x-dx+1, y-1, num
    else:
        return arr, x-dx+1, y+1, num

def move_down(goal, arr, x, y, num, clockwise):
    dy = 0
    while dy < goal:
        arr[y+dy][x] = num
        num+=1
        dy += 1

    if clockwise == True:
        return arr, x-1, y+dy-1, num
    else:
        return arr, x+1, y+dy-1, num

def move_up(goal, arr, x, y, num, clockwise):
    dy = 0
    while dy < goal:
        arr[y-dy][x] = num
        num+=1
        dy += 1
    if clockwise == True:
        return arr, x+1, y-dy+1, num
    else:
        return arr, x-1, y-dy+1, num

def solution(n, clockwise):
    answer = [[0]*(n) for i in range(n)]
    mid_point = []
    if n % 2 ==0:
        mid_point.append([n//2, n//2 -1])
        mid_point.append([n//2 -1, n//2])
        mid_point.append([n//2 -1, n//2 -1])
        mid_point.append([n//2, n//2])
    else:
        mid_point.append([n//2, n//2])
    if clockwise == True:
        start_point = [[0,0], [n-1, 0], [n-1, n-1], [0, n-1]]
        func = [move_right, move_down, move_left, move_up]
        for i, v in enumerate(start_point):
            x, y = v
            num = 1
            goal = n-1
            while goal > 0:
                answer, x, y, num =func[i%4](goal, answer, x, y, num, clockwise)
                goal -=2
                i+=1
    else:

        start_point = [[0,0], [0, n-1], [n-1, n-1], [n-1, 0]]
        func = [move_down, move_right, move_up, move_left]
        for i, v in enumerate(start_point):
            x, y = v
            num = 1
            goal = n-1
            while goal > 0:
                answer, x, y, num =func[i%4](goal, answer, x, y, num, clockwise)
                goal -=2
                i+=1

    if n % 2 ==1:
        for mid_x,mid_y in mid_point:
            answer[mid_y][mid_x] = num    
    else:
        for mid_x,mid_y in mid_point:
            answer[mid_y][mid_x] = num -1
    return answer

print(solution(10,False))

