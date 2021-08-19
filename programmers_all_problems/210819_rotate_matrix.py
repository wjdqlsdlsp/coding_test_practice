def solution(columns, rows, queries):
    answer = []

    a = [[i+j*rows+1 for i in range(rows)] for j in range(columns)]

    for querie in queries:
        tmp = []
        start_y, start_x, end_y, end_x = querie # 2,2,5,4
        # left move
        now = a[end_y-1][start_x-1]
        for i in range(end_y, start_y-1,-1):
            tmp.append(now)
            a[i-1][start_x-1], next = now, a[i-1][start_x-1]
            now = next
        # up move

        for i in range(start_x, end_x):
            tmp.append(now)
            next, a[start_y-1][i] = a[start_y-1][i], now
            now = next

        # right move
        for i in range(start_y, end_y):
            tmp.append(now)
            next, a[i][end_x-1] = a[i][end_x-1], now
            now = next

        # # down move
        for i in range(end_x-2, start_x-1, -1):
            tmp.append(now)
            next, a[end_y-1][i] = a[end_y-1][i], now
            now = next
        a[end_y-1][start_x-1] = now
        tmp.append(now)

        answer.append(min(tmp))

    return answer

print(solution(100,97, [[1,1,100,97]]))