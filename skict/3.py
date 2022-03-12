import math
def solution(width, height, diagonals):

    answer = 0
    
    for i in diagonals:
        x, y = i
        point_1 = math.factorial(x+(y-1))//(math.factorial(x)*math.factorial(y-1))
        point_2 = math.factorial((x-1)+y)//(math.factorial(x-1)*math.factorial(y))

        point_1_after_x, point_1_after_y = width-(x-1), height-y
        point_2_after_x, point_2_after_y = width-x, height-(y-1)

        case_1 = math.factorial(point_1_after_x + point_1_after_y)//(math.factorial(point_1_after_x)*math.factorial(point_1_after_y))
        case_2 = math.factorial(point_2_after_x + point_2_after_y)//(math.factorial(point_2_after_x)*math.factorial(point_2_after_y))

        answer += (point_1*case_1)
        answer += (point_2*case_2)

    return answer % 10000019

print(solution(51, 37, [[17,19]]))