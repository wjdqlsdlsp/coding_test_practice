import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2 + x2*y3 + x3* y1 - (x2*y1 + x3*y2 + x1*y3)

l1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
l2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

if l1 <= 0 and l2 <= 0:
    if l1 == 0 and l2 == 0:
        if min(x1, x2) <= max(x3, x4) and \
            min(x3, x4) <= max(x1, x2) and \
                min(y1, y2) <= max(y3, y4) and \
                    min(y3, y4) <= max(y1, y2):
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)
