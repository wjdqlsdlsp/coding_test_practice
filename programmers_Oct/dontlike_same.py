def solution(arr):
    answer = []
    prev = '0'
    for i in arr:
        if prev == i:
            continue
        else:
            prev = i
            answer.append(i)
    return answer

print(solution([1,1,3,3,0,1,1]))