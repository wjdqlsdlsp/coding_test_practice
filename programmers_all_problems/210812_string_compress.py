import sys
from collections import deque
def solution(s):
    answer = sys.maxsize
    if len(s) ==1:
        return 1
    for i in range(1,len(s)//2+1):
        tmp_list = deque([])
        string = []
        for j in range(0,len(s)-i,i):
            tmp_list.append(s[j:j+i])
        tmp_list.append(s[j+i:])

        while len(tmp_list) >0:
            pop = tmp_list.popleft()
            count = 1
            while len(tmp_list) >0 and pop == tmp_list[0]:
                count+=1
                tmp_list.popleft()
            if count >1:
                string.append(str(count))
                string.append(pop)
            else:
                string.append(pop)
        a = ''.join(string)
        if len(a) < answer:
            answer = len(a)
    return answer
# print(solution("aabbaccc"))
# print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
# print(solution("xababcdcdababcdcd"))
print(solution("a"))
