from collections import deque
c = 11
b = 2
def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # 위치와 시간을 담아줄게요!.
    visited = [{} for _ in range(200001)]
    while cony_loc < 200000:
        cony_loc += time
        if time in visited[cony_loc]:
            return time
        for i in range(0, len(queue)):  # Q. Queue 인데 while 을 안 쓰는 이유를 고민해보세요!
            current_position, current_time = queue.popleft()
            new_position = current_position - 1
            new_time = current_time + 1
            if new_position >= 0 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))
            new_position = current_position + 1
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))
            new_position = current_position * 2
            if new_position < 200001 and new_time not in visited[new_position]:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))
        time += 1
print(catch_me(c, b))
print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))