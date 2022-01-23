import math

def solution(n, stations, w):
    answer = 0
    stations.sort()
    need = []
    start = 1
    for i in stations:
        dis = i-start-w
        need.append(dis)
        start = i + w +1
    if n-start+1 > 0:
        need.append(n-start+1)

    for i in need:
        answer += math.ceil(i / (2*w+1))
    
    return answer

print(solution(11,[4,11], 1))
print(solution(16,[9], 2))
