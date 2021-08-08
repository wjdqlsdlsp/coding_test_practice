def solution(absolutes, signs):
    return sum(list(map(lambda x,y : x if y else -1 * x, absolutes,signs)))


print(solution([4,7,12], [True,False,True]))