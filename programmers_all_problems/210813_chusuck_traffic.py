def solution(lines):
    answer = 0
    log = []
    points = []
    for line in lines:
        date, time, sec = line.split(' ')
        time = time.split(':')
        end_time = float(time[0]) * 60*60 + float(time[1]) * 60 + float(time[2])
        sec = float(sec.split('s')[0])
        start = round(end_time - sec + 0.001,3)
        log.append((start, end_time))
        points.append(start)
        points.append(end_time)

    print(log)

    for point in points:
        count = 0
        for i in range(len(log)):
            if point<=log[i][0]<=point+1 or point<=log[i][1]<=point+1:
                count +=1

            elif log[i][0] <= point and point+1 <=log[i][1]:
                count +=1
        if answer < count:
            answer = count
    return answer

print(solution(["2016-09-15 01:00:04.002 2.0s","2016-09-15 01:00:07.000 2s"]))