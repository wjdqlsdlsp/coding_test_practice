# 시간초과...
import re
from collections import deque
import heapq
def solution(s):
    answer = []
    pattern = re.compile("110")
    for st in s:
        tmp_arr = []
        que_arr = deque([[st, -1]])
        while que_arr:
            a = que_arr.popleft()
            string, index = a[0], a[1]
            m = re.search(pattern, string)
            start_num = m.start()

            if index == start_num:
                m = re.search(pattern, string[start_num+3:])
                if m is None:
                    continue
                else:
                    start_num = m.start() +index+3
            
            tmp = string[:start_num] + string[start_num+3:]
            for i in range(len(tmp)):
                num = tmp[:i] +"110"+ tmp[i:]
                if num in tmp_arr:
                    continue
                heapq.heappush(tmp_arr, num)
                que_arr.append([num, i])
            
        pop = heapq.heappop(tmp_arr)
        answer.append(pop)
    return answer

print(solution(["0111111010"]))