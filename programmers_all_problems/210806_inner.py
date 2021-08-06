def solution(a, b):
    return sum(list(map(lambda x,y : x*y, a,b)))

print(solution([1,2,3,4],[-3,-1,0,2]))