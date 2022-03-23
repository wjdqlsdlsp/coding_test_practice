def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[1])
    arr = [[0]*(m+2) for i in range(n+2)]

    for s in skill:
        t, x0, y0, x1, y1, d = s
        if t == 2:
            d = d*-1
        arr[x0+1][y0+1] +=d
        arr[x0+1][y1+2] -=d
        arr[x1+2][y0+1] -=d
        arr[x1+2][y1+2] +=d

    for i in range(1,n+2):
        for j in range(1,m+2):
            arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1] 
    arr = [*map(lambda x: x[1:] , arr[1:])]

    for i in range(n):
        for j in range(m):
            board[i][j] -= arr[i][j]

            if board[i][j] >0:
                answer+=1
    return answer
print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))