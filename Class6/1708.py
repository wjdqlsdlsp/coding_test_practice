import sys
n = int(sys.stdin.readline())
answer = -2
arr = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]
arr = sorted(arr, key=lambda x:(x[0],x[1]))

def ccw(x1, y1, x2, y2, x3, y3):
    return True if (x2 - x1) * (y3 - y2) - (x3 - x2) * (y2 - y1) >0 else False

def convex_hull(arr):
    convex = []
    for p3 in arr:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1[0],p1[1],p2[0],p2[1],p3[0],p3[1]):
                break
            convex.pop()
        convex.append(p3)
    return len(convex)

answer += convex_hull(arr)

arr.reverse()
answer += convex_hull(arr)
print(answer)