# 실패... 비트마스킹 너무 모르겠다...

import sys
import heapq
from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]

arr = [[0]*5 for _ in range(5)]
star_point = []
group_num = 0
answer = 0
for y in range(5):
    tmp = sys.stdin.readline().split()[0]
    for x in range(5):
        if tmp[x] == '*':
            heapq.heappush(star_point, [1, x, y, group_num])
            arr[y][x] = 1
            group_num += 1

if len(star_point) <= 1:
    print(0)
    pass

while star_point[0][0] != len(star_point):
    group_count, x, y, group_num = heapq.heappop(star_point)
    hide = []
    for i in range(len(star_point)):
        if group_num == star_point[i][3]:
            hide.append([star_point[i][1], star_point[i][2]])
            arr[star_point[i][2]][star_point[i][1]] = 0

    arr[y][x] = 0
    q = deque([[x, y, -1, x, y]])
    dp = set()

    while q:
        tmp_x, tmp_y, count, prev_x, prev_y = q.popleft()
        if (tmp_x,tmp_y) in dp:
            continue

        dp.add((tmp_x,tmp_y))

        if arr[tmp_y][tmp_x] == 1:
            break
        
        for i in range(4):
            if 0<= tmp_x+dx[i] <=4 and 0<= tmp_y+dy[i] <=4:
                q.append([tmp_x+dx[i], tmp_y+dy[i], count+1, tmp_x, tmp_y])

    answer += count    
    arr[prev_y][prev_x] = 1

    match_group_num, match_group_count = 0, 0

    for i in range(len(star_point)):
        if star_point[i][1] == tmp_x and star_point[i][2] == tmp_y:
            match_group_num = star_point[i][3]
            match_group_count = star_point[i][0]
            break

    for i in range(len(star_point)):
        if star_point[i][3] == group_num:
            star_point[i][0] -= 1

        elif star_point[i][3] == match_group_num:
            star_point[i][0] +=1

    star_point.append([match_group_count+1, prev_x, prev_y, match_group_num])
    heapq.heapify(star_point)

    for i in hide:
        arr[i[1]][i[0]] = 1

print(answer)