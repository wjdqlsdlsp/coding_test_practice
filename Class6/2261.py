import sys
n = int(sys.stdin.readline())
arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr = sorted(arr, key = lambda x: x[0])

def distance(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2

def solution(l,r):
    if l == r:
        return sys.maxsize
    
    else:
        m = (l+r)//2
        min_dist = min(solution(l,m), solution(m+1, r))
        target_list = []

        for i in range(m, l-1, -1):
            if (arr[i][0] - arr[m][0])** 2 < min_dist:
                target_list.append(arr[i])
            else:
                break
        
        for j in range(m+1, r+1):
            if (arr[j][0] - arr[m][0]) ** 2 < min_dist:
                target_list.append(arr[j])
            else:
                break
        
        target_list.sort(key=lambda x: x[1])
        for i in range(len(target_list) - 1):
            for j in range(i+1, len(target_list)):
                if (target_list[i][1] - target_list[j][1]) **2 < min_dist:
                    dist = distance(*target_list[i], *target_list[j])
                    min_dist = min(min_dist, dist)
                else:
                    break
        return min_dist

if len(arr) != len(set(arr)):
    print(0)
else:
    print(solution(0, len(arr)-1))