import sys

x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
x3, y3 = map(int, sys.stdin.readline().split())

'''
x1 x2 x3 x1
y1 y2 y3 y1
'''

a = x1*y2 + x2*y3 +x3*y1 - (x2*y1 + x3*y2 + x1 * y3)
if a == 0:
    print(0)
elif a < 0:
    print(-1)
else:
    print(1)