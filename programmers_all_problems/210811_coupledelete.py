from collections import deque
def solution(s):
    s,tmp = deque(s), []
    while len(s) >0:
        pop_char = s.popleft()
        if len(tmp) > 0 and pop_char == tmp[-1]: tmp.pop()
        else: tmp.append(pop_char)
    return 0 if len(tmp) > 0 else 1

print(solution('baabaa'))
print(solution('cdcd'))
