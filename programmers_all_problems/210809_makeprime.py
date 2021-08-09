from itertools import combinations
def solution(nums):
    answer = 0
    com = list(combinations(nums, 3))
    sum_com = list(map(lambda x : sum(x), com))
    for num in sum_com:
        for i in range(2,num):
            if num % i ==0:
                break
        else:
            answer +=1
    return answer

print(solution([1,2,7,6,4]))