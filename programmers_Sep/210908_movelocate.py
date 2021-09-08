import heapq
def solution(land, height):
    ax = [-1,1,0,0]
    ay = [0,0,-1,1]
    answer = 0
    N = len(land)
    visited = [[False for _ in range(N)] for _2 in range(N)]
    visited_count = 0
    q = [(0,0,0)]
    while visited_count < N**2:
        v,y,x = heapq.heappop(q)
        if visited[y][x]:
            continue
        visited[y][x] = True
        visited_count+=1
        answer+=v

        for i in range(4):
            if 0<= x+ax[i] <N and 0 <= y+ay[i] < N and visited[y+ay[i]][x+ax[i]]== False:
                if abs(land[y+ay[i]][x+ax[i]] - land[y][x]) >height:
                    heapq.heappush(q, (abs(land[y+ay[i]][x+ax[i]] - land[y][x]),y+ay[i], x+ax[i] ))
                else:
                    heapq.heappush(q, (0,y+ay[i], x+ax[i]))

    return answer

print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]],3))