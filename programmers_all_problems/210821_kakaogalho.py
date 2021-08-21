def split_1(a):
    count = {"(":0, ")":0}
    for i, c in enumerate(a):
        count[c] +=1
        if count["("] == count[")"]:
            return a[:i+1], a[i+1:]

def is_right(u):
    stack = []
    for i in u:
        if len(stack) > 0 and stack[-1] == '(' and i ==')': stack.pop()
        else: stack.append(i)
    if len(stack) == 0: return True
    else: return False

def change(u):
    if u is not None: return ['(' if i ==')' else ')' for i in u]
    else: return []

def func(now, a):
    if len(a) ==0: return now

    u, v = split_1(a)
    if is_right(u):
        if len(v) ==0:
            return now+u
        else:
            return func(now+u, v)
    
    else:
        return now + ['('] + func([], v) + [')'] + change(u[1:-1])

def solution(p):
    p = list(p)
    return "".join(func([], p))
print(solution("()))((()"))