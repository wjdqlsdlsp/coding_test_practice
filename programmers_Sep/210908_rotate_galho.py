from collections import deque
import copy
def is_right(s):
    stack = [s.popleft()]
    
    for i in range(len(s)):
        tmp = s.popleft()
        if len(stack) > 0 and stack[-1] == "[" and tmp == "]":
            stack.pop()
        elif len(stack) > 0 and stack[-1] == "(" and tmp == ")":
            stack.pop()
        elif len(stack) > 0 and stack[-1] == "{" and tmp == "}":
            stack.pop()
        else:
            stack.append(tmp)
    if len(stack) == 0:
        return 1
    else:
        return 0

def solution(s):
    answer = 0
    arr = deque(s)
    for i in range(len(arr)):
        tmp = arr.copy()
        answer +=is_right(tmp)

        tmp = arr.popleft()
        arr.append(tmp)

    return answer

print(solution("[](){}"))