x_plus = [-1,-1,0,1, 1,1,0,-1]
y_plus = [0,-1,-1,-1, 0,1,1,1]
x_plus2 = [-2,0,0,0, 2,0,0,0]
y_plus2 = [0,0,-2,0, 0,0,2,0]

def is_right_position(x,y):
    if 0 <= x <= 4 and 0<= y <=4 : return 1
    else: return 0

def check_position(place, x,y):
    for i in range(8):
        if i%2 != 0 and is_right_position(x+x_plus[i], y+y_plus[i]) and place[x+x_plus[(i-1)%8]][y+y_plus[(i-1)%8]] =='X' and place[x+x_plus[(i+1)%8]][y+y_plus[(i+1)%8]] =='X': continue
        if is_right_position(x+x_plus[i], y+y_plus[i]) and place[x+x_plus[i]][y+y_plus[i]] =='P': return 0
        if i%2 ==0 and is_right_position(x+x_plus[i], y+y_plus[i]) and place[x+x_plus[i]][y+y_plus[i]] == 'O' and is_right_position(x+x_plus2[i],y+y_plus2[i]) and place[x+x_plus2[i]][y+y_plus2[i]] == 'P': return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        check = 1
        for y in range(5):
            for x in range(5):
                if place[x][y]=='P':
                    if check_position(place,x,y) ==0: check = 0
        if check == 1: answer.append(1)
        else: answer.append(0)
    return answer
    
print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))