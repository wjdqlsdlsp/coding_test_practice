from collections import defaultdict

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solution(maps):
    c_len, r_len =len(maps), len(maps[0])
    meet_list = defaultdict(set)

    for y in range(c_len):
        for x in range(r_len):
            now = maps[y][x]
            if now == '.': continue

            for i in range(4):
                check_x, check_y = x+dx[i], y+dy[i]
                if 0 <= check_x < r_len and 0<= check_y < c_len:
                    meet = maps[check_y][check_x]
                    if meet != '.' and meet != now:
                        meet_list[now].add(meet)

    pair_count, max_count = 0, 0
    for k in meet_list.keys():
        max_count = max(max_count, len(meet_list[k]))
        pair_count += len(meet_list[k])

    return [pair_count//2, max_count]