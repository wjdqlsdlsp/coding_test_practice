import sys

n = int(sys.stdin.readline())

p = []
for i in range(n):
    tmp = sys.stdin.readline().split()
    if tmp[2] == 'Y':
        x, y = int(tmp[0]), int(tmp[1])
        p.append((x,y))

def ccw(x1, y1, x2, y2, x3, y3):
    return False if (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3) >= 0 else True
# ccw 값이 양수이면 반시계방향
'''
x1 x2 x3 x1
y1 y2 y3 y1
'''


def monotoneChain(p):
    stack = []
    for i in p:
        while len(stack) > 1 and ccw(*stack[-2], *stack[-1], *i):
            stack.pop()
        stack.append(i)
    return stack

p.sort()
lower = monotoneChain(p)
p.sort(reverse=True)
uppder =monotoneChain(p)

result = lower[:-1]+ uppder[:-1]

print(len(result))
for i in result:
    print(*i)