import sys
T = int(sys.stdin.readline())

def ccw(p0, p1, p2):
	return (p1[0] - p0[0])*(p2[1] - p0[1]) - (p2[0] - p0[0])*(p1[1] - p0[1])


def get_hull(points):
    points.sort()
    U = []
    for p in points:
        while len(U) > 1 and ccw(U[-2], U[-1], p) < 0:
            U.pop()
        U.append(p)
    return U

for _ in range(T):
    arr = [*map(int, sys.stdin.readline().split())]
    points = []
    i = 1
    while i < len(arr):
        x, y = arr[i], arr[i+1]
        points.append((x,y, i//2))
        i+=2

    hull = get_hull(points)
    points = list(set(points) - set(hull))
    points.sort(reverse=True)
    for i in hull+points:
        print(i[2], end=" ")
    print("")
    