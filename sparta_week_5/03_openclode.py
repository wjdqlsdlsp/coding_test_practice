from collections import deque

balanced_parentheses_string = "()))((()"
def is_right(queue):
    if queue.popleft() ==')':
        return False
    stack = deque(['('])
    
    for i in range(len(queue)):
        pop = queue.popleft()
        if stack[-1] =='(' and pop ==')':
            stack.pop()
        else:
            stack.append(pop)
    if len(stack) == 0:
        return True
    else:
        return False

def correct_u(u, v):
    correct = "("
    correct += get_correct_parentheses(''.join(v))
    u.popleft()
    u.pop()
    for i in range(len(u)):
        if u.popleft() =='(':
            correct += ')'
        else:
            correct += '('
    correct += ')'
    return correct

def split_u_v(string):
    doc = {'(': 0 , ')' :0}
    u = deque()
    v = deque()
    for i in range(len(string)):
        u.append(string[i])
        if string[i] == '(':
            doc['('] += 1
        else:
            doc[')'] += 1

        if doc['('] == doc[')']:
            break
    for j in range(i+1, len(string)):
        v.append(string[j])
    return u, v

def get_correct_parentheses(balanced_parentheses_string):
    if len(balanced_parentheses_string) < 2:
        return balanced_parentheses_string
    correct = ""
    u, v = split_u_v(balanced_parentheses_string)
    tu = ''.join(u)
    tv = ''.join(v)
    if is_right(u):
        correct += tu + get_correct_parentheses(tv)
    else:
        correct += correct_u(deque(list(tu)),v)
    return correct

# print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

# print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
# print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))