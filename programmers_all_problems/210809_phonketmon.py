def solution(nums):
    select_num = len(nums) //2 
    not_duplicate = []
    for num in nums:
        if num not in not_duplicate:
            not_duplicate.append(num)

    return min(len(not_duplicate),select_num)

print(solution([3,1,2,3]))