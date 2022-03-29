from itertools import combinations
import copy
from collections import deque

room_dx = [0, 1, 0, 1]
room_dy = [0, 0, 1, 1]

def solution(n, m, room, bath):
    answer = 0
    tile = [[1]*m for _ in range(n)]
    tile_position = [[y, x] for x in range(m) for y in range(n)]
    bath_type = [[i, bath-i] for i in range(bath+1)]
    for room_position in [*combinations(tile_position, room)]:
        arr = copy.deepcopy(tile)    
        break_tmp=0
        for y, x in room_position:
            if y+1 < n and x+1 <m:
                for k in range(4):
                    if arr[y+room_dy[k]][x+room_dx[k]]:
                        arr[y+room_dy[k]][x+room_dx[k]] = 0
                    else:
                        break_tmp=1
                        break
            else:
                break_tmp=1
                break

        if break_tmp:
            continue

        # bath1 : 가로 , bath2 : 세로
        for bath1, bath2 in bath_type:
            for bath1_position in [*combinations(tile_position, bath1)]:
                arr1 = copy.deepcopy(arr)
                bath1_break = 0
                for y, x in bath1_position:
                    if x+1 < m:
                        for dx, dy in [[0,0], [1,0]]:
                            if arr1[y+dy][x+dx]:
                                arr1[y+dy][x+dx] = 0
                            else:
                                bath1_break=1
                                break
                    else:
                        bath1_break=1
                        break

                if bath1_break:
                    continue

                for bath2_position in [*combinations(tile_position, bath2)]:
                    arr2 = copy.deepcopy(arr1)
                    bath2_break = 0
                    for y, x in bath2_position:
                        if y+1 < n:
                            for dx, dy in [[0,0], [0, 1]]:
                                if arr2[y+dy][x+dx]:
                                    arr2[y+dy][x+dx] = 0
                                else:
                                    bath2_break=1
                                    break
                        else:
                            bath2_break = 1
                            break

                    if bath2_break:
                        continue

                    # 세번째 조건 : 문이 있어야함
                    door = sum(arr2[0]) + sum(arr2[n-1]) + \
                    sum([*map(lambda x : x[0], arr2)]) + sum([*map(lambda x : x[m-1],arr2)])

                    if door == 0:
                        continue

                    # 첫번째 조건 : 한곳이라도 입구가 있어야함
                    is_meet_break = 0

                    for y, x in room_position:
                        meet_place = 0
                        for tmp_dx, tmp_dy in [[0,0], [0,1], [1,0], [1,1]]:
                            now_x, now_y = x+tmp_dx, y+tmp_dy

                            for dx, dy in [[1,0], [0,1], [-1, 0], [0, -1]]:
                                meet_x, meet_y = now_x + dx, now_y +dy
                                if 0<= meet_x < m and 0<= meet_y < n:
                                    meet_place += arr2[meet_y][meet_x]

                        if meet_place == 0:
                            is_meet_break =1
                            break

                    for y, x in bath1_position:
                        meet_place = 0
                        for tmp_dx, tmp_dy in [[0,0], [1,0]]:
                            now_x, now_y = x+tmp_dx, y+tmp_dy

                            for dx, dy in [[1,0], [0,1], [-1, 0], [0, -1]]:
                                meet_x, meet_y = now_x + dx, now_y +dy
                                if 0<= meet_x < m and 0<= meet_y < n:
                                    meet_place += arr2[meet_y][meet_x]
                        if meet_place == 0:
                            is_meet_break =1
                            break

                    for y, x in bath2_position:
                        meet_place = 0
                        for tmp_dx, tmp_dy in [[0,0], [0, 1]]:
                            now_x, now_y = x+tmp_dx, y+tmp_dy

                            for dx, dy in [[1,0], [0,1], [-1, 0], [0, -1]]:
                                meet_x, meet_y = now_x + dx, now_y +dy
                                if 0<= meet_x < m and 0<= meet_y < n:
                                    meet_place += arr2[meet_y][meet_x]
                        if meet_place == 0:
                            is_meet_break =1
                            break

                    if is_meet_break:
                        continue

                    # 두번째 조건 : 모든 빈공간은 이어져있음
                    check_tmp = 0
                    for y in range(n):
                        for x in range(m):
                            if arr2[y][x] == 1:
                                start_y, start_x = y, x
                                check_tmp = 1
                                break
                        if check_tmp:
                            break
                    else:
                        continue

                    q = deque([[start_y, start_x]])
                    visited = set()

                    while q:
                        y, x = q.popleft()
                        if arr2[y][x] == 0:
                            continue
                        if (y, x) in visited:
                            continue
                        visited.add((y,x))

                        for dx, dy in [[1,0], [0,1], [-1, 0], [0, -1]]:
                            next_x, next_y = x+dx, y+dy
                            if 0<= next_x < m and 0 <= next_y < n:
                                q.append([next_y, next_x])

                    total_blank = 0
                    for i in arr2:
                        total_blank += sum(i)

                    if total_blank == len(visited):
                        answer+=1 

    return answer   