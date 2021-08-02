def solution(distance, rocks, n):
    rocks.sort()
    left, mid, right = 0, 0, distance
    while left <= right:
        mid = (left+right)//2
        count =0
        prev = 0
        for i in range(len(rocks)):
            if rocks[i] - prev <mid:
                count+=1
            else:
                prev = rocks[i]

        if count > n :
            right  = mid - 1
        else:
            left = mid + 1
            answer = mid

    return answer

# print(solution(34, [5,19,28],2))
print(solution(25,[2,14,11,21,17],2))

