def solution(citations):
    citations.sort(reverse=True)
    answer = 0
    for index, num in enumerate(citations):
        if index+1 <= num:
            answer = index+1
    return answer

print(solution([10, 8, 5, 4, 3]))
print(solution([25, 8, 5, 3, 3]))
