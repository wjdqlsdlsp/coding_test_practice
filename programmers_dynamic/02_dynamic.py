# 미통과
max_num = 0
dynamic = {'pos' : [], 'value':[]}

def move(now, triangle,index,height,last):
    global max_num
    if height == last:
        if max_num < now:
            max_num = now
        return
    if [index,height] in dynamic['pos']:
        if dynamic['value'][dynamic['pos'].index([index,height])] >= now:
            return
        else:
            dynamic['value'][dynamic['pos'].index([index,height])] = now
    else:
        dynamic['pos'].append([index,height])
        dynamic['value'].append(now)

    
    move(now+triangle[0][index], triangle[1:], index, height+1,last)
    move(now+triangle[0][min(index+1,(height+1)*2-1)], triangle[1:], min(index+1,(height+1)*2-1), height+1,last)

def solution(triangle):
    move(triangle[0][0], triangle[1:],0, 0, len(triangle)-1)
    return max_num

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))