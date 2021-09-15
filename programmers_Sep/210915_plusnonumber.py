def solution(numbers):
    return sum([i for i in [*range(1,10)] if i not in numbers])

print(solution([1,2,3,4,6,7,8,0]))