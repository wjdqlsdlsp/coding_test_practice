import re
from itertools import product
dynamic = []
def DFS(now, arr):
    global count
    i = len(now)
    if i == len(arr):
        dynamic.append(now)
        return
    for j in arr[i]:
        if j in now:
            continue
        DFS(now + [j],arr)

def solution(user_id, banned_id):
    answer = 0
    total_arr = []
    for ban in banned_id:
        ban = ban.replace("*", ".")
        ma = re.compile(ban)
        arr = []
        l = len(ban)
        for id in user_id:
            if re.match(ma, id) and l == len(id):
                arr.append(id)
        total_arr.append(arr)

    for i in total_arr[0]:
        DFS([i],total_arr)
    result =[]
    for j in dynamic:
        if len(j) == len(set(j)) and set(j) not in result:
            result.append(set(j))

    return len(result)

print(solution(["aaaaaaaa", "bbbbbbbb", "cccccccc", "dddddddd", "eeeeeeee", "ffffffff", "gggggggg", "hhhhhhhh"],	["********","********","********","********","********","********","********","********"]))