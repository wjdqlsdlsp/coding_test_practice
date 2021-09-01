# 문제오류가 있어보임
from collections import deque

def change_time(time):
    tmp =divmod(time,60)
    time,min = tmp[0],tmp[1]
    if time<10:
        time = "0" + str(time)
    if min<10:
        min = "0" + str(min)

    return str(time)+":"+str(min)

def solution(n, t, m, timetable):
    answer = ''
    timetable = deque(sorted(list(map(lambda x : int(x.split(":")[0])*60 + int(x.split(":")[1]),timetable))))
    start = 60*9
    okay = []
    for i in range(n):

        for j in range(m):
            if n-1 == i and j==m-1:
                if len(okay) ==0 and timetable[0] <= start : 
                    return change_time(start-1)
                elif len(okay) ==0:
                    return change_time(start)
                elif len(timetable) ==0:
                    return change_time(start)

                else:
                    return change_time(min(timetable[0] -1, start))

            elif len(timetable)> 0 and timetable[0] <= start:
                pop = timetable.popleft()
                okay.append(pop)

        start += t

print(solution(240, 10, 10, ["23:59", "23:59"]))




