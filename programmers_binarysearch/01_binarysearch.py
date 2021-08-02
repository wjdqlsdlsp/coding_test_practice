def solution(n, times):
    answer = 0
    start, end, mid = 1, times[-1] * n, 0
    # start 초기값 : 1
    # end 초기값 : 모든 사람이 가장 오래걸리는 심사대 이용
    while start < end:
        mid = (start + end) // 2
        # print(start, end, mid)

        total = 0
        for time in times:
            total += mid // time

        if total >= n:
            end = mid

        else:
            start = mid + 1
            
    answer = start
    return answer

print(solution(2, [2, 5]))