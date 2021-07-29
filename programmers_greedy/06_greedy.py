def solution(routes):
    routes = sorted(routes)
    print(routes)
    arr = []
    arr.append(routes[0])
    for i in range(1,len(routes)):
        start_1 = routes[i][0]
        end_1 = routes[i][1]

        start_2 = arr[-1][0]
        end_2 = arr[-1][1]

        if start_1 <= end_2:
            start = max(start_2, start_1)
            end = min(end_2,end_1)
            arr[-1] = [start,end]
        else:
            arr.append([start_1,end_1])
    return len(arr)


print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]	))